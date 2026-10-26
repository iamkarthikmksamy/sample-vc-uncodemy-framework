import pytest

from pages.socialmedia import Socialmedia


@pytest.mark.socialmedia
def test_click_socialmedia_links(page):
    s = Socialmedia(page)
    s.click_socialmedia_links()
