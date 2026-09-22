import React, { useState } from 'react';
import { BookOpen, Clock, Quote, AlertCircle, Feather } from 'lucide-react';
import { essayChapters } from '../data/essays';

interface EssayViewProps {
  onSelectPoemId: (poemId: string) => void;
}

export const EssayView: React.FC<EssayViewProps> = ({ onSelectPoemId }) => {
  const [activeChapterId, setActiveChapterId] = useState<string>(essayChapters[0].id);

  const activeChapter = essayChapters.find((c) => c.id === activeChapterId) || essayChapters[0];

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Hero Intro */}
      <div className="rounded-2xl bg-gradient-to-r from-shiv-900 via-shiv-850 to-zinc-900 p-6 sm:p-10 border border-shiv-border/80 parchment-glow">
        <div className="max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 text-xs font-semibold uppercase tracking-wider">
            <BookOpen className="w-3.5 h-3.5" />
            Critical Deconstruction • ਪੜਚੋਲ
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold font-serif-title text-zinc-100">
            Beyond the Bollywood Hits
          </h1>
          <p className="text-sm sm:text-base text-zinc-300 font-reading leading-relaxed">
            Dismantling the romantic caricature of Shiv Kumar Batalvi. An exhaustive philosophical and political inquiry into the metaphysics of <em>Birha</em>, his bitter feuds with the Marxist establishment, the dialectic with revolutionary poet Paash, and the radical subversion of <em>Loona</em>.
          </p>
        </div>
      </div>

      {/* Chapter Selection Tabs */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        {essayChapters.map((chap) => {
          const isActive = chap.id === activeChapterId;
          return (
            <button
              key={chap.id}
              onClick={() => setActiveChapterId(chap.id)}
              className={`p-4 rounded-xl text-left border transition-all flex flex-col justify-between ${
                isActive
                  ? 'bg-amber-500/15 border-amber-500/50 shadow-lg'
                  : 'bg-shiv-900/80 border-shiv-border hover:border-zinc-700 hover:bg-shiv-850'
              }`}
            >
              <div className="space-y-1">
                <div className="flex items-center justify-between text-[11px] font-bold">
                  <span className={isActive ? 'text-amber-400' : 'text-zinc-500'}>
                    CHAPTER {chap.number}
                  </span>
                  <span className="text-zinc-500 flex items-center gap-1 font-sans">
                    <Clock className="w-3 h-3" />
                    {chap.readTime}
                  </span>
                </div>
                <h3 className="font-bold text-sm text-zinc-100 line-clamp-1">
                  {chap.title}
                </h3>
              </div>
              <span className="text-[11px] text-zinc-400 mt-2 block font-serif-title">
                {chap.coverLabel} →
              </span>
            </button>
          );
        })}
      </div>

      {/* Main Reading Article Container */}
      <article className="p-6 sm:p-12 rounded-2xl bg-shiv-900/90 border border-shiv-border max-w-4xl mx-auto shadow-2xl space-y-10">
        {/* Chapter Header */}
        <header className="border-b border-zinc-800 pb-8 space-y-3">
          <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-amber-500">
            <span>Chapter {activeChapter.number}</span>
            <span>•</span>
            <span>{activeChapter.coverLabel}</span>
            <span>•</span>
            <span className="flex items-center gap-1 text-zinc-400">
              <Clock className="w-3 h-3" />
              {activeChapter.readTime}
            </span>
          </div>

          <h2 className="text-2xl sm:text-4xl font-bold font-serif-title text-zinc-100 leading-tight">
            {activeChapter.title}
          </h2>

          <p className="text-base sm:text-lg text-amber-200/80 font-reading italic">
            "{activeChapter.subtitle}"
          </p>
        </header>

        {/* Chapter Sections */}
        <div className="space-y-10">
          {activeChapter.sections.map((sec) => (
            <section key={sec.id} className="space-y-5">
              <h3 className="text-xl sm:text-2xl font-bold text-zinc-100 font-serif-title">
                {sec.heading}
              </h3>

              <div className="space-y-4 text-sm sm:text-base font-reading text-zinc-300 leading-relaxed">
                {sec.paragraphs.map((p, pIdx) => (
                  <p key={pIdx}>{p}</p>
                ))}
              </div>

              {/* Callout Box */}
              {sec.callout && (
                <div
                  className={`p-5 rounded-xl border text-sm sm:text-base ${
                    sec.callout.type === 'quote'
                      ? 'bg-amber-950/20 border-amber-500/40 text-amber-100 italic font-reading'
                      : sec.callout.type === 'alert'
                      ? 'bg-red-950/20 border-red-500/40 text-red-200'
                      : 'bg-zinc-950 border-zinc-800 text-zinc-300'
                  }`}
                >
                  <div className="flex items-start gap-3">
                    {sec.callout.type === 'quote' && (
                      <Quote className="w-5 h-5 text-amber-500 shrink-0 mt-1" />
                    )}
                    {sec.callout.type === 'alert' && (
                      <AlertCircle className="w-5 h-5 text-red-500 shrink-0 mt-1" />
                    )}
                    <div>
                      <p>"{sec.callout.content}"</p>
                      {sec.callout.attribution && (
                        <div className="text-xs text-amber-400 font-sans not-italic font-semibold mt-2">
                          — {sec.callout.attribution}
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}
            </section>
          ))}
        </div>

        {/* Contextual Poem Navigation for This Chapter */}
        <div className="pt-8 border-t border-zinc-800 space-y-3">
          <h4 className="text-xs uppercase tracking-widest text-zinc-400 font-semibold flex items-center gap-1.5">
            <Feather className="w-3.5 h-3.5 text-amber-500" />
            Key Verses Analyzed in this Essay:
          </h4>
          <div className="flex flex-wrap gap-2">
            {activeChapter.id === 'chapter-1-birha' && (
              <>
                <button
                  onClick={() => onSelectPoemId('shikra-yaar')}
                  className="px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-amber-500 hover:text-black text-amber-300 text-xs transition-colors border border-zinc-700 font-medium"
                >
                  Main Ek Shikra Yaar Banaya →
                </button>
                <button
                  onClick={() => onSelectPoemId('joban-rutte-marna')}
                  className="px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-amber-500 hover:text-black text-amber-300 text-xs transition-colors border border-zinc-700 font-medium"
                >
                  Asan Taan Joban Rutte Marna →
                </button>
              </>
            )}

            {activeChapter.id === 'chapter-2-leftist-critique' && (
              <>
                <button
                  onClick={() => onSelectPoemId('kee-puchhde-o-haal')}
                  className="px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-amber-500 hover:text-black text-amber-300 text-xs transition-colors border border-zinc-700 font-medium"
                >
                  Kee Puchhde O Haal Fakiran Da →
                </button>
                <button
                  onClick={() => onSelectPoemId('aarti')}
                  className="px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-amber-500 hover:text-black text-amber-300 text-xs transition-colors border border-zinc-700 font-medium"
                >
                  Aarti (Mera Qatl Hoya) →
                </button>
              </>
            )}

            {activeChapter.id === 'chapter-3-paash-dialectic' && (
              <>
                <button
                  onClick={() => onSelectPoemId('main-te-main')}
                  className="px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-amber-500 hover:text-black text-amber-300 text-xs transition-colors border border-zinc-700 font-medium"
                >
                  Main te Main (The Split Self) →
                </button>
              </>
            )}

            {activeChapter.id === 'chapter-4-loona-subversion' && (
              <>
                <button
                  onClick={() => onSelectPoemId('loona-act4')}
                  className="px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-amber-500 hover:text-black text-amber-300 text-xs transition-colors border border-zinc-700 font-medium"
                >
                  Loona Da Vilaap (Act IV Defense) →
                </button>
              </>
            )}
          </div>
        </div>
      </article>
    </div>
  );
};
