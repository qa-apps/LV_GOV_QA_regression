import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestServices:
    
    @pytest.mark.regression
    def test_all_services_link_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.locator('a:has-text("Visi pakalpojumi")').first.is_visible()
    
    @pytest.mark.regression
    def test_services_menu_has_items(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page.locator('button:has-text("Pakalpojumi")').first.click()
        page.wait_for_timeout(500)
    
    @pytest.mark.regression
    def test_all_services_link_clickable(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        services_link = page.locator('a:has-text("Visi pakalpojumi")').first
        assert services_link.is_enabled()
    
    @pytest.mark.regression
    def test_services_menu_closes(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        services_button = page.locator('button:has-text("Pakalpojumi")').first
        services_button.click()
        page.wait_for_timeout(300)
        services_button.click()
        page.wait_for_timeout(300)

