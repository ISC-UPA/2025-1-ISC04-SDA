import os

def postfix2Value(postfix):
    lista = postfix.split()
    print(lista) 
 
    value = 10      
    return value


infix = '5 * ( 6 + 2 ) - 12 / 4'	
posfix = '5 6 2 + * 12 4 / -'
Valor = 37


infix = "4-3^2/3+7*(1-2)"
postfix = "4 3 2 ^ 3 / - 7 1 2 - * +"
valor = -6

infix  = '2*(2^3*2-6/(4-2)-10)-2' 
postfix = "2 2 3 ^ 2 * 6 4 2 - / - 10 - * 2 -"
valor = 4

infix = '2 ^ 4 / ( 4 * 1 ) + log ( 110 - 10 ) ^ 2'  
posfix = '2 4 ^ 4 1 * / 110 10 - log 2 ^ +'
valor = 8

valor = postfix2Value(postfix)
print(valor)




