#importando SQLite
import sqlite3 as lite

#criando conexão
con = lite.connect('dados.db')

lista = ['Pyhhon','py@mail.com', 123456789, "31/07/2023", 'Normal', 'gostaria de o consultar pessoalmente']

#Create
def inserir_info(i):
    with con:
        cur = con.cursor()
        query ="INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES(?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

inserir_info(lista)

#Read
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query ="SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        
        for i in info:
            lista.append(i)
    return lista

#Update
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query ="UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)

#Delete
def deletar_info(i):
    with con:
        cur = con.cursor()
        query ="DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)