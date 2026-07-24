# pages/login_page.py

import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Desktop header button locator
        self.login_button = self.page.get_by_role("button", name="Sign Up or Login")

        # Flexible locator matching both Desktop ("Hello" / "Sign Up or Login...") and Mobile ("Enter your phone number")
        self.SignUp_Text = self.page.get_by_text(
            re.compile(r"Sign Up or Login to your Beem Account|Enter your phone number|Hello", re.IGNORECASE)
        ).first

    def get_login_element(self):
        """Returns the login control based on current viewport layout."""
        if self.is_mobile():
            self.open_mobile_menu()
            return self.mobile_drawer.get_by_role("link", name="Sign Up or Login")
        else:
            return self.login_button

    def verify_login_button_visible(self):
        """Verifies the login control is visible in both viewports."""
        expect(self.get_login_element()).to_be_visible()

    def click_login_button(self):
        """Clicks the login control based on current viewport layout."""
        self.get_login_element().click()

    def verify_signup_text_visible(self):
        """Verifies authentication container heading/text is displayed."""
        expect(self.SignUp_Text).to_be_visible()