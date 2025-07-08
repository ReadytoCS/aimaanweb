"use client";
import React, { useState } from 'react';
import Link from 'next/link';
import Image from "next/image";

// Navbar component for Aimaan Shergill's website
// Features: Sticky, mobile hamburger menu, easy-to-edit links
const NAV_LINKS = [
  { name: 'Home', href: '/' },
  { name: 'About', href: '/about' },
  { name: 'Blog', href: '/blog' }, // "Grassroot Ideas"
  { name: 'Projects', href: '/projects' },
  { name: 'Contact', href: '/contact' },
];

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-50 w-full bg-white/80 backdrop-blur border-b border-gray-200 transition-colors">
      <div className="max-w-5xl mx-auto flex items-center justify-between px-4 py-3">
        {/* Logo/Name */}
        <Link href="/" className="flex items-center gap-2 font-bold text-xl tracking-tight text-accent">
          <Image src="/aimaan.png" alt="Aimaan Shergill Logo" width={32} height={32} className="rounded-full" />
          Aimaan Shergill
        </Link>
        {/* Desktop Nav Links */}
        <div className="hidden md:flex gap-6 items-center">
          {NAV_LINKS.map((link) => (
            <Link
              key={link.name}
              href={link.href}
              className="text-base font-medium text-text hover:text-accent transition-colors"
            >
              {link.name}
            </Link>
          ))}
        </div>
        {/* Mobile Hamburger */}
        <div className="md:hidden flex items-center">
          <button
            aria-label="Open menu"
            onClick={() => setMenuOpen((v) => !v)}
            className="p-2 rounded hover:bg-accent/10 transition-colors"
          >
            {/* Hamburger icon */}
            <svg width="24" height="24" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
              <path strokeLinecap="round" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>
      {/* Mobile Menu */}
      {menuOpen && (
        <div className="md:hidden bg-white border-t border-gray-200 px-4 pb-4">
          <div className="flex flex-col gap-3 mt-2">
            {NAV_LINKS.map((link) => (
              <Link
                key={link.name}
                href={link.href}
                className="text-base font-medium text-text hover:text-accent transition-colors"
                onClick={() => setMenuOpen(false)}
              >
                {link.name}
              </Link>
            ))}
          </div>
        </div>
      )}
    </nav>
  );
} 