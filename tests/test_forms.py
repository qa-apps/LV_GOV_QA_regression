import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestForms:
    
    @pytest.mark.regression
    def test_search_form_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_form = page.locator('form').first
        assert search_form.is_visible()
    
    @pytest.mark.regression
    def test_search_input_placeholder(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[placeholder*="Meklēt"]').first
        placeholder = search_input.get_attribute('placeholder')
        assert placeholder is not None
    
    @pytest.mark.regression
    def test_search_input_accepts_text(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        search_input.fill("test data")
        assert search_input.input_value() == "test data"
    
    @pytest.mark.regression
    def test_form_validation(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        assert search_input.is_editable()
    
    @pytest.mark.regression
    def test_form_submit_button(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_button = page.locator('button:has-text("Meklēt rezultātus")').first
        assert search_button.is_visible()
    
    @pytest.mark.regression
    def test_input_field_focus(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        search_input.focus()
        assert search_input.is_visible()

