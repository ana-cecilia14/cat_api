# Kawaii Cats 🐱

A pastel-themed web app that displays random cat images, fun cat facts, and a searchable breed gallery.

## Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3 + [FastAPI](https://fastapi.tiangolo.com/) |
| Server | [uvicorn](https://www.uvicorn.org/) (ASGI) |
| HTTP client | [httpx](https://www.python-httpx.org/) (async) |
| Frontend | Vanilla HTML / CSS / JS |
| Styling | Google Fonts (Fredoka One, Nunito), CSS gradients & animations |

## Architecture

```
┌──────────┐   ┌────────────┐   ┌─────────────────┐
│  Browser │──▶│  FastAPI   │──▶│ thecatapi.com   │
│          │   │  (main.py) │   └─────────────────┘
│  index   │   └─────┬──────┘
│ .html    │         │ serves static files
│ style    │         │ (index.html, style.css)
│ .css     │         │
│ breeds   │         │
│ .html    │         │
└──────────┘         │
                     │   ┌─────────────────┐
                     ├──▶│ catfact.ninja   │
                     │   │ (frontend-only) │
                     │   └─────────────────┘
                     │
                     │   ┌──────────────────────────┐
                     └──▶│ The Cat API               │
                         │  /api/breeds              │
                         │  /api/breed-images/{id}   │
                         └──────────────────────────┘
```

- **Backend proxy**: `/random-cat` proxies images from [The Cat API](https://thecatapi.com/) (avoids CORS issues for binary images).
- **Frontend direct calls**: The browser loads cat facts directly from [catfact.ninja](https://catfact.ninja/) and fetches cat images directly from The Cat API for instant display, while `/random-cat` provides a backend fallback.
- **Breed gallery**: `/api/breeds` and `/api/breed-images/{id}` proxy breed metadata and images from The Cat API. The frontend (`/breeds`) displays a searchable grid of breed cards with a detail panel showing description, temperament, origin, and an image grid.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Serves `index.html` |
| GET | `/style.css` | Serves stylesheet |
| GET | `/random-cat` | Proxies a random cat image from The Cat API |
| GET | `/breeds` | Serves `breeds.html` (breed gallery) |
| GET | `/api/breeds` | Returns all cat breeds (id, name, description, temperament, origin, life_span, wikipedia_url) |
| GET | `/api/breed-images/{breed_id}` | Returns up to 8 cat images for a specific breed |

## Project Structure

```
.
├── main.py          # FastAPI application
├── index.html       # Frontend UI (homepage)
├── breeds.html      # Breed gallery page
├── style.css        # Pastel-themed styles
├── breed.md         # Implementation plan
├── requirements.txt # Python dependencies
└── README.md
```

## How to run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://localhost:8000` in your browser.

## External APIs

- **[The Cat API](https://thecatapi.com/)** — random cat images (used both server-side in `/random-cat` and client-side)
- **[Cat Facts API](https://catfact.ninja/)** — random cat facts (called from the browser)
