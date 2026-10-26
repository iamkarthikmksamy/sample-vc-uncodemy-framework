import pytest

from pages.contactus import ContactUs


@pytest.mark.contactus
def test_click_contact_us(page):
    c = ContactUs(page)
    c.click_contact_us()

@pytest.mark.contactus
def test_fill_contact_form(page):
    c = ContactUs(page)
    c.click_contact_us()
    c.fill_contact_form(
        name="Karthikeyan Muthukumarasamy",
        email="iam.karthikmksamy@gmail.com",
        otp="123456",
        company="XYZ Technologies",
        service="App Development",
        phone="8825793266",
        message="Test Message"
    )
