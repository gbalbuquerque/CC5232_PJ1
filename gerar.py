import mysql.connector
from faker import Faker
from lorem_text import lorem

conexao = mysql.connector.connect(
    host = 'localhost',
    database = 'spotify',
    user = 'root',
    password = 'master'
)

if conexao.is_connected():
    print("Conectado ao banco de dados com sucesso!")
    cursor = conexao.cursor()



conexao.close()
cursor.close()    