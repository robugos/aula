# -*- coding: cp1252 -*-
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


def cadastrarReserva(cursor, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, hora1, hora2):
    for horario in range (hora1,hora2,1):
        hora = str(horario)
        id_reserva = hora+"_"+data+"_"+predio_reserva+"_"+local_reserva
        sql = "insert into reservas values('%s','%s','%s', '%s', '%s', '%s', '%d')"%(id_reserva, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, horario)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print "Erro no reserva."
            db.rollback()

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
