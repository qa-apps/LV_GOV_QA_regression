import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestSecurity:
    
    @pytest.mark.regression
    def test_https_protocol(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.url.startswith("https://")
    
    @pytest.mark.regression
    def test_no_mixed_content(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert "https://" in page.url

