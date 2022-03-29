import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestResponsive:
    
    @pytest.mark.regression
    def test_page_loads_full_width(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        viewport = page.viewport_size
        assert viewport['width'] == 1920
    
    @pytest.mark.regression
    def test_mobile_menu_not_visible_desktop(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.viewport_size['width'] >= 1024
    
    @pytest.mark.regression
    def test_viewport_height_correct(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        viewport = page.viewport_size
        assert viewport['height'] == 1080
    
    @pytest.mark.regression
    def test_layout_not_broken(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        header = page.locator('header').first
        assert header.is_visible()

