"""Main module for the auth service."""

import uvicorn
from auth_service.api.v1.routes import auth_router
from fastapi import FastAPI

api = FastAPI(title="Auth Service", version="0.1.0")
api.include_router(auth_router, prefix="/api/v1")


def main():
    """Run the FastAPI application."""
    uvicorn.run(api)


if __name__ == "__main__":
    main()
