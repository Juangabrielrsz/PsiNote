import PyInstaller.__main__

PyInstaller.__main__.run([
    '../app/main.py',         # Caminho relativo
    '--onefile',
    '--windowed',
    '--icon=recursos/icone.ico',
    '--name=PsiNote'
])
