
# 🧠 PsiNote

**PsiNote** é um aplicativo de gestão de pacientes para clínicas de psicologia, desenvolvido com **Python + PyQt6** e banco de dados **PostgreSQL**. Este projeto inclui interface moderna, cadastro de pacientes, prontuários, controle de consultas e um instalador completo para Windows.

---

## 🚀 Funcionalidades

- Cadastro de pacientes
- Registro de prontuários
- Controle de consultas
- Interface moderna com PyQt6
- Instalação automática do PostgreSQL
- Instalador gerado com Inno Setup

---

## 🛠 Tecnologias

- Python 3.11+
- PyQt6
- PostgreSQL 15.5
- PyInstaller
- Inno Setup

---

## 📁 Estrutura do Projeto

```
PsiNote/
├── app/                        # Código-fonte principal
│   ├── main.py                 # Arquivo principal
│   └── ...                    # Outros módulos PyQt6
├── installer/                 # Scripts de instalação
│   ├── instalar_postgres.bat  # Instala e configura o PostgreSQL
│   ├── criar_banco.sql        # Criação do banco e tabelas
│   ├── criar_atalho.py        # Cria atalho na área de trabalho
│   ├── psinote_installer.iss  # Script do Inno Setup
│   ├── setup_installer.py     # Gera instalador com Inno Setup
│   └── postgresql/            # Instalador do PostgreSQL
│       └── postgresql-15.5-windows-x64.exe
├── dist/                      # Executável gerado pelo PyInstaller
│   └── PsiNote.exe
├── instalar_completo.bat     # Instala tudo de forma automatizada
└── README.md
```

---

## 🧪 Etapas de Instalação (Manual)

### 1. Criação do Executável
Use o PyInstaller com a flag `--noconsole` para ocultar o terminal:

```bash
pyinstaller app/main.py --onefile --noconsole --name "PsiNote"
```

O executável será gerado em `dist/PsiNote.exe`.

### 2. Geração do Instalador

Certifique-se de ter o Inno Setup instalado em:
```text
C:\Program Files (x86)\Inno Setup 6\ISCC.exe
```

Execute:

```bash
python installer/setup_installer.py
```

Isso criará o instalador em `PsiNote_Installer.exe`.

---

## 🧰 Instalador Completo

### instalar_completo.bat

Este script:

1. Instala o PostgreSQL silenciosamente
2. Cria o banco de dados e tabelas
3. Gera o executável com PyInstaller
4. Gera o instalador com Inno Setup
5. Cria um atalho na área de trabalho

Execute com:

```bash
instalar_completo.bat
```

---

## 🧾 Configurações Importantes

- **Usuário padrão de login no app:** `admin`
- **Senha padrão:** `123`
- **Porta do PostgreSQL:** `5432`
- **Senha do PostgreSQL:** `123`
- **Banco de dados criado:** `psinote`

---

## 📦 Publicação

### 🚫 Evitando arquivos grandes no GitHub

O `.gitignore` foi configurado para **ignorar** arquivos grandes e temporários:

```gitignore
# Executável do instalador
PsiNote_Installer.exe
```

---

## ☁️ Upload no Google Drive

Para compartilhar o instalador:

1. Faça upload de `PsiNote_Installer.exe` no [Google Drive](https://drive.google.com)
2. Clique com o botão direito > Compartilhar
3. Defina como “Qualquer pessoa com o link”
4. Copie o link e compartilhe

---

## 📸 Capturas de Tela

> *(Adicione aqui screenshots da interface, se desejar)*

---

## 👨‍💻 Autor

**Juan Gabriel**  
Desenvolvedor e entusiasta de soluções para psicologia.  
[LinkedIn](https://linkedin.com) · [GitHub](https://github.com/Juangabrielrsz)

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
