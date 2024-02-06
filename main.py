from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from bot import app as bot_app

app = FastAPI()

# Integrar la aplicación del bot
app.mount("/", bot_app)

