import React from 'react';
import { Radio, Music, ExternalLink, Quote } from 'lucide-react';

interface AudioChamberProps {
  onSelectPoemId: (poemId: string) => void;
}

export const AudioChamber: React.FC<AudioChamberProps> = ({ onSelectPoemId }) => {
  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Hero Header */}
      <div className="rounded-2xl bg-gradient-to-r from-amber-950/40 via-shiv-900 to-zinc-900 p-6 sm:p-10 border border-amber-900/40 amber-border-glow">
        <div className="max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/25 text-xs font-semibold uppercase tracking-wider">
            <Radio className="w-3.5 h-3.5" />
            The Living Voice • ਤਰੰਨੁਮ
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold font-serif-title text-zinc-100">
            The Tarannum Chamber & The 1972 BBC Relic
          </h1>
          <p className="text-sm sm:text-base text-zinc-300 font-reading leading-relaxed">
            Shiv did not merely recite poetry; he possessed a hypnotic, melismatic singing chant known as <em>tarannum</em>. With no instruments, his high-pitched, piercing cadence could bring tens of thousands of listeners to tears in all-night Punjabi mushairas.
          </p>
        </div>
      </div>

      {/* The BBC 1972 Archive Spotlight & Video Player */}
      <div className="p-6 sm:p-10 rounded-2xl bg-shiv-900 border border-shiv-border shadow-2xl space-y-8">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-zinc-800 pb-6">
          <div>
            <span className="text-xs uppercase tracking-widest text-amber-500 font-bold font-serif-title">
              Sole Surviving Visual Broadcast • London, May 1972
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold text-zinc-100 font-serif-title mt-1">
              Interview with Mahendra Kaul (BBC Television)
            </h2>
          </div>

          <a
            href="https://www.youtube.com/watch?v=z4ro9SygyvE"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-zinc-800 hover:bg-zinc-700 text-zinc-200 font-medium text-xs transition-all border border-zinc-700 self-start md:self-auto"
          >
            <span>Open in YouTube</span>
            <ExternalLink className="w-3.5 h-3.5 ml-0.5" />
          </a>
        </div>

        {/* Embedded YouTube Player of the Actual Interview */}
        <div className="rounded-2xl overflow-hidden border-2 border-amber-900/60 shadow-2xl bg-black aspect-video max-w-3xl mx-auto">
          <iframe
            width="100%"
            height="100%"
            src="https://www.youtube-nocookie.com/embed/z4ro9SygyvE"
            title="Shiv Kumar Batalvi BBC Interview 1972"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
            className="w-full h-full"
          />
        </div>

        {/* Narrative & Exegesis */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="space-y-4 text-sm font-reading text-zinc-300 leading-relaxed">
            <p>
              In May 1972, exactly one year before his death, Shiv traveled to London. It was his first journey outside the Indian subcontinent. The Punjabi diaspora flocked to see him, treating him with rockstar reverence, yet Shiv was overwhelmed by exhaustion, chronic liver pain, and acute cultural displacement.
            </p>
            <p>
              Broadcaster <strong>Mahendra Kaul</strong> invited Shiv to the BBC studios. Sitting before the television camera with a silk scarf around his neck, looking frail yet luminous, Shiv spoke with startling honesty about his art, his critics, and his relationship with death.
            </p>
            <p>
              When Mahendra Kaul asked him to recite, Shiv broke into <em>"Kee Puchhde O Haal Fakiran Da"</em>. Stripped of studio reverb or instruments, his naked, tremulous vocal rendition captivated audiences and remains the single most iconic piece of Punjabi broadcast footage in existence.
            </p>
          </div>

          {/* Key Spoken Dialogue Quote Box */}
          <div className="p-6 rounded-xl bg-zinc-950/80 border border-zinc-800 space-y-4">
            <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-amber-400">
              <Quote className="w-4 h-4" />
              Shiv’s Spoken Words to Mahendra Kaul
            </div>
            
            <blockquote className="text-sm font-reading text-amber-100 italic space-y-2 border-l-2 border-amber-500 pl-4">
              <p>
                "People say to me: 'Shiv, you only sing of pain, tears, and death.' But what is a poet if he does not honor the wound? A poet is not an agent for a political manifesto. When a human being bleeds, the sorrow does not ask for permission from a political committee."
              </p>
            </blockquote>

            <div className="pt-2">
              <button
                onClick={() => onSelectPoemId('kee-puchhde-o-haal')}
                className="w-full py-2.5 rounded-lg bg-zinc-800 hover:bg-amber-500 hover:text-black text-amber-300 text-xs font-semibold transition-all border border-zinc-700 text-center"
              >
                Read "Kee Puchhde O Haal Fakiran Da" in Multi-Script →
              </button>
            </div>
          </div>
        </div>

        {/* Why Tarannum Mattered */}
        <div className="border-t border-zinc-800 pt-6 space-y-4">
          <h3 className="text-sm font-serif-title uppercase tracking-widest text-zinc-400 flex items-center gap-2">
            <Music className="w-4 h-4 text-amber-500" />
            The Anatomy of Shiv's Tarannum
          </h3>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
            <div className="p-4 rounded-xl bg-zinc-950 border border-zinc-800 space-y-1.5">
              <span className="font-bold text-amber-400 text-sm">Folk-Sufi Cadence</span>
              <p className="text-zinc-400 leading-relaxed">
                Shiv inherited the unwritten rhythmic breath of Waris Shah and Bulleh Shah, allowing the vowel sounds to linger and hover in the air.
              </p>
            </div>

            <div className="p-4 rounded-xl bg-zinc-950 border border-zinc-800 space-y-1.5">
              <span className="font-bold text-amber-400 text-sm">The Melismatic Glide</span>
              <p className="text-zinc-400 leading-relaxed">
                Rather than singing to a strict beat, he used rubato—speeding up through narrative lines and slowing to a sustained cry on key nouns like <em>shikra</em> or <em>birhon</em>.
              </p>
            </div>

            <div className="p-4 rounded-xl bg-zinc-950 border border-zinc-800 space-y-1.5">
              <span className="font-bold text-amber-400 text-sm">Collective Catharsis</span>
              <p className="text-zinc-400 leading-relaxed">
                In an era before mass electronic media, his voice turned open-air rural mushairas into communal emotional cleansings where strangers held hands and wept together.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
