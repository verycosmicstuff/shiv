import React, { useState, useEffect } from 'react';
import { ActiveTab } from './components/Navbar';
import { ScrollyStory } from './components/ScrollyStory';
import { EssayView } from './components/EssayView';
import { TimelineView } from './components/TimelineView';
import { PoetryExplorer } from './components/PoetryExplorer';
import { LoonaDeepDive } from './components/LoonaDeepDive';
import { ArchiveInvestigationView } from './components/ArchiveInvestigationView';
import { AudioChamber } from './components/AudioChamber';
import { PoemModal } from './components/PoemModal';
import { BibliographyModal } from './components/BibliographyModal';
import { AmbientEffects } from './components/AmbientEffects';
import { Poem } from './types';
import { poemsDatabase } from './data/poems';
import { BookOpen } from 'lucide-react';

export const App: React.FC = () => {
  // 'flow' is the cinematic continuous scrollytelling mode; or user can focus on specific tab
  const [activeTab, setActiveTab] = useState<ActiveTab | 'flow'>('flow');
  const [selectedPoem, setSelectedPoem] = useState<Poem | null>(null);
  const [activeSection, setActiveSection] = useState<string>('prologue');
  const [isBibliographyOpen, setIsBibliographyOpen] = useState<boolean>(false);

  // Track active section for dynamic navigation feedback
  useEffect(() => {
    const handleScroll = () => {
      const sectionIds = ['diwan', 'archives', 'timeline', 'loona', 'leftist', 'birha', 'prologue'];
      for (const id of sectionIds) {
        const el = document.getElementById(id);
        if (el) {
          const rect = el.getBoundingClientRect();
          if (rect.top <= 260) {
            setActiveSection(id);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
    return () => window.removeEventListener('scroll', handleScroll);
  }, [activeTab]);

  const handleSelectPoem = (poemOrId: Poem | string) => {
    if (typeof poemOrId === 'string') {
      const found = poemsDatabase.find((p) => p.id === poemOrId);
      if (found) setSelectedPoem(found);
    } else {
      setSelectedPoem(poemOrId);
    }
  };

  // Direct chapter navigation
  const scrollToStorySection = (sectionId: string) => {
    if (activeTab !== 'flow') {
      setActiveTab('flow');
      setTimeout(() => {
        const el = document.getElementById(sectionId);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth' });
        } else {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      }, 80);
    } else {
      const el = document.getElementById(sectionId);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }
  };

  const navChapters = [
    { id: 'prologue', label: 'Prologue' },
    { id: 'birha', label: 'Birha' },
    { id: 'leftist', label: 'Red Wound' },
    { id: 'loona', label: 'Loona' },
    { id: 'timeline', label: '36 Years' },
    { id: 'archives', label: 'Wiped Tapes' },
    { id: 'diwan', label: 'Diwan', count: poemsDatabase.length },
  ];

  return (
    <div className="min-h-screen bg-shiv-950 text-shiv-parchment flex flex-col selection:bg-amber-600 selection:text-white relative">
      {/* 1960s Ambient Film Grain & Drifting Soot/Ember Particles */}
      <AmbientEffects />

      {/* Top Navigation Bar */}
      <header className="sticky top-0 z-40 bg-shiv-950/95 backdrop-blur-md border-b border-shiv-border/70">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-20">
            {/* Brand Title: Clicking smoothly scrolls to top prologue */}
            <div 
              onClick={() => scrollToStorySection('prologue')}
              className="cursor-pointer group flex flex-col"
              title="Return to Prologue"
            >
              <div className="flex items-center gap-2.5">
                <span className="text-xl sm:text-2xl font-gurmukhi font-bold text-amber-500 tracking-wide group-hover:text-amber-400 transition-colors">
                  ਸਿ਼ਵ ਕੁਮਾਰ ਬਟਾਲਵੀ
                </span>
                <span className="text-[11px] px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 font-medium">
                  1936 – 1973
                </span>
              </div>
              <span className="text-xs sm:text-sm tracking-wider uppercase text-zinc-400 font-serif-title font-medium group-hover:text-zinc-300 transition-colors">
                The Sultan of Birha • Sovereign of Longing
              </span>
            </div>

            {/* Experience Controls & Chapter Navigation */}
            <div className="flex items-center gap-2 sm:gap-3">
              {/* Archival Sources & Academic Citations Modal Button */}
              <button
                onClick={() => setIsBibliographyOpen(true)}
                title="View Archival Sources & Academic Citations"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-stone-900/90 text-amber-300 hover:text-amber-200 hover:bg-stone-800 border border-amber-500/30 transition-all cursor-pointer shadow-sm"
              >
                <BookOpen className="w-3.5 h-3.5 text-amber-400" />
                <span className="hidden sm:inline">Citations & Archives</span>
              </button>

              {/* Quick Chapter Navigation Items */}
              <div className="hidden lg:flex items-center gap-1 border-l border-zinc-800 pl-3">
                {navChapters.map((ch) => {
                  const isActive = activeTab === 'flow' && activeSection === ch.id;
                  return (
                    <button
                      key={ch.id}
                      onClick={() => scrollToStorySection(ch.id)}
                      className={`px-2.5 py-1 text-xs rounded-md transition-all flex items-center gap-1 ${
                        isActive
                          ? 'bg-zinc-800 text-amber-400 font-bold border border-amber-500/30'
                          : 'text-zinc-400 hover:text-zinc-200 hover:bg-zinc-900'
                      }`}
                    >
                      <span>{ch.label}</span>
                      {ch.count && (
                        <span className="text-[10px] px-1.5 py-0.2 rounded-full bg-amber-500/20 text-amber-400 font-mono font-bold">
                          {ch.count}
                        </span>
                      )}
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 relative z-20">
        {activeTab === 'flow' ? (
          <ScrollyStory onOpenPoemModal={handleSelectPoem} />
        ) : (
          <div className="space-y-6">
            <div className="flex items-center justify-between border-b border-zinc-800 pb-3">
              <button
                onClick={() => {
                  setActiveTab('flow');
                  window.scrollTo({ top: 0, behavior: 'smooth' });
                }}
                className="text-xs text-amber-400 hover:text-amber-300 flex items-center gap-1 font-typewriter cursor-pointer"
              >
                ← Back to Continuous Scrollytelling Flow
              </button>
              <span className="text-xs text-zinc-500 uppercase font-mono">FOCUSED VIEW</span>
            </div>

            {activeTab === 'essays' && <EssayView onSelectPoemId={handleSelectPoem} />}
            {activeTab === 'timeline' && <TimelineView onSelectPoemId={handleSelectPoem} />}
            {activeTab === 'poetry' && <PoetryExplorer onSelectPoem={(p) => setSelectedPoem(p)} />}
            {activeTab === 'loona' && <LoonaDeepDive />}
            {activeTab === 'archives' && <ArchiveInvestigationView />}
            {activeTab === 'audio' && <AudioChamber onSelectPoemId={handleSelectPoem} />}
          </div>
        )}
      </main>

      {/* Interactive Global Poem Modal */}
      <PoemModal
        poem={selectedPoem}
        onClose={() => setSelectedPoem(null)}
        onSelectPoem={handleSelectPoem}
      />

      {/* Archival Ledger & Master Bibliography Modal */}
      <BibliographyModal
        isOpen={isBibliographyOpen}
        onClose={() => setIsBibliographyOpen(false)}
      />

      {/* Vintage Literary Footer */}
      <footer className="bg-zinc-950 border-t border-zinc-800/80 mt-24 py-12 relative z-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6 text-xs text-zinc-400">
          <div className="space-y-2 text-center md:text-left">
            <div className="flex items-center justify-center md:justify-start gap-2">
              <span className="font-gurmukhi text-lg font-bold text-amber-500">
                ਸਿ਼ਵ ਕੁਮਾਰ ਬਟਾਲਵੀ
              </span>
              <span className="text-zinc-500">•</span>
              <span className="font-serif-title uppercase tracking-wider text-zinc-300">
                1936 – 1973
              </span>
            </div>
            <p className="max-w-md font-reading text-zinc-400">
              "Birha, birha aakhiye, birha toon sultan..." Dedicated to the unvarnished preservation of Punjab’s greatest modernist and romantic poet.
            </p>
          </div>

          <div className="flex flex-wrap items-center justify-center gap-4 text-xs font-typewriter">
            <button 
              onClick={() => scrollToStorySection('prologue')} 
              className="hover:text-amber-400 transition-colors cursor-pointer"
            >
              Cinematic Flow
            </button>
            <button 
              onClick={() => scrollToStorySection('diwan')} 
              className="hover:text-amber-400 transition-colors cursor-pointer"
            >
              Poetry Archive ({poemsDatabase.length})
            </button>
            <button 
              onClick={() => scrollToStorySection('loona')} 
              className="hover:text-amber-400 transition-colors cursor-pointer"
            >
              Loona Analysis
            </button>
            <button 
              onClick={() => scrollToStorySection('archives')} 
              className="hover:text-amber-400 transition-colors cursor-pointer"
            >
              Wiped Tapes Dossier
            </button>
            <button 
              onClick={() => setIsBibliographyOpen(true)} 
              className="text-amber-400 hover:text-amber-300 underline transition-colors cursor-pointer flex items-center gap-1"
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Archival Citations</span>
            </button>
          </div>

          <div className="text-zinc-500 text-center md:text-right font-typewriter">
            Preserved in text, memory, & voice.
          </div>
        </div>
      </footer>
    </div>
  );
};
