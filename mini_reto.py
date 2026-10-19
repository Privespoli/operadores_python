ml = int(input("Ingrese la cantidad de ml de café: "))

if ml < 200:
    print("Es un Espresso")
elif 200 < ml <=400:
    print("Es un Latte")
else:
    print("Es un Café Gigante!")