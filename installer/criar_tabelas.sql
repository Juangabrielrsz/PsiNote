-- criar_tabelas.sql
-- Script de criação das tabelas do PsiNote para SQLite
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nascimento DATE,
    telefone TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    texto TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_paciente TEXT NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL
);
