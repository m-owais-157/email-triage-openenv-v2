from fastapi import FastAPI
from app.main import app as main_app

app = FastAPI()

# mount your main app
app.mount("/", main_app)
