from fastapi import FastAPI
import uvicorn
from api.user_router import router as user_router
from api.order_router import router as order_router

app = FastAPI(
    title = "Truba"
)
app.include_router(user_router,tags=["users"],prefix="/user")
app.include_router(order_router,tags=["orders"],prefix="/order")


if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost",port=8080,log_level="info")

