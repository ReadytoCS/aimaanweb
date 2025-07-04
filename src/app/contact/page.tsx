"use client";

import React from "react";

// Contact page for Aimaan Shergill
// Features: Contact form, social links, intro text
export default function ContactPage() {
  return (
    <main className="max-w-2xl mx-auto px-4 py-10 flex flex-col gap-10">
      {/* Title and Intro */}
      <section>
        <h1 className="text-3xl font-bold mb-2">Contact</h1>
        <p className="text-text mb-4">
          I’m open to collaborations, coffee chats, and new ideas. Reach out anytime!
        </p>
      </section>

      {/* Contact Form (Formspree or placeholder) */}
      <section className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <form
          action="https://formspree.io/f/xjkrzney"
          method="POST"
          className="flex flex-col gap-4"
        >
          <input
            type="text"
            name="name"
            placeholder="Name"
            required
            className="px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-accent"
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            required
            className="px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-accent"
          />
          <textarea
            name="message"
            placeholder="Message"
            required
            rows={4}
            className="px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-accent"
          />
          <div className="flex justify-end relative group">
            <button
              type="submit"
              className="flex items-center gap-2 px-4 py-2 rounded hover:bg-accent hover:text-white transition-colors group-hover:scale-95 focus:scale-95 active:scale-90"
              title="Send"
            >
              <img src="/logos/send.jpg" alt="Send" className="w-6 h-6 object-contain" />
              <span className="sr-only">Send</span>
            </button>
          </div>
        </form>
      </section>

      {/* Social Links */}
      <section className="flex gap-6 items-center justify-center">
        {/* LinkedIn */}
        <a
          href="https://www.linkedin.com/in/aimaanshergill/"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="LinkedIn"
          className="text-accent hover:text-accent/80 text-2xl"
        >
          {/* LinkedIn icon (simple SVG) */}
          <svg width="28" height="28" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.76 0-5 2.24-5 5v14c0 2.76 2.24 5 5 5h14c2.76 0 5-2.24 5-5v-14c0-2.76-2.24-5-5-5zm-11 19h-3v-10h3v10zm-1.5-11.28c-.97 0-1.75-.79-1.75-1.75s.78-1.75 1.75-1.75 1.75.79 1.75 1.75-.78 1.75-1.75 1.75zm15.5 11.28h-3v-5.6c0-1.34-.03-3.07-1.87-3.07-1.87 0-2.16 1.46-2.16 2.97v5.7h-3v-10h2.89v1.36h.04c.4-.75 1.38-1.54 2.84-1.54 3.04 0 3.6 2 3.6 4.59v5.59z"/></svg>
        </a>
        {/* Email */}
        <a
          href="mailto:aimaan.shergill@gmail.com"
          aria-label="Email"
          className="text-accent hover:text-accent/80 text-2xl"
        >
          {/* Email icon (simple SVG) */}
          <svg width="28" height="28" fill="currentColor" viewBox="0 0 24 24"><path d="M12 13.065l-11.985-7.065v14h23.97v-14l-11.985 7.065zm11.985-9.065h-23.97l11.985 7.065 11.985-7.065z"/></svg>
        </a>
      </section>
    </main>
  );
} 