# -*- coding: utf-8 -*-
"""
generate_unabridged_loona_md.py
Generates full verbatim markdown editions for all 8 acts of Loona (1965)
in books/07_loona_1965/ and exports structured data to src/data/loonaFullScript.ts.
"""

import json
import os
import re

with open("books/07_loona_1965/LOONA_UNABRIDGED_PARSED.json", "r", encoding="utf-8") as f:
    acts = json.load(f)

print(f"Loaded {len(acts)} acts from parsed JSON.")

output_dir = "books/07_loona_1965"

dramatis_personae = """
## 🎭 Dramatis Personæ (ਪਾਤਰ-ਸੂਚੀ)

1. **ਸੂਤਰਧਾਰ (Sūtradhāra)**: The theatrical presenter and cosmic chorus of the play.
2. **ਨਟੀ (Naṭī)**: Sūtradhāra’s consort, muse, and lyrical interlocutor.
3. **ਰਾਜਾ ਸਲਵਾਨ (Rājā Salwān)**: The aged, battle-hardened monarch of Sialkot; father to Pūran.
4. **ਵਰਮਨ (Varman)**: Prime Minister and royal confidant to King Salwān.
5. **ਇੱਛਰਾਂ (Ichhrāṁ)**: Chief Queen of Sialkot; mother of Pūran; abandoned by Salwān.
6. **ਲੂਣਾ (Lūṇā)**: Young leather-worker's (*chamar*) daughter from Chamba; forced into marriage with Salwān; seeker of living love.
7. **ਇਰਾ (Irā)**: Lūṇā’s loyal maiden, confidante, and realist companion.
8. **ਪੂਰਨ (Pūran)**: Prince of Sialkot; raised 18 years in a subterranean vault; devoted ascetic adherent of Dharma.
9. **ਚੰਬਿਆਲਣਾਂ (Women of Chamba)**: Agrarian folk chorus.
10. **ਜੱਲਾਦ (The Executioners)**: Henchmen tasked with mutilating and discarding Pūran into the dry well.
"""

# 1. Generate consolidated master file: 00_loona_complete_unabridged_play.md
master_md = f"""# ਲੂਣਾ (Lūṇā) — Complete Unabridged Verse-Play (ਸੰਪੂਰਨ ਕਾਵਿ-ਨਾਟਕ)

### By Shiv Kumar Batalvi (ਸਿ਼ਵ ਕੁਮਾਰ ਬਟਾਲਵੀ)
### Sahitya Akademi Award Winner (1967) • Navyug Publishers, Delhi (1965)

---

## 📖 Archival Synopsis

> *Loona* (1965) is Shiv Kumar Batalvi's crowning theatrical masterpiece. Across **8 monumental acts** and **4,701 lines of authentic blank-verse dialogue**, Shiv staging a revolutionary feminist and socio-ethical rebellion against the ancient Punjabi myth of *Pūran Bhagat*.
>
> For a thousand years, patriarchal folklore had demonized Loona as the treacherous stepmother who lusted after the chaste saint Puran. Shiv inverted the moral polarity of the myth entirely: exposing King Salwan's forced purchase of an impoverished teenager's body as feudal violence, and crowning Loona's desire for living youth over decrepit gold as pure and sacred human truth.

{dramatis_personae}

---

## 📑 Table of Acts

| Act | Title (Gurmukhi) | English Thematic Title | Total Verse Lines | Standalone File |
|:---:|:---|:---|:---:|:---:|
"""

for act in acts:
    num = act["actNumber"]
    title_g = act["titleGurmukhi"]
    title_e = act["titleEnglish"]
    lines = act["rawLineCount"]
    filename = f"unabridged_act_{num}.md"
    master_md += f"| {num} | [{title_g}](#act-{num}) | {title_e} | {lines} lines | [📄 {filename}](./{filename}) |\n"

master_md += f"\n**Total Verse Dialogue**: **{sum(a['rawLineCount'] for a in acts)} lines** across **8 Acts**.\n\n---\n\n"

# Append each act in full verbatim text
for act in acts:
    num = act["actNumber"]
    title_g = act["titleGurmukhi"]
    title_e = act["titleEnglish"]
    lines = act["rawLineCount"]
    text = act["fullText"]
    
    master_md += f'<a id="act-{num}"></a>\n\n'
    master_md += f"# {title_g}\n"
    master_md += f"## *{title_e}* ({lines} Lines)\n\n"
    master_md += f"[Back to Table of Acts](#table-of-acts) | [View Standalone File](./unabridged_act_{num}.md)\n\n"
    master_md += "---\n\n"
    master_md += f"{text}\n\n"
    master_md += "---\n\n"

master_file_path = os.path.join(output_dir, "00_loona_complete_unabridged_play.md")
with open(master_file_path, "w", encoding="utf-8") as f:
    f.write(master_md)

print(f"Written master unabridged play: {master_file_path} ({len(master_md)} characters)")

# 2. Write individual act standalone files
for act in acts:
    num = act["actNumber"]
    title_g = act["titleGurmukhi"]
    title_e = act["titleEnglish"]
    lines = act["rawLineCount"]
    text = act["fullText"]
    
    prev_link = f"[⬅️ Previous Act](./unabridged_act_{num-1}.md) | " if num > 1 else ""
    next_link = f" | [Next Act ➡️](./unabridged_act_{num+1}.md)" if num < len(acts) else ""
    
    act_md = f"""# {title_g}
## *{title_e}*

- **Play**: [Lūṇā (1965)](./00_loona_complete_unabridged_play.md) by Shiv Kumar Batalvi
- **Act**: {num} of 8
- **Verse Lines**: {lines} lines of authentic dialogue
- **Navigation**: {prev_link}[📖 Master Play Index](./00_loona_complete_unabridged_play.md) | [📚 Anthology Overview](../07_loona_1965.md){next_link}

---

{text}

---

## 🧭 Navigation
{prev_link}[📖 Complete Unabridged Play](./00_loona_complete_unabridged_play.md) | [📚 Book 7: Loona Overview](../07_loona_1965.md){next_link}
"""
    act_file_path = os.path.join(output_dir, f"unabridged_act_{num}.md")
    with open(act_file_path, "w", encoding="utf-8") as f:
        f.write(act_md)
    print(f"Written {act_file_path}")

# 3. Export to src/data/loonaFullScript.ts for React App
ts_code = "export interface UnabridgedLoonaAct {\n"
ts_code += "  actNumber: number;\n"
ts_code += "  titleGurmukhi: string;\n"
ts_code += "  titleEnglish: string;\n"
ts_code += "  rawLineCount: number;\n"
ts_code += "  fullText: string;\n"
ts_code += "}\n\n"
ts_code += "export const loonaFullScript: UnabridgedLoonaAct[] = "
ts_code += json.dumps(acts, ensure_ascii=False, indent=2)
ts_code += ";\n"

with open("src/data/loonaFullScript.ts", "w", encoding="utf-8") as f:
    f.write(ts_code)

print("Exported src/data/loonaFullScript.ts for React Web App!")
