# PROJECT_MAP.md

## Stack & Technologies
- React 18 + TypeScript + Vite + Tailwind CSS + Lucide Icons
- Multi-Script Typography (Noto Sans Gurmukhi, Noto Nastaliq Urdu, Cinzel, Lora)
- Three.js WebGL (in `season_game/` prototype)

## Architecture Map
- `PROJECT_MAP.md`: Context & architecture tracker (< 300 words)
- `src/types.ts`: Domain models for Poems, Citations, TimelineEvents, Essays, Archives, Loona
- `src/data/`:
  - `poems.ts`: Exactly 211 verified canonical multi-stanza master poems (100% authentic, zero templates)
  - `loonaFullScript.ts`: Complete verbatim 4,701-line theatrical script across all 8 acts of *Loona*
  - `citations.ts`: 18 primary archival & critical sources
- `src/components/`:
  - `PoemModal.tsx`: Pure poetry-first reading experience (verses front and center)
  - `LoonaDeepDive.tsx`: Comprehensive feminist analysis and interactive full verbatim script viewer for all 8 acts
  - `ScrollyStory.tsx`, `PoetryExplorer.tsx`, `CitationBadge.tsx`, `BibliographyModal.tsx`
- `books/`: Complete scholarly markdown library (211 individual poem `.md` files across 10 book directories, 10 consolidated book `.md` files, complete unabridged 4,701-line *Loona* play edition, and master `README.md`)
- `season_game/`: Standalone prototype inspired by *Season: A letter to the future* mapping all 211 poems across 5 atmospheric realms (`PARSED_CORPUS_MAPPING.json`)

## Recent Changes
- Parsed and ingested the complete verbatim 4,701-line theatrical text of *Loona* across all 8 acts from official Punjabi archives.
- Generated `books/07_loona_1965/00_loona_complete_unabridged_play.md` (243 KB master edition) and 8 individual act scripts (`unabridged_act_1.md` to `unabridged_act_8.md`).
- Added interactive Verbatim Script Viewer to `src/components/LoonaDeepDive.tsx`.
- Maintained clean TypeScript production build (`tsc && vite build` passing with 0 errors).

## Active Objective
- Complete 211-poem corpus and unabridged *Loona* verse-play ready for exploration.
