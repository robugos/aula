# -*- coding: cp1252 -*-
class Validacao():

    def CPF_Check(self,cpf):
        ver = False
        while ver == False:
            if len(cpf)==11:
                try:
                    for i in cpf:
                        i=int(i)
                    break
                except:
                    print "CPF Inv�lido (somente numeros)"
                    cpf=raw_input("")
                    continue
            else:
                print "CPF Inv�lido (somente 11 numeros)"
                cpf=raw_input("")
                continue
            
        return cpf

#------------TESTE
#CPF = raw_input("CPF\n")
#Test = Validacao()
#CPF = Test.CPF_Check(CPF)
#print CPF, type(CPF)