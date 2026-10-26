from conftest import page


class Socialmedia:
    def __init__(self, page):
        self.page = page
        # social media links that open in a new tab locators

        self.about_us = "//div[@class='menu']//a[normalize-space()='About us']"

        self.facebook_new_tab = '//img[@alt="Facebook"]'

        self.linkedin_new_tab = '//img[@alt="LinkedIn"]'

        self.instagram_new_tab = '(//img[@alt="Instagram"])[1]'

        self.pinterest_new_tab = '(//img[@alt="Instagram"])[2]'

        self.twitter_new_tab = '//img[@alt="Twitter"]'

        self.youtube_new_tab = '//img[@alt="Youtube"]'

        self.qoura_new_tab = '//img[@alt="Quora"]'

        self.social_media_new_tab_list = [
            self.facebook_new_tab,
            self.linkedin_new_tab,
            self.instagram_new_tab,
            self.pinterest_new_tab,
            self.twitter_new_tab,
            self.youtube_new_tab,
            self.qoura_new_tab,
        ]

    def click_socialmedia_links(self):
        self.page.locator(self.about_us).click()
        self.page.wait_for_load_state(state="load")
        for social_media_link in self.social_media_new_tab_list:
            self.scroll_until_visible(self.page, social_media_link)
            with self.page.context.expect_page() as new_page_info:
                self.page.locator(social_media_link).click()
            new_tab = new_page_info.value
            new_tab.wait_for_timeout(2000)
            new_tab.close()

    def scroll_until_visible(self, page, target_selector):
        target = page.locator(target_selector)

        scroll_amount = 800  # Pixels to scroll each step
        direction = 1  # 1 for down, -1 for up

        while not target.is_visible():
            # Scroll the mouse wheel (x=0, y=scroll_amount * direction)
            page.mouse.wheel(0, scroll_amount * direction)

            # Pause briefly for lazy loading / rendering
            page.wait_for_timeout(500)

            # Check if we hit the bottom of the page
            is_at_bottom = page.evaluate(
                "window.innerHeight + window.scrollY >= document.body.scrollHeight"
            )
            # Check if we hit the top of the page
            is_at_top = page.evaluate("window.scrollY === 0")

            # Reverse direction if bounds are reached
            if is_at_bottom and direction == 1:
                direction = -1  # Switch to scrolling up
            elif is_at_top and direction == -1:
                # We searched all the way down and all the way up, break to avoid infinite loop
                print("Element not found on the page.")
                break

        # Once visible, you can interact with it safely
        if target.is_visible():
            target.highlight()  # Optional: highlights the element visually
