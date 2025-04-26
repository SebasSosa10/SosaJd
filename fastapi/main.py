from fastapi import FastAPI, Depends, HTTPException
from api.v1 import Butterfly_routes, ButterflyGarden_routes
import os

# FastAPI app
app = FastAPI(
    title="FastAPI Example",
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "persistAuthorization": True,
    },
)

app.include_router(Butterfly_routes.router, prefix="/api/v1/butterfly")
app.include_router(ButterflyGarden_routes.router, prefix="/api/v1/butterflygarden")