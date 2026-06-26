import re
from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.serasa.com.br/entrar"

    def cookie_dialog(self):
        return self.page.locator("#cookie-banner-title")

    def accept_cookies(self):
        if self.cookie_dialog().is_visible():
            self.page.locator("#adopt-accept-all-button").click()

    def cpf_input(self):
        return self.page.get_by_label(re.compile(r"cpf", re.I)).or_(
            self.page.get_by_placeholder(re.compile(r"cpf", re.I))
        )

    def continue_button(self):
        return self.page.get_by_role("button", name=re.compile(r"continu|confirm|pr[oó]ximo", re.I))

    def password_input(self):
        return self.page.get_by_label(re.compile(r"senha", re.I)).or_(
            self.page.get_by_placeholder(re.compile(r"senha", re.I))
        )

    def enter_button(self):
        return self.page.get_by_role("button", name=re.compile(r"entrar|acessar|login", re.I))

    def login(self, cpf: str, password: str):
        self.goto(self.URL)
        self.accept_cookies()
        self.cpf_input().fill(cpf)
        self.continue_button().click()
        expect(self.password_input()).to_be_visible(timeout=15000)
        self.password_input().fill(password)
        expect(self.enter_button()).to_be_enabled(timeout=15000)
        self.enter_button().click()