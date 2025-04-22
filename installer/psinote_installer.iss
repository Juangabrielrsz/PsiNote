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
Source: "dist\PsiNote.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\PsiNote"; Filename: "{app}\PsiNote.exe"; IconFilename: "{app}\icon.ico"

[Run]
Filename: "{app}\PsiNote.exe"; Description: "Iniciar PsiNote"; Flags: nowait postinstall skipifsilent