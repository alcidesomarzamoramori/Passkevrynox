"""PassKevrynox - Generador de contraseñas seguras.

Genera contraseñas criptográficamente seguras y las copia directamente
al portapapeles, evitando exponerlas en pantalla.
"""

import os
import string
import secrets
import textwrap
from typing import Final, Optional

try:
    import pyperclip
    from pyperclip import PyperclipException
except ImportError:
    pyperclip = None
    PyperclipException = Exception

# Habilita el procesamiento de códigos ANSI en la consola clásica de Windows.
if os.name == "nt":
    os.system("")

MIN_LONGITUD: Final[int] = 12
MAX_LONGITUD: Final[int] = 128
ALFABETO: Final[str] = string.ascii_letters + string.digits + string.punctuation
ANCHO_BANNER: Final[int] = 58

TITULO: Final[str] = "PASSKEVRYNOX - CLAVES CRIPTOGRÁFICAS"
DESCRIPCION: Final[str] = (
    "Cada clave es generada con un generador aleatorio criptográfico "
    "(CSPRNG), la misma clase de mecanismo que usan bancos e "
    "instituciones financieras internacionales para proteger claves "
    "y tokens de acceso."
)


class Color:
    """Códigos ANSI para dar estilo a la salida en terminal."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"


def generar_contrasena(longitud: int = 16) -> str:
    """Genera una contraseña aleatoria de `longitud` caracteres.

    Usa `secrets.choice`, diseñado específicamente para tokens y
    contraseñas (a diferencia de `random`, que no es seguro para
    fines criptográficos).
    """
    return ''.join(secrets.choice(ALFABETO) for _ in range(longitud))


def _borde(izquierda: str, derecha: str) -> str:
    """Construye una línea horizontal de la caja del banner."""
    return f"{izquierda}{'═' * (ANCHO_BANNER - 2)}{derecha}"


def _linea_caja(texto: str, estilo: str = "") -> str:
    """Da formato a una línea de texto dentro de la caja del banner."""
    ancho_interior = ANCHO_BANNER - 4
    borde = f"{Color.CYAN}{Color.BOLD}║{Color.RESET}"
    contenido = f"{estilo}{texto.ljust(ancho_interior)}{Color.RESET}"
    return f"{borde} {contenido} {borde}"


def mostrar_banner() -> None:
    """Muestra el encabezado del programa junto con una breve nota
    sobre el nivel de seguridad de las claves generadas."""
    ancho_interior = ANCHO_BANNER - 4
    color_borde = f"{Color.CYAN}{Color.BOLD}"

    print(f"{color_borde}{_borde('╔', '╗')}{Color.RESET}")
    print(_linea_caja(TITULO.center(ancho_interior), estilo=Color.BOLD))
    print(f"{color_borde}{_borde('╠', '╣')}{Color.RESET}")
    for linea in textwrap.wrap(DESCRIPCION, width=ancho_interior):
        print(_linea_caja(linea, estilo=Color.DIM))
    print(f"{color_borde}{_borde('╚', '╝')}{Color.RESET}")


def solicitar_longitud() -> Optional[int]:
    """Solicita al usuario la longitud deseada.

    Devuelve None si el usuario decide salir del programa.
    Puede lanzar ValueError si la entrada no es un entero válido.
    """
    prompt = f"\n{Color.CYAN}[?]{Color.RESET} Longitud deseada (mín. {MIN_LONGITUD}) o 'salir': "
    entrada = input(prompt).strip()

    if entrada.lower() in ('salir', 'exit', 'q'):
        return None

    longitud = int(entrada)

    if longitud <= 0:
        raise ValueError("La longitud debe ser un número positivo.")

    if longitud < MIN_LONGITUD:
        print(f"{Color.YELLOW}[!] Advertencia: se recomienda un mínimo de {MIN_LONGITUD} caracteres.{Color.RESET}")
    elif longitud > MAX_LONGITUD:
        print(f"{Color.YELLOW}[!] Longitud excesiva, se limita a {MAX_LONGITUD} caracteres.{Color.RESET}")
        longitud = MAX_LONGITUD

    return longitud


def copiar_al_portapapeles(contrasena: str) -> bool:
    """Intenta copiar la contraseña al portapapeles.

    Devuelve True si la copia fue exitosa, False si no hay portapapeles
    disponible (por ejemplo, en un servidor sin entorno gráfico).
    """
    if pyperclip is None:
        return False
    try:
        pyperclip.copy(contrasena)
        return True
    except PyperclipException:
        return False


def main() -> None:
    mostrar_banner()

    while True:
        try:
            longitud = solicitar_longitud()

            if longitud is None:
                print(f"\n{Color.CYAN}[*] Saliendo del programa...{Color.RESET}")
                break

            contrasena = generar_contrasena(longitud)

            if copiar_al_portapapeles(contrasena):
                print(f"{Color.GREEN}[+] ¡Contraseña generada y copiada al portapapeles!{Color.RESET}")
                print(f"{Color.DIM}[-] Por seguridad, la clave no se muestra en pantalla.{Color.RESET}")
            else:
                print(f"{Color.YELLOW}[!] No se encontró portapapeles disponible. Contraseña generada:{Color.RESET}")
                print(f"    {Color.BOLD}{contrasena}{Color.RESET}")

        except ValueError:
            print(f"{Color.RED}[X] Error: ingrese un número entero válido y positivo.{Color.RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Color.CYAN}[*] Programa interrumpido. ¡Hasta luego!{Color.RESET}")
            break


if __name__ == '__main__':
    main()