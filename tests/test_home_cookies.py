import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeCookieAndPrivacy:
    
    @pytest.mark.regression
    def test_cookie_banner_visible_on_first_load(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('button:has-text("Piekrist visam")').first).to_be_visible()

    @pytest.mark.regression
    def test_cookie_accept_all_button_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('button:has-text("Piekrist visam")').first).to_be_visible()

    @pytest.mark.regression
    def test_cookie_manage_button_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('button:has-text("Pārvaldīt")').first).to_be_visible()

    @pytest.mark.regression
    def test_cookie_accept_all_closes_banner(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        page.locator('button:has-text("Piekrist visam")').first.click()
        expect(page.locator('button:has-text("Piekrist visam")').first).not_to_be_visible()

    @pytest.mark.ui
    def test_cookie_manage_button_enabled(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('button:has-text("Pārvaldīt")').first).to_be_enabled()

    @pytest.mark.ui
    def test_privacy_policy_link_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Privātuma politika")').first).to_be_visible()

    @pytest.mark.ui
    def test_terms_link_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Lietošanas noteikumi")').first).to_be_visible()

    @pytest.mark.ui
    def test_change_cookie_settings_button_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('button:has-text("Mainīt sīkdatņu iestatījumus")').first).to_be_visible()

    @pytest.mark.ui
    def test_site_map_link_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Apskatīt lapas karti")').first).to_be_visible()

    @pytest.mark.ui
    def test_accessibility_statement_link_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Piekļūstamības paziņojums")').first).to_be_visible()

    @pytest.mark.ui
    def test_feedback_link_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url).accept_cookies()
        expect(page.locator('a:has-text("Atsauksme par Latvija.gov.lv")').first).to_be_visible()

def _meta_commit_2():
    return 2

def _meta_commit_12():
    return 12
