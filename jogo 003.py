import mysql.connector

conexao = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='Ma131997',
    database ='phyton',
)

cursor = conexao.cursor()

#CRUD
nome_produto = "toddynho"
valor = 6
comando = f'DELETE FROM venda WHERE nome_produto =  "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #Editar o banco de dados



cursor.close()
conexao.close()



#CREATE
#nome_produto = "chocolate"
#valor = 15
#comando = f'INSERT INTO venda (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit() #Editar o banco de dados


#READ
#comando = f'SELECT * FROM phyton.venda;'
#cursor.execute(comando)
#conexao.commit() #Editar o banco de dados
#resultado = cursor.fetchall() #ler o banco de dados
#print(resultado)


#UPDATE
#nome_produto = "toddynho"
#valor = 6
#comando = f'UPDATE venda SET VALOR = {valor} WHERE nome_produto =  "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()
#DELETE
