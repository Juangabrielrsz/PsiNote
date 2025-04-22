@echo off
:: instalar_postgres.bat
:: Instala PostgreSQL 15.5 de forma silenciosa com senha padrão 123

echo Instalando PostgreSQL...

cd installer\postgresql
postgresql-15.5-windows-x64.exe --mode unattended ^
--unattendedmodeui none ^
--superpassword "123" ^
--servicename "psinote_postgres" ^
--serviceaccountpassword "123" ^
--datadir "C:\psinote_postgres\data" ^
--serverport 5432 ^
--install_runtimes 0
cd ../..

echo PostgreSQL instalado com sucesso.
