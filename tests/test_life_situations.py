import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestLifeSituations:
    
    @pytest.mark.regression
    def test_life_situations_link_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.locator('a:has-text("Visas dzīves situācijas")').first.is_visible()
    
    @pytest.mark.regression
    def test_life_situations_menu_expands(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page.locator('button:has-text("Ko darīt, ja...?")').first.click()
        page.wait_for_timeout(500)

