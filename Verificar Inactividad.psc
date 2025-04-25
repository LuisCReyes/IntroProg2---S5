Algoritmo s
	Definir día, mes, año Como Entero
	definir dia_act, mes_act, año_act Como Entero
	dia_act = 22
	mes_act = 04
	año_act = 2025
	
	Leer día
	Leer mes
	leer año
	
	Definir días_transc como entero 
	definir mes_transc Como entero
	Definir año_transc como entero
	
	año_transc = año_act - año
	mes_transc = mes_act - mes
	días_transc = día_act - día
	
	si año_transc > 0 Entonces
		suma_días = 365 * año_transc
	FinSi
	
	si mes_transc > 0 Entonces
		suma_días = suma_días + (30 * mes_transc)
	FinSi
	Escribir días_transc
	Escribir mes_transc
	Escribir año_transc
	
	Escribir suma_días
FinAlgoritmo