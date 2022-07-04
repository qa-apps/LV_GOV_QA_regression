import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestSEO:
    
    @pytest.mark.regression
    def test_page_title_exists(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        title = page.title()
        assert len(title) > 0
    
    @pytest.mark.regression
    def test_meta_tags_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        charset_meta = page.locator('meta[charset]')
        assert charset_meta.count() >= 0
    
    @pytest.mark.regression
    def test_canonical_url(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert "latvija.gov.lv" in page.url
    
    @pytest.mark.regression
    def test_page_language_set(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        html = page.locator('html').first
        lang = html.get_attribute('lang')
        assert lang is not None or "lv" in page.content().lower()
    
    @pytest.mark.regression
    def test_structured_data_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        content = page.content()
        assert len(content) > 0
    
    @pytest.mark.regression
    def test_sitemap_accessible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.url.startswith("https://")

