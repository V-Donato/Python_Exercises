n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('A soma vale {}, o produto é {}, e a divisão é {:.3f}' .format(s, m , d), end='') # O end não deixa quebrar a linha 
print ('A divisão inteira é {}, e á exponenciação é {}' .format(di, e))