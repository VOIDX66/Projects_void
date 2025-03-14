# scripts/hash_password.py
import hashlib
import sys

# Recibe la contraseña desde la línea de comandos
password = sys.argv[1]  
hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hashea la contraseña
print(hashed_password)  # Imprime el resultado
