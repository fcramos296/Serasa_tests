@echo off
setlocal enabledelayedexpansion

echo ==============================
echo  Verificando Python
echo ==============================

where python >nul 2>nul
if errorlevel 1 (
    echo Python nao encontrado.

    where winget >nul 2>nul
    if not errorlevel 1 (
        echo Instalando Python via winget...
        winget install -e --id Python.Python.3.12
    ) else (
        echo winget nao encontrado. Instale Python manualmente em:
        echo https://www.python.org/downloads/windows/
        pause
        exit /b 1
    )
)

python --version

echo ==============================
echo  Verificando pip
echo ==============================

python -m pip --version >nul 2>nul
if errorlevel 1 (
    echo pip nao encontrado. Instalando via ensurepip...
    python -m ensurepip --upgrade
)

python -m pip install --upgrade pip

echo ==============================
echo  Informando CPF
echo ==============================

set /p SERASA_CPF=Digite um CPF valido: 

if "%SERASA_CPF%"=="" (
    echo CPF nao informado.
    pause
    exit /b 1
)

echo ==============================
echo  Criando .env
echo ==============================

(
    echo SERASA_CPF=%SERASA_CPF%
    echo BASE_URL=https://www.serasa.com.br/entrar
) > .env

echo Arquivo .env criado com sucesso.

echo ==============================
echo  Criando virtualenv
echo ==============================

if not exist ".venv" (
    python -m venv .venv
)

call .venv\Scripts\activate.bat

echo ==============================
echo  Instalando dependencias
echo ==============================

pip install -r requirements.txt

echo ==============================
echo  Instalando Playwright
echo ==============================

python -m playwright install

echo ==============================
echo  Concluido
echo ==============================
pause