sueldo_empleado = float(input("Ingrese el sueldo del empleado: $ "))

if sueldo_empleado >= 3000:
    bono = sueldo_empleado * 0.10
   
    print(f"Su bono será del 10% es decir de: {bono:.2f}")
    print(f"Salario total : ${sueldo_empleado + bono:.2f}")
elif sueldo_empleado > 1500 and sueldo_empleado <= 3000:
    bono = sueldo_empleado * 0.05
    print(f"El sueldo es de: {sueldo_empleado}")
    print(f"Su bono será del 5% es decir de: {bono:.2f}")
    print(f"Salario total : ${sueldo_empleado + bono:.2f}")
elif sueldo_empleado <= 1500:
    print(f"El sueldo es de: {sueldo_empleado}")
    print("Su sueldo no contará con un bono :(")