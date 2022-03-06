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

