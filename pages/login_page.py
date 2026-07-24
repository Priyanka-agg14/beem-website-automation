# pages/login_page.py

import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_button = self.page.get_by_role("button", name="Sign Up or Login")
        # Target heading on the verification page or use regex flexible match
        self.SignUp_Text = self.page.get_by_role("heading", name=re.compile(r"Enter your phone number|Sign Up or Login", re.IGNORECASE))

    def get_login_element(self):
        if self.is_mobile():
            self.open_mobile_menu()
            return self.mobile_drawer.get_by_role("link", name="Sign Up or Login")
        else:
            return self.login_button

    def verify_login_button_visible(self):
        expect(self.get_login_element()).to_be_visible()

    def click_login_button(self):
        self.get_login_element().click()

    def verify_signup_text_visible(self):
        expect(self.SignUp_Text).to_be_visible()