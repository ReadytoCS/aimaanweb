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
          {FILTERS.map(f => (
            <button
              key={f.value}
              className={`px-3 py-1 rounded-full border text-sm font-medium transition-colors duration-150 ${activeFilter === f.value ? 'bg-green-100 text-green-600 border-green-600' : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-200 border-gray-300 dark:border-gray-700 hover:bg-green-100 hover:text-green-600 hover:border-green-600'}`}
              onClick={() => setActiveFilter(f.value)}
            >
              {f.label}
            </button>
          ))}
        </div>
      </section>

      {/* Featured Blog Posts */}
      <section>
        <div className="grid md:grid-cols-3 gap-6">
          {filteredPosts.map(post => (
            <div key={post.key} className="bg-white dark:bg-gray-800 rounded-lg shadow p-4 flex flex-col gap-2 dark:text-gray-100">
              <Image
                src={post.image}
                alt={post.title}
                width={400}
                height={200}
                className="object-cover w-full h-32 rounded mb-2"
              />
              <h3 className="font-semibold text-lg">{post.title}</h3>
              <p className="text-sm text-text">{post.description}</p>
              <span className="inline-block mt-1 mb-2 px-2 py-0.5 text-xs rounded bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 font-semibold">{FILTERS.find(f => f.value === post.category)?.label}</span>
              <span className="text-xs text-gray-400 dark:text-gray-400 mb-1">{formatDate(post.date)}</span>
              <button className="text-accent hover:underline text-sm mt-auto" onClick={() => setSelectedPost(post.key as 'narayana' | 'taobao' | 'mpesa' | 'zipline' | 'grameen')}>Read more</button>
            </div>
          ))}
        </div>
      </section>
      {/* Modal rendering */}
      {selectedPost && <PostModal postKey={selectedPost} onClose={() => setSelectedPost(null)} />}
    </main>
  );
} 