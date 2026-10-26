import pytest

from pages.stock_trading import StockTrading


@pytest.mark.stocktrading
def test_click_on_stock_trading(page):
    v = StockTrading(page)
    v.click_on_stock_trading()


@pytest.mark.stocktrading
def test_hover_on_why_choose_us_1(page):
    v = StockTrading(page)
    v.hover_on_why_choose_us_1()


@pytest.mark.stocktrading
def test_hover_on_why_choose_us_2(page):
    v = StockTrading(page)
    v.hover_on_why_choose_us_2()


@pytest.mark.stocktrading
def test_hover_on_why_choose_us_3(page):
    v = StockTrading(page)
    v.hover_on_why_choose_us_3()


@pytest.mark.stocktrading
def test_hover_on_user_authentication(page):
    v = StockTrading(page)
    v.hover_on_user_authentication()


@pytest.mark.stocktrading
def test_hover_on_page_accessibility(page):
    v = StockTrading(page)
    v.hover_on_page_accessibility()


@pytest.mark.stocktrading
def test_hover_on_stock_maintenance(page):
    v = StockTrading(page)
    v.hover_on_stock_maintenance()


@pytest.mark.stocktrading
def test_hover_on_market_analysis(page):
    v = StockTrading(page)
    v.hover_on_market_analysis()


@pytest.mark.stocktrading
def test_hover_on_push_notifications(page):
    v = StockTrading(page)
    v.hover_on_push_notifications()


@pytest.mark.stocktrading
def test_hover_on_eod_charting(page):
    v = StockTrading(page)
    v.hover_on_eod_charting()
