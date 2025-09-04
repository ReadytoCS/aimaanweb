"use client";

import React from "react";

const logos = [
  { src: "/logos/rapidsos.jpg", alt: "RapidSOS" },
  { src: "/logos/deloitte.jpg", alt: "Deloitte" },
  { src: "/logos/pwc.jpg", alt: "PwC" },
  { src: "/logos/ontariohealth.jpg", alt: "Ontario Health" },
  { src: "/logos/markid.png", alt: "Markid" },
  { src: "/logos/ivey.jpg", alt: "Ivey" },
  { src: "/logos/rotman.jpg", alt: "Rotman/University of Toronto" },
  { src: "/logos/cocacola.jpg", alt: "Coca Cola" },
];

export default function LogoBanner() {
  return (
    <div className="relative overflow-hidden py-6 bg-white border border-slate-200 rounded-2xl">
      <div className="marquee flex items-center gap-10 px-10">
        {[...logos, ...logos].map((logo, idx) => (
          <img
            key={idx}
            src={logo.src}
            alt={logo.alt}
            width={180}
            height={72}
            className="h-14 w-auto object-contain block flex-shrink-0"
            loading="lazy"
            draggable={false as any}
          />
        ))}
      </div>
      <style jsx>{`
        .marquee {
          width: max-content;
          animation: scroll-left 40s linear infinite;
        }
        @keyframes scroll-left {
          0% { transform: translateX(0); }
          100% { transform: translateX(-50%); }
        }
        @media (prefers-reduced-motion: reduce) {
          .marquee { animation: none; }
        }
      `}</style>
    </div>
  );
} 