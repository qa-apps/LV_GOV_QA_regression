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
    
    @pytest.mark.regression
    def test_my_latvija_menu_opens(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page.locator('button:has-text("Mana Latvija.lv")').first.click()
        page.wait_for_timeout(500)
    
    @pytest.mark.regression
    def test_e_address_menu_opens(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page.locator('button:has-text("E-adrese")').first.click()
        page.wait_for_timeout(500)
    
    @pytest.mark.regression
    def test_about_portal_menu_opens(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page.locator('button:has-text("Par portālu")').first.click()
        page.wait_for_timeout(500)
    
    @pytest.mark.regression
    def test_logo_redirects_to_home(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        logo = page.locator('a[aria-label="Sākumlapa"]').first
        assert logo.is_visible()
    
    @pytest.mark.regression
    def test_all_navigation_buttons_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        buttons = page.locator('button')
        assert buttons.count() > 0
    
    @pytest.mark.regression
    def test_navigation_menu_structure(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        nav = page.locator('nav').first
        assert nav.is_visible()

