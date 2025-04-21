@echo off
echo Instalando PsiNote...

REM Cria o executável
cd /d %~dp0
python setup_installer.py

REM Cria o atalho
python criar_atalho.py

echo Instalação concluída com sucesso!
pause
