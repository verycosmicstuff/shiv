import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, Disc, Minimize2, ExternalLink, Film, Volume2, VolumeX } from 'lucide-react';

interface AnalogTapeDeckProps {
  onOpenPoemModal?: (poemId: string) => void;
}

export const AnalogTapeDeck: React.FC<AnalogTapeDeckProps> = ({ onOpenPoemModal }) => {
  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const [isMinimized, setIsMinimized] = useState<boolean>(false);
  const [showVideo, setShowVideo] = useState<boolean>(false);
  const [currentLineIndex, setCurrentLineIndex] = useState<number>(0);
  const [isMuted, setIsMuted] = useState<boolean>(false);

  const audioCtxRef = useRef<AudioContext | null>(null);
  const droneOscRef = useRef<OscillatorNode | null>(null);
  const gainNodeRef = useRef<GainNode | null>(null);

  const lines = [
    { gurmukhi: 'ਕੀ ਪੁੱਛਦੇ ਓ ਹਾਲ ਫ਼ਕੀਰਾਂ ਦਾ...', english: 'Why ask after the state of us mendicants...' },
    { gurmukhi: 'ਸਾਡਾ ਅੰਗ ਅੰਗ ਦਾਗ਼਼ ਦੁਖੀਰਾਂ ਦਾ...', english: 'Every limb of ours is scarred with sorrow...' },
    { gurmukhi: 'ਸਾਡੇ ਰੋਣੇ ਵੀ ਕੋਈ ਨਹੀਂ ਸੁਣਦਾ...', english: 'None pauses to listen when we weep...' },
    { gurmukhi: 'ਅਸੀਂ ਹੱਸਦੇ ਤਾਂ ਜੱਗ ਖਿਝਦਾ!', english: 'And when we laugh, the world is enraged!' },
    { gurmukhi: 'ਮੌਤ ਖਲੋਤੀ ਸਿਰਹਾਣੇ ਸਾਡੇ...', english: 'Death stands vigil at the head of our bed...' }
  ];

  // Teleprompter line cycler
  useEffect(() => {
    let interval: any;
    if (isPlaying) {
      interval = setInterval(() => {
        setCurrentLineIndex((prev) => (prev + 1) % lines.length);
      }, 4000);
    }
    return () => clearInterval(interval);
  }, [isPlaying, lines.length]);

  // Web Audio Drone / Analog Tape Ambient Generator
  const startTapeSound = () => {
    try {
      if (!audioCtxRef.current) {
        const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
        audioCtxRef.current = new AudioContextClass();
      }
      const ctx = audioCtxRef.current;
      if (ctx.state === 'suspended') {
        ctx.resume();
      }

      // Create warm analog harmonic drone
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(138.59, ctx.currentTime); // C#3 warm tanpura root

      gain.gain.setValueAtTime(0.001, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(isMuted ? 0.0001 : 0.04, ctx.currentTime + 1);

      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();

      droneOscRef.current = osc;
      gainNodeRef.current = gain;
    } catch (e) {
      console.warn('Web Audio playback error:', e);
    }
  };

  const stopTapeSound = () => {
    if (gainNodeRef.current && audioCtxRef.current) {
      try {
        gainNodeRef.current.gain.exponentialRampToValueAtTime(0.0001, audioCtxRef.current.currentTime + 0.5);
        setTimeout(() => {
          droneOscRef.current?.stop();
          droneOscRef.current?.disconnect();
          droneOscRef.current = null;
        }, 500);
      } catch (e) {
        // ignore
      }
    }
  };

  const togglePlayback = () => {
    if (isPlaying) {
      setIsPlaying(false);
      stopTapeSound();
    } else {
      setIsPlaying(true);
      startTapeSound();
    }
  };

  const toggleMute = () => {
    if (gainNodeRef.current && audioCtxRef.current) {
      const nextMuted = !isMuted;
      setIsMuted(nextMuted);
      gainNodeRef.current.gain.setValueAtTime(nextMuted ? 0.00001 : 0.04, audioCtxRef.current.currentTime);
    } else {
      setIsMuted(!isMuted);
    }
  };

  return (
    <aside 
      aria-label="Analog Audio Reel Player"
      className={`fixed bottom-4 right-4 z-40 transition-all duration-500 font-sans ${
        isMinimized ? 'w-auto' : 'w-84 sm:w-96'
      }`}
    >
      {isMinimized ? (
        <button
          onClick={() => setIsMinimized(false)}
          className="flex items-center gap-2 px-3.5 py-2 rounded-full bg-zinc-900/95 border border-amber-500/50 text-amber-400 text-xs shadow-2xl backdrop-blur-md hover:bg-zinc-800 transition-all"
        >
          <Disc className={`w-4 h-4 text-amber-400 ${isPlaying ? 'animate-spin-slow' : ''}`} />
          <span className="font-medium font-serif-title">1972 BBC Tape Deck</span>
          {isPlaying && (
            <span className="w-2 h-2 rounded-full bg-red-500 animate-ping" />
          )}
        </button>
      ) : (
        <div className="rounded-2xl bg-zinc-950/95 border-2 border-amber-700/50 p-4 shadow-2xl backdrop-blur-md space-y-3 parchment-sheet">
          {/* Deck Header */}
          <div className="flex items-center justify-between border-b border-zinc-800 pb-2">
            <div className="flex items-center gap-2">
              <span className={`w-2.5 h-2.5 rounded-full ${isPlaying ? 'bg-red-500 animate-pulse' : 'bg-zinc-600'}`} />
              <span className="text-[11px] font-mono uppercase tracking-widest text-amber-400 font-bold">
                AKASHVANI / BBC REEL DECK (1972)
              </span>
            </div>

            <div className="flex items-center gap-1.5">
              <button
                onClick={toggleMute}
                className="p-1 text-zinc-400 hover:text-amber-400 rounded transition-colors"
                title={isMuted ? 'Unmute Ambient Tone' : 'Mute Ambient Tone'}
              >
                {isMuted ? <VolumeX className="w-3.5 h-3.5" /> : <Volume2 className="w-3.5 h-3.5" />}
              </button>
              <button
                onClick={() => setIsMinimized(true)}
                className="p-1 text-zinc-400 hover:text-white rounded hover:bg-zinc-800"
                title="Minimize Deck"
              >
                <Minimize2 className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          {/* Dual Spools Visualizer */}
          <div className="relative py-2 px-4 rounded-xl bg-zinc-900/90 border border-zinc-800 flex items-center justify-around overflow-hidden">
            {/* Magnetic tape band */}
            <div className="absolute top-1/2 left-10 right-10 h-[1.5px] bg-zinc-700 -translate-y-1/2 pointer-events-none" />

            {/* Left Reel */}
            <div className="relative flex flex-col items-center">
              <div 
                className={`w-12 h-12 rounded-full border-2 border-zinc-600 bg-zinc-950 flex items-center justify-center shadow-inner ${
                  isPlaying ? 'animate-spin-slow' : 'animate-spin-paused'
                }`}
              >
                <div className="w-3 h-3 rounded-full bg-amber-600 border border-zinc-500" />
                <div className="absolute w-8 h-8 rounded-full border border-dashed border-zinc-700 pointer-events-none" />
              </div>
              <span className="text-[9px] font-mono text-zinc-500 mt-1">FEED REEL</span>
            </div>

            {/* Analog VU Meter */}
            <div className="w-20 px-2 py-1 rounded bg-black/90 border border-zinc-800 text-center space-y-0.5">
              <div className="text-[8px] font-mono text-zinc-500 tracking-tighter">VU LEVEL</div>
              <div className="flex items-center justify-center gap-0.5 h-4">
                {[40, 60, 85, 95, 30, 70, 90, 50].map((h, idx) => (
                  <div
                    key={idx}
                    className={`w-1 rounded-full transition-all duration-200 ${
                      isPlaying 
                        ? idx > 5 ? 'bg-red-500' : 'bg-amber-400'
                        : 'bg-zinc-800'
                    }`}
                    style={{
                      height: isPlaying ? `${Math.min(100, Math.max(20, (h * Math.random()) + 20))}%` : '20%'
                    }}
                  />
                ))}
              </div>
            </div>

            {/* Right Reel */}
            <div className="relative flex flex-col items-center">
              <div 
                className={`w-12 h-12 rounded-full border-2 border-zinc-600 bg-zinc-950 flex items-center justify-center shadow-inner ${
                  isPlaying ? 'animate-spin-slow' : 'animate-spin-paused'
                }`}
              >
                <div className="w-3 h-3 rounded-full bg-amber-600 border border-zinc-500" />
                <div className="absolute w-8 h-8 rounded-full border border-dashed border-zinc-700 pointer-events-none" />
              </div>
              <span className="text-[9px] font-mono text-zinc-500 mt-1">TAKEUP</span>
            </div>
          </div>

          {/* Subtitle / Teleprompter Display */}
          <div className="p-2.5 rounded-lg bg-black/80 border border-zinc-800/80 min-h-[58px] flex flex-col justify-center text-center">
            <div className="text-sm font-gurmukhi font-semibold text-amber-300 transition-all duration-300">
              {isPlaying ? lines[currentLineIndex].gurmukhi : 'ਸਿ਼ਵ ਦੀ ਆਵਾਜ਼ ਸੁਣੋ (BBC 1972)'}
            </div>
            <div className="text-[11px] font-reading text-zinc-400 italic">
              {isPlaying ? lines[currentLineIndex].english : 'Turn on playback to sync audio reels & recitation'}
            </div>
          </div>

          {/* Optional Embedded Video / Audio Player of Shiv's Actual BBC Interview */}
          {showVideo && (
            <div className="rounded-lg overflow-hidden border border-amber-600/40 shadow-inner bg-black">
              <iframe
                width="100%"
                height="180"
                src="https://www.youtube-nocookie.com/embed/z4ro9SygyvE?autoplay=1"
                title="Shiv Kumar Batalvi BBC Interview 1972"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
                className="w-full"
              />
            </div>
          )}

          {/* Controls Bar */}
          <div className="flex flex-wrap items-center justify-between gap-2 pt-1">
            <div className="flex items-center gap-2">
              <button
                onClick={togglePlayback}
                className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-black font-bold text-xs transition-colors shadow"
              >
                {isPlaying ? (
                  <>
                    <Pause className="w-3.5 h-3.5 fill-current" />
                    <span>Stop Spools</span>
                  </>
                ) : (
                  <>
                    <Play className="w-3.5 h-3.5 fill-current" />
                    <span>Run Tape</span>
                  </>
                )}
              </button>

              <button
                onClick={() => setShowVideo(!showVideo)}
                className={`flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                  showVideo 
                    ? 'bg-red-900/60 border-red-500 text-red-200' 
                    : 'bg-zinc-900 hover:bg-zinc-800 border-zinc-700 text-amber-300'
                }`}
              >
                <Film className="w-3 h-3" />
                <span>{showVideo ? 'Hide Video' : 'Real BBC Voice'}</span>
              </button>
            </div>

            {onOpenPoemModal && (
              <button
                onClick={() => onOpenPoemModal('kee-puchhde-o-haal')}
                className="text-[11px] text-amber-400/90 hover:text-amber-300 hover:underline font-medium"
              >
                Full Poem →
              </button>
            )}

            <a
              href="https://www.youtube.com/watch?v=z4ro9SygyvE"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zinc-500 hover:text-zinc-300 p-1"
              title="Open direct YouTube recording"
            >
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          </div>
        </div>
      )}
    </aside>
  );
};
