altura_cm = int(input("¿Cuánto mides en cm? "))
tiene_problemas_cardiacos = input("¿Tienes problemas cardíacos? (si/no): ").lower() == "si"
tiene_pase_vip = input("¿Tienes pase VIP? (si/no): ").lower() == "si"


if tiene_problemas_cardiacos:
    print("Acceso denegado: Por razones de salud, no puedes subir a la montaña rusa.")

elif altura_cm <= 120:
    print("Acceso denegado: Debes medir más de 120 cm para poder subir.")

elif tiene_pase_vip:
    print("¡Acceso concedido por Vía Rápida (Pase VIP)! Disfruta el viaje.")

else:
    print("¡Acceso concedido por la fila regular! Disfruta el viaje.")
s
#El Acceso a la Montaña Rusa
#Para subir, hay reglas estrictas:
#Salud: no tener problemas cardiacos (obligatorio siempre)
#Seguridad: Medir más o igual 120 cm Y no tener problemas cardíacos.
#Vía Rápida: Si tienes el "Pase VIP", entras pero siempre que midas más o igual a 120 cm por seguridad básica).