CREATE TABLE IF NOT EXISTS pacientes (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    nascimento DATE
);

CREATE TABLE IF NOT EXISTS consultas (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(id),
    data DATE NOT NULL,
    hora TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS prontuarios (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER REFERENCES pacientes(id),
    texto TEXT
);
