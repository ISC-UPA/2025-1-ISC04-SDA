import os
import sys

print("raiz: ", os.getcwd())
sys.path.append(os.getcwd())

directorio_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print("padre:" ,directorio_padre)
sys.path.append(directorio_padre)

# import U2.colasP as cola
from U2.colasP import Cola 


#a = cola.Cola()
b = Cola()


token = "-34"   # 3 -34.0 100 100.0 3.14 -3.14 3.14e-1 -3.14e-1
try:
    # print(token.isdigit())
    # print(token.isnumeric())
    print(isinstance(float(token), float))
except:
    print("No es un numero")



