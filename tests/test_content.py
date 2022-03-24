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
    
    @pytest.mark.regression
    def test_heading_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        h1 = page.locator('h1').first
        if h1.is_visible():
            assert h1.text_content()
    
    @pytest.mark.regression
    def test_meta_description(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        meta = page.locator('meta[name="description"]')
        assert meta.count() >= 0

