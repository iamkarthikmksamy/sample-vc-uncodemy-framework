class Verticals:
    def __init__(self, page):
        self.page = page
        self.verticals = "//ul/li[@class='drop_down']/a[text()='Verticals']"
        self.verticals_trading = "//ul[@class='tech-tab']/li[@data-id='trading']"
        self.verticals_retail_ecommerce = (
            "//ul[@class='tech-tab']/li[@data-id='retailEcommerce']"
        )
        self.verticals_healthcare = "//ul[@class='tech-tab']/li[@data-id='healthcare']"
        self.verticals_fintech = "//ul[@class='tech-tab']/li[@data-id='fintech']"
        self.verticals_customapp = "//ul[@class='tech-tab']/li[@data-id='customApp']"
        self.verticals_list = [
            self.verticals_trading,
            self.verticals_retail_ecommerce,
            self.verticals_healthcare,
            self.verticals_fintech,
            self.verticals_customapp,
        ]

        self.vt_stock_trading = (
            "//div[@id='trading']/ul/li/a[normalize-space()='Stock Trading']"
        )
        self.vt_algo_trading = (
            "//div[@id='trading']/ul/li/a[normalize-space()='Algo Trading']"
        )
        self.vt_paper_trading = (
            "//div[@id='trading']/ul/li/a[normalize-space()='Paper Trading']"
        )
        self.vt_custom_trading = (
            "//div[@id='trading']/ul/li/a[contains(text(),'Custom')]"
        )
        self.vt_cfd_trading = (
            "//div[@id='trading']/ul/li/a[normalize-space()='CFD Trading']"
        )
        self.vt_web_portal_trading = (
            "//div[@id='trading']/ul/li/a[normalize-space()='Web Portal Trading']"
        )
        self.vt_trading_app = (
            "//div[@id='trading']/ul/li/a[contains(text(), 'Trading App')]"
        )

        self.vt_trading_list = [
            self.vt_stock_trading,
            self.vt_algo_trading,
            self.vt_paper_trading,
            self.vt_custom_trading,
            self.vt_cfd_trading,
            self.vt_web_portal_trading,
            self.vt_trading_app,
        ]

        self.re_ecommerce_website_development = "//div[@id='retailEcommerce']/ul/li/a[normalize-space()='eCommerce Website Development']"
        self.re_ecommerce_app_development = "//div[@id='retailEcommerce']/ul/li/a[normalize-space()='eCommerce App Development']"
        self.re_retail_and_ecommerce_list = [
            self.re_ecommerce_website_development,
            self.re_ecommerce_app_development,
        ]

        self.hc_diet_and_nutrition = (
            "//div[@id='healthcare']/ul/li/a[normalize-space()='Diet & Nutritions']"
        )
        self.hc_health_tracking_app = (
            "//div[@id='healthcare']/ul/li/a[normalize-space()='Health tracking App']"
        )
        self.hc_healthcare_list = [
            self.hc_diet_and_nutrition,
            self.hc_health_tracking_app,
        ]

        self.ft_pos_software_development = (
            "//div[@id='fintech']/ul/li/a[normalize-space()='Pos Software Development']"
        )
        self.ft_crypto = "//div[@id='fintech']/ul/li/a[normalize-space()='Crypto']"
        self.ft_fintech_list = [self.ft_pos_software_development, self.ft_crypto]

        self.ca_desktop_app_development = "//div[@id='customApp']/ul/li/a[normalize-space()='Desktop App Development']"
        self.ca_crm_development = (
            "//div[@id='customApp']/ul/li/a[normalize-space()='CRM Development']"
        )
        self.ca_hrm_development = (
            "//div[@id='customApp']/ul/li/a[normalize-space()='HRM Development']"
        )
        self.ca_erp_app_development = (
            "//div[@id='customApp']/ul/li/a[normalize-space()='ERP App Development']"
        )
        self.ca_travel = "//div[@id='customApp']/ul/li/a[normalize-space()='Travel']"
        self.ca_elearning = (
            "//div[@id='customApp']/ul/li/a[normalize-space()='E-Learning']"
        )
        self.ca_dating_app_development = (
            "//div[@id='customApp']/ul/li/a[normalize-space()='Dating App Development']"
        )
        self.ca_real_estate = (
            "//div[@id='customApp']/ul/li/a[normalize-space()='Real Estate']"
        )
        self.ca_crm_development_usa = (
            "//div[@id='customApp']/ul/li/a[normalize-space()='CRM Development USA']"
        )
        self.ca_custom_app_list = [
            self.ca_desktop_app_development,
            self.ca_crm_development,
            self.ca_hrm_development,
            self.ca_erp_app_development,
            self.ca_travel,
            self.ca_elearning,
            self.ca_dating_app_development,
            self.ca_real_estate,
            # self.ca_crm_development_usa,
        ]

    def click_trading_options(self, page):
        self.looping_through_sub_menus(
            page, self.verticals_trading, self.vt_trading_list
        )

    def click_retail_and_ecommerge_options(self, page):
        self.looping_through_sub_menus(
            page, self.verticals_retail_ecommerce, self.re_retail_and_ecommerce_list
        )

    def click_healthcare_options(self, page):
        self.looping_through_sub_menus(
            page, self.verticals_healthcare, self.hc_healthcare_list
        )

    def click_fintech_options(self, page):
        self.looping_through_sub_menus(
            page, self.verticals_fintech, self.ft_fintech_list
        )

    def click_custom_app_options(self, page):
        self.looping_through_sub_menus(
            page, self.verticals_customapp, self.ca_custom_app_list
        )

    def looping_through_sub_menus(self, page, main_menu, sub_menu_list):
        for sub_menu in sub_menu_list:
            page.wait_for_load_state("load")
            page.wait_for_selector(self.verticals).hover()
            page.wait_for_selector(main_menu).hover()
            page.wait_for_selector(sub_menu).click()
            page.wait_for_load_state("load")
            page.go_back()
