# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================
from Validacao import Validacao
#===============================================================================

def editarCPF(cursor, id_novo, id_CPF):
    sql = "update usuarios set usuario_cpf='%s' where usuario_CPF='%s'" %(id_novo, id_CPF)
    try:
        cursor.execute(sql)
        db.commit()
        print "CPF editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarSenha(cursor, senha, id_CPF):
    sql = "update usuarios set senha='%s' where usuario_cpf='%s'" %(senha, id_CPF)
    try:
        cursor.execute(sql)
        db.commit()
        print "Senha editada com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarClasse(cursor, classe, id_CPF):
    sql = "update usuarios set classe='%d' where usuario_cpf='%s'" %(classe, id_CPF)
    try:
        cursor.execute(sql)
        db.commit()
        print "Classe editada com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================

#print "------ EDIÇÃO DE USUARIO ------"
#saida = None
#teste = Validacao()
#while saida <> "s":
#    id_CPF = raw_input('Digite o CPF do usuario que deseja editar: ')
#    verificar_user = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(id_CPF)
#    existe = cursor.execute(verificar_user)
#    if existe < 1:
#        print "Usuario não existente."
#        continue
#    else:
#        opcao = input("Digite 1 (editar CPF), 2 (editar senha) ou 3 (editar classe): ")
#        if opcao > 3 or opcao < 1:
#            print "Opção incorreta."
#            continue
#        else:
#            if opcao == 1:
#                id_novo = raw_input("Digite o novo CPF do usuario: ")
#                editarCPF(cursor, id_novo, id_CPF)
#            if opcao == 2:
#                senha = teste.SENHA_Check(raw_input("Digite a nova senha do usuario: "))
#                editarSenha(cursor, senha, id_CPF)
#            if opcao == 3:
#                classe = input("Digite o valor da nova classe (0 ou 1): ")
#                editarClasse(cursor, classe, id_CPF)
#            saida = raw_input('Digite s para sair ou enter pra continuar: ')
#print "------ FINISH ------"
#db.close()
