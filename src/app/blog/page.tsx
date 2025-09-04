"use client";
import React, { useState } from "react";
import Image from "next/image";
import PostModal from '../../components/PostModal';
// import PostModal from "./PostModal"; // Uncomment when PostModal is created

const FILTERS = [
  { label: 'All', value: 'all' },
  { label: 'E-Commerce', value: 'ecommerce' },
  { label: 'Energy', value: 'energy' },
  { label: 'Finance', value: 'finance' },
  { label: 'Healthcare', value: 'healthcare' },
  { label: 'Technology', value: 'technology' },
  { label: 'Other', value: 'other' },
];

const POSTS = [
  {
    key: 'grameen',
    title: 'Grameen Bank',
    image: '/stock/grameen.jpg',
    description: 'Pioneering micro-loans for the poor, Grameen Bank sparked a global micro-finance revolution and proved the unbanked are just underserved.',
    category: 'finance',
    date: '2025-06-18',
  },
  {
    key: 'zipline',
    title: 'Zipline',
    image: '/stock/zipline.jpg',
    description: 'Drones delivering life-saving medical supplies to remote areas, transforming logistics and public health in Africa and beyond.',
    category: 'healthcare',
    date: '2025-07-07',
  },
  {
    key: 'narayana',
    title: 'Narayana Health',
    image: '/stock/narayana-health.jpg',
    description: 'World-class cardiac care at a fraction of the cost, making healthcare accessible for millions in India',
    category: 'healthcare',
    date: '2025-07-02',
  },
  {
    key: 'taobao',
    title: 'Tao Bao Villages',
    image: '/stock/taobao-village.jpg',
    description: 'Rural e-commerce hubs in China empowering small villages to connect to the global digital economy',
    category: 'ecommerce',
    date: '2025-06-28',
  },
  {
    key: 'mpesa',
    title: 'M-Pesa',
    image: '/stock/mpesa.jpg',
    description: 'Mobile money transforming financial inclusion and everyday life for millions across Africa',
    category: 'finance',
    date: '2025-06-23',
  },
];

function formatDate(dateStr: string) {
  const date = new Date(dateStr);
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

export default function BlogPage() {
  const [selectedPost, setSelectedPost] = useState<null | 'narayana' | 'taobao' | 'mpesa' | 'zipline' | 'grameen'>(null);
  const [activeFilter, setActiveFilter] = useState('all');

  const sortedPosts = [...POSTS].sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

  const filteredPosts = activeFilter === 'all'
    ? sortedPosts
    : sortedPosts.filter(post => post.category === activeFilter);

  return (
    <main className="max-w-4xl mx-auto px-4 py-10 flex flex-col gap-10">
      {/* Title and Description */}
      <section>
        <h1 className="text-3xl font-bold mb-2">Grassroot Ideas</h1>
        <p className="text-text mb-4">
          Grassroot Ideas is a storytelling and research platform that spotlights breakthrough innovations emerging from developing countries. I explore how communities across Asia, Africa, and Latin America are solving complex challenges in healthcare, education, finance, and more using creativity, constraint, and local insight.
          <br /><br />
          By sharing overlooked success stories, Grassroot Ideas sparks fresh thinking, expands global playbooks, and shifts how we view innovation. Whether you are a policymaker, builder, investor, or curious mind, it shows what’s working on the ground, and why it matters globally.
        </p>
        {/* Tag filtering */}
        <div className="flex flex-wrap gap-2 mb-4">
          {FILTERS.map(f => {
            const classes = `filter-btn ${f.value} ${activeFilter === f.value ? 'active' : ''}`;
            return (
              <button
                key={f.value}
                className={classes}
                onClick={() => setActiveFilter(f.value)}
              >
                {f.label}
              </button>
            );
          })}
        </div>
      </section>

      {/* Featured Blog Posts */}
      <section>
        <div className="grid md:grid-cols-3 gap-6">
          {filteredPosts.map(post => (
            <div key={post.key} className="bg-white text-slate-900 border border-slate-200 shadow-sm rounded-2xl p-4 flex flex-col gap-2 hover:shadow-md hover:-translate-y-0.5 transition blog-card">
              <Image
                src={post.image}
                alt={post.title}
                width={400}
                height={200}
                className="object-cover w-full h-32 rounded mb-2"
              />
              <h3 className="font-semibold text-lg">{post.title}</h3>
              <p className="text-sm text-text">{post.description}</p>
              <div className="mt-auto pt-2 space-y-1.5">
                <span className={`block category-label ${post.category}`}>{FILTERS.find(f => f.value === post.category)?.label}</span>
                <span className="block text-xs text-gray-500">{formatDate(post.date)}</span>
                <button className="block text-accent hover:underline text-sm" onClick={() => setSelectedPost(post.key as 'narayana' | 'taobao' | 'mpesa' | 'zipline' | 'grameen')}>Read more</button>
              </div>
            </div>
          ))}
        </div>
      </section>
      {/* Modal rendering */}
      {selectedPost && <PostModal postKey={selectedPost} onClose={() => setSelectedPost(null)} />}
    </main>
  );
} 