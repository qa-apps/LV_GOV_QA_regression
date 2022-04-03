import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeNavigationMenus:
    
    @pytest.mark.ui
    def test_services_menu_visible_and_enabled(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.services_menu).first).to_be_visible()
        expect(page.locator(home.services_menu).first).to_be_enabled()

    @pytest.mark.ui
    def test_life_situations_menu_visible_and_enabled(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.life_situations_menu).first).to_be_visible()
        expect(page.locator(home.life_situations_menu).first).to_be_enabled()

    @pytest.mark.ui
    def test_my_latvija_menu_visible_and_enabled(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.my_latvija_menu).first).to_be_visible()
        expect(page.locator(home.my_latvija_menu).first).to_be_enabled()

    @pytest.mark.ui
    def test_e_address_menu_visible_and_enabled(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.e_address_menu).first).to_be_visible()
        expect(page.locator(home.e_address_menu).first).to_be_enabled()

    @pytest.mark.ui
    def test_about_portal_menu_visible_and_enabled(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.about_portal_menu).first).to_be_visible()
        expect(page.locator(home.about_portal_menu).first).to_be_enabled()

    @pytest.mark.ui
    def test_all_services_link_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.all_services_link).first).to_be_visible()

    @pytest.mark.ui
    def test_all_life_situations_link_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.all_life_situations_link).first).to_be_visible()

    @pytest.mark.ui
    def test_login_link_visible_and_enabled(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.login_link).first).to_be_visible()
        expect(page.locator(home.login_link).first).to_be_enabled()

    @pytest.mark.ui
    def test_language_switcher_visible_and_enabled(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.language_switcher).first).to_be_visible()
        expect(page.locator(home.language_switcher).first).to_be_enabled()
