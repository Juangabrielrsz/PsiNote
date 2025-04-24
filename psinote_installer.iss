; psinote_installer.iss
; Script do Inno Setup para gerar instalador do PsiNote

[Setup]
AppName=PsiNote
AppVersion=1.0
DefaultDirName={pf}\PsiNote
DefaultGroupName=PsiNote
UninstallDisplayIcon={app}\icon.ico
Compression=lzma
SolidCompression=yes
OutputDir=.
OutputBaseFilename=PsiNote_Installer

[Files]
Source: "app\dist\PsiNote.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "installer\instalar_postgres.bat"; DestDir: "{app}\installer"; Flags: ignoreversion
Source: "installer\criar_banco.sql"; DestDir: "{app}\installer"; Flags: ignoreversion
Source: "installer\postgresql\postgresql-15.5-windows-x64.exe"; DestDir: "{app}\installer\postgresql"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\PsiNote"; Filename: "{app}\PsiNote.exe"; IconFilename: "{app}\icon.ico"

[Run]
Filename: "{app}\installer\instalar_postgres.bat"; StatusMsg: "Instalando PostgreSQL e configurando banco..."; Flags: runhidden
Filename: "{app}\PsiNote.exe"; Description: "Iniciar PsiNote"; Flags: nowait postinstall skipifsilent
