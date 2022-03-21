import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestUIElements:
    
    @pytest.mark.regression
    def test_page_title_correct(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        title = page.title()
        assert "Latvija.lv" in title or "Sākumlapa" in title
    
    @pytest.mark.regression
    def test_header_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        header = page.locator('header').first
        assert header.is_visible()
    
    @pytest.mark.regression
    def test_main_content_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        main_content = page.locator('main').first
        assert main_content.is_visible()
    
    @pytest.mark.regression
    def test_navigation_bar_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        nav = page.locator('nav').first
        assert nav.is_visible()

