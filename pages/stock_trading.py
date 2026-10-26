class StockTrading:
    def __init__(self, page):
        self.page = page
        self.verticals = (
            "//li[@class='drop_down']//a[@href='#'][normalize-space()='Verticals']"
        )
        self.stock_trading_menu = "//ul[@class='cm-flex cm-flex-wrap']//a[@class='mm-active'][normalize-space()='Stock Trading']"
        self.why_choose_us_back_header_1 = (
            "(//div[@class='cm-industry-choose-item-back-header'])[1]"
        )
        self.why_choose_us_back_header_2 = (
            "(//div[@class='cm-industry-choose-item-back-header'])[2]"
        )
        self.why_choose_us_back_header_3 = (
            "(//div[@class='cm-industry-choose-item-back-header'])[3]"
        )

        self.why_choose_us_front_header_1 = (
            "(//div[@class='cm-industry-choose-item-front'])[1]"
        )
        self.why_choose_us_front_header_2 = (
            "(//div[@class='cm-industry-choose-item-front'])[2]"
        )
        self.why_choose_us_front_header_3 = (
            "(//div[@class='cm-industry-choose-item-front'])[3]"
        )
        self.user_authentication = "//h2[normalize-space()='User Authentication']"
        self.page_accessibility = "//h2[normalize-space()='Page Accessibility']"
        self.stock_maintenance = "//h2[normalize-space()='Stock Maintenance']"
        self.market_analysis = "//h2[normalize-space()='Market Analysis']"
        self.push_notifications = "//h2[normalize-space()='Push Notifications']"
        self.eod_charting = "//h2[normalize-space()='EOD Charting']"

        self.user_authentication_content = (
            "(//div[@class='cm-content-wrapper']/div/p)[1]"
        )
        self.page_accessibility_content = (
            "(//div[@class='cm-content-wrapper']/div/p)[2]"
        )
        self.stock_maintenance_content = "(//div[@class='cm-content-wrapper']/div/p)[3]"
        self.market_analysis_content = "(//div[@class='cm-content-wrapper']/div/p)[4]"
        self.push_notifications_content = (
            "(//div[@class='cm-content-wrapper']/div/p)[5]"
        )
        self.eod_charting_content = "(//div[@class='cm-content-wrapper']/div/p)[6]"

    def click_on_stock_trading(self):
        self.page.wait_for_selector(self.verticals).hover()
        self.page.wait_for_selector(self.stock_trading_menu).click()
        self.page.wait_for_load_state("load")

    def hover_on_why_choose_us_1(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.why_choose_us_back_header_1).hover(force=True)
        self.page.wait_for_timeout(2000)
        info = self.page.wait_for_selector(
            self.why_choose_us_front_header_1
        ).inner_text()

    def hover_on_why_choose_us_2(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.why_choose_us_back_header_2).hover(force=True)
        self.page.wait_for_timeout(2000)
        info = self.page.wait_for_selector(
            self.why_choose_us_front_header_2
        ).inner_text()

    def hover_on_why_choose_us_3(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.why_choose_us_back_header_3).hover(force=True)
        self.page.wait_for_timeout(2000)
        info = self.page.wait_for_selector(
            self.why_choose_us_front_header_3
        ).inner_text()

    def get_user_authentication_content(self):
        return self.page.wait_for_selector(
            self.user_authentication_content
        ).inner_text()

    def get_page_accessibility_content(self):
        return self.page.wait_for_selector(self.page_accessibility_content).inner_text()

    def get_stock_maintenance_content(self):
        return self.page.wait_for_selector(self.stock_maintenance_content).inner_text()

    def get_market_analysis_content(self):
        return self.page.wait_for_selector(self.market_analysis_content).inner_text()

    def get_push_notifications_content(self):
        return self.page.wait_for_selector(self.push_notifications_content).inner_text()

    def get_eod_charting_content(self):
        return self.page.wait_for_selector(self.eod_charting_content).inner_text()

    def hover_on_user_authentication(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.user_authentication).hover(force=True)
        self.page.wait_for_timeout(2000)
        print(self.get_user_authentication_content())

    def hover_on_page_accessibility(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.page_accessibility).hover(force=True)
        self.page.wait_for_timeout(2000)
        print(self.get_page_accessibility_content())

    def hover_on_stock_maintenance(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.stock_maintenance).hover(force=True)
        self.page.wait_for_timeout(2000)
        print(self.get_stock_maintenance_content())

    def hover_on_market_analysis(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.market_analysis).hover(force=True)
        self.page.wait_for_timeout(2000)
        print(self.get_market_analysis_content())

    def hover_on_push_notifications(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.push_notifications).hover(force=True)
        self.page.wait_for_timeout(2000)
        print(self.get_push_notifications_content())

    def hover_on_eod_charting(self):
        self.click_on_stock_trading()
        self.page.wait_for_selector(self.eod_charting).hover(force=True)
        self.page.wait_for_timeout(2000)
        print(self.get_eod_charting_content())
