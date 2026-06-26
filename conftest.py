import os
from dataclasses import dataclass

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://www.serasa.com.br/entrar")
    cpf: str = os.getenv("SERASA_CPF", "")
    password: str = os.getenv("SERASA_PASSWORD", "")

@pytest.fixture(scope="session")
def settings():
    return Settings()

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(locale="pt-BR", viewport={"width": 1440, "height": 1080})
        page = context.new_page()
        yield page
        context.close()
        browser.close()
