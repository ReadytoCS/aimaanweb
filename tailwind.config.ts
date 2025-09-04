import type { Config } from 'tailwindcss';

const config = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  safelist: [
    'animate-scroll',
  ],
  darkMode: 'class', // class-based; no 'dark' class is applied
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'SF Pro', 'ui-sans-serif', 'system-ui'],
      },
      colors: {
        background: '#fff',
        text: '#1e1e1e',
        accent: {
          DEFAULT: '#2b6777', // Muted Navy/Teal
        },
      },
      animation: {
        scroll: 'scroll 40s linear infinite',
        'scroll-mobile': 'scroll 20s linear infinite',
      },
      keyframes: {
        scroll: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
      },
    },
  },
  plugins: [],
};

export default config; 