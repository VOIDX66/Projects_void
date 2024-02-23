import pyttsx3

# Abre el archivo TXT en modo lectura
with open("Projects_void/Python/Cosas/t.txt","r") as f:
    # Lee el contenido del archivo
    texto = f.read()

# Crea un objeto de voz
engine = pyttsx3.init()

# Define la velocidad de la voz
engine.setProperty('rate', 125)

# Reproduce la cadena
voces = engine.getProperty('voices')
engine.setProperty('voice', voces[0].id)
engine.setProperty('voice', 'es-es-f1')
engine.say(texto + " ")
engine.say("Siguiente frase")
#engine.say(texto)

# Espera a que la voz termine de hablar
engine.runAndWait()