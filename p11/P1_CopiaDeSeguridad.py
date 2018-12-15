import io

x=input("Introduce el nombre del archivo para hacer el Backup (Hola): ")

fichero=open(x+".txt","r")#Abrimos el fichero en modo lectura
texto = fichero.readlines()#leemos las lineas del fichero
fichero.close()#lo cerramos
fichero2 = open("D:\Repositorio\di\p11\H.txt","w")#creamos un fichero en modo escritura
fichero2.writelines(texto)#escribimos las lineas de texto
fichero2.close()#cerramos el fichero del backup