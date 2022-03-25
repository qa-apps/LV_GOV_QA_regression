import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeSectionCards:
    
    @pytest.mark.ui
    def test_vsaa_card_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("VSAA informācija un pakalpojumi")').first).to_be_visible()

    @pytest.mark.ui
    def test_residence_declaration_card_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Dzīvesvietas deklarēšana vai norādīšana")').first).to_be_visible()

    @pytest.mark.ui
    def test_sick_leave_benefit_card_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Slimības pabalsta piešķiršana (B lapa)")').first).to_be_visible()

    @pytest.mark.ui
    def test_petition_signatures_card_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Parakstu vākšana par tautas nobalsošanas un pašvaldību referenduma ierosināšanu")').first).to_be_visible()

    @pytest.mark.ui
    def test_all_services_link_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Visi pakalpojumi")').first).to_be_visible()

    @pytest.mark.ui
    def test_unemployment_benefit_card_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Bezdarbnieku pabalsts un darba meklēšana")').first).to_be_visible()

    @pytest.mark.ui
    def test_annual_income_declaration_card_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Gada ienākumu deklarācija")').first).to_be_visible()

    @pytest.mark.ui
    def test_child_birth_card_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Bērna gaidīšana un piedzimšana")').first).to_be_visible()

    @pytest.mark.ui
    def test_action_in_case_of_illness_card_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Rīcība saslimšanas gadījumā")').first).to_be_visible()

    @pytest.mark.ui
    def test_all_life_situations_link_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Visas dzīves situācijas")').first).to_be_visible()

def _meta_commit_5():
    return 5

def _meta_commit_15():
    return 15

@pytest.mark.ui
def test_auto_5_a(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.logo).first).to_be_visible()

@pytest.mark.ui
def test_auto_5_b(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.search_input).first).to_be_visible()

@pytest.mark.ui
def test_auto_5_c(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.login_link).first).to_be_visible()

@pytest.mark.ui
def test_auto_5_d(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.services_menu).first).to_be_visible()

@pytest.mark.ui
def test_auto_5_e(page: Page, base_url: str):
    hp = HomePage(page)
    hp.open(base_url)
    hp.accept_cookies()
    expect(page.locator(hp.all_services_link).first).to_be_visible()
