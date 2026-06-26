import pytest
import requests

@pytest.mark.api
def test_login_page_returns_html():
    r = requests.get("https://www.serasa.com.br/entrar", timeout=20)
    assert "text/html" in r.headers.get("content-type", "")
