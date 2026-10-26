import pytest

from pages.portfolio import Portfolio


@pytest.mark.portfolio
def test_click_portfolio_links(page):
    p = Portfolio(page)
    p.click_portfolio_links()
