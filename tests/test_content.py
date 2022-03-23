import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestContent:
    
    @pytest.mark.regression
    def test_page_has_content(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        content = page.content()
        assert len(content) > 100
    
    @pytest.mark.regression
    def test_latvian_content_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        content = page.content()
        assert "Pakalpojumi" in content or "Latvija" in content

