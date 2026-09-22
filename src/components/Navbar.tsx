import React from 'react';
import { BookOpen, Clock, Feather, ShieldAlert, Sparkles, Radio } from 'lucide-react';

export type ActiveTab = 'essays' | 'timeline' | 'poetry' | 'loona' | 'archives' | 'audio';

interface NavbarProps {
  activeTab: ActiveTab;
  setActiveTab: (tab: ActiveTab) => void;
}

export const Navbar: React.FC<NavbarProps> = ({ activeTab, setActiveTab }) => {
  const navItems = [
    { id: 'essays' as ActiveTab, label: 'Essays & Politics', icon: BookOpen, sublabel: 'Critics, Sekhon & Paash' },
    { id: 'timeline' as ActiveTab, label: 'The 36 Years', icon: Clock, sublabel: '1936–1973 Chronicles' },
    { id: 'poetry' as ActiveTab, label: 'Poetry Explorer', icon: Feather, sublabel: 'Multi-Script Diwan' },
    { id: 'loona' as ActiveTab, label: 'Loona Masterpiece', icon: Sparkles, sublabel: 'Feminist Heresy' },
    { id: 'archives' as ActiveTab, label: 'The Lost Archives', icon: ShieldAlert, sublabel: 'Burned Diaries & Tapes' },
    { id: 'audio' as ActiveTab, label: 'Tarannum Chamber', icon: Radio, sublabel: 'BBC 1972 Voice' }
  ];

  return (
    <header className="sticky top-0 z-40 bg-shiv-950/90 backdrop-blur-md border-b border-shiv-border/70 transition-all">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          {/* Brand Header */}
          <div 
            onClick={() => setActiveTab('essays')}
            className="cursor-pointer group flex flex-col"
          >
            <div className="flex items-center gap-2.5">
              <span className="text-xl sm:text-2xl font-gurmukhi font-bold text-amber-500 tracking-wide group-hover:text-amber-400 transition-colors">
                ਸਿ਼ਵ ਕੁਮਾਰ ਬਟਾਲਵੀ
              </span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 font-medium">
                1936 – 1973
              </span>
            </div>
            <span className="text-xs sm:text-sm tracking-wider uppercase text-zinc-400 font-serif-title font-medium">
              The Sultan of Birha • Sovereign of Longing
            </span>
          </div>

          {/* Desktop Nav */}
          <nav className="hidden md:flex items-center space-x-1 lg:space-x-2">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setActiveTab(item.id)}
                  className={`flex flex-col items-start px-3 py-2 rounded-lg text-left transition-all ${
                    isActive
                      ? 'bg-amber-500/15 text-amber-400 border border-amber-500/30'
                      : 'text-zinc-400 hover:text-zinc-200 hover:bg-zinc-900/60 border border-transparent'
                  }`}
                >
                  <div className="flex items-center gap-1.5 text-xs font-semibold tracking-wide">
                    <Icon className={`w-3.5 h-3.5 ${isActive ? 'text-amber-400' : 'text-zinc-500'}`} />
                    <span>{item.label}</span>
                  </div>
                  <span className="text-[10px] text-zinc-500 font-sans pl-5 hidden lg:inline">
                    {item.sublabel}
                  </span>
                </button>
              );
            })}
          </nav>
        </div>

        {/* Mobile Nav Horizontal Scroll */}
        <div className="md:hidden flex overflow-x-auto py-2 gap-2 border-t border-shiv-border/40 scrollbar-none">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs whitespace-nowrap transition-all ${
                  isActive
                    ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 font-medium'
                    : 'text-zinc-400 bg-zinc-900/70 border border-zinc-800'
                }`}
              >
                <Icon className="w-3.5 h-3.5" />
                <span>{item.label}</span>
              </button>
            );
          })}
        </div>
      </div>
    </header>
  );
};
