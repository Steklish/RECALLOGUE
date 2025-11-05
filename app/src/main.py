from fastapi import FastAPI
from app.src.database import init_db, engine
from app.src.api.routers import dev, login, user, access_group

app = FastAPI()

# Include the routers
app.include_router(user.router)
app.include_router(access_group.router)
app.include_router(login.router)
app.include_router(dev.router)


@app.on_event("startup")
def on_startup():
    # Initialize the database tables
    init_db(engine)