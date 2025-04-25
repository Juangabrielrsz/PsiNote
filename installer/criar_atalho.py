import os
import win32com.client

def criar_atalho():
    nome_app = 'PsiNote'
    caminho_exe = os.path.abspath(os.path.join('..', 'dist', f'{nome_app}.exe'))
    caminho_icone = os.path.abspath(os.path.join('recursos', 'PsiNote.ico'))
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    caminho_atalho = os.path.join(desktop, f'{nome_app}.lnk')

    shell = win32com.client.Dispatch("WScript.Shell")
    atalho = shell.CreateShortCut(caminho_atalho)
    atalho.TargetPath = caminho_exe
    atalho.IconLocation = caminho_icone
    atalho.Save()

if __name__ == '__main__':
    criar_atalho()
