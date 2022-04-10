import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeSearchBehaviors:
    
    @pytest.mark.regression
    def test_search_accepts_text(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        locator = page.locator('input[aria-label*="Meklēšanas"]').first
        locator.fill('pensija')
        expect(locator).to_have_value('pensija')

    @pytest.mark.regression
    def test_search_clears_text(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        locator = page.locator('input[aria-label*="Meklēšanas"]').first
        locator.fill('abc')
        locator.fill('')
        expect(locator).to_have_value('')

    @pytest.mark.regression
    def test_search_allows_latvian_chars(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        locator = page.locator('input[aria-label*="Meklēšanas"]').first
        locator.fill('āčēīū')
        expect(locator).to_have_value('āčēīū')

    @pytest.mark.ui
    def test_search_button_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('button', name=lambda n: 'Meklēt' in n)).to_be_visible()

    @pytest.mark.ui
    def test_search_placeholder_present(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        ph = page.locator('input[placeholder*="Meklēt"]').first
        expect(ph).to_be_visible()

    @pytest.mark.ui
    def test_search_input_is_enabled(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        locator = page.locator('input[aria-label*="Meklēšanas"]').first
        expect(locator).to_be_enabled()

    @pytest.mark.ui
    def test_search_input_focusable(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        locator = page.locator('input[aria-label*="Meklēšanas"]').first
        locator.focus()
        expect(locator).to_be_focused()

    @pytest.mark.ui
    def test_search_input_not_password(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        t = page.locator('input[aria-label*="Meklēšanas"]').first.get_attribute('type')
        assert t in (None, 'text', 'search')

def _meta_commit_6():
    return 6
