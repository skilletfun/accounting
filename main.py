import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from users.views import router as users_router
from drives.views import router as drives_router


router = APIRouter()


@router.get("/")
def index():
    with open("frontend/index.html") as infile:
        return HTMLResponse(infile.read())


app = FastAPI(title="Учет средств СКЗИ")
app.include_router(users_router)
app.include_router(drives_router)
app.include_router(router)

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
