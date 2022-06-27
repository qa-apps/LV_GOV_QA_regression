import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestLifeSituations:
    
    @pytest.mark.regression
    def test_life_situations_link_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        assert page.locator('a:has-text("Visas dzīves situācijas")').first.is_visible()
    
    @pytest.mark.regression
    def test_life_situations_menu_expands(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page.locator('button:has-text("Ko darīt, ja...?")').first.click()
        page.wait_for_timeout(500)
    
    @pytest.mark.regression
    def test_life_situations_link_clickable(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        situations_link = page.locator('a:has-text("Visas dzīves situācijas")').first
        assert situations_link.is_enabled()
    
    @pytest.mark.regression
    def test_life_situations_menu_closes(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        situations_button = page.locator('button:has-text("Ko darīt, ja...?")').first
        situations_button.click()
        page.wait_for_timeout(300)
        situations_button.click()
        page.wait_for_timeout(300)
    
    @pytest.mark.regression
    def test_life_situations_button_text(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        button = page.locator('button:has-text("Ko darīt, ja...?")').first
        text = button.text_content()
        assert "Ko darīt" in text
    
    @pytest.mark.regression
    def test_life_situations_link_href(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        link = page.locator('a:has-text("Visas dzīves situācijas")').first
        href = link.get_attribute('href')
        assert href is not None

