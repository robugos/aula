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

    def SENHA_Check(self, senha):
        self.numeros = "0123456789"
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.senha = senha
        resultteste = True
        c = 0 #Contador
        while resultteste == True and c < len(self.senha):
            if (self.senha[c] in self.numeros or self.senha[c].upper() in self.alfabeto) and len(self.senha) <= 16:
                c+=1
            else:
                print "Senha fora do padrão"
                teste = Validacao()
                self.senha = teste.SENHA_Check(raw_input("Digite uma nova senha: "))
                
        return self.senha
    
