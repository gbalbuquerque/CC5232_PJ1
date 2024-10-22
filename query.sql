create database spotify;

use spotify;

CREATE TABLE musica(
    id INT PRIMARY KEY auto_increment,
    titulo varchar(255),
    duracao int,
    disco_id int,
    artista_id int
    FOREIGN KEY (disco_id) REFERENCES Disco(id)
   
);

CREATE TABLE disco (
  id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(255) NOT NULL,
  data_lancamento DATE NOT NULL,
  artista_id INT NOT NULL
  musica_ids TEXT
  FOREIGN KEY (artista_id) REFERENCES Artista(id)

);

CREATE TABLE artista (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  data_nascimento DATE
  FOREIGN KEY (musica_id) REFERENCES Musica(id),
  FOREIGN KEY (artista_id) REFERENCES Artista(id)
);

CREATE TABLE usuario (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  data_registro DATE NOT NULL
);

CREATE TABLE playlist (
  id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(255) NOT NULL,
  usuario_id INT NOT NULL
  FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
  musica_ids TEXT
);

