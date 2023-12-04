import Lenguaje
import sintactico

texto = input("Introduce el texto a analizar: ")
print(texto)
elementos = Lenguaje.analizador(texto)
arbol = sintactico.analizador(elementos)
variables = []
funciones = []
arbol_2 = arbol
if (arbol):
    arbol = arbol.Definiciones
    while(arbol):                   
        definicion = arbol.Definicion
        defvar = None
        try:
            defvar = definicion.DefVar
        except AttributeError:
            pass
        if(defvar):
            tipo = defvar.tipo
            while(defvar):
                variables.append({'id':defvar.identificador,'tipo':tipo,'valor':None,'contexto':"#"})
                try:
                    defvar = defvar.ListaVar.extra
                except AttributeError:
                    defvar = defvar.ListaVar
        deffun = None
        try:
            deffun = definicion.DefFunc
        except AttributeError:
            pass
        if(deffun):
            funcion = deffun.identificador
            funciones.append({'id':deffun.identificador,'tipo':deffun.tipo})
            try:
                param = deffun.Parametros.extra    
            except AttributeError:
                param = deffun.Parametros
            while(param):
                variables.append({'id':param.identificador,'tipo':param.tipo,'valor':None,'contexto':funcion})
                try:
                    param = param.ListaParam.extra
                except AttributeError:
                    param = param.ListaParam
            bloc = deffun.BloqFunc
            try:
                bloc = bloc.DefLocales.extra        
            except AttributeError:
                bloc = bloc.DefLocales
            while(bloc):
                try:
                    defvar = bloc.DefLocal.DefVar    
                except AttributeError:
                    defvar = None
                if(defvar):
                    tipo = defvar.tipo
                    while(defvar):
                        variables.append({'id':defvar.identificador,'tipo':tipo,'valor':None,'contexto':funcion})
                        try:
                            defvar = defvar.ListaVar.extra
                        except AttributeError:
                            defvar = defvar.ListaVar
                try:
                    bloc = bloc.DefLocales.extra
                except AttributeError:
                    bloc = bloc.DefLocales
        try:
            arbol = arbol.Definiciones.extra
        except AttributeError:
            arbol = arbol.Definiciones

if(arbol_2):
    arbol_2 = arbol_2.Definiciones
    while(arbol_2):                   
        definicion = arbol_2.Definicion
        deffun = None
        try:
            deffun = definicion.DefFunc
        except AttributeError:
            pass
        if(deffun):
            funcion = deffun.identificador
            bloc = deffun.BloqFunc
            try:
                bloc = bloc.DefLocales.extra        
            except AttributeError:
                bloc = bloc.DefLocales
            while(bloc):
                try:
                    sentencia = bloc.DefLocal.Sentencia.identificador     
                    sentencia = bloc.DefLocal.Sentencia
                except AttributeError:
                    sentencia = None
                if(sentencia):
                    id = sentencia.identificador
                    try:
                        expresion = sentencia.Expresion.Termino
                    except AttributeError:
                        expresion = None
                    if(expresion):
                        for a in variables:
                            if(a["id"]==id):
                                try:
                                    a["valor"] = expresion.entero
                                except AttributeError:
                                    try:
                                        a["valor"] = expresion.real
                                    except AttributeError:
                                        try:
                                            a["valor"] = expresion.cadena
                                        except AttributeError:
                                            for b in variables:
                                                if(b["id"]==expresion.identificador):
                                                    a["valor"] = b["valor"]
                    try:
                        expresion = sentencia.Expresion.Expresion2
                        expresion = sentencia.Expresion
                    except AttributeError:
                        expresion = None
                    if(expresion):
                        a=0
                        b=0
                        try:
                            a = expresion.Expresion.Termino.entero
                        except AttributeError:
                            try:
                                a = expresion.Expresion.Termino.real
                            except AttributeError:
                                try:
                                    a = expresion.Expresion.Termino.cadena
                                except AttributeError:
                                    for b in variables:
                                        if(b["id"]==expresion.Expresion.Termino.identificador):
                                            a = b["valor"]
                        try:
                            b = expresion.Expresion2.Termino.entero
                        except AttributeError:
                            try:
                                b = expresion.Expresion2.Termino.real
                            except AttributeError:
                                try:
                                    b = expresion.Expresion2.Termino.cadena
                                except AttributeError:
                                    for c in variables:
                                        if(c["id"]==expresion.Expresion2.Termino.identificador):
                                            b = c["valor"]
                        try:
                            operacion = expresion.opSuma
                        except AttributeError:
                            try:
                                operacion = expresion.opMul
                            except AttributeError:
                                operacion = None
                        if(operacion == "+"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=a+b
                        elif(operacion == "-"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=a-b
                        elif(operacion == "*"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=int(a)*int(b)
                        elif(operacion == "/"):
                            for i in variables:
                                if(i["id"] == id):
                                    i["valor"]=a/b
                try:
                    bloc = bloc.DefLocales.extra
                except AttributeError:
                    bloc = bloc.DefLocales
        try:
            arbol_2 = arbol_2.Definiciones.extra
        except AttributeError:
            arbol_2 = arbol_2.Definiciones

print("\n")
print("FUNCIONES")
print("ID","\t","TIPO")
for a in funciones:
    print(a["id"],"\t",a["tipo"])

print("\n")
print("VARIABLES")
print("ID","\t","TIPO","\t","VALOR","\t","CONTEXTO")
for a in variables:
    print(a["id"],"\t",a["tipo"],"\t",a["valor"],"\t",a["contexto"])