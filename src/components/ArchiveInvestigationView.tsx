import React, { useState } from 'react';
import { ShieldAlert, Flame, FileText, CheckCircle2, AlertTriangle } from 'lucide-react';
import { archiveInvestigations } from '../data/archives';
import { CitationBadge } from './CitationBadge';

export const ArchiveInvestigationView: React.FC = () => {
  const [selectedItem, setSelectedItem] = useState(archiveInvestigations[0]);

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header */}
      <div className="rounded-2xl bg-gradient-to-r from-red-950/40 via-shiv-900 to-zinc-900 p-6 sm:p-10 border border-red-900/40 amber-border-glow">
        <div className="max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-500/10 text-red-400 border border-red-500/25 text-xs font-semibold uppercase tracking-wider">
            <ShieldAlert className="w-3.5 h-3.5" />
            Forensic Investigation • ਅਣਸੁਲਝੀ ਪੜਤਾਲ
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold font-serif-title text-zinc-100">
            The Myth of the Burned Diaries & Erased Tapes
          </h1>
          <p className="text-sm sm:text-base text-zinc-300 font-reading leading-relaxed">
            In modern Punjabi cultural discourse and viral internet exposés, it is alleged that rival leftist factions intentionally burned Shiv’s private diaries and deleted all his recordings from Akashvani and Doordarshan. What does historical evidence reveal?
          </p>
        </div>
      </div>

      {/* 2-Column Forensic Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Navigation List */}
        <div className="space-y-3">
          <h3 className="text-xs font-serif-title uppercase tracking-widest text-zinc-400 px-1">
            Investigation Case Files
          </h3>

          <div className="space-y-2">
            {archiveInvestigations.map((inv) => {
              const isSelected = inv.id === selectedItem.id;
              return (
                <button
                  key={inv.id}
                  onClick={() => setSelectedItem(inv)}
                  className={`w-full p-4 rounded-xl text-left border transition-all flex flex-col gap-2 ${
                    isSelected
                      ? 'bg-amber-500/15 border-amber-500/60 shadow-lg'
                      : 'bg-shiv-900/80 border-shiv-border hover:border-zinc-700 hover:bg-shiv-850'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span
                      className={`text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full ${
                        inv.verdict === 'Documented Loss'
                          ? 'bg-orange-500/20 text-orange-400 border border-orange-500/30'
                          : 'bg-red-500/20 text-red-400 border border-red-500/30'
                      }`}
                    >
                      {inv.verdict}
                    </span>
                  </div>
                  <h4 className="font-bold text-sm text-zinc-200 line-clamp-2">
                    {inv.title}
                  </h4>
                </button>
              );
            })}
          </div>

          {/* Quick Summary Infobox */}
          <div className="p-4 rounded-xl bg-zinc-900/70 border border-zinc-800 text-xs text-zinc-400 space-y-2 mt-4">
            <div className="flex items-center gap-1.5 text-amber-400 font-bold">
              <AlertTriangle className="w-3.5 h-3.5" />
              The Forensic Takeaway
            </div>
            <p className="leading-relaxed">
              The erasure was accomplished through a deadly combination of <strong>Shiv’s bohemian carelessness with papers</strong>, <strong>landlord room clearances</strong>, and <strong>state broadcaster tape-overwriting practices</strong>—exacerbated by cultural bureaucrats who showed zero interest in preserving his legacy while archiving political seminars.
            </p>
          </div>
        </div>

        {/* Right Active Case File Details */}
        <div className="lg:col-span-2 space-y-6">
          <div className="p-6 sm:p-8 rounded-2xl bg-shiv-900 border border-shiv-border shadow-xl space-y-6">
            {/* Header & Verdict */}
            <div className="border-b border-zinc-800 pb-5 space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-xs uppercase tracking-widest text-amber-500 font-semibold font-serif-title">
                  Archival Inquiry
                </span>
                <span className="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-amber-500/10 text-amber-400 border border-amber-500/30">
                  Verdict: {selectedItem.verdict}
                </span>
              </div>
              <h2 className="text-2xl sm:text-3xl font-bold font-serif-title text-zinc-100 flex flex-wrap items-center gap-1.5">
                <span>{selectedItem.title}</span>
                {selectedItem.citationIds && selectedItem.citationIds.map(cid => (
                  <CitationBadge key={cid} id={cid} />
                ))}
              </h2>
            </div>

            {/* The Myth vs The Reality Comparator */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="p-5 rounded-xl bg-red-950/20 border border-red-900/50 space-y-2">
                <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-red-400">
                  <Flame className="w-4 h-4" />
                  The Myth / Popular Allegation
                </div>
                <p className="text-xs sm:text-sm text-zinc-300 font-reading leading-relaxed">
                  {selectedItem.theMyth}
                </p>
              </div>

              <div className="p-5 rounded-xl bg-amber-950/20 border border-amber-900/50 space-y-2">
                <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-amber-400">
                  <CheckCircle2 className="w-4 h-4" />
                  The Historical Reality
                </div>
                <p className="text-xs sm:text-sm text-zinc-300 font-reading leading-relaxed">
                  {selectedItem.theReality}
                </p>
              </div>
            </div>

            {/* Historical Details */}
            <div className="p-4 rounded-xl bg-zinc-950 border border-zinc-800 text-xs sm:text-sm font-reading text-amber-100/90 leading-relaxed italic">
              "{selectedItem.historicalDetails}"
            </div>

            {/* Evidence Checklist */}
            <div className="space-y-3 pt-2">
              <h4 className="text-xs uppercase tracking-widest text-zinc-400 font-semibold flex items-center gap-1.5">
                <FileText className="w-3.5 h-3.5 text-amber-500" />
                Documented Evidence & Testimonies
              </h4>

              <div className="space-y-2.5">
                {selectedItem.evidence.map((ev, idx) => (
                  <div
                    key={idx}
                    className="p-3.5 rounded-lg bg-zinc-950/60 border border-zinc-800/80 flex items-start gap-3 text-xs sm:text-sm text-zinc-300"
                  >
                    <span className="text-amber-500 font-bold shrink-0">0{idx + 1}.</span>
                    <span className="leading-relaxed">{ev}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
