import React, { useState, useMemo } from 'react';
import { Search, Filter, Feather, BookOpen, Music, Sparkles } from 'lucide-react';
import { Poem } from '../types';
import { poemsDatabase } from '../data/poems';

interface PoetryExplorerProps {
  onSelectPoem: (poem: Poem) => void;
}

export const PoetryExplorer: React.FC<PoetryExplorerProps> = ({ onSelectPoem }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedBook, setSelectedBook] = useState<string>('all');
  const [selectedTheme, setSelectedTheme] = useState<string>('all');
  const [visibleCount, setVisibleCount] = useState<number>(24);

  // Reset pagination when search or filters change
  React.useEffect(() => {
    setVisibleCount(24);
  }, [searchQuery, selectedBook, selectedTheme]);

  const books = useMemo(() => {
    const list = Array.from(new Set(poemsDatabase.map((p) => p.book)));
    return ['all', ...list];
  }, []);

  const getBookCount = (bookName: string) => {
    if (bookName === 'all') return poemsDatabase.length;
    return poemsDatabase.filter(p => p.book === bookName).length;
  };

  const themes = [
    { id: 'all', label: 'All Themes' },
    { id: 'birha', label: 'Birha & Cosmic Longing' },
    { id: 'mortality', label: 'Maut & Romance of Youth' },
    { id: 'feminism', label: 'Loona & Anti-Patriarchy' },
    { id: 'folklore', label: 'Agrarian Punjab & Kilns' },
    { id: 'modernism', label: 'Split Psyche & Alienation' },
    { id: 'rebellion', label: 'Defiance & Existential Rebellion' },
    { id: 'solitude', label: 'Solitude & The Inner Void' },
  ];

  const filteredPoems = useMemo(() => {
    return poemsDatabase.filter((p) => {
      const q = searchQuery.toLowerCase().trim();
      const matchesSearch =
        !q ||
        p.titleGurmukhi.toLowerCase().includes(q) ||
        p.titleShahmukhi.toLowerCase().includes(q) ||
        p.titleRoman.toLowerCase().includes(q) ||
        p.titleEnglish.toLowerCase().includes(q) ||
        p.summary.toLowerCase().includes(q) ||
        p.tags.some((t) => t.toLowerCase().includes(q)) ||
        p.stanzas.some(
          (s) =>
            s.gurmukhi.toLowerCase().includes(q) ||
            s.english.toLowerCase().includes(q) ||
            s.roman.toLowerCase().includes(q)
        );

      const matchesBook = selectedBook === 'all' || p.book === selectedBook;
      const matchesTheme = selectedTheme === 'all' || p.philosophyTheme === selectedTheme;

      return matchesSearch && matchesBook && matchesTheme;
    });
  }, [searchQuery, selectedBook, selectedTheme]);

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Hero Header */}
      <div className="relative rounded-2xl bg-gradient-to-br from-shiv-900 via-shiv-850 to-amber-950/30 p-6 sm:p-10 border border-shiv-border/80 overflow-hidden parchment-glow">
        <div className="relative z-10 max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 text-xs font-semibold uppercase tracking-wider">
            <Feather className="w-3.5 h-3.5" />
            Complete Digital Diwan • ਸਮੁੱਚੀ ਕਵਿਤਾ
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold font-gurmukhi text-zinc-100 tracking-tight">
            ਕਵਿਤਾ ਕੋਸ਼ : ਸ਼ਿਵ ਦਾ ਦੀਵਾਨ
          </h1>
          <p className="text-sm sm:text-base text-zinc-300 font-reading leading-relaxed">
            Explore the poetry of Shiv Kumar Batalvi across his canonical anthologies. Read in original{' '}
            <strong className="text-amber-400">Gurmukhi</strong>,{' '}
            <strong className="text-amber-400">Shahmukhi</strong> (Western Punjabi),{' '}
            <strong className="text-amber-400">Romanized phonetics</strong>, and verse-by-verse{' '}
            <strong className="text-amber-400">poetic English translations</strong> with cultural annotations.
          </p>
        </div>
      </div>

      {/* Search & Filter Controls */}
      <div className="space-y-4 p-5 rounded-xl bg-shiv-900 border border-shiv-border">
        {/* Search Bar */}
        <div className="relative">
          <Search className="w-5 h-5 absolute left-3.5 top-1/2 -translate-y-1/2 text-zinc-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search by poem title, lyrics (Gurmukhi / English), theme, or folk metaphor (e.g., shikra, bhatthi)..."
            className="w-full pl-11 pr-4 py-3 rounded-lg bg-zinc-950 border border-zinc-800 text-sm text-zinc-100 placeholder-zinc-500 focus:outline-none focus:border-amber-500 focus:ring-1 focus:ring-amber-500 transition-colors"
          />
          {searchQuery && (
            <button
              onClick={() => setSearchQuery('')}
              className="absolute right-3.5 top-1/2 -translate-y-1/2 text-xs text-zinc-500 hover:text-zinc-300 bg-zinc-800 px-2 py-0.5 rounded"
            >
              Clear
            </button>
          )}
        </div>

        {/* Filter Rows */}
        <div className="flex flex-col sm:flex-row gap-4 justify-between items-start sm:items-center pt-2">
          {/* Theme Filters */}
          <div className="flex flex-wrap gap-1.5 items-center">
            <span className="text-xs font-semibold text-zinc-400 flex items-center gap-1 mr-1">
              <Filter className="w-3.5 h-3.5 text-amber-500" />
              Theme:
            </span>
            {themes.map((t) => (
              <button
                key={t.id}
                onClick={() => setSelectedTheme(t.id)}
                className={`px-3 py-1 rounded-full text-xs transition-all ${
                  selectedTheme === t.id
                    ? 'bg-amber-500 text-black font-semibold'
                    : 'bg-zinc-800/80 text-zinc-400 hover:text-zinc-200 hover:bg-zinc-700'
                }`}
              >
                {t.label}
              </button>
            ))}
          </div>

          {/* Book Dropdown */}
          <div className="flex items-center gap-2 text-xs text-zinc-400 self-end sm:self-auto">
            <BookOpen className="w-3.5 h-3.5 text-amber-500" />
            <span>Anthology:</span>
            <select
              value={selectedBook}
              onChange={(e) => setSelectedBook(e.target.value)}
              className="bg-zinc-950 border border-zinc-800 rounded-md px-2.5 py-1 text-xs text-zinc-200 focus:outline-none focus:border-amber-500"
            >
              {books.map((b) => (
                <option key={b} value={b}>
                  {b === 'all' ? `All Anthologies (${poemsDatabase.length})` : `${b} (${getBookCount(b)})`}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* Results Count */}
      <div className="flex items-center justify-between text-xs text-zinc-400 px-1">
        <span>
          Showing <strong className="text-amber-400">{Math.min(visibleCount, filteredPoems.length)}</strong> of <strong className="text-amber-400">{filteredPoems.length}</strong> masterworks
        </span>
        <span className="italic">Click any card to launch the multi-script reader</span>
      </div>

      {/* Poems Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredPoems.slice(0, visibleCount).map((poem) => (
          <div
            key={poem.id}
            onClick={() => onSelectPoem(poem)}
            className="group cursor-pointer rounded-xl bg-shiv-900/90 hover:bg-shiv-850 border border-shiv-border hover:border-amber-500/50 p-6 flex flex-col justify-between transition-all duration-300 hover:shadow-xl hover:-translate-y-1"
          >
            <div className="space-y-4">
              {/* Card Meta */}
              <div className="flex items-center justify-between gap-2">
                <span className="text-[11px] font-semibold px-2 py-0.5 rounded bg-zinc-800 text-zinc-300 border border-zinc-700">
                  {poem.book} ({poem.year})
                </span>
                <span className="text-[10px] uppercase font-bold tracking-wider text-amber-400/80">
                  {poem.philosophyTheme}
                </span>
              </div>

              {/* Card Title */}
              <div>
                <h3 className="text-xl font-bold font-gurmukhi text-zinc-100 group-hover:text-amber-300 transition-colors">
                  {poem.titleGurmukhi}
                </h3>
                <div className="text-xs text-zinc-400 italic font-serif-title mt-0.5">
                  {poem.titleRoman}
                </div>
                <div className="text-xs text-zinc-300 font-reading mt-0.5">
                  "{poem.titleEnglish}"
                </div>
              </div>

              {/* Stanza Excerpt */}
              <div className="p-3 rounded-lg bg-zinc-950/70 border border-zinc-800/80 text-xs font-gurmukhi text-zinc-300 leading-relaxed italic line-clamp-3">
                {poem.stanzas[0]?.gurmukhi}
              </div>

              {/* Summary */}
              <p className="text-xs text-zinc-400 line-clamp-2 leading-relaxed">
                {poem.summary}
              </p>
            </div>

            {/* Card Footer */}
            <div className="pt-4 mt-4 border-t border-zinc-800/80 flex items-center justify-between text-xs">
              <div className="flex items-center gap-1.5 text-zinc-500 group-hover:text-amber-400 transition-colors">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Multi-Script Reader</span>
              </div>

              {poem.tarannumNote && (
                <span className="flex items-center gap-1 text-[11px] text-amber-500/80">
                  <Music className="w-3 h-3" />
                  Tarannum
                </span>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Load More Button */}
      {visibleCount < filteredPoems.length && (
        <div className="flex justify-center pt-6 pb-2">
          <button
            onClick={() => setVisibleCount((prev) => prev + 24)}
            className="px-6 py-3 rounded-xl bg-amber-500/15 hover:bg-amber-500 text-amber-300 hover:text-black border border-amber-500/30 text-xs font-bold uppercase tracking-wider transition-all shadow-lg hover:shadow-amber-500/20 cursor-pointer flex items-center gap-2"
          >
            <span>Load Next 24 Poems ({filteredPoems.length - visibleCount} remaining)</span>
            <Feather className="w-3.5 h-3.5" />
          </button>
        </div>
      )}

      {filteredPoems.length === 0 && (
        <div className="text-center py-16 p-8 rounded-2xl bg-zinc-900 border border-zinc-800 space-y-3">
          <Feather className="w-10 h-10 text-zinc-600 mx-auto" />
          <h3 className="text-lg font-bold text-zinc-300">No poems match your search</h3>
          <p className="text-xs text-zinc-500">
            Try adjusting your search terms or clearing the theme/book filters.
          </p>
          <button
            onClick={() => {
              setSearchQuery('');
              setSelectedBook('all');
              setSelectedTheme('all');
            }}
            className="px-4 py-2 rounded-lg bg-amber-500 text-black font-semibold text-xs mt-2"
          >
            Reset Filters
          </button>
        </div>
      )}
    </div>
  );
};
