# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def editarID(cursor, id_novo, id_disciplina):
    sql = "update disciplinas set id_disciplina='%s' where id_disciplina='%s'" %(id_novo, id_disciplina)
    try:
        cursor.execute(sql)
        db.commit()
        print "ID editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarNome(cursor, nome, id_disciplina):
    sql = "update disciplinas set nome_disciplina='%s' where id_disciplina='%s'" %(nome, id_disciplina)
    try:
        cursor.execute(sql)
        db.commit()
        print "Nome da disciplina editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarCurso(cursor, curso, id_disciplina):
    sql = "update disciplinas set curso_disciplina='%s' where id_disciplina='%s'" %(curso, id_disciplina)
    try:
        cursor.execute(sql)
        db.commit()
        print "Curso da disciplina editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================

print "------ EDIÇÃO DE DISCIPLINAS ------"
saida = None
while saida <> "s":
    id_disciplina = raw_input('Digite o id da disciplina que deseja editar: ')
    verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(id_disciplina)
    existe = cursor.execute(verificar_dis)
    if existe < 1:
        print "ID não existente."
        continue
    else:
        opcao = input("Digite 1 (editar id), 2 (editar nome) ou 3 (editar curso): ")
        if opcao > 3 or opcao < 1:
            print "Opção incorreta."
            continue
        else:
            if opcao == 1:
                id_novo = raw_input("Digite o novo ID da disciplina: ")
                editarID(cursor, id_novo, id_disciplina)
            if opcao == 2:
                nome = raw_input("Digite o novo nome da disciplina: ")
                editarNome(cursor, nome, id_disciplina)
            if opcao == 3:
                curso = raw_input("Digite o id do novo curso: ")
                verificar_curso = "select id_curso from cursos where id_curso='%s'" %(curso)
                existe = cursor.execute(verificar_curso)
                if existe < 1:
                    print "Curso não existente."
                else:
                    editarCurso(cursor, curso, id_disciplina)
            saida = raw_input('Digite s para sair ou enter pra continuar: ')
print "------ FINISH ------"
db.close()
