"use client";

import React from "react";

// Horizontally scrolling, infinite loop logo banner
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
  // Duplicate logos for seamless looping
  const allLogos = [...logos, ...logos];
  return (
    <div className="overflow-hidden py-6 bg-white dark:bg-gray-900">
      <div className="logo-scroll-track whitespace-nowrap flex space-x-10 items-center">
        {allLogos.map((logo, idx) => (
          <img
            key={idx}
            src={logo.src}
            alt={logo.alt}
            className={`grayscale hover:grayscale-0 transition duration-300 inline-block ${
              ["/logos/markid.png", "/logos/rotman.jpg"].includes(logo.src)
                ? "h-20"
                : ["/logos/rapidsos.jpg", "/logos/deloitte.jpg"].includes(logo.src)
                ? "h-14"
                : "h-10"
            }`}
            draggable={false}
          />
        ))}
      </div>
      <style jsx>{`
        .logo-scroll-track {
          animation: logo-scroll 40s linear infinite;
        }
        @keyframes logo-scroll {
          0% {
            transform: translateX(0);
          }
          100% {
            transform: translateX(-50%);
          }
        }
      `}</style>
    </div>
  );
} 