import Lenguaje
import sintactico
import semantico

texto = input("Introduce el texto a analizar: ")
print(texto)
elementos = Lenguaje.analizador(texto)
arbol = sintactico.analizador(elementos)
try:
    f = open("codigo.asm", "x")
    f.close()
except:
    pass
semantico.analizador(arbol)