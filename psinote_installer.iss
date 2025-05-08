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
Source: "installer\criar_tabelas.py"; DestDir: "{app}\installer"; Flags: ignoreversion
Source: "installer\python\python-3.11.4-amd64.exe"; DestDir: "{tmp}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\PsiNote"; Filename: "{app}\PsiNote.exe"; IconFilename: "{app}\icon.ico"

[Run]
; Instala Python se não estiver instalado
Filename: "{tmp}\python-3.12.10-amd64.exe"; Parameters: "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0"; StatusMsg: "Instalando Python..."; Check: not PythonIsInstalled

; Roda o script para criar o banco SQLite
Filename: "python"; Parameters: """{app}\installer\criar_tabelas.py"""; StatusMsg: "Criando banco de dados..."; Flags: postinstall waituntilterminated skipifsilent

; Executa o PsiNote
Filename: "{app}\PsiNote.exe"; Description: "Iniciar PsiNote"; Flags: nowait postinstall skipifsilent

[Code]
function PythonIsInstalled(): Boolean;
var
  ErrorCode: Integer;
begin
  Result := Exec('python', '--version', '', SW_HIDE, ewWaitUntilTerminated, ErrorCode);
end;
