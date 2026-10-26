class Blog:
    def __init__(self, page):
        self.page = page
        self.blog = "//div[@class='menu']/ul/li/a[normalize-space()='Blog']"

        self.blog_app_development = (
            "//div[@class='cat-grid-box']/li/a[normalize-space()='App Development']"
        )
        self.blog_artificial_intelligence = "//div[@class='cat-grid-box']/li/a[normalize-space()='Artificial Intelligence']"
        self.blog_content_marketing = (
            "//div[@class='cat-grid-box']/li/a[normalize-space()='Content Marketing']"
        )
        self.blog_crm_development = (
            "//div[@class='cat-grid-box']/li/a[normalize-space()='CRM Development']"
        )
        self.blog_digital_marketing = (
            "//div[@class='cat-grid-box']/li/a[normalize-space()='Digital Marketing']"
        )
        self.blog_ecommerce_development = "//div[@class='cat-grid-box']/li/a[normalize-space()='ECommerce Development']"
        self.blog_email_marketing = (
            "//div[@class='cat-grid-box']/li/a[normalize-space()='Email Marketing']"
        )

        self.blog_graphi_design = (
            "//div[@class='cat-grid-box']/li/a[normalize-space()='Graphic Design']"
        )

        self.blog_software_and_it_company = "//div[@class='cat-grid-box']/li/a[normalize-space()='Software & IT Company']"

        self.blog_software_development = "//div[@class='cat-grid-box']/li/a[normalize-space()='Software Development']"

        self.blog_ui_ux_design = (
            "//div[@class='cat-grid-box']/li/a[normalize-space()='UI UX Design']"
        )

        self.blog_web_development = (
            "//div[@class='cat-grid-box']/li/a[normalize-space()='Web Development']"
        )

        self.blog_categories_list = [
            self.blog_app_development,
            self.blog_artificial_intelligence,
            self.blog_content_marketing,
            self.blog_crm_development,
            self.blog_digital_marketing,
            self.blog_ecommerce_development,
            self.blog_email_marketing,
            self.blog_graphi_design,
            self.blog_software_and_it_company,
            self.blog_software_development,
            self.blog_ui_ux_design,
            self.blog_web_development,
        ]

    def click_blog(self, page):
        page.wait_for_selector(self.blog).click()
        page.wait_for_load_state("load")

    def click_categories(self, page):
        for blog_item in self.blog_categories_list:
            page.wait_for_load_state("load")
            bt = page.wait_for_selector(blog_item)
            bin = bt.inner_text()
            bt.click()
            page.wait_for_load_state("load")
            print(f"Clicked {bin} under Blog and navigated to {page.url}")
            page.go_back()
