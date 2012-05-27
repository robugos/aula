# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def excluirReserva(cursor, deletado):
    sql = "delete from reservas where id_reserva='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Reserva excluido com sucesso."
    except:
        print "Erro na exclus�o, n�o existe reserva nesse hor�rio."
        db.rollback()
        
#===============================================================================

print "------ EXCLUS�O DE RESERVA ------"
saida = None
while saida <> "s": 
    data = raw_input("Digite a data da reserva (0000-00-00) ")
    predio_reserva = raw_input("Digite o pr�dio da reserva ")
    local_reserva = raw_input("Digite o local da reserva: ")
    hora1 = input("Digite hor�rio de inicio: ")
    hora2 = input("Digite hor�rio de fim: ")
    
    for horario in range (hora1,hora2,1):
        hora = str(horario)
        id_reserva = hora+"_"+data+"_"+predio_reserva+"_"+local_reserva
    
        verificar_reserva = "select id_reserva from reservas where id_reserva='%s'" %(id_reserva)
        existe = cursor.execute(verificar_reserva)
    
        if existe < 1:
            print "Reserva n�o existente no hor�rio das %s horas" %(hora)
            continue
        else:
            excluirReserva(cursor, id_reserva)
    saida = raw_input('Digite s para sair ou enter para continuar excluindo: ')
            
print "------ FINISH ------"
db.close()