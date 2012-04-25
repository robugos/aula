# -*- coding: cp1252 -*-
class Verificar():
    def __init__(self,CPF):
        self.userCPF = CPF
        self.check=0
        one=1
        while self.check == 0:
            if len(self.userCPF)==11:
                try:
                    for i in self.userCPF:
                        if int(i) in [0,1,2,3,4,5,6,7,8,9]:
                            continue
                        else:
                            break
                except:
                    print "CPF ERROR: (somente números)"
                    self.userCPF = raw_input("CPF: ")
                    Test = Verificar(self.userCPF)
            else:
                print "CPF ERROR: (somente 11 números)"
                self.userCPF = raw_input("CPF: ")
                Test = Verificar(self.userCPF)

            self.check+=1

#------------TESTE
#CPF = raw_input("Digite o CPF\n")
#Test = Verificar(CPF)
