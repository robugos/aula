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
        id_reserva = data+"_"+hora+"_"+predio_reserva+"_"+local_reserva
        sql = "insert into reservas values('%s','%s','%s', '%s', '%s', '%s', '%d')"%(id_reserva, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, horario)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print "Erro no reserva."
            db.rollback()

#===============================================================================
        
print "------ CADASTRO DE RESERVAS ------"
saida = None
while saida <> "s":
    Test = Validacao()
    predio_reserva = raw_input("Digite o prédio da reserva ")
    local_reserva = raw_input("Digite o local da reserva: ")
    data = raw_input("Digite a data da reserva (0000-00-00) ")
    disciplina_reserva = raw_input("Digite a disciplina da reserva: ")
    professor_reserva = raw_input("Digite o professo da reserva: ")
    hora1 = input("Digite horário de inicio: ")
    hora2 = input("Digite horário de fim: ")
    cadastrarReserva(cursor, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, hora1, hora2)
    saida = raw_input('Digite s para sair ou enter pra continuar: ')
    
print "------ CADASTRO EFETUADO COM SUCESSO ------"
db.close()