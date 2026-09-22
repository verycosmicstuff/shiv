import React, { useState } from 'react';
import { X, Book, Sparkles, AlertCircle, Music, Languages, Info } from 'lucide-react';
import { Poem, ScriptMode } from '../types';

interface PoemModalProps {
  poem: Poem | null;
  onClose: () => void;
  onSelectPoem?: (poemId: string) => void;
}

export const PoemModal: React.FC<PoemModalProps> = ({ poem, onClose, onSelectPoem }) => {
  const [scriptMode, setScriptMode] = useState<ScriptMode>('bilingual');

  if (!poem) return null;

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto bg-black/80 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6 animate-fadeIn">
      <div 
        className="bg-shiv-900 border border-shiv-border/90 rounded-2xl w-full max-w-4xl max-h-[92vh] flex flex-col shadow-2xl overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Modal Header */}
        <div className="p-5 sm:p-6 border-b border-shiv-border bg-shiv-850/80 flex items-start justify-between gap-4">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-2">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/15 text-amber-400 border border-amber-500/30 flex items-center gap-1">
                <Book className="w-3 h-3" />
                {poem.book} ({poem.year})
              </span>
              <span className="px-2.5 py-0.5 rounded-full text-xs font-medium bg-zinc-800 text-zinc-300 border border-zinc-700">
                Theme: {poem.philosophyTheme.toUpperCase()}
              </span>
            </div>
            
            <h2 className="text-2xl sm:text-3xl font-bold font-gurmukhi text-amber-300">
              {poem.titleGurmukhi}
            </h2>
            <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm text-zinc-400 mt-1">
              <span className="font-shahmukhi text-base text-zinc-300">{poem.titleShahmukhi}</span>
              <span>•</span>
              <span className="italic font-serif-title">{poem.titleRoman}</span>
              <span>•</span>
              <span className="text-zinc-300">{poem.titleEnglish}</span>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-full bg-zinc-800/80 hover:bg-zinc-700 text-zinc-400 hover:text-white transition-colors"
            aria-label="Close modal"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Script Selection Bar */}
        <div className="px-5 py-3 bg-shiv-950 border-b border-shiv-border flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-1.5 text-xs text-zinc-400">
            <Languages className="w-4 h-4 text-amber-500" />
            <span className="font-medium">Reading Mode:</span>
          </div>

          <div className="flex flex-wrap gap-1 bg-zinc-900 p-1 rounded-lg border border-zinc-800">
            {[
              { id: 'bilingual' as ScriptMode, label: 'Side-by-Side (Bilingual)' },
              { id: 'gurmukhi' as ScriptMode, label: 'ਗੁਰਮੁਖੀ' },
              { id: 'shahmukhi' as ScriptMode, label: 'شاہ مکھی' },
              { id: 'roman' as ScriptMode, label: 'Romanized' },
              { id: 'english' as ScriptMode, label: 'English' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setScriptMode(tab.id)}
                className={`px-2.5 py-1 text-xs rounded-md transition-all font-medium ${
                  scriptMode === tab.id
                    ? 'bg-amber-500 text-black font-semibold shadow-sm'
                    : 'text-zinc-400 hover:text-white hover:bg-zinc-800/80'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </div>

        {/* Modal Scrollable Body */}
        <div className="overflow-y-auto p-5 sm:p-8 space-y-8 flex-1">
          {/* Stanzas Display - POEMS FIRST */}
          <div className="space-y-6">
            <div className="flex items-center justify-between border-b border-zinc-800 pb-2">
              <h3 className="text-xs font-serif-title uppercase tracking-widest text-amber-400 font-semibold flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-amber-500" />
                ਕਵਿਤਾ • Poetic Verses ({poem.stanzas.length} Stanzas)
              </h3>
              <span className="text-[11px] text-zinc-500 italic">
                Multi-Script Masterwork
              </span>
            </div>

            {poem.stanzas.map((stanza, idx) => (
              <div 
                key={idx} 
                className="p-5 sm:p-6 rounded-xl bg-shiv-850/50 border border-shiv-border hover:border-amber-500/40 transition-colors"
              >
                {scriptMode === 'bilingual' ? (
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {/* Left: Original Gurmukhi */}
                    <div className="space-y-3">
                      <div className="text-[11px] font-semibold tracking-wider uppercase text-amber-500">
                        Gurmukhi (Original)
                      </div>
                      <p className="text-lg sm:text-xl font-gurmukhi leading-loose text-zinc-100 whitespace-pre-line">
                        {stanza.gurmukhi}
                      </p>
                      <div className="pt-2 border-t border-zinc-800/60 text-xs text-zinc-400 font-sans italic">
                        {stanza.roman}
                      </div>
                    </div>

                    {/* Right: English Translation */}
                    <div className="space-y-3">
                      <div className="text-[11px] font-semibold tracking-wider uppercase text-zinc-400">
                        Poetic Translation
                      </div>
                      <p className="text-base font-reading leading-relaxed text-amber-100/90 whitespace-pre-line">
                        {stanza.english}
                      </p>
                      {stanza.commentary && (
                        <div className="pt-2 border-t border-zinc-800/60 text-xs text-zinc-400 italic">
                          💡 {stanza.commentary}
                        </div>
                      )}
                    </div>
                  </div>
                ) : (
                  <div className="space-y-3">
                    {scriptMode === 'gurmukhi' && (
                      <p className="text-xl sm:text-2xl font-gurmukhi leading-loose text-zinc-100 whitespace-pre-line">
                        {stanza.gurmukhi}
                      </p>
                    )}
                    {scriptMode === 'shahmukhi' && (
                      <p className="text-2xl font-shahmukhi leading-loose text-zinc-100 whitespace-pre-line text-right" dir="rtl">
                        {stanza.shahmukhi}
                      </p>
                    )}
                    {scriptMode === 'roman' && (
                      <p className="text-base sm:text-lg font-sans italic leading-relaxed text-zinc-200 whitespace-pre-line">
                        {stanza.roman}
                      </p>
                    )}
                    {scriptMode === 'english' && (
                      <p className="text-base sm:text-lg font-reading leading-relaxed text-amber-100 whitespace-pre-line">
                        {stanza.english}
                      </p>
                    )}

                    {stanza.commentary && (
                      <p className="text-xs text-zinc-400 pt-2 border-t border-zinc-800/80 italic">
                        💡 {stanza.commentary}
                      </p>
                    )}
                  </div>
                )}
              </div>
            ))}
          </div>

          {/* Cultural Glossary Section */}
          {poem.culturalGlossary && poem.culturalGlossary.length > 0 && (
            <div className="space-y-3 pt-4 border-t border-zinc-800">
              <h3 className="text-xs font-serif-title uppercase tracking-widest text-zinc-400">
                Cultural & Agrarian Idiom Glossary
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {poem.culturalGlossary.map((item, idx) => (
                  <div key={idx} className="p-3 rounded-lg bg-zinc-900 border border-zinc-800">
                    <div className="flex items-baseline justify-between mb-1">
                      <span className="font-bold text-amber-400 text-sm">{item.term}</span>
                      <span className="text-[11px] text-zinc-500 font-sans italic">{item.pronunciation}</span>
                    </div>
                    <div className="text-xs text-zinc-300 font-medium mb-1">
                      Literal: <span className="text-zinc-400">{item.literal}</span>
                    </div>
                    <p className="text-xs text-zinc-400 leading-snug">
                      {item.culturalMeaning}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Related Poems Links */}
          {poem.relatedPoemIds && poem.relatedPoemIds.length > 0 && onSelectPoem && (
            <div className="pt-4 border-t border-zinc-800 flex items-center gap-2 text-xs">
              <span className="text-zinc-400 font-medium">Thematically Linked Poems:</span>
              <div className="flex flex-wrap gap-2">
                {poem.relatedPoemIds.map((relId) => (
                  <button
                    key={relId}
                    onClick={() => onSelectPoem(relId)}
                    className="px-2.5 py-1 rounded bg-zinc-800 hover:bg-amber-500 hover:text-black text-amber-300 border border-zinc-700 transition-colors"
                  >
                    View {relId} →
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Optional Collapsible Archival & Context Notes (Hidden by default) */}
          {(poem.summary || poem.backstory || poem.critiqueContext || poem.tarannumNote) && (
            <details className="group rounded-xl border border-zinc-800/80 bg-zinc-900/30 overflow-hidden text-xs">
              <summary className="p-3.5 cursor-pointer flex items-center justify-between text-zinc-500 hover:text-amber-400 font-medium select-none transition-colors">
                <div className="flex items-center gap-2">
                  <Info className="w-3.5 h-3.5 text-zinc-500 group-hover:text-amber-400" />
                  <span>Archival Background & Reception Notes (Optional)</span>
                </div>
                <span className="text-[10px] text-zinc-500 group-open:rotate-180 transition-transform">▼</span>
              </summary>
              <div className="p-4 pt-2 border-t border-zinc-800/60 space-y-4">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {poem.summary && (
                    <div className="p-3 rounded-lg bg-zinc-950/60 border border-zinc-800/80">
                      <span className="text-amber-400/90 font-bold block mb-1 text-[11px] uppercase tracking-wide">Philosophical Core</span>
                      <p className="text-zinc-300 leading-relaxed">{poem.summary}</p>
                    </div>
                  )}
                  {poem.backstory && (
                    <div className="p-3 rounded-lg bg-zinc-950/60 border border-zinc-800/80">
                      <span className="text-amber-400/90 font-bold block mb-1 text-[11px] uppercase tracking-wide">The Backstory & The Muse</span>
                      <p className="text-zinc-300 leading-relaxed">{poem.backstory}</p>
                    </div>
                  )}
                </div>

                {(poem.critiqueContext || poem.tarannumNote) && (
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {poem.critiqueContext && (
                      <div className="p-3 rounded-lg bg-red-950/20 border border-red-800/30 text-zinc-300">
                        <div className="flex items-center gap-1.5 font-bold mb-1 text-red-400 uppercase tracking-wide">
                          <AlertCircle className="w-3 h-3" />
                          <span>Leftist / Critical Reception</span>
                        </div>
                        <p className="leading-relaxed">{poem.critiqueContext}</p>
                      </div>
                    )}
                    {poem.tarannumNote && (
                      <div className="p-3 rounded-lg bg-amber-950/20 border border-amber-800/30 text-zinc-300">
                        <div className="flex items-center gap-1.5 font-bold mb-1 text-amber-400 uppercase tracking-wide">
                          <Music className="w-3 h-3" />
                          <span>Tarannum Performance Note</span>
                        </div>
                        <p className="leading-relaxed">{poem.tarannumNote}</p>
                      </div>
                    )}
                  </div>
                )}
              </div>
            </details>
          )}
        </div>

        {/* Modal Footer */}
        <div className="p-4 bg-shiv-950 border-t border-shiv-border flex items-center justify-between text-xs text-zinc-500">
          <span>Shiv Kumar Batalvi (1936–1973) • Sahitya Akademi Laureate</span>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-zinc-800 hover:bg-zinc-700 text-zinc-200 transition-colors font-medium"
          >
            Close Reader
          </button>
        </div>
      </div>
    </div>
  );
};
