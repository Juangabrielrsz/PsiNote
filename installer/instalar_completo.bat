@echo off
cd /d %~dp0
cls
echo Instalando PsiNote...

:: Cria o banco e tabelas com Python
python criar_tabelas.py

echo Instalacao concluida com sucesso!
pause
