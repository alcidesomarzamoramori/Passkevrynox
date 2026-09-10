import random
import string

def generar_contrasena(longitud=16):
    """Genera una cadena aleatoria de caracteres."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == '__main__':
    print("--- Generador de Contraseñas ---")
    try:
        longitud_usuario = int(input("Ingresa la longitud deseada (ej. 16): "))
        
        if longitud_usuario < 12:
            print("Advertencia: Para mayor resistencia, se recomienda un mínimo de 12 caracteres.")
        
        nueva_contrasena = generar_contrasena(longitud_usuario)
        print(f"\nTu contraseña generada es: {nueva_contrasena}")
        
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
