from fastapi import FastAPI, File, UploadFile
from pdf2image import convert_from_path
import os
from tempfile import NamedTemporaryFile

app = FastAPI()

# Carpeta donde se guardarán las imágenes generadas
CARPETA_IMAGENES = "imagenes_generadas"
os.makedirs(CARPETA_IMAGENES, exist_ok=True)

@app.post("/convertir-pdf-a-imagen")
async def convertir_pdf_a_imagen(file: UploadFile = File(...)):
    # Validar que el archivo sea un PDF
    if not file.content_type == "application/pdf":
        return {"error": "El archivo debe ser un PDF"}

    # Guardar el archivo PDF temporalmente
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        content = await file.read()
        tmp_pdf.write(content)
        tmp_pdf_path = tmp_pdf.name

    try:
        # Convertir PDF a imágenes con DPI 300
        imagenes = convert_from_path(tmp_pdf_path, dpi=300)

        # Guardar cada imagen en la carpeta
        for i, imagen in enumerate(imagenes):
            nombre_imagen = f"{file.filename.replace('.pdf', '')}_pagina_{i+1}.png"
            ruta_imagen = os.path.join(CARPETA_IMAGENES, nombre_imagen)
            imagen.save(ruta_imagen, "PNG")

    finally:
        # Eliminar el archivo PDF temporal
        os.unlink(tmp_pdf_path)

    return {"mensaje": "ok imagen generada"}
