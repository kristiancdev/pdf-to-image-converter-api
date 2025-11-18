Perfecto. A continuación, te proporciono el contenido para un archivo `requirements.txt` y un archivo `README.md` que explican cómo levantar la API en un entorno Windows.

---

### 📁 `requirements.txt`

Este archivo lista todas las dependencias necesarias para que tu API funcione.

```txt
fastapi==0.115.6
pdf2image==1.17.0
python-multipart==0.0.20
Pillow==11.0.0
uvicorn[standard]==0.32.0
```

> **Nota**: Puedes ajustar las versiones si lo deseas (por ejemplo, usar `fastapi>=0.115.0`), pero es recomendable usar versiones fijas para garantizar la reproducibilidad.

---

### 📄 `README.md`

Este archivo contiene las instrucciones paso a paso para ejecutar la API en Windows.

```markdown
# API de Conversión de PDF a Imágenes

Esta API convierte cada página de un archivo PDF subido en imágenes PNG con una resolución de 300 DPI. Las imágenes generadas se almacenan en una carpeta local.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- [Python 3.8 o superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/download/win) (opcional, para clonar el repositorio)

## Instalación

1. **Clona o descarga el repositorio** (si aplica).
2. **Abre una terminal de comandos** (como `cmd` o PowerShell).
3. **Navega hasta la carpeta raíz** de tu proyecto donde están `main.py` y `requirements.txt`.
4. **(Recomendado) Crea un entorno virtual** para aislar las dependencias del proyecto:

   ```bash
   python -m venv venv
   ```

5. **Activa el entorno virtual**:

   - En `cmd`:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - En PowerShell:
     ```powershell
     venv\Scripts\Activate.ps1
     ```
     > **Nota para PowerShell**: Si obtienes un error de ejecución de scripts, ejecuta `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` en una nueva sesión de PowerShell como administrador y confirma con `S`.

6. **Instala las dependencias** usando `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## Instalación de Poppler (Requerido por `pdf2image`)

`pdf2image` necesita `poppler` instalado en tu sistema para funcionar.

1.  Descarga `poppler` para Windows desde: http://blog.alivate.com.au/poppler-windows/
2.  Extrae el archivo ZIP descargado a una carpeta (por ejemplo, `C:\poppler`).
3.  **Agrega la carpeta `bin` de `poppler` a tu `PATH` del sistema**:
    - Busca "Editar las variables de entorno del sistema" en el menú Inicio.
    - Haz clic en "Variables de entorno...".
    - En la sección "Variables del sistema", busca y selecciona la variable `Path`.
    - Haz clic en "Editar...".
    - Haz clic en "Nuevo".
    - Pega la ruta completa a la carpeta `bin` de `poppler` (por ejemplo, `C:\poppler\Library\bin`).
    - Haz clic en "Aceptar" en todas las ventanas.

## Ejecución

1.  Asegúrate de tener el entorno virtual activado (ver paso 5 de "Instalación").
2.  Desde la carpeta raíz del proyecto, ejecuta:

    ```bash
    uvicorn main:app --reload
    ```

    > El flag `--reload` reinicia automáticamente el servidor si haces cambios en el código.

3.  La API se iniciará y mostrará un mensaje similar a:

    ```
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```

## Uso

1.  Abre tu navegador web o una herramienta como [Postman](https://www.postman.com/).
2.  Ve a la URL: `http://127.0.0.1:8000/docs`
3.  Se abrirá la interfaz interactiva de **Swagger UI**.
4.  Busca el endpoint `POST /convertir-pdf-a-imagen`.
5.  Haz clic en "Try it out".
6.  En la sección de parámetros, selecciona un archivo PDF usando el botón "Choose File".
7.  Haz clic en "Execute" para enviar la solicitud.
8.  Si la operación es exitosa, recibirás una respuesta como `{"mensaje": "ok imagen generada"}`.
9.  Las imágenes generadas (PNG) se guardarán en la carpeta `imagenes_generadas` dentro del directorio del proyecto.

## Detener la API

Para detener la API, vuelve a la terminal donde está corriendo `uvicorn` y presiona `CTRL+C`.

---
```

---

### 📌 Pasos Resumidos para el Usuario Final

1.  Asegurarse de tener Python y Git instalados.
2.  Abrir la terminal y navegar al proyecto.
3.  Crear y activar un entorno virtual.
4.  Instalar dependencias con `pip install -r requirements.txt`.
5.  Instalar `poppler` y agregarlo al `PATH`.
6.  Ejecutar `uvicorn main:app --reload`.
7.  Acceder a `http://127.0.0.1:8000/docs` para interactuar con la API.

Este `README.md` debería ser suficientemente claro para que cualquier persona con un entorno Windows pueda levantar tu API.