from fastapi import FastAPI
from router.main import router as main_router

main_app = FastAPI()
main_app.include_router(main_router, prefix="/api")