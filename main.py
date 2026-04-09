#!/usr/bin/env python3
"""
Conversor automático PDF/DOCX a TXT con categoría.
Procesa todos los archivos dentro de la carpeta 'IN' (junto al script)
y guarda los resultados en la carpeta 'OUT' manteniendo la estructura.
"""

import sys
import os
from pathlib import Path

# ------------------------------------------------------------
# Configuración
# ------------------------------------------------------------
CARPETA_ENTRADA = "IN"
CARPETA_SALIDA = "OUT"
EXTENSIONES_SOPORTADAS = {".pdf", ".docx"}

# ------------------------------------------------------------
# Funciones de extracción
# ------------------------------------------------------------
def extraer_texto_pdf(ruta_pdf):
    try:
        import pdfplumber
    except ImportError:
        print("ERROR: pdfplumber no está instalado.")
        print("       Ejecuta en tu entorno conda: conda install -c conda-forge pdfplumber")
        return None
    texto = ""
    try:
        with pdfplumber.open(ruta_pdf) as pdf:
            for i, pagina in enumerate(pdf.pages):
                t = pagina.extract_text()
                if t:
                    texto += t + "\n"
    except Exception as e:
        print(f"  [!] Error al leer PDF {ruta_pdf.name}: {e}")
        return None
    return texto

def extraer_texto_docx(ruta_docx):
    try:
        from docx import Document
    except ImportError:
        print("ERROR: python-docx no está instalado.")
        print("       Ejecuta en tu entorno conda: conda install -c conda-forge python-docx")
        return None
    texto = ""
    try:
        doc = Document(ruta_docx)
        for p in doc.paragraphs:
            texto += p.text + "\n"
    except Exception as e:
        print(f"  [!] Error al leer DOCX {ruta_docx.name}: {e}")
        return None
    return texto

# ------------------------------------------------------------
# Función para procesar un archivo individual
# ------------------------------------------------------------
def convertir_archivo(ruta_archivo, carpeta_base_entrada, carpeta_base_salida):
    """
    Convierte un archivo PDF/DOCX a TXT, guardándolo en la carpeta de salida
    con la misma estructura relativa que tiene respecto a carpeta_base_entrada.
    Añade al inicio del TXT: "categoría: ruta/relativa/de/la/carpeta"
    """
    ext = ruta_archivo.suffix.lower()
    if ext == ".pdf":
        texto = extraer_texto_pdf(ruta_archivo)
    elif ext == ".docx":
        texto = extraer_texto_docx(ruta_archivo)
    else:
        return  # No debería llegar aquí por el filtro previo

    if texto is None:
        return  # Error ya mostrado

    # Calcular la ruta relativa respecto a la carpeta de entrada
    try:
        ruta_relativa = ruta_archivo.relative_to(carpeta_base_entrada)
    except ValueError:
        print(f"  [!] No se pudo calcular ruta relativa para {ruta_archivo}")
        return

    # La categoría es la carpeta contenedora (sin el nombre del archivo)
    categoria_relativa = ruta_relativa.parent
    if str(categoria_relativa) == ".":
        categoria = "Raíz"
    else:
        # Reemplazar separadores por " > " para una lectura más clara
        categoria = str(categoria_relativa).replace(os.sep, " > ")

    # Ruta de salida: carpeta base de salida + misma estructura de subcarpetas
    ruta_salida = carpeta_base_salida / ruta_relativa.with_suffix(".txt")

    # Crear las subcarpetas necesarias
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    # Contenido final del TXT
    contenido_final = f"categoría: {categoria}\n\n{texto}"

    # Guardar con UTF-8
    try:
        with open(ruta_salida, "w", encoding="utf-8") as f:
            f.write(contenido_final)
        print(f"  [+] Creado: {ruta_salida.relative_to(carpeta_base_salida)}  (categoría: {categoria})")
    except Exception as e:
        print(f"  [!] Error guardando TXT: {e}")

# ------------------------------------------------------------
# Procesamiento recursivo de la carpeta IN
# ------------------------------------------------------------
def procesar_carpeta_in_out():
    # Determinar la ubicación del script
    script_dir = Path(__file__).parent.resolve()
    carpeta_in = script_dir / CARPETA_ENTRADA
    carpeta_out = script_dir / CARPETA_SALIDA

    print(f"\n📂 Directorio del script: {script_dir}")
    print(f"📥 Carpeta de entrada: {carpeta_in}")
    print(f"📤 Carpeta de salida : {carpeta_out}")

    if not carpeta_in.exists():
        print(f"\n❌ Error: No se encontró la carpeta '{CARPETA_ENTRADA}' en {script_dir}")
        print("   Crea una carpeta llamada 'IN' junto al script y coloca allí tus archivos PDF/DOCX.")
        input("\nPresiona Enter para salir...")  # Pausa si se ejecuta con doble clic
        return

    if not carpeta_in.is_dir():
        print(f"\n❌ Error: '{CARPETA_ENTRADA}' existe pero no es una carpeta.")
        return

    # Buscar todos los archivos soportados recursivamente
    archivos_a_procesar = []
    for ext in EXTENSIONES_SOPORTADAS:
        archivos_a_procesar.extend(carpeta_in.rglob(f"*{ext}"))

    total = len(archivos_a_procesar)
    if total == 0:
        print(f"\n⚠️  No se encontraron archivos PDF o DOCX dentro de '{CARPETA_ENTRADA}'.")
        return

    print(f"\n🔍 Se encontraron {total} archivo(s) para procesar.\n")

    # Crear carpeta OUT si no existe
    carpeta_out.mkdir(exist_ok=True)

    contador = 0
    for archivo in archivos_a_procesar:
        contador += 1
        print(f"[{contador}/{total}] Procesando: {archivo.relative_to(carpeta_in)}")
        convertir_archivo(archivo, carpeta_in, carpeta_out)

    print("\n✅ ¡Proceso completado! Los archivos TXT están en la carpeta 'OUT'.\n")

# ------------------------------------------------------------
# Punto de entrada (soporta también pasar ruta por argumento)
# ------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Modo manual con argumento (compatible con versión anterior)
        print("Modo manual con argumento (uso heredado)")
        ruta_entrada = sys.argv[1]
        path_entrada = Path(ruta_entrada)
        if not path_entrada.exists():
            print(f"Error: '{ruta_entrada}' no existe.")
            sys.exit(1)
        if path_entrada.is_file():
            # Procesar archivo único (carpeta base será la contenedora)
            convertir_archivo(path_entrada, path_entrada.parent, path_entrada.parent)
        else:
            # Procesar directorio manual (salida en el mismo directorio)
            # Esta parte es solo para compatibilidad, no usa OUT automático.
            print("Procesando directorio manual...")
            # Podrías implementarlo si quieres, pero nos centramos en el modo IN/OUT
    else:
        # Modo automático IN/OUT (sin argumentos)
        procesar_carpeta_in_out()
        # Si se ejecuta con doble clic, mantener ventana abierta para ver resultado
        input("\nPresiona Enter para cerrar...")