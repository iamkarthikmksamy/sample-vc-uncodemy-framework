from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright
from pytest_html import extras
from config import BASE_URL


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False, args=["--start-maximized"]
        )
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def context(browser):
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    yield context
    context.close()


@pytest.fixture
def page(request, context):
    page = context.new_page()
    request.node.stash[_PAGE_CLOSED_KEY] = False

    try:
        page.goto(BASE_URL)
        page.wait_for_load_state("load")
        yield page
    finally:
        if not request.node.stash.get(_PAGE_CLOSED_KEY, False):
            page.close()


_PAGE_CLOSED_KEY = pytest.StashKey[bool]()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extras", [])

    if report.when == "call":
        page = item.funcargs.get("page")

        if page:
            if report.failed:
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)

                file_name = screenshots_dir / f"{item.name}.png"

                page.screenshot(path=str(file_name))
                extra.append(extras.image(str(file_name)))

            video = page.video
            if video is None:
                raise RuntimeError(f"No video recording was created for {item.name}")

            page.close()
            item.stash[_PAGE_CLOSED_KEY] = True
            video_path = Path(video.path())
            if not video_path.is_file():
                raise FileNotFoundError(
                    f"Video recording for {item.name} was not found: {video_path}"
                )

            extra.append(
                extras.video(
                    str(video_path),
                    name="Execution recording",
                    mime_type="video/webm",
                    extension="webm",
                )
            )

        report.extras = extra
