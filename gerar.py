import mysql.connector
import random
from faker import Faker
from lorem_text import lorem

fake = Faker()

#Conexão com o db
conexao = mysql.connector.connect(
    host = 'localhost',
    database = 'spotify',
    user = 'root',
    password = 'master'
)

if conexao.is_connected():
    print("Conectado ao banco de dados com sucesso!")
    cursor = conexao.cursor()
    
# Dados aleatórios artista
for _ in range(20):
    data = fake.date()
    nome = fake.name()
    cursor.execute("INSERT INTO artista (nome,data_nascimento) VALUES (%s,%s)", (nome,data))
for _ in range(20):
    titulo = lorem.words(4)
    data = fake.date()
    cursor.execute("INSERT INTO artista (nome,data_nascimento) VALUES (%s,%s)", (nome,data))


conexao.commit()

cursor.execute("SELECT id FROM artista")
artistas = cursor.fetchall()

# Gerar dados aleatórios para Discos
for _ in range(20):
    titulo = lorem.words(4)
    data_lancamento = fake.date()
    artista_id = random.choice(artistas)[0]

    cursor.execute("INSERT INTO disco (titulo, data_lancamento, artista_id) VALUES (%s, %s, %s)",  (titulo, data_lancamento, artista_id))

conexao.commit()

# Gerar dados aleatórios para Musica

cursor.execute("SELECT id FROM disco")
discos = cursor.fetchall()

for _ in range(50):
    titulo = lorem.words(3)
    duracao = round(random.uniform(0, 5.5),2)
    artista_id = random.choice(artistas)[0]
    disco_id = random.choice(discos)[0]
    cursor.execute("INSERT INTO musica (titulo, duracao, artista_id, disco_id) VALUES (%s, %s, %s, %s)", (titulo, duracao, artista_id, disco_id))

conexao.commit()

# Gerar dados aleatórios para Usuario

lista_de_dominios = (
    'com',
    'com.br',
    'net',
    'net.br',
    'org',
    'org.br',
    'gov',
    'gov.br'
)

for _ in range(20):
    primeiro_nome = fake.first_name()
    ultimo_nome = fake.last_name()

    company = fake.company().split()[0].strip(',')
    dns_org = fake.random_choices(
        elements=lista_de_dominios,
        length=1
    )[0]
    email = f"{primeiro_nome}.{ultimo_nome}@{company}.{dns_org}".lower()
    nome = fake.name()
    data_registro = fake.date()

    cursor.execute("INSERT INTO usuario (nome,email,data_registro) VALUES (%s, %s, %s)" , (nome,email,data_registro))

# Gerar dados aleatórios para Playlist

cursor.execute("SELECT id FROM usuario")
usuarios = cursor.fetchall()

for _ in range(20):
    titulo = lorem.words(3)
    usuario_id = random.choice(usuarios)[0]
    cursor.execute("INSERT INTO playlist (titulo,usuario_id) VALUES (%s,%s)",(titulo,usuario_id))

conexao.commit()

conexao.close()
cursor.close()    