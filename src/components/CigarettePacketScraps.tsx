import React, { useState } from 'react';
import { Feather, Pin, X } from 'lucide-react';

interface Scrap {
  id: string;
  source: string;
  vintageLabel: string;
  rotation: string;
  gurmukhi: string;
  english: string;
  poemId: string;
  story: string;
}

interface CigarettePacketScrapsProps {
  onOpenPoemModal: (poemId: string) => void;
}

export const CigarettePacketScraps: React.FC<CigarettePacketScrapsProps> = ({ onOpenPoemModal }) => {
  const [selectedScrap, setSelectedScrap] = useState<Scrap | null>(null);

  const scraps: Scrap[] = [
    {
      id: 'gold-flake',
      source: 'Gold Flake Cigarette Packet Foil',
      vintageLabel: 'BATALA, 1964 • GOLD FLAKE',
      rotation: '-rotate-2',
      gurmukhi: 'ਮਾਏ ਨੀ ਮਾਏ ਮੈਂ ਇੱਕ ਸ਼ਿਕਰਾ ਯਾਰ ਬਣਾਇਆ...\nਚੂਰੀ ਕੁੱਟਾਂ ਤਾਂ ਉਹ ਖਾਂਵਦਾ ਨਾਹੀ,\nਉਹਨੂੰ ਦਿਲ ਦਾ ਮਾਸ ਖਵਾਇਆ!',
      english: 'O mother, I took a falcon as my lover;\nI offered sweet bread, but he would not eat,\nSo I fed him the raw flesh of my heart!',
      poemId: 'shikra-yaar',
      story: 'Scribbled after midnight in a Batala rooming house on the torn silver foil of a 10-pack of Gold Flake cigarettes.'
    },
    {
      id: 'coffee-house',
      source: 'Indian Coffee House Napkin, Sector 17',
      vintageLabel: 'CHANDIGARH, 1966 • NAPKIN',
      rotation: 'rotate-3',
      gurmukhi: 'ਕੀ ਪੁੱਛਦੇ ਓ ਹਾਲ ਫ਼ਕੀਰਾਂ ਦਾ...\nਸਾਡਾ ਅੰਗ ਅੰਗ ਦਾਗ਼਼ ਦੁਖੀਰਾਂ ਦਾ!\nਅਸੀਂ ਹੱਸਦੇ ਤਾਂ ਜੱਗ ਖਿਝਦਾ!',
      english: 'Why ask after the state of us wandering beggars?\nEvery limb of ours is scarred with sorrow!\nAnd when we laugh, the world is enraged!',
      poemId: 'kee-puchhde-o-haal',
      story: 'Written with a leaking fountain pen over black coffee while Marxist writers argued about Soviet five-year plans at the adjacent table.'
    },
    {
      id: 'bank-slip',
      source: 'State Bank of India Deposit Voucher',
      vintageLabel: 'SECTOR 17 BANK, 1968 • VOUCHER',
      rotation: '-rotate-1',
      gurmukhi: 'ਅਸਾਂ ਤਾਂ ਜੋਬਨ ਰੁੱਤੇ ਮਰਨਾ...\nਮੁਰਝਾ ਜਾਣਾ ਰੂਪ ਕੁਆਰਾਂ,\nਤੁਰ ਜਾਣਾ ਬੇ-ਡਰਨਾ!',
      english: 'We shall die in the springtime of our years...\nLike unplucked blossoms withering before their time,\nWalking into the night without fear!',
      poemId: 'joban-rutte-marna',
      story: 'Penned behind the bank counter during work hours when Shiv was supposed to be balancing credit ledgers.'
    }
  ];

  return (
    <div className="space-y-4 my-10">
      <div className="text-center space-y-1">
        <div className="inline-flex items-center gap-1.5 text-xs font-typewriter uppercase tracking-widest text-amber-500 font-bold">
          <Pin className="w-3.5 h-3.5" />
          The Ephemera of Genius • ਸਿਗਰਟਾਂ ਦੇ ਖੋਲ੍ਹ
        </div>
        <h3 className="text-xl sm:text-2xl font-serif-title font-bold text-zinc-100">
          Lost Verses Scribbled on Scrap Paper
        </h3>
        <p className="text-xs sm:text-sm text-zinc-400 max-w-xl mx-auto font-reading">
          Shiv never sat at a polished mahogany desk. He scribbled masterpieces in smoke-filled cafes, bars, and bank desks. Click any paper scrap to unfold the original handwritten verse:
        </p>
      </div>

      {/* Scattered Scraps Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4">
        {scraps.map((scrap) => (
          <div
            key={scrap.id}
            onClick={() => setSelectedScrap(scrap)}
            className={`cursor-pointer transform ${scrap.rotation} hover:rotate-0 hover:scale-105 transition-all duration-300 p-6 rounded-lg bg-[#f4ebe1] text-zinc-900 shadow-2xl border border-[#d8ccbe] flex flex-col justify-between relative overflow-hidden group`}
          >
            {/* Paper Pin Graphic */}
            <div className="absolute top-2 right-3 flex items-center gap-1 opacity-60">
              <span className="w-2.5 h-2.5 rounded-full bg-red-800 shadow" />
            </div>

            <div className="space-y-3">
              <div className="text-[10px] font-typewriter font-bold tracking-widest uppercase text-red-800 border-b border-zinc-300 pb-1">
                {scrap.vintageLabel}
              </div>

              <div className="font-gurmukhi text-lg font-bold text-zinc-900 leading-snug whitespace-pre-line">
                {scrap.gurmukhi}
              </div>

              <div className="text-xs font-reading text-zinc-700 italic border-t border-zinc-300/80 pt-2 line-clamp-2">
                "{scrap.english}"
              </div>
            </div>

            <div className="mt-4 pt-2 border-t border-zinc-300/60 flex items-center justify-between text-[11px] font-typewriter text-zinc-600">
              <span className="underline group-hover:text-red-800">Unfold Scrap ↗</span>
              <span className="text-[10px] bg-zinc-200/80 px-1.5 py-0.5 rounded">ORIGINAL</span>
            </div>
          </div>
        ))}
      </div>

      {/* Unfolded Scrap Modal */}
      {selectedScrap && (
        <div 
          className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4"
          onClick={() => setSelectedScrap(null)}
        >
          <div 
            className="bg-[#f7efe6] text-zinc-900 max-w-lg w-full p-8 rounded-xl shadow-2xl border-2 border-amber-800/40 space-y-6 relative animate-fadeIn"
            onClick={(e) => e.stopPropagation()}
          >
            <button
              onClick={() => setSelectedScrap(null)}
              className="absolute top-4 right-4 p-1.5 rounded-full bg-zinc-300/60 hover:bg-zinc-300 text-zinc-800"
            >
              <X className="w-4 h-4" />
            </button>

            <div className="space-y-1">
              <span className="text-xs font-typewriter font-bold text-red-800 uppercase tracking-widest">
                {selectedScrap.vintageLabel}
              </span>
              <h4 className="text-lg font-bold font-serif-title text-zinc-900">
                {selectedScrap.source}
              </h4>
            </div>

            <div className="p-5 rounded-lg bg-[#ede0d1] border border-[#dac7b3] space-y-3">
              <p className="text-xl font-gurmukhi font-bold text-zinc-950 leading-loose whitespace-pre-line">
                {selectedScrap.gurmukhi}
              </p>
              <p className="text-sm font-reading text-zinc-800 italic pt-2 border-t border-zinc-400/50">
                "{selectedScrap.english}"
              </p>
            </div>

            <div className="text-xs font-reading text-zinc-700 leading-relaxed bg-amber-100/40 p-3 rounded border border-amber-200">
              <strong>Historical Context: </strong>
              {selectedScrap.story}
            </div>

            <div className="flex items-center justify-between pt-2">
              <button
                onClick={() => setSelectedScrap(null)}
                className="text-xs font-typewriter text-zinc-600 hover:text-zinc-900"
              >
                ← Fold Back
              </button>
              <button
                onClick={() => {
                  const poemId = selectedScrap.poemId;
                  setSelectedScrap(null);
                  onOpenPoemModal(poemId);
                }}
                className="px-4 py-2 rounded-lg bg-red-900 hover:bg-red-800 text-amber-100 font-bold text-xs flex items-center gap-1.5 shadow"
              >
                <Feather className="w-3.5 h-3.5" />
                Read Full Multi-Script Poem →
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
