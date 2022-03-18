import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestAccessibility:
    
    @pytest.mark.regression
    def test_aria_labels_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        logo = page.locator('a[aria-label="Sākumlapa"]').first
        assert logo.is_visible()
    
    @pytest.mark.regression
    def test_buttons_have_text(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        services_button = page.locator('button:has-text("Pakalpojumi")').first
        assert services_button.text_content()

