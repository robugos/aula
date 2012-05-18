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
                    print "CPF Inválido (somente numeros)"
                    cpf=raw_input("")
                    continue
            else:
                print "CPF Inválido (somente 11 numeros)"
                cpf=raw_input("")
                continue
            
        return cpf


#    def SENHA_Check(self,password):
        
#    def USER_Check(self,Username):