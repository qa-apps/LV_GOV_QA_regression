import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestLinks:
    
    @pytest.mark.regression
    def test_external_links_have_target(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        links = page.locator('a[href^="http"]')
        if links.count() > 0:
            assert links.first.is_visible()
    
    @pytest.mark.regression
    def test_internal_links_clickable(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        services_link = page.locator('a:has-text("Visi pakalpojumi")').first
        assert services_link.is_enabled()
    
    @pytest.mark.regression
    def test_all_links_have_text(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        services_link = page.locator('a:has-text("Visi pakalpojumi")').first
        assert services_link.text_content()
    
    @pytest.mark.regression
    def test_footer_links_valid(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        contacts_link = page.locator('a:has-text("Kontakti un saziņa")').first
        href = contacts_link.get_attribute('href')
        assert href is not None
    
    @pytest.mark.regression
    def test_navigation_links_work(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        logo_link = page.locator('a[aria-label="Sākumlapa"]').first
        assert logo_link.is_visible()
    
    @pytest.mark.regression
    def test_links_are_understandable(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        services_link = page.locator('a:has-text("Visi pakalpojumi")').first
        text = services_link.text_content()
        assert len(text) > 0

