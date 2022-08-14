from fastapi import FastAPI

from api.routers import task,done

app = FastAPI()

#ROUTERパスオペレーション
app.include_router(task.router)
app.include_router(done.router)