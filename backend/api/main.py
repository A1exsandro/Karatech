import uvicorn
from fastapi import FastAPI

from database import db

def init_app():
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

    from routers import user_router

    app.include_router(user_router.router)

    return app

app = init_app()

    
@app.get("/")
async def root():
    return {"message": "Hello Karatech"}
