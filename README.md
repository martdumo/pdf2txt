# PDF2TXT 📄➡️📝

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![pdfplumber](https://img.shields.io/badge/pdfplumber-✓-orange.svg)](https://github.com/jsvine/pdfplumber)
[![python-docx](https://img.shields.io/badge/python--docx-✓-lightgrey.svg)](https://python-docx.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Descripción

Conversor automático de archivos **PDF** y **DOCX** a **TXT** con categorización automática basada en la estructura de carpetas.

Procesa todos los archivos dentro de la carpeta `IN` y guarda los resultados en la carpeta `OUT`, manteniendo la estructura de directorios original.

## ✨ Características

- 🔄 Conversión recursiva de PDF y DOCX a texto plano
- 📂 Mantiene la estructura de carpetas en la salida
- 🏷️ Categorización automática según la ubicación del archivo
- 🖥️ Compatible con Windows (ejecución con doble clic)
- 📝 Exportación en UTF-8

## 📋 Requisitos

### Dependencias externas

```bash
conda install -c conda-forge pdfplumber
conda install -c conda-forge python-docx
```

### Bibliotecas estándar

- `sys`
- `os`
- `pathlib`

## 🚀 Uso

### Modo automático (recomendado)

1. Coloca tus archivos PDF/DOCX en la carpeta `IN`
2. Ejecuta el script:

```bash
python main.py
```

Los archivos TXT se guardarán automáticamente en la carpeta `OUT`.

### Modo manual (argumento)

```bash
python main.py <ruta_archivo_o_carpeta>
```

## 📁 Estructura del proyecto

```
pdf2txt/
├── main.py          # Script principal
├── IN/              # Carpeta de entrada (colocar aquí archivos)
├── OUT/             # Carpeta de salida (archivos convertidos)
└── README.md        # Este archivo
```

## 🔧 Funcionamiento

1. **Detección de archivos**: Busca recursivamente todos los `.pdf` y `.docx` en `IN/`
2. **Extracción de texto**: Usa `pdfplumber` para PDFs y `python-docx` para DOCX
3. **Categorización**: Añade al inicio de cada TXT la ruta relativa como categoría
4. **Exportación**: Guarda el archivo en `OUT/` manteniendo la estructura de carpetas

## 📤 Ejemplo de salida

```
categoría: documentos > facturas

[contenido extraído del archivo...]
```

## ⚠️ Notas

- Los archivos se guardan con codificación **UTF-8**
- Si un archivo no puede procesarse, se muestra un mensaje de error pero continúa con el siguiente
- Compatible con ejecución mediante doble clic en Windows

## 📄 Licencia

MIT

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes una sugerencia, no dudes en compartirla.
