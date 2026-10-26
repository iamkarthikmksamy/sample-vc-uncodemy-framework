class Portfolio:
    def __init__(self, page):
        self.page = page
        self.portfolio = "//div[@class='menu']/ul/li/a[normalize-space()='Portfolio']"
        self.ics_homework = "//a[@href='https://www.icshomework.in/']"
        self.wings_pharma = "//a[@href='https://www.wingspharma.com/']"
        self.arena_animation = "//a[@href='https://arenasonipat.com/']"
        self.home360 = "//a[@href='https://home360stores.com/']"
        # self.club_meetings = "//html[1]/body[1]/section[2]/div[2]/div[5]/div[1]/a[1]"
        self.cords_cables = "//a[@href='https://cordscable.tranktechnologies.com/']"

        self.portfolia_new_tab_list = [
            self.ics_homework,
            self.wings_pharma,
            self.arena_animation,
            self.home360,
            # self.club_meetings,
            self.cords_cables,
        ]

    def click_portfolio(self):
        self.page.wait_for_selector(self.portfolio).click()
        self.page.wait_for_load_state("load")
        print(f"Clicked Portfolio and navigated to {self.page.url}")

    def click_portfolio_links(self):
        self.page.locator(self.portfolio).click()
        self.page.wait_for_load_state(state="domcontentloaded")
        for portfolio_link in self.portfolia_new_tab_list:
            locator = self.page.locator(portfolio_link)
            locator.scroll_into_view_if_needed()
            with self.page.context.expect_page() as new_page_info:
                locator.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("domcontentloaded")
            new_tab.close()
            print(f"Successfully processed link {portfolio_link}")
