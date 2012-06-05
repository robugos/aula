# -*- coding: cp1252 -*-
#inicio do programa
import os
inicio=0
while inicio == 0:
    choice=input("Digite:\n1 - Pesquisa\n2 - Login\n3 - Sair\n->")
    if choice > 3 or choice <1:
        print "[ERRO 000] Opção inválida. Tente novamente\n"
    else:
        if choice == 1:
            print "=====================PESQUISA======================"
            
        if choice == 2:
            print "=======================LOGIN======================="
            from main_login import *
            
        if choice == 3:
            inicio = 1
            print "=================PROGRAMA FINALIZADO==============="
            
    os.system("cls")
        