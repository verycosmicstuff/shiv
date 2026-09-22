/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        shiv: {
          950: '#0a0a0d',
          900: '#111116',
          850: '#17171e',
          800: '#1f1f28',
          750: '#282834',
          700: '#343444',
          600: '#4c4c62',
          border: '#2e2e3d',
          accent: '#d97706',
          gold: '#f59e0b',
          crimson: '#dc2626',
          blood: '#991b1b',
          parchment: '#f5efe6',
          cream: '#ede2d3',
          faded: '#9ca3af',
        }
      },
      fontFamily: {
        serif: ['"Cinzel"', '"Playfair Display"', 'Georgia', 'serif'],
        decorative: ['"Cinzel Decorative"', 'serif'],
        reading: ['"Lora"', '"Merriweather"', 'Georgia', 'serif'],
        typewriter: ['"Courier Prime"', '"Special Elite"', 'monospace'],
        sans: ['"Inter"', 'system-ui', 'sans-serif'],
        gurmukhi: ['"Noto Sans Gurmukhi"', '"Mukta Mahee"', '"Raavi"', 'sans-serif'],
        shahmukhi: ['"Noto Nastaliq Urdu"', '"Nafees Web Naskh"', 'serif']
      }
    },
  },
  plugins: [],
}
