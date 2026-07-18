from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)


        self.login_button = self.page.get_by_role("button", name="Sign Up or Login")
        self.SignUp_Text = self.page.get_by_text("Sign Up or Login to your Beem Account")


    def verify_login_button_visible(self):
        expect(self.login_button).to_be_visible()

    def click_login_button(self):
        self.login_button.click()

    def verify_signup_text_visible(self):
        expect(self.SignUp_Text).to_be_visible()