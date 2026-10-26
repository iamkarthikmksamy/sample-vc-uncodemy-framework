class ContactUs:
    def __init__(self, page):
        self.page = page
        self.contact_us = "//div[@class='menu']/ul/li/a[normalize-space()='Contact us']"
        self.name = "(//input[@placeholder='Your Name'])[2]"
        self.your_email = "(//input[@class='form-control email-input'])[1]"
        self.otp = "(//input[@placeholder='Enter OTP'])[2]"
        self.company = "(//input[@placeholder='Your Company'])[2]"
        self.service = "//div[@class='cm-form-field']//select[@name='service']"
        self.phone = "(//input[@placeholder='Your Phone'])[2]"
        self.message = "(//textarea[@placeholder='Message'])[2]"

    def click_contact_us(self):
        self.page.wait_for_selector(self.contact_us).click()
        self.page.wait_for_load_state("load")
        print(f"Clicked Contact us and navigated to {self.page.url}")

    def enter_name(self, name):
        self.page.wait_for_selector(self.name)
        self.page.fill(self.name, name)

    def enter_email(self, email):
        self.page.wait_for_selector(self.your_email)
        self.page.fill(self.your_email, email)

    def enter_otp(self, otp):
        self.page.wait_for_selector(self.otp)
        self.page.fill(self.otp, otp)

    def enter_company(self, company):
        self.page.wait_for_selector(self.company)
        self.page.fill(self.company, company)

    def select_service(self, service):
        self.page.wait_for_selector(self.service)
        self.page.click(self.service)
        self.page.select_option(self.service, service)

    def enter_phone(self, phone):
        self.page.wait_for_selector(self.phone)
        self.page.fill(self.phone, phone)

    def enter_message(self, message):
        self.page.wait_for_selector(self.message)
        self.page.fill(self.message, message)

    def fill_contact_form(self, name, email, otp, company, service, phone, message):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_otp(otp)
        self.enter_company(company)
        self.select_service(service)
        self.enter_phone(phone)
        self.enter_message(message)
        self.page.wait_for_timeout(4000)
