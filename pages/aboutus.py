class AboutUs:
    def __init__(self, page):
        self.page = page
        self.about_us = "//div[@class='menu']//a[normalize-space()='About us']"
        self.counterySelector = "//select[@id='countrySelector']"
        self.country_option_india = (
            "//select[@id='countrySelector']/option[normalize-space()='India']"
        )
        self.country_option_usa = (
            "//select[@id='countrySelector']/option[normalize-space()='USA']"
        )
        self.country_option_uk = (
            "//select[@id='countrySelector']/option[normalize-space()='UK']"
        )

    def click_about_us(self):
        self.page.wait_for_selector(self.about_us).click()
        self.page.wait_for_load_state("load")

    def click_country_option_india(self):
        self.page.wait_for_selector(self.counterySelector).click()
        self.page.wait_for_selector(self.counterySelector).select_option("India")
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(2000)

    def click_country_option_usa(self):
        self.page.wait_for_selector(self.counterySelector).click()
        self.page.wait_for_selector(self.counterySelector).select_option("USA")
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(2000)

    def click_country_option_uk(self):
        self.page.wait_for_selector(self.counterySelector).click()
        self.page.wait_for_selector(self.counterySelector).select_option("UAE")
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(2000)
