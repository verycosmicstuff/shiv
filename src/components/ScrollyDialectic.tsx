import React, { useState } from 'react';
import { Feather, Flame, ArrowRightLeft } from 'lucide-react';

interface ComparisonPair {
  id: string;
  theme: string;
  shivVerseGurmukhi: string;
  shivVerseEnglish: string;
  shivSource: string;
  paashVerseGurmukhi: string;
  paashVerseEnglish: string;
  paashSource: string;
  analysis: string;
}

export const ScrollyDialectic: React.FC = () => {
  const [activeComparisonIndex, setActiveComparisonIndex] = useState<number>(0);

  const comparisons: ComparisonPair[] = [
    {
      id: 'metaphor',
      theme: '1. The Falcon vs. The Grass (ਪੰਛੀ ਬਨਾਮ ਘਾਹ)',
      shivVerseGurmukhi: 'ਮੈਂ ਇੱਕ ਸ਼ਿਕਰਾ ਯਾਰ ਬਣਾਇਆ,\nਚੂਰੀ ਕੁੱਟਾਂ ਤਾਂ ਉਹ ਖਾਂਵਦਾ ਨਾਹੀ,\nਉਹਨੂੰ ਦਿਲ ਦਾ ਮਾਸ ਖਵਾਇਆ।',
      shivVerseEnglish: 'I took a falcon as my lover,\nHe would not touch sweet crumbled bread,\nSo I fed him the raw flesh of my own heart.',
      shivSource: 'Main Ek Shikra Yaar Banaya (1964)',
      paashVerseGurmukhi: 'ਮੈਂ ਘਾਹ ਹਾਂ,\nਮੈਂ ਤੁਹਾਡੇ ਹਰ ਕੀਤੇ ਤੇ ਉੱਗ ਆਵਾਂਗਾ,\nਬੰਬ ਸੁੱਟ ਦਿਓ ਚਾਹੇ ਯੂਨੀਵਰਸਿਟੀ ਬਣਾ ਦਿਓ!',
      paashVerseEnglish: 'I am grass,\nI will sprout upon your every slaughter,\nDrop your bombs, pave your universities—I will return!',
      paashSource: 'Main Ghaah Haan (1970)',
      analysis: 'Shiv personalizes the raptor that consumes him from within; Paash universalizes the stubborn, unkillable peasantry that outlives state brutality.'
    },
    {
      id: 'death',
      theme: '2. The Romance of Death vs. The Threat of Numbness',
      shivVerseGurmukhi: 'ਅਸਾਂ ਤਾਂ ਜੋਬਨ ਰੁੱਤੇ ਮਰਨਾ,\nਮੁਰਝਾ ਜਾਣਾ ਰੂਪ ਕੁਆਰਾਂ,\nਤੁਰ ਜਾਣਾ ਬੇ-ਡਰਨਾ।',
      shivVerseEnglish: 'We shall die in the springtime of our years,\nLike unplucked blossoms withering before their time,\nWalking into the night without fear.',
      shivSource: 'Asan Taan Joban Rutte Marna (1964)',
      paashVerseGurmukhi: 'ਸਭ ਤੋਂ ਖ਼ਤਰਨਾਕ ਹੁੰਦਾ ਹੈ\nਸਾਡੇ ਸੁਪਨਿਆਂ ਦਾ ਮਰ ਜਾਣਾ,\nਮੁਰਦਾ ਸ਼ਾਂਤੀ ਨਾਲ ਭਰ ਜਾਣਾ!',
      paashVerseEnglish: 'The most dangerous thing of all\nIs the death of our dreams,\nTo be filled with the silence of the graveyard!',
      paashSource: 'Sabhton Khatarnak (1973)',
      analysis: 'Shiv courts death to preserve the purity of youth before it decays; Paash warns that the real death is apathy, numbness, and subservience to tyranny.'
    },
    {
      id: 'blood',
      theme: '3. The Red Wound vs. The Red Flag',
      shivVerseGurmukhi: 'ਉਹ ਆਖਦੇ ਨੇ ਝੰਡੇ ਦੀ ਲਾਲੀ ਤੇ ਲਿਖ,\nਮੈਂ ਆਖਦਾ ਹਾਂ ਜ਼ਖ਼ਮ ਦੀ ਲਾਲੀ ਤੇ ਲਿਖਾਂਗਾ!',
      shivVerseEnglish: 'They command me to write about the redness of the flag;\nI answer: I can only write about the redness of the wound!',
      shivSource: 'Spoken in Chandigarh Coffee House',
      paashVerseGurmukhi: 'ਜੇ ਲਹੂ ਚਾਹੀਦਾ ਹੈ ਕ੍ਰਾਂਤੀ ਨੂੰ,\nਤਾਂ ਅਸੀਂ ਆਪਣੀਆਂ ਨਸਾਂ ਖੋਲ੍ਹ ਦਿਆਂਗੇ,\nਪਰ ਹੰਝੂਆਂ ਨਾਲ ਹਲ ਨਹੀਂ ਚੱਲਦੇ!',
      paashVerseEnglish: 'If the revolution demands blood,\nWe will slice open our very veins,\nFor wooden plows cannot turn soil wet with tears!',
      paashSource: 'Loh-Katha (1970)',
      analysis: 'Shiv insists that authentic human agony cannot be subjected to a committee; Paash insists that mere sorrow without resistance changes nothing.'
    }
  ];

  const current = comparisons[activeComparisonIndex];

  return (
    <div className="space-y-6 my-12 p-6 sm:p-10 rounded-2xl bg-zinc-950 border-2 border-zinc-800 shadow-2xl parchment-sheet">
      {/* Header */}
      <div className="text-center space-y-2 max-w-2xl mx-auto">
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-red-950/60 border border-red-800 text-red-400 text-xs font-typewriter font-bold uppercase tracking-widest">
          <ArrowRightLeft className="w-3.5 h-3.5" />
          The Great Dialectic of Punjab • 1968–1973
        </div>
        <h3 className="text-2xl sm:text-3xl font-serif-title font-bold text-zinc-100">
          The Hawk vs. The Grass : Shiv & Paash
        </h3>
        <p className="text-xs sm:text-sm text-zinc-400 font-reading">
          The two opposite poles of the modern Punjabi soul: The <em>Aesthetics of Being</em> (inward heartbreak) versus the <em>Ethics of Revolution</em> (outward peasant rebellion).
        </p>
      </div>

      {/* Comparison Selector */}
      <div className="flex flex-wrap justify-center gap-2 pt-2">
        {comparisons.map((c, idx) => (
          <button
            key={c.id}
            onClick={() => setActiveComparisonIndex(idx)}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
              activeComparisonIndex === idx
                ? 'bg-amber-500 text-black shadow-md'
                : 'bg-zinc-900 text-zinc-400 hover:text-zinc-200 border border-zinc-800'
            }`}
          >
            {c.theme}
          </button>
        ))}
      </div>

      {/* Side-by-Side Dual Pane */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4">
        {/* Left Column: Shiv Kumar Batalvi */}
        <div className="p-6 rounded-xl bg-amber-950/20 border border-amber-800/40 space-y-4 relative overflow-hidden">
          <div className="flex items-center justify-between border-b border-amber-800/40 pb-2">
            <div className="flex items-center gap-2">
              <Feather className="w-4 h-4 text-amber-500" />
              <span className="font-bold text-amber-400 font-serif-title text-sm">
                ਸਿ਼ਵ ਕੁਮਾਰ ਬਟਾਲਵੀ
              </span>
            </div>
            <span className="text-[10px] font-mono uppercase bg-amber-950 px-2 py-0.5 rounded border border-amber-800 text-amber-300">
              The Intimate Wound
            </span>
          </div>

          <div className="space-y-3">
            <p className="text-lg font-gurmukhi font-bold text-amber-100 leading-relaxed whitespace-pre-line">
              {current.shivVerseGurmukhi}
            </p>
            <p className="text-sm font-reading text-amber-200/80 italic pt-2 border-t border-amber-900/50">
              "{current.shivVerseEnglish}"
            </p>
          </div>

          <div className="text-[11px] font-typewriter text-amber-400/80 pt-2 border-t border-amber-900/40">
            Source: {current.shivSource}
          </div>
        </div>

        {/* Right Column: Paash */}
        <div className="p-6 rounded-xl bg-red-950/20 border border-red-800/40 space-y-4 relative overflow-hidden">
          <div className="flex items-center justify-between border-b border-red-800/40 pb-2">
            <div className="flex items-center gap-2">
              <Flame className="w-4 h-4 text-red-500" />
              <span className="font-bold text-red-400 font-serif-title text-sm">
                ਅਵਤਾਰ ਸਿੰਘ ਪਾਸ਼ (PAASH)
              </span>
            </div>
            <span className="text-[10px] font-mono uppercase bg-red-950 px-2 py-0.5 rounded border border-red-800 text-red-300">
              The Revolutionary Fire
            </span>
          </div>

          <div className="space-y-3">
            <p className="text-lg font-gurmukhi font-bold text-red-100 leading-relaxed whitespace-pre-line">
              {current.paashVerseGurmukhi}
            </p>
            <p className="text-sm font-reading text-red-200/80 italic pt-2 border-t border-red-900/50">
              "{current.paashVerseEnglish}"
            </p>
          </div>

          <div className="text-[11px] font-typewriter text-red-400/80 pt-2 border-t border-red-900/40">
            Source: {current.paashSource}
          </div>
        </div>
      </div>

      {/* Critical Synthesis Callout */}
      <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800 text-xs sm:text-sm text-zinc-300 font-reading leading-relaxed">
        <strong className="text-amber-400 font-serif-title">Critical Dialectic: </strong>
        {current.analysis}
      </div>
    </div>
  );
};
