DROP DATABASE IF EXISTS clinica_medica;
CREATE DATABASE clinica_medica;
USE clinica_medica;

-- ============================
-- PACIENTES
-- ============================


CREATE TABLE pacientes (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    sexo ENUM('Masculino','Feminino','Outro') NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    cidade VARCHAR(60),
    estado CHAR(2),
    endereco VARCHAR(150),
    data_cadastro DATE NOT NULL
);

-- ============================
-- ESPECIALIDADES
-- ============================
CREATE TABLE especialidades (
    id_especialidade INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL UNIQUE
);

-- ============================
-- MÉDICOS
-- ============================
CREATE TABLE medicos (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    crm VARCHAR(20) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    email VARCHAR(100),
    salario DECIMAL(10,2),
    data_admissao DATE,
    id_especialidade INT NOT NULL,

    CONSTRAINT fk_medico_especialidade
        FOREIGN KEY (id_especialidade)
        REFERENCES especialidades(id_especialidade)
);

-- ============================
-- CONSULTÓRIOS
-- ============================
CREATE TABLE consultorios (
    id_consultorio INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(10) NOT NULL,
    bloco VARCHAR(20),
    andar INT
);

-- ============================
-- CONSULTAS
-- ============================
CREATE TABLE consultas (
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    id_consultorio INT NOT NULL,
    data_consulta DATE NOT NULL,
    horario TIME NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    status ENUM(
        'Agendada',
        'Realizada',
        'Cancelada'
    ) DEFAULT 'Agendada',
    observacoes VARCHAR(255),

    CONSTRAINT fk_consulta_paciente
        FOREIGN KEY (id_paciente)
        REFERENCES pacientes(id_paciente),

    CONSTRAINT fk_consulta_medico
        FOREIGN KEY (id_medico)
        REFERENCES medicos(id_medico),

    CONSTRAINT fk_consulta_consultorio
        FOREIGN KEY (id_consultorio)
        REFERENCES consultorios(id_consultorio)
);

-- ============================
-- PAGAMENTOS
-- ============================
CREATE TABLE pagamentos (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_consulta INT NOT NULL,
    forma_pagamento ENUM(
        'Dinheiro',
        'Pix',
        'Cartao Credito',
        'Cartao Debito'
    ) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data_pagamento DATE NOT NULL,
    status ENUM(
        'Pago',
        'Pendente'
    ) DEFAULT 'Pendente',

    CONSTRAINT fk_pagamento_consulta
        FOREIGN KEY (id_consulta)
        REFERENCES consultas(id_consulta)
);



-- ============================
-- ESPECIALIDADES
-- ============================
INSERT INTO especialidades (nome) VALUES
('Cardiologia'),
('Dermatologia'),
('Ortopedia'),
('Pediatria'),
('Neurologia');

-- ============================
-- CONSULTÓRIOS
-- ============================
INSERT INTO consultorios (numero, bloco, andar) VALUES
('101', 'A', 1),
('102', 'A', 1),
('201', 'B', 2),
('202', 'B', 2),
('301', 'C', 3);

-- ============================
-- MÉDICOS
-- ============================
INSERT INTO medicos
(nome, crm, telefone, email, salario, data_admissao, id_especialidade)
VALUES
('Dr. Carlos Pereira', 'CRM1001', '11999990001', 'carlos@clinica.com', 18000.00, '2022-01-10', 1),
('Dra. Ana Souza', 'CRM1002', '11999990002', 'ana@clinica.com', 16500.00, '2023-03-15', 2),
('Dr. Ricardo Lima', 'CRM1003', '11999990003', 'ricardo@clinica.com', 20000.00, '2021-06-20', 3),
('Dra. Juliana Costa', 'CRM1004', '11999990004', 'juliana@clinica.com', 15000.00, '2024-02-01', 4),
('Dr. Marcos Almeida', 'CRM1005', '11999990005', 'marcos@clinica.com', 22000.00, '2020-11-11', 5);

-- ============================
-- PACIENTES
-- ============================
INSERT INTO pacientes
(nome, cpf, data_nascimento, sexo, telefone, email, cidade, estado, endereco, data_cadastro)
VALUES
('João Silva', '12345678901', '1995-04-15', 'Masculino', '11998765432', 'joao@email.com', 'São Paulo', 'SP', 'Rua das Flores, 120', CURDATE()),
('Maria Oliveira', '23456789012', '1988-09-21', 'Feminino', '21999887766', 'maria@email.com', 'Rio de Janeiro', 'RJ', 'Av. Atlântica, 500', CURDATE()),
('Pedro Santos', '34567890123', '2000-01-30', 'Masculino', '31991234567', 'pedro@email.com', 'Belo Horizonte', 'MG', 'Rua Minas, 45', CURDATE()),
('Fernanda Lima', '45678901234', '1993-07-18', 'Feminino', '71995554433', 'fernanda@email.com', 'Salvador', 'BA', 'Rua Bahia, 80', CURDATE()),
('Lucas Almeida', '56789012345', '1998-11-11', 'Masculino', '85994443322', 'lucas@email.com', 'Fortaleza', 'CE', 'Av. Beira Mar, 910', CURDATE());

-- ============================
-- CONSULTAS
-- ============================
INSERT INTO consultas
(id_paciente, id_medico, id_consultorio, data_consulta, horario, valor, status, observacoes)
VALUES
(1, 1, 1, '2026-07-01', '09:00:00', 250.00, 'Realizada', 'Retorno anual'),
(2, 2, 2, '2026-07-03', '10:30:00', 180.00, 'Realizada', 'Consulta dermatológica'),
(3, 3, 3, '2026-07-05', '14:00:00', 300.00, 'Realizada', 'Dor no joelho'),
(4, 4, 4, '2026-07-08', '08:00:00', 150.00, 'Cancelada', 'Paciente remarcou'),
(5, 5, 5, '2026-07-10', '16:00:00', 350.00, 'Agendada', 'Primeira consulta'),
(1, 1, 1, '2026-08-01', '11:00:00', 250.00, 'Agendada', 'Exames recentes'),
(2, 2, 2, '2026-08-02', '15:00:00', 180.00, 'Agendada', 'Acompanhamento');



-- ============================
-- PAGAMENTOS
-- ============================
INSERT INTO pagamentos
(id_consulta, forma_pagamento, valor, data_pagamento, status)
VALUES
(1, 'Pix', 250.00, '2026-07-01', 'Pago'),
(2, 'Cartao Credito', 180.00, '2026-07-03', 'Pago'),
(3, 'Cartao Debito', 300.00, '2026-07-05', 'Pago'),
(4, 'Dinheiro', 150.00, '2026-07-08', 'Pendente'),
(5, 'Pix', 350.00, '2026-07-10', 'Pendente');



select
	p.nome as paciente,
    m.nome as medico,
    e.nome as especialidade,
    c.data_consulta,
    c.valor as valor_consulta
from pacientes p inner join consultas c on(p.id_paciente = c.id_paciente)
inner join medicos m on(m.id_medico = c.id_medico)
inner join especialidades e on(m.id_especialidade = e.id_especialidade)
group by p.nome, m.nome, e.nome, c.valor, c.data_consulta;

select
	m.nome as medico,
    count(c.id_consulta) as qtd_consultas,
    sum(c.valor) as faturamento
from medicos m inner join consultas c on(m.id_medico = c.id_medico)
group by m.nome
order by faturamento desc;

select
	e.nome as especialidade,
    count(c.id_consulta) as qtd_consultas,
    sum(c.valor) as faturamento,
    round(sum(c.valor) / count(c.id_consulta), 2) as ticket_medio
from consultas c inner join medicos m on(c.id_medico = m.id_medico)
inner join especialidades e on(m.id_especialidade = e.id_especialidade)
group by e.nome;

select
	p.nome as paciente,
    m.nome as medico,
    e.nome as especialidade,
    co.id_consultorio,
    c.data_consulta,
    pa.forma_pagamento,
    pa.status
from pacientes p inner join consultas c on(p.id_paciente = c.id_paciente)
inner join consultorios co on(co.id_consultorio = c.id_consultorio)
inner join medicos m on(m.id_medico = c.id_medico)
inner join especialidades e on(e.id_especialidade = m.id_especialidade)
inner join pagamentos pa on(pa.id_consulta = c.id_consulta)
group by p.nome, m.nome, e.nome, co.id_consultorio, c.data_consulta, pa.forma_pagamento, pa.status
order by paciente;

select
	m.nome as medico,
    sum(c.valor) as faturamento,
    rank() over(order by faturamento desc) as ranking
from medicos m join consultas c on(m.id_medico = c.id_medico)
group by m.nome
order by ranking;

select
	e.nome as especialidade,
    count(c.id_consulta) as qtd_consultas,
    dense_rank() over(order by c.id_consulta desc) as ranking
from consultas c join medicos m on(m.id_medico = c.id_medico)
join especialidades e on(e.id_especialidade = m.id_especialidade)
group by e.nome
order by ranking;


select
	data_consulta,
    row_number() over(order by data_consulta ) as ranking
from consultas;

WITH pacientes as(select
	p.nome as paciente,
    sum(c.valor) as faturamento
from pacientes p join consultas c on(p.id_paciente = c.id_paciente)
group by p.nome)
select
	paciente,
    faturamento,
    lag(faturamento) over(order by faturamento) as mes_anterior
from pacientes;


WITH relatorio_pacientes as(select
	p.nome as paciente,
    p.email,
    c.data_consulta,
    sum(c.valor) as faturamento,
    count(distinct c.id_consulta) as qtd_consulta,
    e.nome as especialidade,
    m.nome as medico,
    pa.forma_pagamento,
    pa.data_pagamento,
    pa.status
from pacientes p inner join consultas c on(c.id_paciente = p.id_paciente)
inner join medicos m on(m.id_medico = c.id_medico)
inner join especialidades e on(e.id_especialidade = m.id_especialidade)
inner join pagamentos pa on(pa.id_consulta = c.id_consulta)
group by p.nome, p.email, c.data_consulta, e.nome, m.nome, pa.forma_pagamento, pa.data_pagamento, pa.status),
ranking_pacientes as(
select
*,
    dense_rank() over(order by faturamento desc) as ranking
from relatorio_pacientes),
faturamento_anterior as(
select
*,
    lag(faturamento) over(order by faturamento) as faturamento_anterior
from ranking_pacientes),
crescimento_percentual as(select
*,
    round((faturamento - faturamento_anterior) / nullif(faturamento_anterior,0) * 100, 2) as crescimento_percentual
from faturamento_anterior),
percentual_participacao as(
select
  *,
    round(faturamento / nullif(sum(faturamento) over(),0) * 100, 2) as percentual_participacao
from crescimento_percentual),
classificacao_pacientes as(
select
*,
case
	when faturamento >= 7000 then 'Valor alto'
    when faturamento >= 5000 then 'Valor medio'
else 'Valor baixo'
end classificacao
from percentual_participacao)
select
* from classificacao_pacientes;
