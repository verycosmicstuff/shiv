import React, { useState } from 'react';
import { citationsDatabase } from '../data/citations';
import { ExternalLink, Bookmark, ShieldCheck } from 'lucide-react';

interface CitationBadgeProps {
  id: string;
  label?: string;
  className?: string;
}

export const CitationBadge: React.FC<CitationBadgeProps> = ({ id, label, className = '' }) => {
  const [isOpen, setIsOpen] = useState(false);
  const citation = citationsDatabase[id];

  if (!citation) return null;

  const displayLabel = label || `[${citation.author.split(' ')[0]} '${citation.publicationYear.toString().slice(2)}]`;

  return (
    <span className={`relative inline-block font-sans text-xs align-super ml-1 ${className}`}>
      <button
        type="button"
        onClick={(e) => {
          e.stopPropagation();
          setIsOpen(!isOpen);
        }}
        onMouseEnter={() => setIsOpen(true)}
        onMouseLeave={() => setIsOpen(false)}
        className="px-1.5 py-0.5 rounded text-[10px] tracking-wider font-mono font-medium text-amber-300/90 bg-amber-950/60 border border-amber-500/30 hover:bg-amber-800/60 hover:border-amber-400/70 hover:text-amber-200 transition-all duration-200 shadow-sm cursor-help"
        title={`Citation: ${citation.author}, ${citation.sourceTitle}`}
      >
        {displayLabel}
      </button>

      {isOpen && (
        <div 
          className="absolute z-50 bottom-full left-1/2 -translate-x-1/2 mb-2 w-80 max-w-[90vw] p-3.5 rounded-lg bg-stone-900/95 border border-amber-500/40 text-stone-200 shadow-2xl backdrop-blur-md animate-in fade-in zoom-in-95 duration-150 text-left font-sans normal-case pointer-events-auto"
          onMouseEnter={() => setIsOpen(true)}
          onMouseLeave={() => setIsOpen(false)}
        >
          {/* Header */}
          <div className="flex items-center justify-between pb-2 mb-2 border-b border-stone-800/80">
            <div className="flex items-center gap-1.5">
              <ShieldCheck className="w-3.5 h-3.5 text-amber-400" />
              <span className="text-[10px] uppercase font-mono tracking-wider text-amber-400/90 font-semibold">
                {citation.archiveType}
              </span>
            </div>
            <span className="text-[10px] font-mono text-stone-500">
              {citation.publicationYear}
            </span>
          </div>

          {/* Source Details */}
          <h4 className="text-xs font-serif font-bold text-amber-100 leading-snug">
            {citation.sourceTitle}
          </h4>
          <p className="text-[11px] text-stone-400 italic mb-2">
            by {citation.author} {citation.publisher && `• ${citation.publisher}`}
          </p>

          {/* Page or Timestamp */}
          {citation.pageOrTimestamp && (
            <div className="flex items-center gap-1 text-[10px] font-mono text-amber-300/70 mb-2">
              <Bookmark className="w-3 h-3" />
              <span>{citation.pageOrTimestamp}</span>
            </div>
          )}

          {/* Context Excerpt */}
          <p className="text-[11px] text-stone-300 leading-relaxed bg-stone-950/60 p-2 rounded border border-stone-800/60 font-serif">
            "{citation.contextExcerpt}"
          </p>

          {/* External Link if any */}
          {citation.url && (
            <a
              href={citation.url}
              target="_blank"
              rel="noopener noreferrer"
              className="mt-2 inline-flex items-center gap-1 text-[10px] text-amber-400 hover:text-amber-300 underline font-mono"
            >
              <span>View Archival Record</span>
              <ExternalLink className="w-2.5 h-2.5" />
            </a>
          )}
        </div>
      )}
    </span>
  );
};
