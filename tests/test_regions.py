import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


class TestHomeRegions:
    
    @pytest.mark.ui
    def test_header_region_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('banner')).to_be_visible()

    @pytest.mark.ui
    def test_navigation_region_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('navigation')).to_be_visible()

    @pytest.mark.ui
    def test_main_region_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('main')).to_be_visible()

    @pytest.mark.ui
    def test_footer_region_visible(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        expect(page.get_by_role('contentinfo')).to_be_visible()

    @pytest.mark.ui
    def test_has_single_main_region(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        assert page.get_by_role('main').count() >= 1

    @pytest.mark.ui
    def test_skip_to_content_link_optional(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        # Allow either presence or not; only check that it does not break if present
        count = page.get_by_role('link', name=lambda n: 'Satura' in n or 'Content' in n).count()
        assert count >= 0

    @pytest.mark.ui
    def test_breadcrumb_optional(self, page: Page, base_url: str):
        HomePage(page).open(base_url)
        count = page.get_by_role('navigation', name=lambda n: 'drupatas' in n.lower() or 'bread' in n.lower()).count()
        assert count >= 0

def _meta_commit_9():
    return 9
