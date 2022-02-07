import pytest
from playwright.sync_api import Page, BrowserContext
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://latvija.gov.lv")

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        locale="lv-LV"
    )
    context.set_default_timeout(30000)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext):
    page = context.new_page()
    yield page
    page.close()


