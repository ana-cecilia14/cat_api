# Cat Breed Gallery — Implementation Plan

## API Endpoints (all from The Cat API — already in use)

| Endpoint | Purpose |
|----------|---------|
| `GET /v1/breeds` | All breeds with id, name, description, temperament, origin, life_span, wikipedia_url |
| `GET /v1/images/search?breed_ids={id}` | Cat image for a specific breed |
| `GET /v1/images/search?breed_ids={id}&limit=8` | Multiple images for one breed |

## Backend — add to `main.py`

Two new endpoints:

```
GET /api/breeds        → returns simplified breed list (id, name, description, temperament, origin, life_span, wikipedia_url)
GET /api/breed-images/{breed_id} → returns list of image URLs for that breed (limit=8)
```

One new route:

```
GET /breeds → serves breeds.html
```

## Frontend — new `breeds.html`

- Self-contained HTML page with searchable breed list
- Search input filters breeds by name (pure JS, no deps)
- Breed cards in a grid (name + origin)
- Click card → detail panel with description, temperament, origin, and image grid
- Reuse the same CSS file (`style.css`) — add a few extra styles inline or in a `<style>` block

## File changes

```
main.py       # +2 API endpoints, +1 route
breeds.html   # newmain.py       # +2 API endpoints, +1 route
breeds.html   # new

style.css     # minor additions (or inline styles in breeds.html)
```

## No new dependencies, no API keys, no database.
