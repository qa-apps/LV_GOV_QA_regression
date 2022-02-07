from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logo = 'a[aria-label="Sākumlapa"]'
        self.search_input = 'input[aria-label*="Meklēšanas ievadlauks"], input[placeholder*="Meklēt"]'
        self.search_button = 'button:has-text("Meklēt rezultātus")'
        self.login_link = 'a:has-text("Ienākt Mana Latvija.lv")'
        self.language_switcher = 'a[aria-label="Pārslēgties uz angļu valodu"]'
        self.services_menu = 'button:has-text("Pakalpojumi")'
        self.life_situations_menu = 'button:has-text("Ko darīt, ja...?")'
        self.my_latvija_menu = 'button:has-text("Mana Latvija.lv")'
        self.e_address_menu = 'button:has-text("E-adrese")'
        self.about_portal_menu = 'button:has-text("Par portālu")'
        self.all_services_link = 'a:has-text("Visi pakalpojumi")'
        self.all_life_situations_link = 'a:has-text("Visas dzīves situācijas")'
        self.cookie_accept_button = 'button:has-text("Piekrist visam")'
        self.cookie_manage_button = 'button:has-text("Pārvaldīt")'
    
    def open(self, base_url: str):
        self.navigate(f"{base_url}/Home/")
        self.wait_for_load_state("domcontentloaded")
    
    def accept_cookies(self):
        if self.is_visible(self.cookie_accept_button):
            self.click(self.cookie_accept_button)
    
    def search(self, query: str):
        self.fill(self.search_input, query)
        self.click(self.search_button)
    
    def switch_to_english(self):
        self.click(self.language_switcher)
    
    def click_login(self):
        self.click(self.login_link)
    
    def navigate_to_services(self):
        self.click(self.services_menu)
    
    def navigate_to_life_situations(self):
        self.click(self.life_situations_menu)
    
    def navigate_to_my_latvija(self):
        self.click(self.my_latvija_menu)
    
    def navigate_to_e_address(self):
        self.click(self.e_address_menu)
    
    def navigate_to_about_portal(self):
        self.click(self.about_portal_menu)
    
    def is_logo_visible(self) -> bool:
        return self.is_visible(self.logo)
    
    def is_search_visible(self) -> bool:
        return self.is_visible(self.search_input)
    
    def is_login_visible(self) -> bool:
        return self.is_visible(self.login_link)


