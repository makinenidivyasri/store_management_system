from fastapi import FastAPI
from . import models
from .database import engine, SessionLocal,get_db
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app.routers import kids,men,women,user,auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='LMS', user='postgres', password='password',
                            cursor_factory=RealDictCursor)
        cur = conn.cursor()
        print("Successfully logined")
        break
    except Exception as error:
        print("login not successful")
        print("error was", error)
        time.sleep(2)

app.include_router(kids.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(men.router)
app.include_router(women.router)
