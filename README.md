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

---

## 🛠️ Requisitos del Sistema e Instalación

### Requisitos del Sistema

- **Sistema Operativo**: Windows 10/11
- **Python**: 3.6 o superior
- **Git**: Para clonar el repositorio
- **Permisos**: Acceso de escritura en el directorio del proyecto

### Instalación Paso a Paso

#### 1. Instalar Python (si no está instalado)

Descarga e instala Python desde [python.org](https://www.python.org/downloads/).

**Verificar instalación:**
```powershell
python --version
```

#### 2. Instalar Git (si no está instalado)

Descarga Git desde [git-scm.com](https://git-scm.com/download/win).

**Verificar instalación:**
```powershell
git --version
```

#### 3. Clonar el Repositorio

```powershell
git clone <URL_DEL_REPOSITORIO>
cd pdf2txt
```

#### 4. Instalar Dependencias

**Opción A: Usando pip (recomendado)**

```powershell
pip install pdfplumber python-docx
```

**Opción B: Usando conda**

```powershell
conda install -c conda-forge pdfplumber python-docx
```

#### 5. Verificar Instalación

```powershell
python -c "import pdfplumber; print('pdfplumber: OK')"
python -c "from docx import Document; print('python-docx: OK')"
```

#### 6. Ejecutar el Programa

```powershell
# Coloca tus archivos PDF/DOCX en la carpeta IN
python main.py
```

### Resumen de Comandos (Copia y Pega)

Si ya tienes Python y Git instalados, ejecuta esto en PowerShell:

```powershell
# Clonar y entrar al directorio
git clone <URL_DEL_REPOSITORIO>
cd pdf2txt

# Instalar dependencias
pip install pdfplumber python-docx

# Ejecutar
python main.py
```

### Solución de Problemas

**Error: "pip no se reconoce"**
```powershell
python -m pip install pdfplumber python-docx
```

**Error: Permisos de instalación**
```powershell
pip install --user pdfplumber python-docx
```

**Error: pdfplumber/python-docx no encontrado**
```powershell
# Actualizar pip primero
python -m pip install --upgrade pip
pip install pdfplumber python-docx
```

---

## 🐍 Instalación de Conda (Miniconda/Anaconda) en Windows 10/11

Si prefieres usar **conda** para manejar tus dependencias, necesitas instalar Miniconda o Anaconda.

### ¿Cuál elegir?

| Característica | **Miniconda** (Recomendado) | **Anaconda** |
|---|---|---|
| Tamaño | ~100 MB | ~3 GB |
| Instalación | Rápida | Lenta |
| Paquetes incluidos | Solo conda + Python | +400 paquetes científicos |
| Ideal para | Proyectos específicos | Data science completo |

**Recomendación:** Usa **Miniconda** si solo necesitas conda para este proyecto.

---

### Opción A: Instalar Miniconda (Recomendado)

#### Paso 1: Descargar Miniconda

1. Ve a: https://docs.conda.io/en/latest/miniconda.html
2. Descarga el instalador **Windows 64-bit** (archivo `.exe`)

O descarga directamente:
```
https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
```

#### Paso 2: Instalar Miniconda

1. Ejecuta el archivo `.exe` descargado
2. Haz clic en **Next**
3. Acepta los términos de licencia
4. Elige **Just Me** (recomendado)
5. Selecciona la carpeta de instalación (por defecto: `C:\Users\TuUsuario\miniconda3`)
6. ✅ **Importante:** Marca ambas casillas:
   - ☑️ **Add Miniconda3 to my PATH environment variable** (opcional pero recomendado)
   - ☑️ **Register Miniconda3 as my default Python**
7. Haz clic en **Install**

#### Paso 3: Verificar Instalación

Abre una **nueva** ventana de PowerShell o CMD y ejecuta:

```powershell
conda --version
```

Deberías ver algo como: `conda 24.x.x`

#### Paso 4: Configurar Entorno (Primera vez)

```powershell
# Crear un entorno virtual para el proyecto
conda create -n pdf2txt python=3.11 -y

# Activar el entorno
conda activate pdf2txt

# Verificar que estás en el entorno correcto
conda info --envs
```

#### Paso 5: Instalar Dependencias del Proyecto

```powershell
conda install -c conda-forge pdfplumber python-docx -y
```

#### Paso 6: Ejecutar el Proyecto

```powershell
# Asegúrate de estar en el entorno activado
conda activate pdf2txt

# Navega a la carpeta del proyecto
cd F:\Proyectos\pdf2txt

# Ejecuta el script
python main.py
```

---

### Opción B: Instalar Anaconda

#### Paso 1: Descargar Anaconda

1. Ve a: https://www.anaconda.com/download
2. Descarga la versión para **Windows**

O descarga directamente:
```
https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Windows-x86_64.exe
```

#### Paso 2: Instalar Anaconda

1. Ejecuta el archivo `.exe` descargado
2. Sigue el asistente de instalación (similar a Miniconda)
3. ✅ Marca las mismas casillas que en Miniconda:
   - ☑️ **Add Anaconda3 to my PATH environment variable**
   - ☑️ **Register Anaconda3 as my default Python**
4. La instalación tardará más debido a la cantidad de paquetes incluidos

#### Paso 3: Verificar Instalación

Abre una **nueva** ventana de PowerShell o CMD:

```powershell
conda --version
```

#### Paso 4: Usar Anaconda con el Proyecto

Anaconda ya incluye muchos paquetes, pero para asegurar que tienes los necesarios:

```powershell
# (Opcional) Crear entorno específico
conda create -n pdf2txt python=3.11 -y
conda activate pdf2txt

# Instalar dependencias si no están incluidas
conda install -c conda-forge pdfplumber python-docx -y

# Ejecutar el proyecto
cd F:\Proyectos\pdf2txt
python main.py
```

---

### 📋 Resumen Rápido: Miniconda + Proyecto

```powershell
# 1. Descargar e instalar Miniconda (manualmente desde la web)
# 2. Abrir PowerShell y ejecutar:

conda create -n pdf2txt python=3.11 -y
conda activate pdf2txt
conda install -c conda-forge pdfplumber python-docx -y

cd F:\Proyectos\pdf2txt
python main.py
```

---

### ⚠️ Notas Importantes sobre Conda en Windows

1. **PATH Environment Variable:**
   - Si no marcaste la opción de agregar al PATH durante la instalación, busca **Anaconda Prompt** o **Miniconda Prompt** en el menú Inicio
   - También puedes agregarlo manualmente después desde Anaconda Navigator

2. **Activar Entorno:**
   - Siempre ejecuta `conda activate pdf2txt` antes de usar el proyecto
   - Para desactivar: `conda deactivate`

3. **Actualizar Conda:**
   ```powershell
   conda update conda
   conda update --all
   ```

4. **Listar Entornos:**
   ```powershell
   conda env list
   ```

5. **Eliminar Entorno:**
   ```powershell
   conda deactivate
   conda env remove -n pdf2txt
   ```

6. **PowerShell Execution Policy:**
   Si no puedes activar entornos en PowerShell, ejecuta esto como **Administrador**:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
