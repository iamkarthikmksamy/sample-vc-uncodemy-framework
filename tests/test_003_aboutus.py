import pytest

from pages.aboutus import AboutUs


@pytest.mark.aboutus
def test_click_about_us(page):
    v = AboutUs(page)
    v.click_about_us()


@pytest.mark.aboutus
def test_click_country_option_usa(page):
    v = AboutUs(page)
    v.click_country_option_usa()


@pytest.mark.aboutus
def test_click_country_option_uk(page):
    v = AboutUs(page)
    v.click_country_option_uk()


@pytest.mark.aboutus
def test_click_country_option_india(page):
    v = AboutUs(page)
    v.click_country_option_india()
