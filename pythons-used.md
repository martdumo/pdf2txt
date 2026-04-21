# Índice

1. [main.py](#mainpy) – raíz (Analyzed)


- **main.py** – raíz (Analyzed)

*Nota: El índice muestra los archivos en el orden de aparición.*


## Descripciones de archivos analizados

### main.py – raíz
Script principal encargado de la conversión recursiva de archivos PDF y DOCX a formato TXT. Implementa funciones específicas para la extracción de texto (`extraer_texto_pdf` usando `pdfplumber` y `extraer_texto_docx` usando `python-docx`). El proceso organiza los archivos resultantes en una carpeta `OUT`, replicando la estructura de la carpeta `IN` y agregando un encabezado de "categoria" basado en la ubicación relativa del archivo original.
