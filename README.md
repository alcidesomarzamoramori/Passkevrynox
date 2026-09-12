# PassKevrynox

Generador de contraseñas seguras para línea de comandos, escrito en Python. Crea claves aleatorias criptográficamente seguras y las copia directamente al portapapeles, sin exponerlas en pantalla. Esto asegura que solo tú tengas el control de tus claves.

<p align="center"><img src="Passkevrynox banner.jpg" alt="PassKevrynox banner" width="100%"></p>

## Descripción

PassKevrynox genera contraseñas usando el módulo `secrets` de Python, la misma clase de generador aleatorio criptográfico (CSPRNG) que usan bancos e instituciones financieras internacionales para proteger claves y tokens de acceso. La contraseña se copia automáticamente al portapapeles y nunca se muestra en pantalla, salvo que el sistema no tenga un portapapeles disponible (por ejemplo, en un entorno sin sesión gráfica).

## Características

- Generación criptográficamente segura con `secrets.choice` (no con `random`).
- Longitud configurable, entre 12 y 128 caracteres.
- Copiado automático al portapapeles vía `pyperclip`.
- Respaldo automático: si no hay portapapeles disponible, muestra la contraseña en pantalla en vez de fallar (fallback).
- Manejo de errores para entradas inválidas, `Ctrl+C` y cierre inesperado.
- Interfaz de consola con colores y un banner informativo sobre el nivel de seguridad.
- Disponible como ejecutable `.exe` independiente, sin necesidad de tener Python instalado.
- El programa ejecutable es 100% portable y ligero, puedes llevarlo hasta en USB, sin necesidad de instalarlo en tu pc.

## Requisitos

**Para usar el ejecutable (.exe):**
- Windows 10 u 11. No necesitas tener Python instalado.

**Para ejecutar desde el código fuente:**
- Python 3.8 o superior.
- El paquete `pyperclip`.

## Instalación y uso

### Opción 1: Ejecutable (recomendado)

1. Ve a la pestaña [Releases](../../releases) de este repositorio.
2. Descarga el archivo `PassKevrynox.exe` de la versión más reciente.
3. Haz doble clic para ejecutarlo. Windows puede mostrar una advertencia de "editor desconocido" por no estar firmado digitalmente; es normal en proyectos personales como este.

### Opción 2: Desde el código fuente

```bash
git clone https://github.com/<tu-usuario>/<tu-repositorio>.git
cd <tu-repositorio>
pip install pyperclip
python generador_contrasenas.py
```

### Cómo usarlo

Al iniciar el programa, se pedirá la longitud deseada:

```
[?] Longitud deseada (mín. 12) o 'salir': 20
[+] ¡Contraseña generada y copiada al portapapeles!
[-] Por seguridad, la clave no se muestra en pantalla.
```

- Escribe un número entre 12 y 128 para generar una contraseña de esa longitud.
- Escribe `salir` (o `exit` / `q`) para cerrar el programa.
- Si el número ingresado es menor a 12, el programa lo genera igual pero muestra una advertencia.

## Seguridad

La aleatoriedad se genera con el módulo estándar [`secrets`](https://docs.python.org/3/library/secrets.html) de Python, diseñado específicamente para tokens y contraseñas, a diferencia de `random`, que no es apto para fines criptográficos. Cada contraseña combina letras mayúsculas, minúsculas, números y símbolos de puntuación.

## Estructura del proyecto

```
.
├── LICENSE.md                 # Licencia del proyecto
├── Passkevrynox banner.jpg    # Banner del programa
├── Passkevrynox v1.0.2.py     # Primeras versiones del proyecto
├── Passkevrynox v1.0.3.py     # Código fuente principal
└── README.md                  # Archivo instructivo
```

## Licencia

MIT licence: Este es un proyecto personal, libre y permisivo.

## Autor

Desarrollado por Omar Zamora.
