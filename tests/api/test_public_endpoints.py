import pytest
import requests

@pytest.mark.api
@pytest.mark.smoke
def test_serasa_home_is_reachable():
    r = requests.get("https://www.serasa.com.br", timeout=20)
    assert r.status_code in (200, 301, 302)

@pytest.mark.api
def test_login_page_is_reachable():
    r = requests.get("https://www.serasa.com.br/entrar", timeout=20)
    assert r.status_code in (200, 301, 302)
