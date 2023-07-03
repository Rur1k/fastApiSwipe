import asyncio

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routers.announcement import announcement_router
from routers.flat import flat_router
from routers.notary import notary_router
from init_project import populate_data
from routers.house import house_router
from config.db import DB_CONFIG
from config.settings import Settings
import uvicorn

settings = Settings()
app = FastAPI(title=settings.APP_NAME)

register_tortoise(
    app,
    config=DB_CONFIG,
    generate_schemas=False,
)


@app.on_event("startup")
async def startup_event():
    await populate_data()


def include_routers():
    from routers.auth import auth_router
    app.include_router(
        auth_router,
        prefix=settings.API_PREFIX + '/auth',
        tags=['Authentication'],
    )

    app.include_router(
        house_router,
        prefix=settings.API_PREFIX + '/house',
        tags=['House'],
    )

    app.include_router(
        flat_router,
        prefix=settings.API_PREFIX + '/flat',
        tags=['Flat'],
    )

    app.include_router(
        announcement_router,
        prefix=settings.API_PREFIX + '/announcement',
        tags=['Announcement'],
    )

    app.include_router(
        notary_router,
        prefix=settings.API_PREFIX + '/notary',
        tags=['Notary'],
    )


if __name__ == '__main__':
    include_routers()
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
