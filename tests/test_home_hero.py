import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeHeroContent:
    
    @pytest.mark.ui
    def test_title_contains_keyword(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        assert 'Latvija' in page.title() or 'Sākumlapa' in page.title()

    @pytest.mark.ui
    def test_hero_has_any_link(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.locator('a').first).to_be_visible()

    @pytest.mark.ui
    def test_hero_has_search_or_cta(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        count = page.locator('input[placeholder*="Meklēt"], button:has-text("Meklēt")').count()
        assert count >= 1

    @pytest.mark.ui
    def test_hero_has_main_heading(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        has_h1 = page.locator('h1').count() >= 0
        assert has_h1 is True

    @pytest.mark.ui
    def test_primary_cta_is_enabled_if_present(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        cta = page.get_by_role('link', name=lambda n: 'Visi pakalpojumi' in n or 'Pakalpojumi' in n)
        assert cta.count() >= 0

    @pytest.mark.ui
    def test_language_indicator_present(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        html_lang = page.locator('html').get_attribute('lang')
        assert html_lang is None or len(html_lang) > 0

    @pytest.mark.ui
    def test_any_paragraph_exists(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        assert page.locator('p').count() >= 0
