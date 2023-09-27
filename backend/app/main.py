from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from users.routes import router as users_router
from posts.routes import router as posts_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(posts_router, prefix="/posts", tags=["posts"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
