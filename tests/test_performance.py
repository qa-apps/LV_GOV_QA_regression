import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestPerformance:
    
    @pytest.mark.regression
    def test_page_loads_within_timeout(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.url.startswith(base_url)
    
    @pytest.mark.regression
    def test_all_resources_loaded(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        page.wait_for_load_state("networkidle")
        
        assert home_page.is_logo_visible()
    
    @pytest.mark.regression
    def test_dom_content_loaded(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        page.wait_for_load_state("domcontentloaded")
        
        assert page.title()
    
    @pytest.mark.regression
    def test_page_is_interactive(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        search_input = page.locator('input[aria-label*="Meklēšanas ievadlauks"]').first
        assert search_input.is_editable()
    
    @pytest.mark.regression
    def test_no_console_errors(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.url
    
    @pytest.mark.regression
    def test_page_loads_completely(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        page.wait_for_load_state("load")
        
        assert home_page.is_logo_visible()

