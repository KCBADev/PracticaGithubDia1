# Crea un programa qué: Defina cuanto dinero tienes disponibe al inicio de la semana,registre 3 gastos principales,calcule el gasto total
#  determine cuanto dinero te queda, muestre una recomendación de ahorro según tu situación financiera y muestre un mensaje final de despedida.


Dinero_Al_Inicio = float(
    input("Ingrese el dinero disponible al inicio de la semana: "))
Gasto_despensa = float(input("Ingrese lo gastado en despensa en la semana: "))
Gasto_transporte = float(
    input("Ingrese lo gastado en transporte en la semana: "))
Gasto_entretenimiento = float(
    input("Ingrese lo gastado en entretenimiento en la semana: "))
Gasto_Total_Semana = Gasto_despensa + Gasto_transporte + Gasto_entretenimiento
Dinero_Al_Finalizar_Semana = Dinero_Al_Inicio - Gasto_Total_Semana
print(f"Tu saldo al iniciar la semana es: ${Dinero_Al_Inicio:,.2f}")
print(f"Tu gasto total en la semana es: ${Gasto_Total_Semana:,.2f}")
print(
    f"Tu saldo al finalizar la semana es: ${Dinero_Al_Finalizar_Semana:,.2f}")
if Dinero_Al_Finalizar_Semana <= Dinero_Al_Inicio * 0.2:
    print(f"Tu saldo final es: ${Dinero_Al_Finalizar_Semana:,.2f}")
    print("Tu situación financiera es crítica, te recomendamos ahorrar más.")
elif Dinero_Al_Finalizar_Semana == 0:
    print("Tu situación financiera es crítica, te recomendamos ahorrar más.")
elif Dinero_Al_Finalizar_Semana < 0:
    print("Haz gastado más de lo que tenías disponible, no adquieras más deudas")
else:
    print(
        f"Tu saldo final después de todos los gastos es: ${Dinero_Al_Finalizar_Semana:,.2f}")
    print("Cuidado vaquero, tu saldo está por debajo del 20% de tu saldo inicial")

print("Gracias por usar nuestro programa, ¡hasta la próxima!")