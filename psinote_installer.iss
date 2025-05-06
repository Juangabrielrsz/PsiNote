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
Source: "dist\PsiNote.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "installer\recursos\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "installer\instalar_completo.bat"; DestDir: "{app}\installer"; Flags: ignoreversion
Source: "installer\criar_tabelas.sql"; DestDir: "{app}\installer"; Flags: ignoreversion
Source: "installer\criar_tabelas.py"; DestDir: "{app}\installer"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\PsiNote"; Filename: "{app}\PsiNote.exe"; IconFilename: "{app}\icon.ico"

[Run]
Filename: "{app}\installer\instalar_completo.bat"; StatusMsg: "Inicializando banco de dados..."; Flags: runhidden
Filename: "{app}\PsiNote.exe"; Description: "Iniciar PsiNote"; Flags: nowait postinstall skipifsilent
