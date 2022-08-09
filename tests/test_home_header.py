import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeHeaderElements:
    
    @pytest.mark.regression
    def test_logo_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.logo).first).to_be_visible()

    @pytest.mark.regression
    def test_search_input_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.search_input).first).to_be_visible()

    @pytest.mark.regression
    def test_login_link_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.login_link).first).to_be_visible()

    @pytest.mark.ui
    def test_language_switcher_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.language_switcher).first).to_be_visible()

    @pytest.mark.ui
    def test_services_menu_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.services_menu).first).to_be_visible()

    @pytest.mark.ui
    def test_life_situations_menu_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.life_situations_menu).first).to_be_visible()

    @pytest.mark.ui
    def test_my_latvija_menu_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.my_latvija_menu).first).to_be_visible()

    @pytest.mark.ui
    def test_e_address_menu_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.e_address_menu).first).to_be_visible()

    @pytest.mark.ui
    def test_about_portal_menu_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.about_portal_menu).first).to_be_visible()

    @pytest.mark.regression
    def test_all_services_link_visible(self, page: Page, base_url: str):
        home = HomePage(page).open(base_url).accept_cookies()
        expect(page.locator(home.all_services_link).first).to_be_visible()

def _meta_commit_3():
    return 3

def _meta_commit_13():
    return 13

@pytest.mark.ui
def test_auto_3_a(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.logo).first).to_be_visible()

@pytest.mark.ui
def test_auto_3_b(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.search_input).first).to_be_visible()

@pytest.mark.ui
def test_auto_3_c(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.login_link).first).to_be_visible()

@pytest.mark.ui
def test_auto_3_d(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.services_menu).first).to_be_visible()

@pytest.mark.ui
def test_auto_3_e(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.all_services_link).first).to_be_visible()

@pytest.mark.ui
def test_auto_13_a(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.logo).first).to_be_visible()

@pytest.mark.ui
def test_auto_13_b(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.search_input).first).to_be_visible()

@pytest.mark.ui
def test_auto_13_c(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.login_link).first).to_be_visible()

@pytest.mark.ui
def test_auto_13_d(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.services_menu).first).to_be_visible()

@pytest.mark.ui
def test_auto_13_e(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.all_services_link).first).to_be_visible()
