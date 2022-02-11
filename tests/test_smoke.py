import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestSmoke:
    
    @pytest.mark.smoke
    def test_homepage_loads_successfully(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert "Sākumlapa" in home_page.get_title()
        assert "latvija.gov.lv" in home_page.get_url()
    
    @pytest.mark.smoke
    def test_main_elements_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert home_page.is_logo_visible()
        assert home_page.is_search_visible()
        assert home_page.is_login_visible()
    
    @pytest.mark.smoke
    def test_navigation_menu_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.locator('button:has-text("Pakalpojumi")').first.is_visible()
        assert page.locator('button:has-text("Ko darīt, ja...?")').first.is_visible()
        assert page.locator('button:has-text("Mana Latvija.lv")').first.is_visible()
    
    @pytest.mark.smoke
    def test_language_switcher_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.locator('a[aria-label="Pārslēgties uz angļu valodu"]').first.is_visible()
    
    @pytest.mark.smoke
    def test_services_links_accessible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.locator('a:has-text("Visi pakalpojumi")').first.is_visible()
        assert page.locator('a:has-text("Visas dzīves situācijas")').first.is_visible()

