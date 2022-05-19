import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeTopNav:
    
    @pytest.mark.ui
    def test_nav_services_button(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='Pakalpojumi')).to_be_visible()

    @pytest.mark.ui
    def test_nav_life_situations_button(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='Ko darīt, ja...?')).to_be_visible()

    @pytest.mark.ui
    def test_nav_my_latvija_button(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='Mana Latvija.lv')).to_be_visible()

    @pytest.mark.ui
    def test_nav_e_address_button(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='E-adrese')).to_be_visible()

    @pytest.mark.ui
    def test_nav_about_portal_button(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name='Par portālu')).to_be_visible()

    @pytest.mark.ui
    def test_nav_language_switcher(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('a[aria-label="Pārslēgties uz angļu valodu"]').first).to_be_visible()

    @pytest.mark.ui
    def test_nav_search_input(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('input[aria-label*="Meklēšanas"]').first).to_be_visible()

    @pytest.mark.ui
    def test_nav_search_button(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name=lambda n: 'Meklēt' in n)).to_be_visible()

    @pytest.mark.ui
    def test_nav_logo_link(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('link', name='Sākumlapa')).to_be_visible()

    @pytest.mark.ui
    def test_nav_all_services_link(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('link', name='Visi pakalpojumi')).to_be_visible()

def _meta_commit_8():
    return 8
