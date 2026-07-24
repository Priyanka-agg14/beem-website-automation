# pages/base_page.py

import re
from playwright.sync_api import Page, expect


class BasePage:
    MOBILE_BREAKPOINT = 768

    def __init__(self, page: Page):
        self.page = page

    # ==========================================================
    # Generic Helpers
    # ==========================================================
    def safe_click(self, locator, expected_href_pattern=None):
        """
        Clicks an element safely, verifying its href and handling potential 
        network aborts caused by blocked external redirects (e.g. App Store / OneLink).
        """
        locator.wait_for(state="visible")
        
        # Verify link pattern if provided
        if expected_href_pattern:
            href = locator.get_attribute("href") or ""
            assert re.search(expected_href_pattern, href), f"Unexpected href target: {href}"
            
        # Perform click and catch expected network aborts from intercepted routes
        try:
            locator.click()
        except Exception as e:
            if "ERR_ABORTED" not in str(e):
                raise e
            
    def launch_url(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded", timeout=45000)

    def verify_url(self, expected_url: str):
        expected = expected_url.rstrip("/")
        expect(self.page).to_have_url(
            re.compile(re.escape(expected) + r"/?")
        )

    def is_mobile(self) -> bool:
        viewport = self.page.viewport_size
        return viewport and viewport["width"] < self.MOBILE_BREAKPOINT

    # ==========================================================
    # Mobile Drawer
    # ==========================================================

    @property
    def mobile_drawer(self):
        return self.page.locator("[id^='headlessui-dialog-panel']").first

    @property
    def hamburger_button(self):
        return self.page.locator("header button").first

    @property
    def close_button(self):
        return self.mobile_drawer.get_by_role("button").first

    def open_mobile_menu(self):

        if not self.is_mobile():
            return

        if not self.mobile_drawer.is_visible():
            self.hamburger_button.click()
            expect(self.mobile_drawer).to_be_visible()

    def close_mobile_menu(self):

        if not self.is_mobile():
            return

        if self.mobile_drawer.is_visible():
            self.close_button.click()

    # ==========================================================
    # Menu Handling
    # ==========================================================

    def open_menu(self, desktop_locator, menu_name: str):

        if self.is_mobile():

            self.open_mobile_menu()

            button = self.mobile_drawer.get_by_role(
                "button",
                name=menu_name,
                exact=True
            )

            expect(button).to_be_visible()

            expanded = button.get_attribute("aria-expanded")

            if expanded == "false":
                button.click()

            expect(button).to_have_attribute(
                "aria-expanded",
                "true"
            )

        else:

            desktop_locator.hover()

    # ==========================================================
    # Dropdown Verification
    # ==========================================================

    def verify_dropdown(
        self,
        desktop_items,
        desktop_icons,
        expected_items,
        icon_count=None
    ):

        if self.is_mobile():

            panel = self.mobile_drawer.locator(
                "button[aria-expanded='true'] + ul"
            ).first

            expect(panel).to_be_visible()

            for item in expected_items:
                expect(panel).to_contain_text(item)

        else:

            expect(desktop_items).to_contain_text(expected_items)

            if icon_count is not None:
                expect(desktop_icons).to_have_count(icon_count)

    # ==========================================================
    # Navigation
    # ==========================================================

    def navigate(
        self,
        locator,
        expected_regex: re.Pattern
    ):

        href = locator.get_attribute("href") or ""

        if "apps.apple.com" in href or "play.google.com" in href:

            assert expected_regex.search(href), \
                f"Unexpected href: {href}"

            return
        
        # ROUTE INTERCEPTION: Abort any background redirects heading to the App Store
        self.page.route(
            "**/apps.apple.com/**", 
            lambda route: route.abort()
        )

        target = locator.get_attribute("target")

        if target == "_blank":

            with self.page.context.expect_page() as page_info:
                locator.click()

            new_page = page_info.value

            new_page.wait_for_load_state("domcontentloaded")

            expect(new_page).to_have_url(expected_regex)

            new_page.close()

        else:

            locator.click()

            expect(self.page).to_have_url(expected_regex)
