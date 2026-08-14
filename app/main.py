from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db, engine
from contextlib import asynccontextmanager
from app.config import settings
from app.exceptions import DuplicateResourceError, handle_duplicate_resource_error, handle_internal_exception, handle_unprocessable_entity_exception
from app.router import main_router
from fastapi.exceptions import RequestValidationError


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_name = app.title
    print(f"Starting up {app_name}...")
    try:
        async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
                print(f"{app_name} is ready to serve requests and connected to database. running in {settings.environment}")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise
    
    yield
    print(f"Shutting down {app_name}...")


app = FastAPI(title="F1 FastAPI Application", lifespan=lifespan)

# Routes
app.include_router(main_router)


#Exception
app.add_exception_handler(Exception, handle_internal_exception)
app.add_exception_handler(DuplicateResourceError, handle_duplicate_resource_error)
app.add_exception_handler(RequestValidationError, handle_unprocessable_entity_exception)

# health and root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to f1 FastAPI application!"}

@app.get("/health")
async def check_health(db: AsyncSession = Depends(get_db)):
    # Perform any necessary health checks here
    result = await db.execute(text("SELECT 1"))
    if result.scalar() == 1:
        return {"status": "healthy"}
    else:
        return {"status": "unhealthy"}
