!define APP_NAME "PsiNote"
!define APP_VERSION "1.0"
!define APP_EXE "main\\main.exe"
!define DB_FILE "psinote.db"

OutFile "PsiNote_Installer.exe"
InstallDir "$PROGRAMFILES\\${APP_NAME}"
RequestExecutionLevel admin
SetCompress auto
SetCompressor lzma

!include "MUI2.nsh"

Name "${APP_NAME}"
BrandingText "Instalador do PsiNote"
InstallDirRegKey HKLM "Software\\${APP_NAME}" ""

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

Section "Instalar PsiNote" SEC01
  SetOutPath "$INSTDIR"
  File /r "dist\\*.*" ; ✅ Copia tudo da build

  CreateDirectory "$INSTDIR\\app"
  SetOutPath "$INSTDIR\\app"
  File "app\\${DB_FILE}"

  SetOutPath "$INSTDIR"
  File "installer\\recursos\\icon.ico"

  Call CheckPython
  Pop $0
  ${If} $0 == "0"
    DetailPrint "Instalando Python..."
    nsExec::Exec '"$TEMP\\python-installer.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0'
  ${EndIf}

  CreateShortCut "$DESKTOP\\${APP_NAME}.lnk" "$INSTDIR\\${APP_EXE}" "" "$INSTDIR\\icon.ico"

  ; Criação do desinstalador
  WriteUninstaller "$INSTDIR\\Uninstall.exe"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" "DisplayName" "${APP_NAME}"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" "UninstallString" "$\"$INSTDIR\\Uninstall.exe$\""
SectionEnd

Section "Arquivos Temporários"
  SetOutPath "$TEMP"
  File /oname=python-installer.exe "installer\\python\\python-3.11.4-amd64.exe"
SectionEnd

Function CheckPython
  nsExec::ExecToStack "python --version"
  Pop $0
  Pop $1
  ${If} $0 == "0"
    Push "1"
  ${Else}
    Push "0"
  ${EndIf}
FunctionEnd

;--------------------------------
; Desinstalação
Section "Uninstall"
  Delete "$INSTDIR\\${APP_EXE}"
  Delete "$INSTDIR\\icon.ico"
  Delete "$INSTDIR\\app\\${DB_FILE}"
  Delete "$DESKTOP\\${APP_NAME}.lnk"
  Delete "$INSTDIR\\Uninstall.exe"

  RMDir /r "$INSTDIR\\app"
  RMDir "$INSTDIR"

  DeleteRegKey HKLM "Software\\${APP_NAME}"
  DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}"
SectionEnd
