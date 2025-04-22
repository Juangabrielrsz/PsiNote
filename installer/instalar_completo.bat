@echo off
:: instalar_completo.bat
:: Script mestre que instala PostgreSQL, configura o banco e instala o PsiNote

cls
echo Iniciando instalador completo do PsiNote...

:: Etapa 1: Instalar PostgreSQL
call installer\instalar_postgres.bat

:: Aguarda o serviço iniciar completamente
echo Aguardando inicialização do PostgreSQL...
timeout /t 10 /nobreak

:: Etapa 2: Criar banco e tabelas
set PSQL_PATH="C:\Program Files\PostgreSQL\15\bin\psql.exe"
%PSQL_PATH% -U postgres -d postgres -f installer\criar_banco.sql

:: Etapa 3: Criar o executável
python installer\setup_installer.py

:: Etapa 4: Criar atalho na área de trabalho
python installer\criar_atalho.py

echo Instalacao concluida com sucesso!
pause