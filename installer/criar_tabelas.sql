-- Tabela de Pacientes
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nascimento TEXT,
    cpf TEXT UNIQUE,
    telefone TEXT,
    endereco TEXT,
    email TEXT
);

-- Tabela de Prontuários
CREATE TABLE IF NOT EXISTS prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    texto TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE CASCADE
);

-- Tabela de Consultas
CREATE TABLE IF NOT EXISTS consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER,
    nome_paciente TEXT,
    data TEXT,
    hora TEXT,
    observacoes TEXT,
    FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
);