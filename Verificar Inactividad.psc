Algoritmo s
	Definir d�a, mes, a�o Como Entero
	definir dia_act, mes_act, a�o_act Como Entero
	dia_act = 22
	mes_act = 04
	a�o_act = 2025
	
	Leer d�a
	Leer mes
	leer a�o
	
	Definir d�as_transc como entero 
	definir mes_transc Como entero
	Definir a�o_transc como entero
	
	a�o_transc = a�o_act - a�o
	mes_transc = mes_act - mes
	d�as_transc = d�a_act - d�a
	
	si a�o_transc > 0 Entonces
		suma_d�as = 365 * a�o_transc
	FinSi
	
	si mes_transc > 0 Entonces
		suma_d�as = suma_d�as + (30 * mes_transc)
	FinSi
	Escribir d�as_transc
	Escribir mes_transc
	Escribir a�o_transc
	
	Escribir suma_d�as
FinAlgoritmo