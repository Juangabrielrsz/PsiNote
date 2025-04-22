@echo off
:: Script para instalar PostgreSQL e criar banco + tabelas do PsiNote

echo Instalando PostgreSQL...

:: Caminho do instalador
cd installer\postgresql

:: Instalação silenciosa do PostgreSQL
postgresql-15.5-windows-x64.exe --mode unattended ^
--unattendedmodeui none ^
--superpassword "123" ^
--servicename "psinote_postgres" ^
--serviceaccountpassword "123" ^
--datadir "C:\psinote_postgres\data" ^
--serverport 5432 ^
--install_runtimes 0

cd ../..

:: Aguarda o serviço iniciar
timeout /t 10 /nobreak > nul

echo Criando banco de dados e tabelas...

:: Define a senha para o usuário postgres
set PGPASSWORD=123

:: Executa o script SQL
"C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -h localhost -p 5432 -f "%~dp0criar_banco.sql"

echo Banco de dados e tabelas criados com sucesso!
pause
