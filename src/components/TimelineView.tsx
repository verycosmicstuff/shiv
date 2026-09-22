import React, { useState, useMemo } from 'react';
import { Clock, MapPin, Quote, Feather, AlertTriangle, Book, User, History } from 'lucide-react';
import { timelineDatabase } from '../data/timeline';
import { poemsDatabase } from '../data/poems';
import { CitationBadge } from './CitationBadge';

interface TimelineViewProps {
  onSelectPoemId: (poemId: string) => void;
}

export const TimelineView: React.FC<TimelineViewProps> = ({ onSelectPoemId }) => {
  const [selectedCategory, setSelectedCategory] = useState<string>('all');

  const categories = [
    { id: 'all', label: 'All Milestones' },
    { id: 'personal', label: 'Personal & Bohemia', icon: User },
    { id: 'literary', label: 'Literary Publications', icon: Book },
    { id: 'controversy', label: 'Feuds & Backlash', icon: AlertTriangle },
    { id: 'political_context', label: 'Partition & Politics', icon: History }
  ];

  const filteredEvents = useMemo(() => {
    if (selectedCategory === 'all') return timelineDatabase;
    return timelineDatabase.filter((e) => e.category === selectedCategory);
  }, [selectedCategory]);

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-shiv-900 via-shiv-850 to-zinc-900 p-6 sm:p-10 border border-shiv-border/80 parchment-glow">
        <div className="max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 text-xs font-semibold uppercase tracking-wider">
            <Clock className="w-3.5 h-3.5" />
            The Fated 36 Years • 1936–1973
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold font-serif-title text-zinc-100">
            Chronicles of the Tortured Genius
          </h1>
          <p className="text-sm sm:text-base text-zinc-300 font-reading leading-relaxed">
            From childhood displacement during the 1947 Partition to becoming the youngest Sahitya Akademi laureate at 31, and his tragic death at 36 in Kir Mangyal. Explore how each personal and political earthquake birthed his most famous verses.
          </p>
        </div>
      </div>

      {/* Category Filter Chips */}
      <div className="flex flex-wrap gap-2 p-3 bg-shiv-900 rounded-xl border border-shiv-border">
        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(cat.id)}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
              selectedCategory === cat.id
                ? 'bg-amber-500 text-black font-semibold shadow-md'
                : 'bg-zinc-800/80 text-zinc-400 hover:text-zinc-200 hover:bg-zinc-700'
            }`}
          >
            {cat.label}
          </button>
        ))}
      </div>

      {/* Timeline Vertical Track */}
      <div className="relative border-l-2 border-zinc-800 ml-4 sm:ml-8 pl-6 sm:pl-10 space-y-12 pb-8">
        {filteredEvents.map((event) => {
          const relatedPoems = poemsDatabase.filter((p) => event.relatedPoemIds.includes(p.id));

          return (
            <div key={event.id} className="relative group">
              {/* Timeline Marker Dot */}
              <div 
                className={`absolute -left-[31px] sm:-left-[47px] top-1 w-6 h-6 rounded-full border-2 transition-all flex items-center justify-center ${
                  event.category === 'controversy'
                    ? 'border-red-500 bg-red-950 text-red-400'
                    : event.category === 'literary'
                    ? 'border-amber-500 bg-amber-950 text-amber-400'
                    : 'border-zinc-500 bg-zinc-900 text-zinc-300'
                }`}
              >
                <div className="w-2 h-2 rounded-full bg-current" />
              </div>

              {/* Event Card */}
              <div className="p-6 rounded-2xl bg-shiv-900 border border-shiv-border hover:border-amber-500/40 transition-all shadow-lg space-y-4">
                {/* Event Header */}
                <div className="flex flex-wrap items-center justify-between gap-2 border-b border-zinc-800/80 pb-3">
                  <div className="flex items-center gap-3">
                    <span className="text-xl sm:text-2xl font-black font-serif-title text-amber-400">
                      {event.year}
                    </span>
                    <span className="text-xs text-zinc-400 font-medium px-2 py-0.5 rounded bg-zinc-800">
                      {event.period}
                    </span>
                  </div>

                  <div className="flex items-center gap-1.5 text-xs text-zinc-400">
                    <MapPin className="w-3.5 h-3.5 text-amber-500" />
                    <span>{event.location}</span>
                  </div>
                </div>

                {/* Event Title */}
                <div>
                  <h3 className="text-xl sm:text-2xl font-bold text-zinc-100 flex flex-wrap items-center gap-1.5">
                    <span>{event.title}</span>
                    {event.citationIds && event.citationIds.map(cid => (
                      <CitationBadge key={cid} id={cid} />
                    ))}
                  </h3>
                  <p className="text-sm text-zinc-300 mt-1 font-reading">
                    {event.summary}
                  </p>
                </div>

                {/* Narrative Details */}
                <div className="space-y-3 pt-1">
                  <p className="text-xs sm:text-sm text-zinc-300 leading-relaxed">
                    {event.deepNarrative}
                  </p>

                  <div className="p-3 rounded-lg bg-zinc-950/60 border border-zinc-800/80 text-xs">
                    <strong className="text-amber-400">Impact on His Art: </strong>
                    <span className="text-zinc-300">{event.impactOnPoetry}</span>
                  </div>
                </div>

                {/* Quote Box if present */}
                {event.keyQuote && (
                  <div className="p-3.5 rounded-xl bg-amber-950/20 border-l-4 border-amber-500 text-xs sm:text-sm italic font-reading text-amber-100 flex items-start gap-2.5">
                    <Quote className="w-4 h-4 text-amber-500 shrink-0 mt-0.5" />
                    <div>
                      <p>"{event.keyQuote.text}"</p>
                      <span className="text-[11px] text-amber-400/80 font-sans not-italic block mt-1">
                        — {event.keyQuote.source}
                      </span>
                    </div>
                  </div>
                )}

                {/* Related Poems Buttons */}
                {relatedPoems.length > 0 && (
                  <div className="pt-2 border-t border-zinc-800/80 flex flex-wrap items-center gap-2">
                    <span className="text-xs text-zinc-400 font-semibold flex items-center gap-1">
                      <Feather className="w-3.5 h-3.5 text-amber-500" />
                      Verses Written in This Era:
                    </span>
                    {relatedPoems.map((p) => (
                      <button
                        key={p.id}
                        onClick={() => onSelectPoemId(p.id)}
                        className="px-2.5 py-1 rounded-md bg-amber-500/10 hover:bg-amber-500 text-amber-300 hover:text-black border border-amber-500/25 text-xs font-medium transition-all"
                      >
                        {p.titleGurmukhi} ({p.titleRoman}) →
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
