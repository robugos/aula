import MySQLdb

class Servidor():
    def __init__ (self):
        self.user = "yoshi"
        self.password = "mario1234"
        self.host = "7.16.20.75"
        self.banco = "AULADB"

    def set_host(self,localhost):
        self.host = localhost
        
    def set_user(self,usuario):
        self.user = usuario
        
    def set_password(self,senha):
        self.password = senha
        
    def set_banco(self,nomedb):
        self.banco = nomedb
        
Serve = Servidor()

#Serve.set_host(raw_input("Host: "))
#Serve.set_user(raw_input("Usuario: "))
#Serve.set_password(raw_input("Senha: "))
#Serve.set_banco(raw_input("Nome Banco: "))

db = MySQLdb.connect(Serve.host,Serve.user,Serve.password,Serve.banco) 

#TESTESTESTESTES usaremos no outro arquivo
#cursor=db.cursor()
#sql="insert into DEPARTAMENTOS values( '0007','DEINFO','Giodano' ) "
#cursor.execute(sql)
#    
