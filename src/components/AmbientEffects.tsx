import React, { useEffect, useState } from 'react';

export const AmbientEffects: React.FC = () => {
  const [particles, setParticles] = useState<Array<{ id: number; left: number; duration: number; delay: number; size: number }>>([]);

  useEffect(() => {
    // Generate subtle drifting ember/soot particles
    const items = Array.from({ length: 24 }).map((_, i) => ({
      id: i,
      left: Math.random() * 100,
      duration: 6 + Math.random() * 8,
      delay: Math.random() * 6,
      size: 2 + Math.random() * 3
    }));
    setParticles(items);
  }, []);

  return (
    <>
      {/* 1960s Film Grain Texture Layer */}
      <div 
        className="fixed inset-0 pointer-events-none z-50 bg-film-grain opacity-80 mix-blend-overlay"
        aria-hidden="true"
      />

      {/* Floating Ash / Embers from the Bhatthi & Burned Manuscripts */}
      <div className="fixed inset-0 pointer-events-none z-10 overflow-hidden" aria-hidden="true">
        {particles.map((p) => (
          <div
            key={p.id}
            className="absolute rounded-full bg-amber-500/40 blur-[0.5px] animate-ember"
            style={{
              left: `${p.left}%`,
              bottom: '-20px',
              width: `${p.size}px`,
              height: `${p.size}px`,
              animationDuration: `${p.duration}s`,
              animationDelay: `${p.delay}s`,
            }}
          />
        ))}
      </div>
    </>
  );
};
