# -*- coding: utf-8 -*-
"""
parse_corpus_for_game.py
Deeply parses all 211 poems from src/data/poems.ts into game environments,
sketching mechanics, atmospheric climates, and historical memory fragments,
inspired by 'Season: A Letter to the Future'.
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("src/data/poems.ts", "r", encoding="utf-8") as f:
    code = f.read()

# Extract json from export const poemsDatabase: Poem[] = [...]
eq_idx = code.find("=")
start_idx = code.find("[", eq_idx)
end_idx = code.rfind("]") + 1
poems_data = json.loads(code[start_idx:end_idx])

print(f"Loaded {len(poems_data)} poems to parse for game world.")

# Realms definition inspired by 'Season: A Letter to the Future'
realms = {
    "realm_1_dawn_hills": {
        "id": "realm_1_dawn_hills",
        "name": "The Dawn Hills of Batala (ਸਵੇਰ ਦੀਆਂ ਪਹਾੜੀਆਂ)",
        "climate": "Serene Sunrise, Dew-drenched green grass, soft morning mist, light golden horizon",
        "atmosphereTone": "Quiet nostalgia, innocence before exile, gentle bicycle cadence, birds chirping",
        "gameplayActivity": "Cycling along undulating dirt paths, recording morning songbirds, finding stone markers",
        "sketchSubject": "Charcoal outlines of an abandoned bicycle, wild jasmine blossoms (chamba), and rolling green knolls",
        "historicalThemes": [
            "Childhood in undivided Punjab",
            "Flight across Ravi during 1947 Partition",
            "Refusal to become a village revenue clerk (patwari)"
        ],
        "poems": []
    },
    "realm_2_monsoon_river": {
        "id": "realm_2_monsoon_river",
        "name": "The River Chenab & Village Trinjan (ਝਨਾਬ ਤੇ ਤ੍ਰਿੰਞਣ)",
        "climate": "Warm monsoon rain, rushing silted riverwaters, overcast silver clouds, dripping willows",
        "atmosphereTone": "Sensual melancholy, agrarian community, the rhythm of spinning wheels and clay pots",
        "gameplayActivity": "Walking alongside riverbanks, recording the rush of water and the creak of wooden water-wheels",
        "sketchSubject": "Charcoal drawings of dough sparrows dissolving in the rain, broken glass bangles, clay dolls (mitti da bawa)",
        "historicalThemes": [
            "The influence of classical Sufi poetry (Waris Shah, Bulleh Shah)",
            "Agrarian metaphors of kilns, ovens, and seasonal harvests"
        ],
        "poems": []
    },
    "realm_3_snowy_cabin": {
        "id": "realm_3_snowy_cabin",
        "name": "The Solitary Ridge Cabin (ਬਰਫ਼ੀਲੀ ਰਾਤ ਦਾ ਕੈਬਿਨ)",
        "climate": "Cold snowy midnight, whistling mountain wind, glowing hearth fire, frosted windowpanes",
        "atmosphereTone": "Intense solitude, existential isolation, shelter from the blizzard, warmth of dying embers",
        "gameplayActivity": "Seeking refuge inside the cabin, warming hands at the wood stove, opening worn leather journals",
        "sketchSubject": "Charcoal tracing of the crested Falcon (Shikra) perched on a gaunt wrist, oil lamps burning in snow",
        "historicalThemes": [
            "The metaphysics of Birha: grief as sacred essence",
            "Writing on Gold Flake cigarette packets and café napkins in Chandigarh",
            "The Marxist Progressive critics attacking him for 'bourgeois escapism'"
        ],
        "poems": []
    },
    "realm_4_mountain_loona": {
        "id": "realm_4_mountain_loona",
        "name": "The Barren Peaks of Sialkot (ਲੂਣਾ ਦੀਆਂ ਕਾਲੀਆਂ ਚੱਟਾਨਾਂ)",
        "climate": "Twilight storm, jagged dark slate cliffs, wind howling through abandoned marble archways",
        "atmosphereTone": "Fierce defiance, anti-patriarchal rage, moral tragedy, shattered feudal statues",
        "gameplayActivity": "Ascending desolate rock staircases, discovering cracked palace edicts, peering into dry ancient wells",
        "sketchSubject": "Charcoal sketches of Loona throwing her golden crown into the dust, Puran's severed limbs, the dry well",
        "historicalThemes": [
            "Subversion of the 1,000-year-old Puran Bhagat legend",
            "Winning the Sahitya Akademi Award at 31 as the youngest laureate",
            "Backlash from conservative moralists and jealous literary gatekeepers"
        ],
        "poems": []
    },
    "realm_5_crossroad_void": {
        "id": "realm_5_crossroad_void",
        "name": "The Crossroad of the Void & Kir Mangyal (ਸੁੰਨ ਦਾ ਚੌਰਾਹਾ)",
        "climate": "Dusk turning to deep indigo night, distant ember sparks, autumn leaves drifting across railway tracks",
        "atmosphereTone": "Terminal peace, weary surrender, ghostly radio signals fading into static, immortality",
        "gameplayActivity": "Following faint audio static on an old tape recorder, discovering wiped reels, arriving at the silent village orchard",
        "sketchSubject": "Charcoal drawing of empty tape spools unwinding into the wind, a solitary hospital cot at dawn",
        "historicalThemes": [
            "The London exile and sole surviving BBC 1972 broadcast",
            "Institutional wiping of Akashvani and Doordarshan broadcast spools",
            "Untimely death at 36 in Kir Mangyal on May 6/7, 1973"
        ],
        "poems": []
    }
}

# Categorize each poem into the realms
for p in poems_data:
    biome = p.get("landscapeBiome", "")
    theme = p.get("philosophyTheme", "")
    book = p.get("book", "")

    if "loona" in p["id"] or theme == "feminism" or biome == "barren_mountain_loona":
        realms["realm_4_mountain_loona"]["poems"].append({
            "id": p["id"],
            "titleGurmukhi": p["titleGurmukhi"],
            "titleRoman": p["titleRoman"],
            "titleEnglish": p["titleEnglish"],
            "book": p["book"],
            "year": p["year"],
            "stanzasCount": len(p["stanzas"]),
            "sketchPrompt": p.get("sketchPrompt", "")
        })
    elif biome == "snowy_cabin_night" or "shikra" in p["id"] or "birha" in p["id"] or book == "Birha Tu Sultan":
        realms["realm_3_snowy_cabin"]["poems"].append({
            "id": p["id"],
            "titleGurmukhi": p["titleGurmukhi"],
            "titleRoman": p["titleRoman"],
            "titleEnglish": p["titleEnglish"],
            "book": p["book"],
            "year": p["year"],
            "stanzasCount": len(p["stanzas"]),
            "sketchPrompt": p.get("sketchPrompt", "")
        })
    elif biome == "cremation_dusk" or biome == "tavern_midnight" or book in ["Aarti & Aalvida", "Main Te Main"]:
        realms["realm_5_crossroad_void"]["poems"].append({
            "id": p["id"],
            "titleGurmukhi": p["titleGurmukhi"],
            "titleRoman": p["titleRoman"],
            "titleEnglish": p["titleEnglish"],
            "book": p["book"],
            "year": p["year"],
            "stanzasCount": len(p["stanzas"]),
            "sketchPrompt": p.get("sketchPrompt", "")
        })
    elif biome == "village_monsoon" or book in ["Aate Dian Chiriyean", "Piran da Paraga"]:
        realms["realm_2_monsoon_river"]["poems"].append({
            "id": p["id"],
            "titleGurmukhi": p["titleGurmukhi"],
            "titleRoman": p["titleRoman"],
            "titleEnglish": p["titleEnglish"],
            "book": p["book"],
            "year": p["year"],
            "stanzasCount": len(p["stanzas"]),
            "sketchPrompt": p.get("sketchPrompt", "")
        })
    else:
        realms["realm_1_dawn_hills"]["poems"].append({
            "id": p["id"],
            "titleGurmukhi": p["titleGurmukhi"],
            "titleRoman": p["titleRoman"],
            "titleEnglish": p["titleEnglish"],
            "book": p["book"],
            "year": p["year"],
            "stanzasCount": len(p["stanzas"]),
            "sketchPrompt": p.get("sketchPrompt", "")
        })

for r_key, r_val in realms.items():
    print(f"{r_val['name']}: {len(r_val['poems'])} poems allocated.")

# Save mapping
with open("season_game/PARSED_CORPUS_MAPPING.json", "w", encoding="utf-8") as f:
    json.dump(realms, f, ensure_ascii=False, indent=2)

print("Saved season_game/PARSED_CORPUS_MAPPING.json successfully!")
