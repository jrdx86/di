
def distancia(lista):
    laSuma = 0
    for i in range(0,len(lista)):
        laSuma +=  lista[i]
    return print("La suma de tramos es: ",laSuma)

lista = []
print("")
print("---Introduce tramos y cuando quieras parar introduce una letra cualquiera---\n")
while(True):
	try:
		tramo=int(input("Introduce un tramo: "))
		lista.append(tramo)
	except:
		break


distancia(lista)
