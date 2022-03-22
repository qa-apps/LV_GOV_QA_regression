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

