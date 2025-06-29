from fastapi import FastAPI
from app.routes import router
from app.database import create_db_and_tables
import os
from dotenv import load_dotenv

load_dotenv()  # تحميل المتغيرات

app_name = os.getenv("APP_NAME", "FastAPI App")

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router)


