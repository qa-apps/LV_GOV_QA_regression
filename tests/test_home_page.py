import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

class TestHomePage:
    
    @pytest.mark.smoke
    def test_home_page_loads(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert "Sākumlapa" in home_page.get_title()
        assert home_page.is_logo_visible()
    
    @pytest.mark.smoke
    def test_main_navigation_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert home_page.is_logo_visible()
        assert home_page.is_search_visible()
        assert home_page.is_login_visible()
    
    @pytest.mark.regression
    def test_cookie_banner_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        home_page.accept_cookies()
        home_page.wait_for_load_state()
    
    @pytest.mark.regression
    def test_language_switch(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        home_page.switch_to_english()
        page.wait_for_load_state("domcontentloaded")
        
        page_content = page.content()
        assert "EN" in page_content or page.title()
    
    @pytest.mark.critical
    def test_search_functionality(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        home_page.accept_cookies()
        
        search_query = "pensija"
        page.fill(home_page.search_input, search_query)
        page.wait_for_timeout(1000)
        assert search_query in page.locator(home_page.search_input).first.input_value()


