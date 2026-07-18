import re
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # --- Dropdown Menus (Desktop Anchors) ---
        self.get_cash_menu = self.page.locator("#nav-trigger-Get-Cash")
        self.get_cash_dropdown_items = self.page.locator("#mega-Get-Cash a")
        self.get_cash_dropdown_icons = self.page.locator("#mega-Get-Cash img")

        self.earn_money_menu = self.page.locator("#nav-trigger-Earn-Money")
        self.earn_money_dropdown_items = self.page.locator("#mega-Earn-Money a")
        self.earn_money_dropdown_icons = self.page.locator("#mega-Earn-Money img")

        self.save_money_menu = self.page.locator("#nav-trigger-Save-Money")
        self.save_money_dropdown_items = self.page.locator("#mega-Save-Money a")
        self.save_money_dropdown_icons = self.page.locator("#mega-Save-Money img")

        self.stay_protected_menu = self.page.locator("#nav-trigger-Stay-Protected")
        self.stay_protected_dropdown_items = self.page.locator("#mega-Stay-Protected a")
        self.stay_protected_dropdown_icons = self.page.locator("#mega-Stay-Protected img")

        self.resources_menu = self.page.locator("#nav-trigger-Resources")
        self.resources_dropdown_items = self.page.locator("#mega-Resources a")
        self.resources_dropdown_icons = self.page.locator("#mega-Resources img")

        # --- Main CTAs & Links ---
        # --- Main CTAs & Links ---
        self.get_started_button = self.page.get_by_role("link", name="Get Started", exact=True).first
        self.get_instant_cash_button = self.page.get_by_role("link", name="Get Instant Cash", exact=True).first
        self.get_personal_loans_button = self.page.get_by_role("link", name="Check Loan Options", exact=True).first
        self.beem_arcade_button = self.page.get_by_role("link", name="Play Games and Earn Now", exact=True).first
        self.explore_faqs_button = self.page.get_by_role("link", name="Explore FAQs", exact=True).first
        self.explore_blogs_button = self.page.get_by_role("link", name="Explore Blogs", exact=True).first
        self.view_all_benefits_button = self.page.get_by_role("link", name="View All Benefits", exact=True).first

        # Scoped to ensure we pick up the actionable link wrappers rather than duplicate paragraphs
        self.device_insurance_link = self.page.get_by_role("link").filter(has_text="Device Insurance up to $1,000").first
        self.job_loss_insurance_link = self.page.get_by_role("link").filter(has_text="Job Loss & Disability Insurance").first
        self.will_trust_planning_link = self.page.get_by_role("link").filter(has_text="Will, Trust & Estate Planning").first
        self.life_insurance_link = self.page.get_by_role("link").filter(has_text="Life insurance coverage up to $1,000").first
    
    # === Dropdown Assertions using BasePage verify_dropdown ===

    def verify_get_cash_dropdown(self):
        self.open_menu(self.get_cash_menu, "Get Cash")
        expected = ["Get Instant Cash", "Get Personal Loans", "Send & Receive Money", "Beem Pass for Family"]
        self.verify_dropdown(self.get_cash_dropdown_items, self.get_cash_dropdown_icons, expected, icon_count=4)

    def verify_earn_money_dropdown(self):
        self.open_menu(self.earn_money_menu, "Earn Money")
        self.verify_dropdown(self.earn_money_dropdown_items, self.earn_money_dropdown_icons, ["Play Games & Earn Cash"])

    def verify_save_money_dropdown(self):
        self.open_menu(self.save_money_menu, "Save Money")
        self.verify_dropdown(self.save_money_dropdown_items, self.save_money_dropdown_icons, ["Earn Side Income"])

    def verify_stay_protected_dropdown(self):
        self.open_menu(self.stay_protected_menu, "Stay Protected")
        self.verify_dropdown(self.stay_protected_dropdown_items, self.stay_protected_dropdown_icons, ["Protect Your Job"])

    def verify_resources_dropdown(self):
        self.open_menu(self.resources_menu, "Resources")
        self.verify_dropdown(self.resources_dropdown_items, self.resources_dropdown_icons, ["About Us"])

    # === Navigation Steps using BasePage navigate ===

    def click_get_started_button(self):
        self.close_mobile_menu()
        self.navigate(self.get_started_button, re.compile(r"/app/d/auth/verify|apps\.apple\.com"))

    def click_get_instant_cash_button(self):
        self.open_menu(self.get_cash_menu, "Get Cash")
        self.navigate(self.get_instant_cash_button, re.compile(r"/get-instant-cash-advance|apps\.apple\.com"))

    def click_get_personal_loans_button(self):
        self.open_menu(self.get_cash_menu, "Get Cash")
        self.navigate(self.get_personal_loans_button, re.compile(r"/personal-loan"))

    def click_beem_arcade_button(self):
        self.open_menu(self.earn_money_menu, "Earn Money")
        self.navigate(self.beem_arcade_button, re.compile(r"/beem-arcade"))

    def click_device_insurance_link(self):
        self.open_menu(self.stay_protected_menu, "Stay Protected")
        self.navigate(self.device_insurance_link, re.compile(r"/beem-totalcare"))

    def click_job_loss_insurance_link(self):
        self.open_menu(self.stay_protected_menu, "Stay Protected")
        self.navigate(self.job_loss_insurance_link, re.compile(r"/job-loss-and-disability-insurance"))

    def click_will_trust_planning_link(self):
        self.open_menu(self.stay_protected_menu, "Stay Protected")
        self.navigate(self.will_trust_planning_link, re.compile(r"/will-and-trust-planning"))

    def click_life_insurance_link(self):
        self.open_menu(self.stay_protected_menu, "Stay Protected")
        self.navigate(self.life_insurance_link, re.compile(r"/life-insurance"))

    def click_view_all_benefits_button(self):
        self.close_mobile_menu()
        self.navigate(self.view_all_benefits_button, re.compile(r"/pricing"))

    def click_explore_faqs_button(self):
        self.close_mobile_menu()
        self.navigate(self.explore_faqs_button, re.compile(r"/support/home"))

    def click_explore_blogs_button(self):
        self.close_mobile_menu()
        self.navigate(self.explore_blogs_button, re.compile(r"/blog"))