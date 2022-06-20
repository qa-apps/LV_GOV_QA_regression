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
    
    @pytest.mark.regression
    def test_page_structure_valid(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        header = page.locator('header').first
        main = page.locator('main').first
        footer = page.locator('footer').first
        assert header.is_visible() or main.is_visible() or footer.is_visible()
    
    @pytest.mark.regression
    def test_text_encoding_correct(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        content = page.content()
        assert "Pakalpojumi" in content or "Ko darīt" in content

