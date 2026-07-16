from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
import httpx

app = FastAPI(title="Cat API")

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/style.css")
async def css():
    return FileResponse("style.css", media_type="text/css")

@app.get("/random-cat")
async def random_cat():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.thecatapi.com/v1/images/search")
        resp.raise_for_status()
        data = resp.json()
        url = data[0]["url"]

        img_resp = await client.get(url)
        img_resp.raise_for_status()

        content_type = img_resp.headers.get("content-type", "image/jpeg")

        return Response(content=img_resp.content, media_type=content_type)
