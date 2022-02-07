from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        self.page.goto(url)
    
    def get_title(self) -> str:
        return self.page.title()
    
    def get_url(self) -> str:
        return self.page.url
    
    def wait_for_load_state(self, state: str = "networkidle"):
        self.page.wait_for_load_state(state)
    
    def click(self, selector: str):
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()
    
    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).first.is_visible()
    
    def screenshot(self, path: str):
        self.page.screenshot(path=path)


