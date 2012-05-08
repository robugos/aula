#!/usr/bin/python2
 
# Importa o modulo de conexao com o mysql
import MySQLdb
 
# Gera a string de conexao ex.: seu host, seu usuario, sua senha e seu db
db = MySQLdb.connect("7.16.20.75", "robson", "ulrich11", "AULADB")
# Posiciona o cursor
cursor = db.cursor()
# Executa a consulta na tabela selecionada
cursor.execute("SELECT * FROM AULADB.DEPARTAMENTOS")
# Conta o numero de linhas na tabela
numrows = int(cursor.rowcount)
# Algumas frescuras
print "--------------------------------------------------"
print "| ID  Campo                                      |"
print "--------------------------------------------------"
# Laco for para retornar os valores, ex.: row[0] primeira coluna, row[1] segunda coluna, row[2] terceira coluna, etc.
for row in cursor.fetchall():
   print "\t",row[0],"\t",row[1]
# Mais algumas frescuras
print "--------------------------------------------------"
print "|Teste de conexao com o Mysql em python          |"
print "--------------------------------------------------"