import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeAccessibility:
    
    @pytest.mark.accessibility
    def test_logo_has_aria_label(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('a[aria-label="Sākumlapa"]').first).to_be_visible()

    @pytest.mark.accessibility
    def test_search_input_has_accessible_name(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('input[aria-label*="Meklēšanas ievadlauks"], input[placeholder*="Meklēt"]').first).to_be_visible()

    @pytest.mark.accessibility
    def test_language_switcher_has_aria_label(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('a[aria-label="Pārslēgties uz angļu valodu"]').first).to_be_visible()

    @pytest.mark.accessibility
    def test_services_button_role(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='Pakalpojumi')).to_be_visible()

    @pytest.mark.accessibility
    def test_life_situations_button_role(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='Ko darīt, ja...?')).to_be_visible()

    @pytest.mark.accessibility
    def test_my_latvija_button_role(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='Mana Latvija.lv')).to_be_visible()

    @pytest.mark.accessibility
    def test_e_address_button_role(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='E-adrese')).to_be_visible()

    @pytest.mark.accessibility
    def test_about_portal_button_role(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='Par portālu')).to_be_visible()

    @pytest.mark.accessibility
    def test_footer_region_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('footer').first).to_be_visible()

    @pytest.mark.accessibility
    def test_main_navigation_region(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('navigation')).to_be_visible()

def _meta_commit_1():
    return 1

def _meta_commit_11():
    return 11
