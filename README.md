# Where everyone is

A map + searchable list of people and the cities they live in. Runs entirely on
GitHub — no database, no paid services, no API keys. Data lives in one file you
edit by hand.

## What it does

- Interactive world map, one marker per person (people in the same city cluster).
- Search **by person** (type a name) or **by location** (type a city, see everyone there).
- Clicking a list entry flies the map to that person; clicking a marker highlights the list.

## Add or update a person

Edit **`people.yml`**. Each person is four lines:

```yaml
  - name: Anna Becker
    city: Berlin
    lat: 52.5200
    lng: 13.4050
```

To find `lat` / `lng`: open [openstreetmap.org](https://www.openstreetmap.org),
search the city, right-click the location, choose "Show address" (or read the
two numbers out of the page URL after `#map=`). Four or five decimals is plenty.

Commit the change. The site rebuilds and redeploys automatically (~1 minute).

You never touch `people.json` — the GitHub Action generates it from `people.yml`
on every push. If the file has a typo (missing field, bad coordinate), the build
fails loudly instead of publishing a broken map.

## One-time setup

1. Push these files to a repo (branch `main`).
2. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push once (or run the workflow manually). The Action prints the live URL.

## Preview locally

```bash
pip install pyyaml
python3 build.py          # writes people.json
python3 -m http.server    # open http://localhost:8000
```

(Opening `index.html` directly won't work — the browser blocks `fetch` of a
local file. Use the tiny server above.)

## Note on privacy

The site is public and search-engine indexable: anyone can see the names and
cities. That's inherent to a no-backend GitHub Pages site — there's no login
layer. Only publish real people's locations if everyone's fine being listed
publicly, and consider using first names or cities only if not.
