from fastapi import FastAPI
from app.src.database import init_db, engine
from app.src.api.routers import dev, login, user, access_group
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Recallogue")

# This will be our sub-application to hold all the prefixed routes
sub_app = FastAPI()

# Include your routers in the sub-application
sub_app.include_router(user.router)
sub_app.include_router(access_group.router)
sub_app.include_router(login.router)
sub_app.include_router(dev.router)

# Mount the sub-application with the global prefix "/api/v1"
app.mount("/api/v1", sub_app)

# Add middleware to the main application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # <-- Important for cookies
    allow_methods=["*"],     # <-- Allows all methods (GET, POST, etc.)
    allow_headers=["*"],     # <-- Allows all headers
)

@app.on_event("startup")
def on_startup():
    # Initialize the database tables
    init_db(engine)