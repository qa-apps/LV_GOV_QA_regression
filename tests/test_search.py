import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestSearch:
    
    @pytest.mark.regression
    def test_search_field_accepts_input(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        search_input.fill("tests")
        assert "tests" in search_input.input_value()
    
    @pytest.mark.regression
    def test_search_button_is_clickable(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_button = page.locator('button:has-text("Meklēt rezultātus")').first
        assert search_button.is_visible()

