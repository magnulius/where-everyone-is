#!/usr/bin/env python3
"""Convert people.yml -> people.json for the frontend to fetch.

Run locally with `python3 build.py`, or let the GitHub Action run it on push.
Validates that every entry has name, city, lat, lng and that coords are numbers
in valid ranges, so a typo fails the build instead of silently breaking the map.
"""
import json
import sys
import yaml

def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)

with open("people.yml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

people = (data or {}).get("people")
if not isinstance(people, list) or not people:
    fail("people.yml has no 'people:' list or it is empty.")

clean = []
for i, p in enumerate(people, 1):
    for key in ("name", "city", "lat", "lng"):
        if key not in p:
            fail(f"Entry #{i} is missing '{key}': {p!r}")
    name, city = str(p["name"]).strip(), str(p["city"]).strip()
    try:
        lat, lng = float(p["lat"]), float(p["lng"])
    except (TypeError, ValueError):
        fail(f"Entry #{i} ({name}) has non-numeric lat/lng.")
    if not (-90 <= lat <= 90 and -180 <= lng <= 180):
        fail(f"Entry #{i} ({name}) has out-of-range coordinates.")
    clean.append({"name": name, "city": city, "lat": lat, "lng": lng})

with open("people.json", "w", encoding="utf-8") as f:
    json.dump(clean, f, ensure_ascii=False, indent=2)

print(f"Wrote people.json with {len(clean)} entries.")
