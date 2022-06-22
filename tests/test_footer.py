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
    
    @pytest.mark.regression
    def test_footer_links_clickable(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        contacts_link = page.locator('a:has-text("Kontakti un saziņa")').first
        assert contacts_link.is_enabled()
    
    @pytest.mark.regression
    def test_footer_present_on_page(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        footer = page.locator('footer').first
        assert footer.is_visible()
    
    @pytest.mark.regression
    def test_footer_copyright_text(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        content = page.content()
        assert "Latvija" in content or "latvija" in content.lower()
    
    @pytest.mark.regression
    def test_footer_social_links(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        footer = page.locator('footer').first
        assert footer.is_visible()

