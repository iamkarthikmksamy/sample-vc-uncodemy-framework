import pytest

from pages.technologies import Technologies


@pytest.mark.ecommerce_development
def test_click_ecommerce_development(page):
    t = Technologies(page)
    t.click_ecommerce_development(page)


@pytest.mark.mobile_app_development
def test_click_mobile_app_development_options(page):
    t = Technologies(page)
    t.click_mobile_app_development_options(page)
