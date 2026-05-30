from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

templates = Jinja2Templates(directory="templates")


posts: list[dict] = [
    {
        "id": 1,
        "author": "raghuveer",
        "title": "FastAPI is awesome",
        "content": "This framwork is really easy and is fast api use and super fast.",
        "date_posted": "april 20,2025"
    },
    {
        "id": 2,
        "author": "jane donme",
        "title": "Python is great for web development",
        "content": "Python is a great language for web development and FastAPI makes it even better.",
        "date_posted": "april 21,2025"
    },
]


@app.get("/", include_in_schema=False,name="home")
@app.get("/posts", include_in_schema=False,name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"},)


@app.get("/api/posts")
def get_posts():
    return posts
