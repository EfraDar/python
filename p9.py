import msvcrt

def costo():
	propina = 18.0 / 100
	propina2 = 20.0 / 100
	propina3 = 25.0 / 100
	print ("Bienvenid@ al calculador de propinas, que calcula el total a pagar de su plato con I.V.A., y además le dice cuánto es el mínimo que, generosidad mediante, debería dejársele a el/la amable moz@ que l@ atendió.")
	print ("")
	comida = input("Ingrese el costo de el plato que ordenó, sólo dígitos: ")
	print("")
	total = float(comida)
	print("El total de su comida es: $" + "%.2f" % total)
	print("La propina es del 18% equivalente a: $" + str("%.2f" %(total * propina)))
	print("La propina es del 20% equivalente a: $" + str("%.2f" %(total * propina2)))
	print("La propina es del 25% equivalente a: $" + str("%.2f" %(total * propina3)))
	print("En usted esta cuanto porcentaje de propina desea dejar")
	print("Pulse cualquier tecla para salir.")
	while True:
		if msvcrt.kbhit():
			break
	

costo()