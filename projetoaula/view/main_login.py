# -*- coding: cp1252 -*-
from login import *

Login = Login_professor()
end=0
while end == 0:
    cpf = raw_input("Digite o login (CPF): ")
    verificar_CPF = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(cpf)
    existe = cursor.execute(verificar_CPF)
    if existe < 1:
        print "Usuario não existente."
        continue
    else:
        Login.prof_CPF(cpf)
        acesso = False
        while acesso == False:
            senha = raw_input("Digite a senha: ")
            verificar_senha = "select usuario_cpf='%s' from usuarios where senha='%s'" %(cpf,senha)
            executar = cursor.execute(verificar_senha)
            if executar < 1:
                print "Senha incorreta."
            else:
                acesso = True
                Login.userSenha(senha)
        if acesso == True:
            cursor.execute("SELECT * FROM usuarios where usuario_cpf='%s'" %(cpf))
            for row in cursor.fetchall():
                classe_user = row[2]

            if classe_user == 1:
                print "ADM"
            else:
                print "PROF"
        end=1