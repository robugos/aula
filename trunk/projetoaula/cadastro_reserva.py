# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
from exclusao_reserva import *
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================
from Validacao import Validacao
#===============================================================================


def cadastrarReserva(cursor, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, hora1, hora2):
    count_erro = 0
    for horario in range (hora1,hora2,1):
        hora = str(horario)
        id_reserva = hora+"_"+data+"_"+predio_reserva+"_"+local_reserva
        sql = "insert into reservas values('%s','%s','%s', '%s', '%s', '%s', '%d')"%(id_reserva, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, horario)
        try:
            cursor.execute(sql)
            db.commit()
            print "Cadastro efetuado com sucesso as %s horas" %(hora)
        except:
            count_erro += 1
            print "[ERRO 002] Reserva já existente para %s horas." %(hora)
            db.rollback()
    while count_erro <> 0:
        pre_reserva = raw_input("Deseja confirmar as reservas realizadas? S/N")
        pre_reserva = pre_reserva.upper()
        if pre_reserva == "S":
            count_erro = 0
        elif pre_reserva == "N":
            count_erro = 0
            for horario in range (hora1,hora2,1):
                horadel = str(horario)
                id_reserva = horadel+"_"+data+"_"+predio_reserva+"_"+local_reserva
            
                verificar_reserva = "select id_reserva from reservas where id_reserva='%s'" %(id_reserva)
                existe = cursor.execute(verificar_reserva)
            
                if existe < 1:
                    continue
                else:
                    excluirReserva(cursor, id_reserva)
        else:
            print "[ERRO 004] Opcao invalida"
            
            
            
            
def print_predios():
    cursor.execute("select * from predios")
    lista_predios_ID=[]
    lista_predios_Nome=[]
    for row in cursor.fetchall():
        lista_predios_ID.append(row[0])
        lista_predios_Nome.append(row[1])
    print "  ID      NOME"
    for i in range (len(lista_predios_ID)):
        print "["+lista_predios_ID[i]+"] - "+lista_predios_Nome[i]
        
def print_local(predio_reserva):
    cursor.execute("select * from locais where predio_local='%s'" %(predio_reserva))
    lista_locais_ID=[]
    lista_locais_Nome=[]
    lista_locais_Tipo=[]
    for row in cursor.fetchall():
        lista_locais_ID.append(row[0])
        lista_locais_Nome.append(row[1])
        lista_locais_Tipo.append(row[2])
    print " ID     NOME     TIPO"
    for i in range (len(lista_locais_ID)):
        print "["+lista_locais_ID[i]+"] - "+lista_locais_Nome[i]+" - "+lista_locais_Tipo[i]
#===============================================================================
