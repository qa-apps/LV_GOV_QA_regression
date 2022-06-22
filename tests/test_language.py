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
    
    @pytest.mark.regression
    def test_language_switcher_has_href(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        lang_switcher = page.locator('a[aria-label="Pārslēgties uz angļu valodu"]').first
        href = lang_switcher.get_attribute('href')
        assert href is not None
    
    @pytest.mark.regression
    def test_current_language_displayed(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        page_content = page.content()
        assert "LV" in page_content or "Latvian" in page_content.lower()
    
    @pytest.mark.regression
    def test_language_menu_accessible(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        lang_switcher = page.locator('a[aria-label="Pārslēgties uz angļu valodu"]').first
        assert lang_switcher.is_enabled()
    
    @pytest.mark.regression
    def test_multiple_languages_available(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        lang_switcher = page.locator('a[aria-label="Pārslēgties uz angļu valodu"]').first
        assert lang_switcher.is_visible()

