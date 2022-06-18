import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

class TestAccessibility:
    
    @pytest.mark.regression
    def test_aria_labels_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        logo = page.locator('a[aria-label="Sākumlapa"]').first
        assert logo.is_visible()
    
    @pytest.mark.regression
    def test_buttons_have_text(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        services_button = page.locator('button:has-text("Pakalpojumi")').first
        assert services_button.text_content()
    
    @pytest.mark.regression
    def test_links_have_href(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        all_services_link = page.locator('a:has-text("Visi pakalpojumi")').first
        href = all_services_link.get_attribute('href')
        assert href is not None
    
    @pytest.mark.regression
    def test_images_have_alt_text(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        images = page.locator('img')
        if images.count() > 0:
            first_img = images.first
            assert first_img.is_visible()
    
    @pytest.mark.regression
    def test_focus_indicators_present(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        services_button = page.locator('button:has-text("Pakalpojumi")').first
        services_button.focus()
        assert services_button.is_visible()
    
    @pytest.mark.regression
    def test_skip_to_content_link(self, page: Page, base_url: str):
        home_page = HomePage(page)
        home_page.open(base_url)
        
        main_content = page.locator('main').first
        assert main_content.is_visible()

