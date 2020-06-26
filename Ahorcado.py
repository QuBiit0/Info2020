# Importación de funciones

import random
import os
import time
os.system("cls")

#Listas y variables

animales=["GATO","PERRO","CABALLO","CERDO","ELEFANTE","BURRO",
          "POLLO","PATO","PAVO","VACA","CABRA","ZORRO","CONEJO",
          "CODORNIZ","CAMELLO","ORNITORRINCO","RATA","PAJARO",
          "OVEJA","ARDILLA"]
plantas=["JAZMIN","HELECHO","CEIBO","AROMO","ROSA","AMAPOLA",
         "ALBACA","ALOE","AZALEA","CAMELIA", "PETUNIA","CLAVEL",
         "CRISANTEMO","CROTON","PALMERA", "FICUS","PARAISO",
         "MARGARITA","MENTA","BROMELIA","DIEFEMBAQUIA"]
insectos=["HORMIGA","ARAÑA","LANGOSTA","MOSCA","GRILLO","ABEJA",
          "TERMITA","ORUGA","ESCARABAJO","LIBELULA","CHINCHE",
          "MARIPOSA","CHICHARRA","LIBELULA","ALACRAN","POLILLA",
          "MOSQUITO","PULGA","CUCARACHA","GUSANO"]
dato=[]
error=0

# Inicio del programa, validación de datos y eleccion de listas

nombre=input("Ingrese su Nickname: ")
print()
print("Hola {}!!".format((nombre).upper()))
print()
opcion= input("Elija el tema con el cual desee empezar a jugar:   \n\n 1)Animales" 
             " \n 2)Plantas\n 3)Insectos \n \n Opcion: ")
while True:
    if opcion=="1":
        opcion="Animales"        
        print("Ha elegido jugar con: ",opcion)
        print()
        lista=list(random.choice(animales))
        break
    elif opcion=="2":
        opcion="Plantas"
        print()        
        print("Ha elegido jugar con: ",opcion)
        lista=list(random.choice(plantas))
        break
    elif opcion=="3":
        opcion="Insectos"        
        print("Ha elegido jugar con: ",opcion)
        print()
        lista=list(random.choice(insectos))
        break
    else:
        opcion= input("Ingrese una opción válida por favor: ")

# Pantalla Principal

os.system("cls")
for i in range(len(lista)):
    dato.append(" _ ")
print()
print("*****************************")
print("***   JUEGO DEL AHORCADO  ***")
print("*****************************")
print()
print("Haz elegido: ",opcion.upper())
print()
print("            ╦═══╗            ")
print("                ║            ")
print("                ║            ")
print("                ║            ")
print("          ══════╩═           ")
print()
print("       ","".join(dato),"          ")
print()

#Ingreso de Letra x Letra y validación

while True:
    print()
    letra=input("Dime una letra: ").upper()    
    if len(letra)!=1:
        print()
        print("Debes digitar una sola letra")
        time.sleep(2)
    elif letra.upper() in dato:
        print()
        print("Letra ya elegida")
        time.sleep(2)
    elif letra not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":  
        print()
        print("Caracter no identificado") 
        time.sleep(2)    
    if letra in lista: 
        for i in range(len(dato)):
            if lista[i]==letra:
                dato[i]=letra
    else:
        error+=1       
    
    os.system("cls")
    
    if error==0:
        print()
        print("*****************************")
        print("***   JUEGO DEL AHORCADO  ***")
        print("*****************************")
        print("Haz elegido: ",opcion.upper())
        print()
        print("            ╦═══╗            ")
        print("                ║   VIDAS    ")
        print("                ║     6      ")
        print("                ║            ")
        print("          ══════╩═           ")
        print("         ","".join(dato))
#        print("     ",end="")
#        for i in dato:
#            print(i,end=" ")
                   
    elif error==1:
        print()
        print("*****************************")
        print("***   JUEGO DEL AHORCADO  ***")
        print("*****************************")
        print("Haz elegido: ",opcion.upper())
        print()
        print("            ╦═══╗            ")
        print("            ☻   ║    VIDAS   ")
        print("                ║      5     ")
        print("                ║            ")
        print("          ══════╩═           ")
        print("         ","".join(dato))           
    elif error==2:
        print()
        print("*****************************")
        print("***   JUEGO DEL AHORCADO  ***")
        print("*****************************")
        print("Haz elegido: ",opcion.upper())
        print()
        print("            ╦═══╗            ")
        print("            ☻   ║    VIDAS   ")
        print("            |   ║      4     ")
        print("                ║            ")
        print("          ══════╩═           ")
        print("         ","".join(dato))    
    elif error==3:
        print()
        print("*****************************")
        print("***   JUEGO DEL AHORCADO  ***")
        print("*****************************")
        print("Haz elegido: ",opcion.upper())
        print()
        print("            ╦═══╗            ")
        print("            ☻   ║    VIDAS   ")
        print("           /|   ║      3     ")
        print("                ║            ")
        print("          ══════╩═           ")
        print("         ","".join(dato))            
    elif error==4:
        print()
        print("*****************************")
        print("***   JUEGO DEL AHORCADO  ***")
        print("*****************************")
        print("Haz elegido: ",opcion.upper())
        print()
        print("            ╦═══╗            ")
        print("            ☻   ║    VIDAS   ")
        print("           /|\  ║      2     ")
        print("                ║            ")
        print("          ══════╩═           ")
        print("         ","".join(dato))        
    elif error==5:
        print()
        print("*****************************")
        print("***   JUEGO DEL AHORCADO  ***")
        print("*****************************")
        print("Haz elegido: ",opcion.upper())
        print()
        print("            ╦═══╗            ")
        print("            ☻   ║    VIDAS   ")
        print("           /|\  ║      1     ")
        print("           /    ║            ")
        print("          ══════╩═           ")
        print("         ","".join(dato))    
    elif error==6:
        print()
        print("*****************************")
        print("***   JUEGO DEL AHORCADO  ***")
        print("*****************************")
        print("Haz elegido: ",opcion.upper())
        print()
        print("            ╦═══╗            ")
        print("            ☻   ║    VIDAS   ")
        print("           /|\  ║      0     ")
        print("           / \  ║            ")
        print("          ══════╩═           ")
        print()
        print("    (☻) Has perdido!! (☻)    ")
        print("             ☠              ")
        print("La palabra era:","".join(lista))
        break    
    if dato==lista:
        print()
        print("(☺) Felicitaciones {}, GANASTE!! (☺)".format((nombre).upper()))
        break
print()  
    