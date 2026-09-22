import React, { useState } from 'react';
import { citationsDatabase } from '../data/citations';
import { BookOpen, X, Search, Bookmark, ExternalLink, Filter } from 'lucide-react';

interface BibliographyModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const BibliographyModal: React.FC<BibliographyModalProps> = ({ isOpen, onClose }) => {
  const [search, setSearch] = useState('');
  const [selectedType, setSelectedType] = useState<string>('all');

  if (!isOpen) return null;

  const allCitations = Object.values(citationsDatabase);
  const archiveTypes = ['all', ...Array.from(new Set(allCitations.map(c => c.archiveType)))];

  const filteredCitations = allCitations.filter(c => {
    const matchesSearch = 
      c.author.toLowerCase().includes(search.toLowerCase()) ||
      c.sourceTitle.toLowerCase().includes(search.toLowerCase()) ||
      c.contextExcerpt.toLowerCase().includes(search.toLowerCase());
    const matchesType = selectedType === 'all' || c.archiveType === selectedType;
    return matchesSearch && matchesType;
  });

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md animate-in fade-in duration-200">
      <div 
        className="relative w-full max-w-4xl max-h-[90vh] flex flex-col bg-stone-900 border border-amber-500/30 rounded-2xl shadow-2xl overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-5 border-b border-stone-800 bg-stone-950/60">
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-xl font-serif font-bold text-amber-100">
                Archival Ledger & Bibliography
              </h3>
              <p className="text-xs text-stone-400 font-sans">
                Academic provenance, primary memoirs, and broadcast archives cited across this retrospective
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-xl text-stone-400 hover:text-stone-100 hover:bg-stone-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Search & Filter Controls */}
        <div className="flex flex-wrap items-center gap-3 px-6 py-4 bg-stone-900/90 border-b border-stone-800">
          <div className="relative flex-1 min-w-[240px]">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-stone-500" />
            <input
              type="text"
              placeholder="Search by author, source title, or historical quote..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full pl-9 pr-4 py-2 text-xs bg-stone-950/80 border border-stone-800 rounded-lg text-stone-200 placeholder-stone-500 focus:outline-none focus:border-amber-500/50"
            />
          </div>

          <div className="flex items-center gap-1.5 overflow-x-auto pb-1 max-w-full">
            <Filter className="w-3.5 h-3.5 text-stone-500 mr-1" />
            {archiveTypes.map(type => (
              <button
                key={type}
                onClick={() => setSelectedType(type)}
                className={`px-2.5 py-1 rounded-md text-[11px] font-mono whitespace-nowrap transition-colors ${
                  selectedType === type
                    ? 'bg-amber-500/20 border border-amber-500/50 text-amber-300 font-medium'
                    : 'bg-stone-800/60 border border-stone-700/40 text-stone-400 hover:text-stone-200'
                }`}
              >
                {type === 'all' ? 'All Sources' : type}
              </button>
            ))}
          </div>
        </div>

        {/* Citation Cards List */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4 divide-y divide-stone-800/40">
          {filteredCitations.map(c => (
            <div key={c.id} className="pt-4 first:pt-0 space-y-2">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="px-2 py-0.5 rounded text-[10px] font-mono uppercase tracking-wider bg-stone-800 border border-stone-700 text-amber-400">
                      {c.archiveType}
                    </span>
                    <span className="text-xs font-mono text-stone-500">
                      {c.publicationYear}
                    </span>
                    <span className="text-[11px] font-mono text-stone-600">
                      ID: {c.id}
                    </span>
                  </div>
                  <h4 className="text-base font-serif font-bold text-amber-100">
                    {c.sourceTitle}
                  </h4>
                  <p className="text-xs text-stone-400 italic">
                    Authored by <strong className="text-stone-300 font-sans">{c.author}</strong>
                    {c.publisher && ` • Published by ${c.publisher}`}
                  </p>
                </div>

                {c.pageOrTimestamp && (
                  <div className="flex items-center gap-1.5 text-xs font-mono text-amber-400/80 bg-stone-950 px-2.5 py-1 rounded border border-stone-800 shrink-0">
                    <Bookmark className="w-3.5 h-3.5 text-amber-500" />
                    <span>{c.pageOrTimestamp}</span>
                  </div>
                )}
              </div>

              <div className="bg-stone-950/70 border border-stone-800/80 rounded-xl p-3.5">
                <p className="text-xs font-serif text-stone-300 leading-relaxed">
                  "{c.contextExcerpt}"
                </p>
              </div>

              {c.url && (
                <div className="pt-1">
                  <a
                    href={c.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1.5 text-xs text-amber-400 hover:text-amber-300 underline font-mono"
                  >
                    <span>Inspect Holding Institution Record</span>
                    <ExternalLink className="w-3 h-3" />
                  </a>
                </div>
              )}
            </div>
          ))}

          {filteredCitations.length === 0 && (
            <div className="py-12 text-center text-stone-500 font-serif">
              No matching archival citations found.
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-stone-950 border-t border-stone-800 flex items-center justify-between text-xs text-stone-500 font-mono">
          <span>{filteredCitations.length} of {allCitations.length} Citations Available</span>
          <span className="text-stone-600">Archival verification standard: Primary Memoirs & University Archives</span>
        </div>
      </div>
    </div>
  );
};
