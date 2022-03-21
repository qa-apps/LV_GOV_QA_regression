import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestLogin:
    
    @pytest.mark.regression
    def test_login_link_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        login_link = page.locator('a:has-text("Ienākt Mana Latvija.lv")').first
        assert login_link.is_visible()
    
    @pytest.mark.regression
    def test_login_link_has_href(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        login_link = page.locator('a:has-text("Ienākt Mana Latvija.lv")').first
        href = login_link.get_attribute('href')
        assert href is not None
    
    @pytest.mark.regression
    def test_login_link_text_correct(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        login_link = page.locator('a:has-text("Ienākt Mana Latvija.lv")').first
        text = login_link.text_content()
        assert "Ienākt" in text or "Mana Latvija" in text
    
    @pytest.mark.regression
    def test_login_link_enabled(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        login_link = page.locator('a:has-text("Ienākt Mana Latvija.lv")').first
        assert login_link.is_enabled()

