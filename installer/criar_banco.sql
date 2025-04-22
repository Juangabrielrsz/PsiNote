-- criar_banco.sql
-- Script de criação do banco e tabelas do PsiNote

-- Criação do banco de dados (executado no banco postgres)
CREATE DATABASE psinote;

\c psinote

-- Tabela de pacientes
CREATE TABLE pacientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    nascimento DATE,
    telefone VARCHAR(20),
    email VARCHAR(255)
);

-- Tabela de prontuários
CREATE TABLE prontuarios (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(id) ON DELETE CASCADE,
    texto TEXT
);

-- Tabela de consultas
CREATE TABLE consultas (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(id) ON DELETE CASCADE,
    data DATE NOT NULL,
    hora TIME NOT NULL
);
