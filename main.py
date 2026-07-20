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

@app.get("/breeds")
async def breeds_page():
    return FileResponse("breeds.html")

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

@app.get("/api/breeds")
async def get_breeds():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.thecatapi.com/v1/breeds")
        resp.raise_for_status()
        breeds = resp.json()
        return [
            {
                "id": b["id"],
                "name": b["name"],
                "description": b.get("description", ""),
                "temperament": b.get("temperament", ""),
                "origin": b.get("origin", ""),
                "life_span": b.get("life_span", ""),
                "wikipedia_url": b.get("wikipedia_url", ""),
            }
            for b in breeds
        ]

@app.get("/api/breed-images/{breed_id}")
async def get_breed_images(breed_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}&limit=8"
        )
        resp.raise_for_status()
        images = resp.json()
        return [img["url"] for img in images]
