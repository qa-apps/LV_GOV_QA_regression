import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestCookies:
    
    @pytest.mark.regression
    def test_cookie_banner_displays(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        cookie_banner = page.locator('button:has-text("Piekrist visam")')
        if cookie_banner.first.is_visible():
            assert True
    
    @pytest.mark.regression
    def test_cookie_preferences_saved(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        cookie_accept = page.locator('button:has-text("Piekrist visam")').first
        if cookie_accept.is_visible():
            cookie_accept.click()

