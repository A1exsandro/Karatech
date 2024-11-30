import uvicorn
from fastapi import FastAPI

from database import db
from routers import user_router, technique_router


def init_app()-> FastAPI:

    db.init()

    app = FastAPI(
        title="Study Fast",
        description="CRUD",
        version="1"
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    app.include_router(user_router.router, prefix="/users", tags=["Users"])
    app.include_router(technique_router.router, prefix="/techniques", tags=["Techniques"])

    return app

app = init_app()

    
@app.get("/")
async def root():
    return {"message": "Hello Karatech"}
