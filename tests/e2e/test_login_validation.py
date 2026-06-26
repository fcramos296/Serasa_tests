import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

@pytest.mark.e2e
def test_empty_login_shows_validation(settings, page):
    login = LoginPage(page)
    login.goto(settings.base_url)
    expect(login.continue_button()).to_be_disabled()

def test_continue_button_becomes_enabled_after_cpf(settings, page):
    login = LoginPage(page)
    login.goto(settings.base_url)
    login.cpf_input().fill("10954527623")
    expect(login.continue_button()).to_be_enabled()