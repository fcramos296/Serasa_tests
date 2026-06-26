import re
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

@pytest.mark.e2e
@pytest.mark.smoke
def test_login_page_loads(settings, page):
    login = LoginPage(page)
    login.goto(settings.base_url)
    expect(page).to_have_title(re.compile(r".+"))
    expect(page.locator("body")).to_be_visible()

@pytest.mark.e2e
def test_login_flow_with_valid_credentials(settings, page):
    if not settings.cpf or not settings.password:
        pytest.skip("Credenciais ausentes no .env")

    login = LoginPage(page)
    login.goto(settings.base_url)
    login.accept_cookies()
    login.cpf_input().fill(settings.cpf)
    login.continue_button().click()
