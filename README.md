# Serasa Playwright POM

Projeto de testes automatizados com Pytest + Playwright usando Page Object Model para cenários básicos de E2E e API.

## Instalação
```bash
Baixe ou clone o repositório e execute o arquivo Setup.bat, ele fará todo o necessário para executar os testes.

- Verifica se o Python existe.
- Instala Python se necessário.
- Verifica pip e o instala se necessário.
- Pede ao usuário para digitar um CPF válido para teste.
- Cria o arquivo .env na raiz do projeto.
- Cria/ativa um ambiente virtual.
- Instala dependências.
- Instala Playwright e seus browsers se necessário.
```

## Execução
```bash
pytest (executa ambos os testes)
pytest -m e2e (executa apenas testes e2e)
pytest -m api (executa paenas testes de api)
```
