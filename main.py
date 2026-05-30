from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "raghuveer",
        "title": "FASTAPI is awsom",
        "content": "this is fast api use and super fast",
        "date_posted": "april 20,2025"
    },
    {
        "id": 2,
        "author": "jane donme",
        "title": "FASTAPI not so awsom",
        "content": "python is gretad for develpment",
        "date_posted": "april 21,2025"
    },
]


@app.get("/",response_class=HTMLResponse,include_in_schema=False)
@app.get("/posts",response_class=HTMLResponse,include_in_schema=False)
def home():
    return f"<h1>this is titles  {posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts
