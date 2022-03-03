import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestFooter:
    
    @pytest.mark.regression
    def test_footer_contacts_link_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.locator('a:has-text("Kontakti un saziņa")').first.is_visible()
    
    @pytest.mark.regression
    def test_footer_about_link_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.locator('a:has-text("Par portālu")').first.is_visible()

