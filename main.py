from fastapi import FastAPI

from routers import datamanager, serverchecks

app = FastAPI()

app.include_router(datamanager.router)
app.include_router(serverchecks.router)
