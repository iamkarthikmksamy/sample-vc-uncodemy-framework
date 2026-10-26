class Technologies:
    def __init__(self, page):
        self.page = page
        self.technologies = "//div[@class='menu']/ul/li[@class='drop_down']/a[normalize-space()='Technologies']"
        self.technologies_ecommerce_development = (
            "//ul[@class='tech-tab']/li[@data-id='ecomm']"
        )
        self.technologies_mobile_app = (
            "//ul[@class='tech-tab']/li[@data-id='mobileApp']"
        )
        self.technologies_ai_page = "//ul[@class='tech-tab']/li[@data-id='aipage']"

        self.technologies_list = [
            self.technologies_ecommerce_development,
            self.technologies_mobile_app,
            self.technologies_ai_page,
        ]

        self.ed_magento_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Magento Development']"
        )
        self.ed_opencart_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Opencart Development']"
        )
        self.ed_codeigniter_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Codeigniter Development']"
        )
        self.ed_wordpress_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='WordPress Development']"
        )
        self.ed_big_commerce = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Big Commerce']"
        )
        self.ed_shopify_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Shopify Development']"
        )
        self.ed_cs_cart_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='CS-Cart Development']"
        )
        self.ed_node_js_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Node JS Development']"
        )
        self.ed_nop_commerce = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Nop Commerce']"
        )
        self.ed_woo_commerce = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Woo Commerce']"
        )
        self.ed_laravel_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Laravel Development']"
        )
        self.ed_prestashop_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Prestashop Development']"
        )
        self.ed_drupal_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Drupal Development']"
        )
        self.ed_wix_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Wix Development']"
        )
        self.ed_joomla_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Joomla Development']"
        )
        self.ed_react_js_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='React JS Development']"
        )
        self.ed_express_js_development = (
            "//div[@id='ecomm']/ul/li/a[normalize-space()='Express JS Development']"
        )

        self.ed_list = [
            self.ed_magento_development,
            self.ed_opencart_development,
            self.ed_codeigniter_development,
            self.ed_wordpress_development,
            self.ed_shopify_development,
            self.ed_cs_cart_development,
            self.ed_node_js_development,
            self.ed_nop_commerce,
            self.ed_woo_commerce,
            self.ed_laravel_development,
            self.ed_prestashop_development,
            self.ed_drupal_development,
            self.ed_wix_development,
            self.ed_joomla_development,
            self.ed_react_js_development,
            self.ed_express_js_development,
        ]

        self.mp_react_native_mobile_app_development = "//div[@id='mobileApp']/ul/li/a[normalize-space()='React Native Mobile App Development']"
        self.mp_enterprise_mobile_app_development = "//div[@id='mobileApp']/ul/li/a[normalize-space()='Enterprise Mobile App Development']"
        self.mp_xamarin_mobile_app_development = "//div[@id='mobileApp']/ul/li/a[normalize-space()='Xamarin Mobile App Development']"
        self.mp_kotlin_mobile_app_development = "//div[@id='mobileApp']/ul/li/a[normalize-space()='Kotlin Mobile App Development']"
        self.mp_flutter_mobile_app_development = "//div[@id='mobileApp']/ul/li/a[normalize-space()='Flutter Mobile App Development']"
        self.mp_ionic_mobile_app_development = (
            "//div[@id='mobileApp']/ul/li/a[normalize-space()='Ionic App Development']"
        )
        self.mp_swift_mobile_app_development = (
            "//div[@id='mobileApp']/ul/li/a[normalize-space()='Swift App Development']"
        )
        self.mp_appointment_booking_development = "//div[@id='mobileApp']/ul/li/a[normalize-space()='Appointment Booking Development']"

        self.mp_list = [
            self.mp_react_native_mobile_app_development,
            self.mp_enterprise_mobile_app_development,
            self.mp_xamarin_mobile_app_development,
            self.mp_kotlin_mobile_app_development,
            self.mp_flutter_mobile_app_development,
            self.mp_ionic_mobile_app_development,
            self.mp_swift_mobile_app_development,
            self.mp_appointment_booking_development,
        ]

    def click_ecommerce_development(self, page):
        self.looping_through_sub_menus(
            page, self.technologies_ecommerce_development, self.ed_list
        )

    def click_mobile_app_development_options(self, page):
        self.looping_through_sub_menus(page, self.technologies_mobile_app, self.mp_list)

    def click_ai(self, page):
        self.looping_through_sub_menus(page, self.technologies_ai, self.ai_list)

    def looping_through_sub_menus(self, page, main_menu, sub_menu_list):
        for sub_menu in sub_menu_list:
            page.wait_for_load_state("load")
            page.wait_for_selector(self.technologies).hover()
            page.wait_for_selector(main_menu).hover()
            page.wait_for_selector(sub_menu).click()
            page.wait_for_load_state("load")
            page.go_back()
