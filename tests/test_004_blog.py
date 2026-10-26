import pytest

from pages.blog import Blog


@pytest.mark.blog
def test_click_blog(page):
    b = Blog(page)
    b.click_blog(page)
    b.click_categories(page)
