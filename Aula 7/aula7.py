n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1+n2
m = n1+n2
d = n1/n2
di = n1//n2
e = n1 ** n2
r = n1%n2
print('A soma é {}, \n a multiplicação é {}, a divisão é {:.2f}'.format(s,m,d), end='')
print('A divisão inteira é {}, o resto é {} e a exponenciação é {}'.format(di,r,e))