import pytest


@pytest.fixture(autouse=True)
def go_to_homepage(pom, base_url: str):
    context = pom.home_page.page.context
    while len(context.pages) > 1:
        context.pages[-1].close()
    pom.home_page.launch_url(base_url)
    
    if pom.home_page.is_mobile():
        pom.home_page.close_mobile_menu()


def test_getcash_menuitem_icons(pom, base_url: str):
    pom.home_page.verify_url(base_url)
    pom.home_page.verify_get_cash_dropdown()
    pom.home_page.verify_earn_money_dropdown()
    pom.home_page.verify_save_money_dropdown()
    pom.home_page.verify_stay_protected_dropdown()
    pom.home_page.verify_resources_dropdown()


def test_get_started_navigation(pom, base_url: str):
    pom.home_page.click_get_started_button()


def test_instant_cash_navigation(pom, base_url: str):
    pom.home_page.click_get_instant_cash_button()


def test_personal_loans_navigation(pom, base_url: str):
    pom.home_page.click_get_personal_loans_button()


def test_beem_arcade_navigation(pom, base_url: str):
    pom.home_page.click_beem_arcade_button()


def test_device_insurance_navigation(pom, base_url: str):
    pom.home_page.click_device_insurance_link()


def test_job_loss_insurance_navigation(pom, base_url: str):
    pom.home_page.click_job_loss_insurance_link()


def test_will_trust_planning_navigation(pom, base_url: str):
    pom.home_page.click_will_trust_planning_link()


def test_life_insurance_navigation(pom, base_url: str):
    pom.home_page.click_life_insurance_link()


def test_explore_faqs_navigation(pom, base_url: str):
    pom.home_page.click_explore_faqs_button()


def test_view_all_benefits_navigation(pom, base_url: str):
    pom.home_page.click_view_all_benefits_button()


def test_explore_blogs_navigation(pom, base_url: str):
    pom.home_page.click_explore_blogs_button()