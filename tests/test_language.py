import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestLanguage:
    
    @pytest.mark.regression
    def test_language_switcher_visible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        lang_switcher = page.locator('a[aria-label="Pārslēgties uz angļu valodu"]').first
        assert lang_switcher.is_visible()
    
    @pytest.mark.regression
    def test_language_switcher_clickable(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        lang_switcher = page.locator('a[aria-label="Pārslēgties uz angļu valodu"]').first
        assert lang_switcher.is_enabled()

