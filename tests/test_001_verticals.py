import pytest

from pages.verticals import Verticals


@pytest.mark.trading
def test_click_trading_options(page):
    v = Verticals(page)
    v.click_trading_options(page)


@pytest.mark.retail_and_ecommerce
def test_click_retail_and_ecommerge_options(page):
    v = Verticals(page)
    v.click_retail_and_ecommerge_options(page)


@pytest.mark.healthcare
def test_click_healthcare_options(page):
    v = Verticals(page)
    v.click_healthcare_options(page)


@pytest.mark.fintech
def test_click_fintech_options(page):
    v = Verticals(page)
    v.click_fintech_options(page)


@pytest.mark.custom_app
def test_click_custom_app_options(page):
    v = Verticals(page)
    v.click_custom_app_options(page)
