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
    
    @pytest.mark.regression
    def test_search_with_latvian_characters(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        search_input.fill("pārvaldes")
        assert "pārvaldes" in search_input.input_value()
    
    @pytest.mark.regression
    def test_search_clears_previous_input(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        search_input.fill("test1")
        search_input.fill("")
        search_input.fill("test2")
        assert "test2" in search_input.input_value()
    
    @pytest.mark.regression
    def test_search_field_max_length(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        long_text = "a" * 500
        search_input.fill(long_text)
        assert len(search_input.input_value()) > 0
    
    @pytest.mark.regression
    def test_search_special_characters(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        search_input.fill("@#$%")
        assert search_input.input_value()

