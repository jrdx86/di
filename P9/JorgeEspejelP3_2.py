
def distancia(tramo):
    laSuma = 0
    for i in range(0,len(tramo)):
        laSuma +=  tramo[i]
    return print("La suma de tramos es: ",laSuma)

lista = []

print("Introduce tramos y cuando quieras parar introduce una letra cualquiera")
while(True):
	try:
		tramo=int(input("Introduce un tramo: "))
		lista.append(tramo)
	except:
		break


distancia(lista)
