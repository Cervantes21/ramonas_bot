from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Montar la carpeta "CSS" en la ruta "/CSS"
app.mount("/CSS", StaticFiles(directory="CSS"), name="CSS")
# Montar la carpeta "raw" en la ruta "/raw"
app.mount("/raw", StaticFiles(directory="raw"), name="raw")

# Crear una ruta que devuelva una respuesta HTML
@app.get("/", response_class=HTMLResponse)
async def read_html():
    # Lee el contenido del archivo HTML
    with open("index.html", "r") as f:
        html_content = f.read()
    # Devuelve el contenido HTML como respuesta
    return html_content
