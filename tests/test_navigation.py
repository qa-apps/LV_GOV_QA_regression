import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestNavigation:
    
    @pytest.mark.regression
    def test_services_menu_opens(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page.locator('button:has-text("Pakalpojumi")').first.click()
        page.wait_for_timeout(500)
    
    @pytest.mark.regression
    def test_life_situations_menu_opens(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page.locator('button:has-text("Ko darīt, ja...?")').first.click()
        page.wait_for_timeout(500)

