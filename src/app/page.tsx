"use client";

import Image from "next/image";
import Link from "next/link";
import LogoBanner from "../components/LogoBanner";
import React, { useState } from "react";
import PostModal from "../components/PostModal";

// Homepage for Aimaan Shergill
// Features: Hero, About, Featured Blog, Projects, Newsletter
export default function Home() {
  const [selectedPost, setSelectedPost] = useState<null | 'narayana' | 'taobao' | 'mpesa'>(null);
  return (
    <main className="max-w-5xl mx-auto px-4 py-10 flex flex-col gap-16">
      {/* Hero Section */}
      <section className="flex flex-col md:flex-row items-center gap-8 md:gap-12">
        {/* Photo placeholder - replace src with your photo */}
        <div className="flex-shrink-0">
          <div className="w-36 h-36 md:w-48 md:h-48 rounded-full overflow-hidden bg-gray-200 dark:bg-gray-700 flex items-center justify-center">
            {/* Replace with your image in /public/profile.jpg */}
            <Image src="/profile.jpg" alt="Aimaan Shergill" width={192} height={192} className="object-cover w-full h-full" />
          </div>
        </div>
        {/* Intro Text & CTAs */}
        <div className="flex-1 text-center md:text-left">
          <h1 className="text-3xl md:text-4xl font-bold mb-2">Hi, I&apos;m Aimaan Shergill.</h1>
          <p className="text-lg md:text-xl mb-6 text-text">
            I help businesses grow through strategy, data, and innovation.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
            {/* LinkedIn CTA */}
            <a
              href="https://www.linkedin.com/in/aimaanshergill/"
              target="_blank"
              rel="noopener noreferrer"
              className="px-6 py-2 rounded-full border border-accent text-accent font-semibold hover:bg-accent hover:text-white transition-colors shadow"
            >
              Find me on LinkedIn
            </a>
            {/* Explore Grassroot Ideas CTA */}
            <Link
              href="/blog"
              className="px-6 py-2 rounded-full border border-accent text-accent font-semibold hover:bg-accent hover:text-white transition-colors shadow"
            >
              Explore Grassroot Ideas
            </Link>
          </div>
        </div>
      </section>

      {/* About Summary */}
      <section className="bg-transparent rounded-xl p-6 shadow flex flex-col md:flex-row gap-6 items-center">
        <div className="flex-1">
          <h2 className="text-2xl font-bold mb-2">About Me</h2>
          <p className="text-text mb-0">
            I’m a Strategy & Corporate Development analyst at RapidSOS, working across GTM, M&A, and investor strategy. I’ve supported projects in public safety, healthcare, and infrastructure across North America, the Middle East, and South Asia.
          </p>
        </div>
        <Link href="/about" className="mt-4 md:mt-0 px-5 py-2 rounded-full border border-accent text-accent font-semibold hover:bg-accent hover:text-white transition-colors">
          Learn More
        </Link>
      </section>

      {/* Featured Blog Posts */}
      <section>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-bold">Featured Blog Posts</h2>
          <Link href="/blog" className="text-accent hover:underline font-medium">See all</Link>
        </div>
        <div className="grid md:grid-cols-3 gap-6">
          {/* Blog Post Card 1 */}
          <div className="bg-white text-slate-900 border border-slate-200 shadow-sm rounded-2xl p-4 flex flex-col gap-2 hover:shadow-md hover:-translate-y-0.5 transition">
            <Image
              src="/stock/narayana-health.jpg"
              alt="Narayana Health"
              width={400}
              height={200}
              className="object-cover w-full h-32 rounded mb-2"
            />
            <h3 className="font-semibold text-lg">Narayana Health</h3>
            <p className="text-sm text-text">World-class cardiac care at a fraction of the cost, making healthcare accessible for millions in India</p>
            <button className="text-accent hover:underline text-sm mt-auto" onClick={() => setSelectedPost('narayana')}>Read more</button>
          </div>
          {/* Blog Post Card 2 */}
          <div className="bg-white text-slate-900 border border-slate-200 shadow-sm rounded-2xl p-4 flex flex-col gap-2 hover:shadow-md hover:-translate-y-0.5 transition">
            <Image
              src="/stock/taobao-village.jpg"
              alt="Tao Bao Villages"
              width={400}
              height={200}
              className="object-cover w-full h-32 rounded mb-2"
            />
            <h3 className="font-semibold text-lg">Tao Bao Villages</h3>
            <p className="text-sm text-text">Rural e-commerce hubs in China empowering small villages to connect to the global digital economy</p>
            <button className="text-accent hover:underline text-sm mt-auto" onClick={() => setSelectedPost('taobao')}>Read more</button>
          </div>
          {/* Blog Post Card 3 */}
          <div className="bg-white text-slate-900 border border-slate-200 shadow-sm rounded-2xl p-4 flex flex-col gap-2 hover:shadow-md hover:-translate-y-0.5 transition">
            <Image
              src="/stock/mpesa.jpg"
              alt="M-Pesa"
              width={400}
              height={200}
              className="object-cover w-full h-32 rounded mb-2"
            />
            <h3 className="font-semibold text-lg">M-Pesa</h3>
            <p className="text-sm text-text">Mobile money transforming financial inclusion and everyday life for millions across Africa</p>
            <button className="text-accent hover:underline text-sm mt-auto" onClick={() => setSelectedPost('mpesa')}>Read more</button>
          </div>
        </div>
      </section>
      {/* Modal rendering */}
      {selectedPost && <PostModal postKey={selectedPost} onClose={() => setSelectedPost(null)} />}
      {/* Featured Projects */}
      <section>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-bold">Featured Projects</h2>
          <Link href="/projects" className="text-accent hover:underline font-medium">See all</Link>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 auto-rows-fr">
          {/* Project Card 1: Independent Consulting Projects */}
          <Link href="/projects#consulting" className="block bg-white text-slate-900 border border-slate-200 shadow-sm rounded-2xl p-5 hover:shadow-md transition">
            <div className="flex flex-col h-full space-y-2">
              <h3 className="font-semibold text-lg">Independent Consulting Projects</h3>
              <p className="text-sm text-gray-600">Strategy & fundraising for nonprofits</p>
              <div className="mt-auto pt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">MailChimp</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Google Workspace</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Tableau</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">SQL</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Python</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">OpenAI GPT-4 API</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Asana</span>
              </div>
            </div>
          </Link>
          {/* Project Card 2: GrainAI (Fintech for Gig Workers) */}
          <Link href="/projects#grainai" className="block bg-white text-slate-900 border border-slate-200 shadow-sm rounded-2xl p-5 hover:shadow-md transition">
            <div className="flex flex-col h-full space-y-2">
              <h3 className="font-semibold text-lg">GrainAI (Fintech for Gig Workers)</h3>
              <p className="text-sm text-gray-600">Strategy, product design, and user research for a personal finance platform tailored to gig workers.</p>
              <div className="mt-auto pt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">CursorAI</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Python</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Google Sheets API</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Lovable</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">OpenAI GPT-4 API</span>
              </div>
            </div>
          </Link>
          {/* Project Card 3: Custom Financial Sentiment GPT */}
          <Link href="/projects#gpt" className="block bg-white text-slate-900 border border-slate-200 shadow-sm rounded-2xl p-5 hover:shadow-md transition">
            <div className="flex flex-col h-full space-y-2">
              <h3 className="font-semibold text-lg">Custom Financial Sentiment GPT</h3>
              <p className="text-sm text-gray-600">Built GPT-based tool to assist with early-stage investment research and memo drafting.</p>
              <div className="mt-auto pt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">OpenAI GPT-4 API</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Google Sheets API</span>
              </div>
            </div>
          </Link>
          {/* Project Card 4: Renewable Energy Research */}
          <Link href="/projects#research" className="block bg-white text-slate-900 border border-slate-200 shadow-sm rounded-2xl p-5 hover:shadow-md transition">
            <div className="flex flex-col h-full space-y-2">
              <h3 className="font-semibold text-lg">Renewable Energy Research</h3>
              <p className="text-sm text-gray-600">Research and policy analysis on low-emission energy solutions in emerging markets.</p>
              <div className="mt-auto pt-3 flex flex-wrap gap-2">
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Excel</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Canva</span>
                <span className="text-xs px-2.5 py-1 rounded-full border border-slate-200 bg-slate-50 text-slate-600">Google Docs</span>
              </div>
            </div>
          </Link>
        </div>
      </section>
      {/* Logo Banner (scrolling logos) */}
      <LogoBanner />

      {/* Newsletter Signup (placeholder) */}
      <section className="bg-accent/10 dark:bg-accent/20 rounded-xl p-6 shadow flex flex-col items-center">
        <h2 className="text-2xl font-bold mb-2">Newsletter</h2>
        <p className="mb-4 text-text text-center">Get insights on strategy, innovation, and grassroots ideas. No spam, ever.</p>
        {/* Formspree newsletter form */}
        <form action="https://formspree.io/f/xjkrzney" method="POST" className="flex flex-col sm:flex-row gap-3 w-full max-w-md">
          <input
            type="email"
            name="email"
            placeholder="Your email"
            className="flex-1 px-4 py-2 rounded border border-gray-300 focus:outline-none focus:ring-2 focus:ring-accent"
            required
          />
          <button
            type="submit"
            className="px-6 py-2 rounded bg-accent text-white font-semibold hover:bg-accent/80 transition-colors"
          >
            Subscribe
          </button>
        </form>
      </section>
    </main>
  );
}
