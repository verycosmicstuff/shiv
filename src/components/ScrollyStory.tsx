import React, { useState, useEffect } from 'react';
import { Flame, BookOpen, ArrowDown, Compass } from 'lucide-react';
import { CigarettePacketScraps } from './CigarettePacketScraps';
import { ScrollyDialectic } from './ScrollyDialectic';
import { LoonaDeepDive } from './LoonaDeepDive';
import { TimelineView } from './TimelineView';
import { ArchiveInvestigationView } from './ArchiveInvestigationView';
import { AudioChamber } from './AudioChamber';
import { PoetryExplorer } from './PoetryExplorer';
import { Poem } from '../types';
import { CitationBadge } from './CitationBadge';

interface ScrollyStoryProps {
  onOpenPoemModal: (poem: Poem | string) => void;
}

export const ScrollyStory: React.FC<ScrollyStoryProps> = ({ onOpenPoemModal }) => {
  const [activeSection, setActiveSection] = useState<string>('prologue');
  const [scrollProgress, setScrollProgress] = useState<number>(0);

  useEffect(() => {
    const handleScroll = () => {
      const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (totalHeight > 0) {
        const progress = (window.scrollY / totalHeight) * 100;
        setScrollProgress(progress);
      }

      // Check current section in viewport
      const sections = ['prologue', 'birha', 'leftist', 'loona', 'timeline', 'archives', 'diwan'];
      for (const s of sections) {
        const el = document.getElementById(s);
        if (el) {
          const rect = el.getBoundingClientRect();
          if (rect.top <= 200 && rect.bottom >= 200) {
            setActiveSection(s);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (id: string) => {
    if (id === 'prologue') {
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="relative space-y-24 sm:space-y-36">
      {/* Sticky Atmospheric Progress River */}
      <nav 
        aria-label="Story Acts Navigation"
        className="sticky top-20 z-30 -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-8 py-2.5 bg-shiv-950/80 backdrop-blur-md border-y border-shiv-border/60 flex items-center justify-between"
      >
        <div className="flex items-center gap-1.5 text-xs text-amber-500/90 font-typewriter uppercase tracking-wider">
          <Compass className="w-3.5 h-3.5 animate-spin-slow" />
          <span className="hidden sm:inline">Chapter River:</span>
        </div>

        <div className="flex items-center gap-1 sm:gap-2 overflow-x-auto scrollbar-none text-xs">
          {[
            { id: 'prologue', label: 'Prologue' },
            { id: 'birha', label: 'Act I: Birha Void' },
            { id: 'leftist', label: 'Act II: The Red Wound' },
            { id: 'loona', label: 'Act III: Loona Heresy' },
            { id: 'timeline', label: 'Act IV: The 36 Years' },
            { id: 'archives', label: 'Act V: Wiped Tapes' },
            { id: 'diwan', label: 'Complete Diwan' },
          ].map((item) => (
            <button
              key={item.id}
              onClick={() => scrollToSection(item.id)}
              className={`px-2.5 py-1 rounded-full whitespace-nowrap text-[11px] font-medium transition-all ${
                activeSection === item.id
                  ? 'bg-amber-500 text-black font-bold shadow-md'
                  : 'text-zinc-400 hover:text-zinc-200 hover:bg-zinc-800/60'
              }`}
            >
              {item.label}
            </button>
          ))}
        </div>

        {/* Global Scroll Progress Bar */}
        <div className="hidden md:block w-24 h-1.5 bg-zinc-800 rounded-full overflow-hidden ml-3">
          <div 
            className="h-full bg-amber-500 transition-all duration-150"
            style={{ width: `${scrollProgress}%` }}
          />
        </div>
      </nav>

      {/* ========================================================================= */}
      {/* PROLOGUE: HERO & THE SHADOW OF YOUTH                                      */}
      {/* ========================================================================= */}
      <section id="prologue" className="min-h-[85vh] flex flex-col justify-center relative py-12">
        <div className="max-w-4xl mx-auto text-center space-y-8">
          {/* Vintage Archival Stamp */}
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border-2 border-dashed border-red-800/80 bg-red-950/20 text-red-400 text-xs font-typewriter uppercase tracking-widest animate-pulse">
            <Flame className="w-3.5 h-3.5" />
            Declassified Literary Dossier • 1936–1973
          </div>

          {/* Monumental Gurmukhi Hero Title */}
          <div className="space-y-4">
            <h1 className="text-5xl sm:text-7xl lg:text-8xl font-bold font-gurmukhi text-amber-100 tracking-tight leading-none drop-shadow-2xl">
              ਸਿ਼ਵ ਕੁਮਾਰ ਬਟਾਲਵੀ
            </h1>
            <div className="text-xl sm:text-2xl lg:text-3xl font-serif-title uppercase tracking-widest text-amber-500 font-bold">
              The Sultan of Birha • Sovereign of Longing
            </div>
            <p className="font-typewriter text-xs sm:text-sm text-zinc-400 max-w-xl mx-auto italic">
              "We shall die in the springtime of our years... like unplucked blossoms withering before their time."
            </p>
          </div>

          {/* Editorial Hook Narrative */}
          <div className="max-w-2xl mx-auto p-6 sm:p-8 rounded-2xl bg-zinc-950/80 border border-amber-900/40 shadow-2xl parchment-sheet space-y-4 text-left">
            <div className="flex items-center gap-2 text-xs font-mono uppercase text-amber-400 font-bold border-b border-zinc-800 pb-2">
              <BookOpen className="w-3.5 h-3.5" />
              Beyond the Bollywood Balcony
            </div>
            <p className="text-sm sm:text-base font-reading text-zinc-300 leading-relaxed">
              Mainstream tributes have reduced him to acoustic pop covers like <em>"Ikk Kudi"</em>. But the real Shiv Kumar was dangerous. He was the young iconoclast who dismantled 1,000 years of Punjabi moralism, waged war against the Marxist literary establishment, wrote verses on cigarette foils in smoky taverns, and predicted his own death at 36.
            </p>
            <div className="flex items-center justify-between pt-2 text-xs font-typewriter text-zinc-500">
              <span>Bara Pind Lohtian → Batala → London → Kir Mangyal</span>
              <span className="text-amber-500">Scroll to enter ↓</span>
            </div>
          </div>

          {/* Interactive Cigarette Packet Ephemera */}
          <CigarettePacketScraps onOpenPoemModal={(id) => onOpenPoemModal(id)} />

          {/* Prompt to scroll */}
          <button
            onClick={() => scrollToSection('birha')}
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-zinc-900/80 hover:bg-amber-500 hover:text-black text-amber-400 border border-zinc-800 text-xs font-semibold transition-all shadow-lg animate-bounce mt-8"
          >
            <span>Descend into the Agony of Birha</span>
            <ArrowDown className="w-3.5 h-3.5" />
          </button>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* ACT I: THE METAPHYSICS OF BIRHA                                           */}
      {/* ========================================================================= */}
      <section id="birha" className="scroll-mt-32 space-y-12">
        <div className="border-l-4 border-amber-500 pl-4 sm:pl-6 space-y-2">
          <span className="text-xs font-typewriter uppercase tracking-widest text-amber-500 font-bold">
            ACT I • THE VOID
          </span>
          <h2 className="text-3xl sm:text-5xl font-serif-title font-bold text-zinc-100 flex flex-wrap items-center gap-2">
            <span>The Metaphysics of Birha : Death as the Bride</span>
            <CitationBadge id="GARGI-1979-SURME" />
            <CitationBadge id="AMRITA-1974-NAGMANI" />
          </h2>
          <p className="text-sm sm:text-base text-zinc-400 font-reading max-w-2xl">
            Why reducing Shiv to "romantic heartbreak" is an insult to his art. Separation as the cosmic condition of 20th-century existence.
          </p>
        </div>

        {/* Scrollytelling Visual Poem Feature: Main Ek Shikra Yaar Banaya */}
        <div className="p-6 sm:p-12 rounded-2xl bg-zinc-950 border-2 border-amber-800/40 shadow-2xl parchment-sheet space-y-8">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-zinc-800 pb-4">
            <div>
              <span className="text-xs font-mono uppercase text-red-400 tracking-wider font-bold">
                CANONICAL MASTERWORK • 1964
              </span>
              <h3 className="text-2xl sm:text-3xl font-gurmukhi font-bold text-amber-300 mt-1">
                ਮੈਂ ਇੱਕ ਸ਼ਿਕਰਾ ਯਾਰ ਬਣਾਇਆ (The Falcon Lover)
              </h3>
            </div>
            <button
              onClick={() => onOpenPoemModal('shikra-yaar')}
              className="px-4 py-2 rounded-lg bg-amber-500 hover:bg-amber-400 text-black font-bold text-xs self-start sm:self-auto transition-colors"
            >
              Open Full Multi-Script Reader →
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Left: Original Poem Excerpt */}
            <div className="p-6 rounded-xl bg-zinc-900/80 border border-zinc-800 space-y-4">
              <div className="font-gurmukhi text-lg text-amber-100 leading-relaxed">
                ਮੈਂ ਇੱਕ ਸ਼ਿਕਰਾ ਯਾਰ ਬਣਾਇਆ<br />
                ਉਹਦੇ ਸਿਰ ਤੇ ਕਲਗੀ<br />
                ਤੇ ਉਹਦੇ ਪੈਰੀਂ ਝਾਂਜਰ<br />
                ਉਹ ਚੋਗ ਚੁਗਿੰਦਾ ਆਇਆ...
              </div>
              <div className="text-xs font-reading text-zinc-400 italic">
                "I took a falcon as my lover...<br />
                A royal crest upon his crown, anklets around his talons.<br />
                I offered sweet bread, but he would not touch it,<br />
                So I fed him the raw, living flesh of my own heart!"
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* ACT II: THE RED FLAG VS. THE RED WOUND (THE LEFTIST FEUD)                 */}
      {/* ========================================================================= */}
      <section id="leftist" className="scroll-mt-32 space-y-12">
        <div className="border-l-4 border-red-600 pl-4 sm:pl-6 space-y-2">
          <span className="text-xs font-typewriter uppercase tracking-widest text-red-500 font-bold">
            ACT II • THE LITERARY FEUD
          </span>
          <h2 className="text-3xl sm:text-5xl font-serif-title font-bold text-zinc-100 flex flex-wrap items-center gap-2">
            <span>The Red Flag & The Red Wound</span>
            <CitationBadge id="SEKHON-1972-PUNJABI-KAVI" />
            <CitationBadge id="PAASH-1973-SIARH" />
            <CitationBadge id="KISHAN-SINGH-1971" />
          </h2>
          <p className="text-sm sm:text-base text-zinc-400 font-reading max-w-2xl">
            The Progressive Writers' Movement condemned his sorrow as "bourgeois escapism". How Shiv defied party manifestos to defend the sovereignty of the soul.
          </p>
        </div>

        {/* Historical Narrative Dossier */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="p-6 rounded-xl bg-zinc-950 border border-zinc-800 space-y-3">
            <div className="text-xs font-typewriter font-bold text-red-400 uppercase">
              1. The Hegemony of Sekhon
            </div>
            <p className="text-xs sm:text-sm font-reading text-zinc-300 leading-relaxed">
              In the 1960s, Marxist critic <strong>Sant Singh Sekhon</strong> decreed that literature must serve only Socialist Realism. Shiv was condescendingly labeled the <em>"Keats of Punjabi poetry"</em>—great at melodic rhymes, but lacking ideological spine.
            </p>
          </div>

          <div className="p-6 rounded-xl bg-zinc-950 border border-zinc-800 space-y-3">
            <div className="text-xs font-typewriter font-bold text-red-400 uppercase">
              2. "Poison for the Youth"
            </div>
            <p className="text-xs sm:text-sm font-reading text-zinc-300 leading-relaxed">
              Critics like <strong>Kishan Singh</strong> accused Shiv of spreading a cult of suicide. They argued that while farmers should have been picking up the sickle of revolt, Shiv was teaching them to weep into their glasses in imitation of his bohemian persona.
            </p>
          </div>

          <div className="p-6 rounded-xl bg-zinc-950 border border-zinc-800 space-y-3">
            <div className="text-xs font-typewriter font-bold text-amber-400 uppercase">
              3. The Defiant Retort
            </div>
            <p className="text-xs sm:text-sm font-reading text-zinc-300 leading-relaxed">
              At the Chandigarh Indian Coffee House, Shiv retorted: <em>"They command me to write about the redness of the flag; I can only write about the redness of the wound."</em>
            </p>
          </div>
        </div>

        {/* The Side-by-Side Shiv vs Paash Dialectic */}
        <ScrollyDialectic />
      </section>

      {/* ========================================================================= */}
      {/* ACT III: THE HERESY OF LOONA (1965)                                       */}
      {/* ========================================================================= */}
      <section id="loona" className="scroll-mt-32 space-y-12">
        <div className="border-l-4 border-amber-400 pl-4 sm:pl-6 space-y-2">
          <span className="text-xs font-typewriter uppercase tracking-widest text-amber-400 font-bold">
            ACT III • FEMINIST HERESY
          </span>
          <h2 className="text-3xl sm:text-5xl font-serif-title font-bold text-zinc-100 flex flex-wrap items-center gap-2">
            <span>Loona : The Decapitation of Ancient Morality</span>
            <CitationBadge id="SAHITYA-1967-LOONA" />
            <CitationBadge id="QADIR-YAR-1840" />
          </h2>
          <p className="text-sm sm:text-base text-zinc-400 font-reading max-w-2xl">
            Inverting 1,000 years of the Puran Bhagat legend. Winning the Sahitya Akademi Award at 31 and enraging both conservatives and party commissars.
          </p>
        </div>

        <LoonaDeepDive />
      </section>

      {/* ========================================================================= */}
      {/* ACT IV: THE 36-YEAR TIMELINE                                              */}
      {/* ========================================================================= */}
      <section id="timeline" className="scroll-mt-32 space-y-12">
        <div className="border-l-4 border-zinc-500 pl-4 sm:pl-6 space-y-2">
          <span className="text-xs font-typewriter uppercase tracking-widest text-zinc-400 font-bold">
            ACT IV • THE CHRONICLES
          </span>
          <h2 className="text-3xl sm:text-5xl font-serif-title font-bold text-zinc-100">
            The 36 Fated Years (1936–1973)
          </h2>
          <p className="text-sm sm:text-base text-zinc-400 font-reading max-w-2xl">
            From the Partition displacement across the Ravi river to the cold exile in London and the final dawn in Kir Mangyal.
          </p>
        </div>

        <TimelineView onSelectPoemId={(id) => onOpenPoemModal(id)} />
      </section>

      {/* ========================================================================= */}
      {/* ACT V: THE LOST ARCHIVES & WIPED TAPES                                    */}
      {/* ========================================================================= */}
      <section id="archives" className="scroll-mt-32 space-y-12">
        <div className="border-l-4 border-red-700 pl-4 sm:pl-6 space-y-2">
          <span className="text-xs font-typewriter uppercase tracking-widest text-red-500 font-bold">
            ACT V • FORENSIC INVESTIGATION
          </span>
          <h2 className="text-3xl sm:text-5xl font-serif-title font-bold text-zinc-100 flex flex-wrap items-center gap-2">
            <span>The Burned Diaries & The Wiped Tapes</span>
            <CitationBadge id="AIR-ARCHIVES-JALANDHAR" />
            <CitationBadge id="BBC-1972-KAUL" />
            <CitationBadge id="BATALVI-ARUNA-1988" />
          </h2>
          <p className="text-sm sm:text-base text-zinc-400 font-reading max-w-2xl">
            Separating the folklore of burned manuscripts from the tragic institutional reality of overwritten magnetic tapes at Akashvani and Doordarshan.
          </p>
        </div>

        <ArchiveInvestigationView />
        <AudioChamber onSelectPoemId={(id) => onOpenPoemModal(id)} />
      </section>

      {/* ========================================================================= */}
      {/* ACT VI: THE LIVING DIWAN (COMPLETE POETRY ARCHIVE)                        */}
      {/* ========================================================================= */}
      <section id="diwan" className="scroll-mt-32 space-y-12 pt-8 border-t-2 border-zinc-800">
        <div className="border-l-4 border-amber-500 pl-4 sm:pl-6 space-y-2">
          <span className="text-xs font-typewriter uppercase tracking-widest text-amber-500 font-bold">
            ACT VI • THE IMMORTAL CANON
          </span>
          <h2 className="text-3xl sm:text-5xl font-serif-title font-bold text-zinc-100">
            ਸਮੁੱਚਾ ਦੀਵਾਨ : Complete Poetry Explorer
          </h2>
          <p className="text-sm sm:text-base text-zinc-400 font-reading max-w-2xl">
            Search, filter, and read his complete works across all 8 canonical anthologies in Gurmukhi, Shahmukhi, Roman, and English with full cultural glossaries.
          </p>
        </div>

        <PoetryExplorer onSelectPoem={(p) => onOpenPoemModal(p)} />
      </section>
    </div>
  );
};
