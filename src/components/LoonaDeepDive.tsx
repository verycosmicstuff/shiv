import React, { useState } from 'react';
import { Sparkles, Crown, AlertCircle, Feather, BookOpen, ScrollText } from 'lucide-react';
import { loonaActs } from '../data/loonaAnalysis';
import { loonaFullScript } from '../data/loonaFullScript';
import { CitationBadge } from './CitationBadge';

export const LoonaDeepDive: React.FC = () => {
  const [selectedActIndex, setSelectedActIndex] = useState(0);
  const [showFullScript, setShowFullScript] = useState<boolean>(false);

  const activeAct = loonaActs[selectedActIndex];
  const fullScriptAct = loonaFullScript[selectedActIndex];

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header Banner */}
      <div className="rounded-2xl bg-gradient-to-r from-amber-950/40 via-shiv-900 to-zinc-900 p-6 sm:p-10 border border-amber-900/40 amber-border-glow">
        <div className="max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/25 text-xs font-semibold uppercase tracking-wider">
            <Sparkles className="w-3.5 h-3.5" />
            The Sahitya Akademi Masterpiece (1965)
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold font-serif-title text-zinc-100">
            ਲੂਣਾ • The Subversion of Patriarchal Myth
          </h1>
          <p className="text-sm sm:text-base text-zinc-300 font-reading leading-relaxed">
            In 1965, at age 29, Shiv committed what conservatives called cultural heresy: he inverted the sacred legend of Puran Bhagat. Rather than portraying Loona as an evil temptress, he exposed the moral bankruptcy of an old king buying a teenage girl’s body with gold.
          </p>
        </div>
      </div>

      {/* Act Selection Tabs */}
      <div className="flex flex-wrap gap-2 p-2 rounded-xl bg-shiv-900 border border-shiv-border">
        {loonaActs.map((actItem, idx) => (
          <button
            key={actItem.act}
            onClick={() => setSelectedActIndex(idx)}
            className={`px-4 py-2.5 rounded-lg text-xs font-semibold transition-all flex items-center gap-2 ${
              selectedActIndex === idx
                ? 'bg-amber-500 text-black shadow-md'
                : 'bg-zinc-800/80 text-zinc-400 hover:text-zinc-200 hover:bg-zinc-700'
            }`}
          >
            <Crown className="w-3.5 h-3.5" />
            <span>Act {actItem.act}: {actItem.title.split(' ')[0]}</span>
          </button>
        ))}
      </div>

      {/* Act Comparison Display */}
      <div className="p-6 sm:p-10 rounded-2xl bg-shiv-900 border border-shiv-border shadow-2xl space-y-8">
        {/* Act Header */}
        <div className="border-b border-zinc-800 pb-5 space-y-2">
          <div className="text-xs uppercase tracking-widest text-amber-500 font-semibold font-serif-title">
            Act {activeAct.act} Analysis
          </div>
          <h2 className="text-2xl sm:text-3xl font-bold text-zinc-100 font-serif-title flex flex-wrap items-center gap-1.5">
            <span>{activeAct.title}</span>
            {activeAct.citationIds && activeAct.citationIds.map(cid => (
              <CitationBadge key={cid} id={cid} />
            ))}
          </h2>
        </div>

        {/* The Great Dialectic: Classical Folklore vs Shiv's Radical Subversion */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Classical Patriarchal Myth */}
          <div className="p-6 rounded-xl bg-zinc-950/80 border border-zinc-800 space-y-3">
            <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zinc-400">
              <AlertCircle className="w-4 h-4 text-zinc-500" />
              Classical Myth (Qadir Yar & Puran Legend)
            </div>
            <p className="text-sm font-reading text-zinc-300 leading-relaxed">
              {activeAct.classicalMyth}
            </p>
          </div>

          {/* Shiv's Feminist Subversion */}
          <div className="p-6 rounded-xl bg-amber-950/20 border border-amber-500/30 space-y-3">
            <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-amber-400">
              <Sparkles className="w-4 h-4 text-amber-500" />
              Shiv Kumar Batalvi’s Feminist Inversion
            </div>
            <p className="text-sm font-reading text-amber-100 leading-relaxed">
              {activeAct.shivSubversion}
            </p>
          </div>
        </div>

        {/* Philosophical Conflict Summary */}
        <div className="p-4 rounded-xl bg-zinc-950 border border-zinc-800 text-xs sm:text-sm text-zinc-300">
          <strong className="text-amber-400">Core Philosophical Tension: </strong>
          {activeAct.philosophicalConflict}
        </div>

        {/* Key Verses from the Act */}
        <div className="space-y-4 pt-4 border-t border-zinc-800">
          <h3 className="text-xs font-serif-title uppercase tracking-widest text-zinc-400 flex items-center gap-1.5">
            <Feather className="w-3.5 h-3.5 text-amber-500" />
            Key Dramatic Dialogue from Act {activeAct.act}
          </h3>

          <div className="space-y-6">
            {activeAct.keyDialogue.map((dialogue, dIdx) => (
              <div
                key={dIdx}
                className="p-6 rounded-xl bg-shiv-850/70 border border-shiv-border space-y-4"
              >
                <div className="flex items-center justify-between">
                  <span className="font-bold text-amber-400 text-sm font-serif-title">
                    {dialogue.speaker}
                  </span>
                  <span className="text-[11px] text-zinc-500 italic">
                    Original Gurmukhi & English Translation
                  </span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
                  <div className="space-y-2">
                    <p className="text-lg font-gurmukhi text-zinc-100 leading-relaxed whitespace-pre-line">
                      {dialogue.gurmukhi}
                    </p>
                    <p className="text-xs text-zinc-400 italic">
                      {dialogue.roman}
                    </p>
                  </div>

                  <div className="space-y-2">
                    <p className="text-sm sm:text-base font-reading text-amber-100 leading-relaxed whitespace-pre-line">
                      "{dialogue.english}"
                    </p>
                    <div className="p-3 rounded-lg bg-zinc-950/70 border border-zinc-800 text-xs text-zinc-400 italic">
                      💡 <strong>Exegesis: </strong>{dialogue.exegesis}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Complete Unabridged Script Section */}
        <div className="pt-6 border-t border-zinc-800 space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div>
              <h3 className="text-sm font-serif-title uppercase tracking-wider text-amber-400 font-bold flex items-center gap-2">
                <ScrollText className="w-4 h-4 text-amber-500" />
                ਸੰਪੂਰਨ ਕਾਵਿ-ਨਾਟਕ • Complete Unabridged Verse-Play Script
              </h3>
              <p className="text-xs text-zinc-400 mt-0.5">
                Verbatim theatrical performance script across all 8 acts (4,701 total verse lines).
              </p>
            </div>

            <button
              onClick={() => setShowFullScript(!showFullScript)}
              className="px-4 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500 text-amber-300 hover:text-black border border-amber-500/40 text-xs font-bold uppercase tracking-wider transition-all flex items-center gap-2 cursor-pointer"
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>{showFullScript ? 'Collapse Full Script' : `Read Verbatim Script of Act ${activeAct.act} (${fullScriptAct?.rawLineCount} Lines)`}</span>
            </button>
          </div>

          {showFullScript && fullScriptAct && (
            <div className="p-6 rounded-2xl bg-zinc-950/90 border border-amber-500/30 space-y-4 animate-fadeIn shadow-2xl">
              <div className="flex items-center justify-between pb-3 border-b border-zinc-800/80">
                <div>
                  <h4 className="text-xl font-bold text-amber-300 font-gurmukhi">
                    {fullScriptAct.titleGurmukhi}
                  </h4>
                  <span className="text-xs text-zinc-400 italic">
                    {fullScriptAct.titleEnglish} • {fullScriptAct.rawLineCount} Verse Lines
                  </span>
                </div>
                <div className="text-[11px] text-zinc-500">
                  Full Theatrical Dialogue
                </div>
              </div>

              <div className="max-h-[550px] overflow-y-auto pr-3 space-y-4 font-gurmukhi text-zinc-200 text-base sm:text-lg leading-loose whitespace-pre-line select-text border-l-2 border-amber-500/30 pl-4 bg-zinc-900/40 rounded-r-lg p-4">
                {fullScriptAct.fullText}
              </div>

              <div className="pt-2 text-xs text-zinc-400 text-center border-t border-zinc-800">
                End of Act {fullScriptAct.actNumber} • Complete offline script available in <code className="text-amber-400">books/07_loona_1965/00_loona_complete_unabridged_play.md</code>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
