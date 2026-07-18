

def test_beem_login_workflow(pom, base_url: str):
    pom.login_page.launch_url(base_url)
    pom.login_page.verify_url(base_url)
    pom.login_page.verify_login_button_visible()
    pom.login_page.click_login_button()
    pom.login_page.verify_signup_text_visible()
  