# setup_installer.py
# Gera um instalador usando Inno Setup a partir do script .iss

import subprocess
import os

INNO_SETUP_PATH = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
SCRIPT_PATH = os.path.join("installer", "psinote_installer.iss")

if not os.path.exists(INNO_SETUP_PATH):
    print("Erro: Inno Setup não está instalado no caminho padrão.")
    exit(1)

if not os.path.exists(SCRIPT_PATH):
    print("Erro: Script .iss não encontrado em installer/psinote_installer.iss")
    exit(1)

subprocess.run([INNO_SETUP_PATH, SCRIPT_PATH])
print("Instalador gerado com sucesso!")
