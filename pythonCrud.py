import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='mydb',
)

cursor = conexao.cursor()

#crud

nome = ""
endereco = ""
telefone = ""
comando = f'INSERT  INTO cinema (nome , endereco , telefone) values ("{nome}" , "{endereco}" , "{telefone}")'
cursor.execute(comando)
conexao.commit() 

nome = ""
genero = ""
diretor = ""
faixa_etaria = ""
comando = f'INSERT  INTO filme (nome , genero , diretor , faixa_etaria ) values ("{nome}" , "{genero}" , "{diretor}" , "{faixa_etaria}")'
cursor.execute(comando)
conexao.commit() 

inicio = ""
fim = ""
idcinema = ""
idfilme = ""
comando = f'INSERT  INTO exibicao (inicio , fim , idcinema , idfilme ) values ("{inicio}" , "{fim}" , "{idcinema}" , "{idfilme}")'
cursor.execute(comando)
conexao.commit() 

comando = f'SELECT * FROM filme'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

comando = f'SELECT * FROM cinema'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

comando = f'SELECT * FROM exibicao'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

idcinema = ""
comando = f'DELETE FROM cinema WHERE idcinema = "{idcinema}"'
cursor.execute(comando)
conexao.commit()

idfilme = ""
comando = f'DELETE FROM filme WHERE idfilme = "{idfilme}"'
cursor.execute(comando)
conexao.commit()

inicio = ""
comando = f'DELETE FROM exibicao WHERE inicio = "{inicio}"'
cursor.execute(comando)
conexao.commit()

nome = ""
idcinema = ""
comando = f'UPDATE cinema SET nome = {nome} WHERE idcinema = "{idcinema}"'
cursor.execute(comando)
conexao.commit()

nome = ""
idfilme = ""
comando = f'UPDATE filme SET nome = {nome} WHERE idfilme = "{idfilme}"'
cursor.execute(comando)
conexao.commit()

inicio = ""
fim = ""
comando = f'UPDATE cinema SET inicio = {inicio} WHERE fim = "{fim}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
