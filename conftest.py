import pytest
from playwright.sync_api import Page, Playwright, Browser
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def base_url():
    return "https://dev-web.trybeem.com"

class POMContainer:
    """A clean container to hold all Page Objects initialized with the same page context."""
    def __init__(self, page: Page):
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)

@pytest.fixture(scope="module")
def shared_page(browser: Browser, browser_context_args):
    """Launches a single browser context and page per test file (module)."""
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture(scope="function")
def pom(shared_page: Page):
    return POMContainer(shared_page)

def pytest_addoption(parser):
    """Adds a custom CLI flag to choose the execution environment layer."""
    parser.addoption(
        "--type", 
        action="store", 
        default="desktop", 
        help="Choose execution type: desktop or mweb"
    )

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright: Playwright, request):
    execution_type = request.config.getoption("--type").lower()
    if execution_type == "mweb":
        mobile_device = playwright.devices["iPhone 14"]
        return {
            **browser_context_args,
            **mobile_device,
        }
    else:
        return {
            **browser_context_args,
            "no_viewport": True
        }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Passes the native maximize flag directly to the browser binary."""
    return {
        **browser_type_launch_args,
        "args": ["--start-maximized"]
    }