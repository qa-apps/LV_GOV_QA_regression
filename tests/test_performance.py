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

