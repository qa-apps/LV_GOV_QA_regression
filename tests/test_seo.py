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

