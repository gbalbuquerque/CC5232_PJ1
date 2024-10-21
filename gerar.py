import mysql.connector
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
    nome = fake.name()
    cursor.execute("INSERT INTO artista (nome) VALUES (%s)", (nome,))
for _ in range(20):
    data = fake.date()
    novaData = data.replace('-','/')  
    cursor.execute("INSERT INTO artista (data_nascimento) VALUES (%s)",(novaData))

# Dados aleatórios disco
for _ in range(20):
    titulo = lorem.words(4)
    cursor.execute("INSERT INTO disco (titulo) VALUES (%s)", (titulo))

conexao.commit()

conexao.close()
cursor.close()    