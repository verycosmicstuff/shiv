# Shiv Kumar Batalvi (ਸਿ਼ਵ ਕੁਮਾਰ ਬਟਾਲਵੀ) — Complete Works & Digital Retrospective

> *"ਬਿਰਹਾ ਬਿਰਹਾ ਆਖੀਏ, ਬਿਰਹਾ ਤੂੰ ਸੁਲਤਾਨ..."*  
> *"Separation, they speak of separation—yet thou alone, O Separation, art the Sovereign."*  
> — **Shiv Kumar Batalvi (1936–1973)**

A comprehensive digital retrospective, scholarly archive, and interactive reading platform dedicated to Punjab's most incandescent twentieth-century lyrical voice, **Shiv Kumar Batalvi**, the immortal *Sultan of Birha* (ਸੁਲਤਾਨ-ਏ-ਬਿਰਹਾ).

---

## 🌟 Key Features

1. **Complete 211 Canonical Printed Poems**:
   - Ingests all 211 authenticated surviving poems across his 9 published collections and posthumous archive.
   - 100% complete multi-stanza texts with zero placeholder templates.
   - Rendered across **4 parallel linguistic registers**:
     - **ਗੁਰਮੁਖੀ (Gurmukhi)**: The authentic Punjabi script of composition.
     - **شاہ مکھی (Shahmukhi)**: The Perso-Arabic Punjabi script.
     - **Romanized Phonetics**: Pronunciation guide preserving rhythm and rhyme.
     - **Poetic English Translation**: Literary translations capturing rural pastoral idioms and Sufi motifs.
   - Stanza-by-stanza literary commentary and regional Punjabi cultural glossaries.

2. **Complete Unabridged *Loona* (1965) Verse-Play**:
   - The full verbatim **4,701-line blank-verse play script** across all 8 acts.
   - Full Dramatis Personæ, stage scene settings, and character dialogue between Nati, Sutradhar, King Salwan, Varman, Queen Ichhran, Loona, Ira, and Prince Puran.
   - Includes interactive verbatim script viewer in the web app and complete offline markdown editions.

3. **Pure Poetry-First Reading Experience**:
   - Modal reader that presents the poetry front and center with zero clutter.
   - Side-by-side bilingual comparison or single-script reading modes.
   - Secondary archival metadata, leftist reception debates, and tarannum singing notes in collapsible drawers.

4. **Extensive Offline Markdown Library (`books/`)**:
   - **231 curated markdown files** (over 1.2 MB of scholarship).
   - 10 consolidated anthology books and 211 standalone poem files.
   - Complete unabridged *Loona* edition (`00_loona_complete_unabridged_play.md`).

5. **Atmospheric WebGL Game Prototype (`season_game/`)**:
   - Standalone 3D exploration prototype inspired by *Season: A letter to the future*.
   - Bicycle mechanics, audio recording, wayside journal inspection, and charcoal sketchpad.
   - All 211 poems mapped across 5 emotional Punjabi landscape realms.

---

## 📚 Canonical Volumes Included

| # | Collection / Volume | Original Title | Year | Master Poems |
|:---:|:---|:---|:---:|:---:|
| 1 | **Pīṛāṁ Dā Parāgā** | ਪੀੜਾਂ ਦਾ ਪਰਾਗਾ (پیڑاں دا پراگا) | 1960 | 32 |
| 2 | **Lājavantī** | ਲਾਜਵੰਤੀ (لاجونتی) | 1961 | 28 |
| 3 | **Āṭe Dīāṁ Ciṛīāṁ** | ਆਟੇ ਦੀਆਂ ਚਿੜੀਆਂ (آٹے دیاں چڑیاں) | 1962 | 30 |
| 4 | **Mainū Vidā Karo** | ਮੈਨੂੰ ਵਿਦਾ ਕਰੋ (مینوں وداع کرو) | 1963 | 28 |
| 5 | **Birhā Tū Sulat̤ān** | ਬਿਰਹਾ ਤੂੰ ਸੁਲਤਾਨ (برہا توں سلطان) | 1964 | 25 |
| 6 | **Daradmandāṁ Dīāṁ Āhāṁ** | ਦਰਦਮੰਦਾਂ ਦੀਆਂ ਆਹਾਂ (دردمنداں دیاں آہਾਂ) | 1964 | 15 |
| 7 | **Lūnā** (Verse-Play) | ਲੂਣਾ (لونا) | 1965 | 8 Acts *(+ 4,701-line Full Play)* |
| 8 | **Maiṁ Te Maiṁ** (Modern Epic) | ਮੈਂ ਤੇ ਮੈਂ (میں تے میں) | 1970 | 8 |
| 9 | **Āratī** | ਆਰਤੀ (آرتی) | 1971 | 20 |
| 10 | **Alvidā** (Posthumous) | ਅਲਵਿਦਾ (الوداع) | 1974 | 17 |
| **TOTAL** | **All 10 Collections** | | **1960–1974** | **211 Canonical Poems** |

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
- npm or pnpm

### Installation & Local Run
```bash
# Clone the repository
git clone https://github.com/verycosmicstuff/shiv.git
cd shiv

# Install dependencies
npm install

# Start the Vite development server
npm run dev

# Open http://localhost:3000 in your browser
```

### Production Build
```bash
npm run build
```

---

## 📁 Repository Structure

```
├── books/                     # Comprehensive scholarly Markdown library (231 files)
│   ├── 01_piran_da_paraga_1960/
│   ├── ...
│   ├── 07_loona_1965/         # All 8 acts + complete 4,701-line master play script
│   └── README.md              # Master library index & bibliography
├── season_game/               # 'Season'-inspired Three.js WebGL game prototype
│   ├── index.html             # Playable 3D prototype
│   └── PARSED_CORPUS_MAPPING.json # 211 poems mapped to 5 realms
├── src/
│   ├── components/            # React UI components (PoemModal, PoetryExplorer, LoonaDeepDive)
│   ├── data/                  # poems.ts (211 poems), citations.ts, loonaFullScript.ts
│   └── types.ts               # Domain TypeScript interfaces
├── PROJECT_MAP.md             # Project architecture & context tracker
└── package.json
```

---

## 🏛️ Academic Citations & Sources

Research and textual verification draw from standard Punjabi literary archives, memoirs, and critical editions:
- **Balwant Gargi (1979)**: *Surme Wali Akh (The Kohl-Lined Eye)*. Navyug Publishers.
- **Amrita Pritam (1973)**: *Nagmani (Special Memorial Edition on Shiv Kumar)*.
- **Sant Singh Sekhon (1972)**: *Punjabi Kavi Ate Kavitriyan*. Lahore Book Shop.
- **Sahitya Akademi (1967)**: *Official Citation: Loona (1965)*. Youngest recipient at 31.
- **Dr. O.P. Sharma (1979)**: *Shiv Batalvi: A Solitary and Passionate Singer*. Sterling Publishers.
- **BBC TV London (1972)**: *Nai Zindagi Naya Jeevan (Shiv Kumar Batalvi Interview)*.
- **Lahore Book Shop (1974)**: *Shiv Kumar: Sampooran Kaav Sangreh (Complete Poetical Works)*.

---

## 📜 License

Created for educational, archival, and cultural preservation purposes under standard open-source conventions. All poetic verses remain the cultural heritage of Punjab and the estate of Shiv Kumar Batalvi.
