import pywhatkit as kit
import time

def enviar_mensajes(numero_telefono, mensaje, cantidad):
    # Enviar los mensajes restantes
    for i in range(0, cantidad + 1):
        kit.sendwhatmsg_instantly(numero_telefono, mensaje, 5, True)
        print(f"Mensaje {i+1} enviado")
        # Esperar unos segundos entre mensajes para no saturar el sistema
        time.sleep(5)

if __name__ == "__main__":
    numero = "+573215727758"
    #numero = "+573137068788"
    mensaje = "Te amo <3"
    cantidad = 5

    enviar_mensajes(numero, mensaje, cantidad)
