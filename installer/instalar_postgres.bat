@echo off
:: Script para instalar PostgreSQL e criar banco + tabelas do PsiNote
:: Caminho do instalador
cd installer\postgresql

:: Verifica se o PostgreSQL já está instalado
IF EXIST "C:\Program Files\PostgreSQL\15\bin\psql.exe" (
    echo PostgreSQL já está instalado. Prosseguindo com a criação das tabelas...
) ELSE (
    echo Instalando PostgreSQL...

    :: Instalação silenciosa do PostgreSQL
    postgresql-15.5-windows-x64.exe --mode unattended ^
    --unattendedmodeui none ^
    --superpassword "123" ^
    --servicename "psinote_postgres" ^
    --serviceaccountpassword "123" ^
    --datadir "C:\psinote_postgres\data" ^
    --serverport 5432 ^
    --install_runtimes 0

    :: Aguarda o serviço iniciar
    timeout /t 10 /nobreak > nul
)

:: Criando banco de dados e tabelas
echo Criando banco de dados e tabelas...

:: Define a senha para o usuário postgres
set PGPASSWORD=123

:: Verifica se o banco já existe, caso não, cria
psql -U postgres -h localhost -p 5432 -c "SELECT 1 FROM pg_database WHERE datname = 'psinote'" | findstr /c:"1" >nul
IF ERRORLEVEL 1 (
    :: Banco de dados não existe, então cria
    echo Criando o banco de dados...
    "C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -h localhost -p 5432 -c "CREATE DATABASE psinote"
) ELSE (
    echo O banco de dados 'psinote' já existe. Prosseguindo com a criação das tabelas...
)

:: Executa o script SQL para criar as tabelas
"C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -h localhost -p 5432 -d psinote -f "%~dp0criar_banco.sql"

echo Banco de dados e tabelas criados com sucesso!
pause
