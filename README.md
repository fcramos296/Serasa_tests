# Serasa Playwright POM

Projeto de testes automatizados com Pytest + Playwright usando Page Object Model para cenários básicos de E2E e API.

## Instalação
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install
```

## .env
Crie um arquivo `.env` na raiz do projeto:
```env
SERASA_CPF=cpf_valido
BASE_URL=https://www.serasa.com.br/entrar
```

## Execução
```bash
pytest
pytest -m e2e
pytest -m api
pytest -m smoke
```
