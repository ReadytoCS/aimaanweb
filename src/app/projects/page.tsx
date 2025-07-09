"use client";
import React from "react";

// Projects page for Aimaan Shergill
// Features: Card grid layout, sample projects
export default function ProjectsPage() {
  return (
    <main className="max-w-4xl mx-auto px-4 py-10 flex flex-col gap-10">
      {/* Title */}
      <h1 className="text-3xl font-bold mb-6">Projects</h1>

      {/* Projects Grid */}
      <section>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 px-6 md:px-12">
          {/* Project Card 1: Independent Consulting Projects */}
          <div id="consulting" className="bg-white dark:bg-gray-900 border-l-4 border-indigo-100 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300 h-full flex flex-col dark:text-gray-100">
            <span className="inline-block bg-indigo-100 text-indigo-800 text-xs font-semibold px-2 py-1 rounded-full mb-3">Consulting</span>
            <h3 className="font-bold text-lg mb-1">Independent Consulting Projects</h3>
            <p className="text-sm text-text italic mb-2">Strategy and fundraising advisory for nonprofits and retailers.</p>
            <div className="border-t border-gray-200 my-3" />
            <div className="mb-2">
              <div className="font-semibold mb-1">🛠️ What I Built</div>
              <ul className="text-base leading-relaxed list-disc pl-5">
                <li><span className="font-semibold">Canada’s largest retailer:</span> Conducted market research and product mapping for their loyalty program, identified key factors influencing customer loyalty and digital rewards engagement</li>
                <li><span className="font-semibold">Canadian Tree Planting NPO:</span> Automated sponsorship outreach using MailChimp and a custom Funding Calculator</li>
                <li><span className="font-semibold">Abacus Mathematics Center:</span> Created a learning platform for Indigenous schools, led 8 consultants from scoping to delivery</li>
                <li><span className="font-semibold">Huron Restoration:</span> Developed a funding strategy and campaign to raise $600,000 CAD for a historic restoration project</li>
              </ul>
            </div>
            <div className="flex flex-wrap gap-2 mt-auto pt-2">
              <span className="bg-gray-100 text-gray-800 text-xs font-semibold px-2 py-1 rounded">MailChimp</span>
              <span className="bg-gray-100 text-gray-800 text-xs font-semibold px-2 py-1 rounded">Google Workspace</span>
              <span className="bg-gray-100 text-gray-800 text-xs font-semibold px-2 py-1 rounded">Tableau</span>
              <span className="bg-gray-100 text-gray-800 text-xs font-semibold px-2 py-1 rounded">SQL</span>
              <span className="bg-gray-100 text-gray-800 text-xs font-semibold px-2 py-1 rounded">Python</span>
              <span className="bg-gray-100 text-gray-800 text-xs font-semibold px-2 py-1 rounded">OpenAI GPT-4 API</span>
              <span className="bg-gray-100 text-gray-800 text-xs font-semibold px-2 py-1 rounded">Asana</span>
            </div>
          </div>
          {/* Project Card 2: Gig Worker Finance Tracker */}
          <div id="grainai" className="bg-white dark:bg-gray-900 border-l-4 border-yellow-200 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300 h-full flex flex-col dark:text-gray-100">
            <span className="inline-block bg-yellow-100 text-yellow-800 text-xs font-semibold px-2 py-1 rounded-full mb-3">Founder-Led Project</span>
            <h3 className="font-bold text-lg mb-1">GrainAI (Fintech for Gig Workers)</h3>
            <p className="text-sm text-text italic mb-2">Strategy, product design, and user research for a personal finance platform tailored to gig workers.</p>
            <div className="border-t border-gray-200 my-3" />
            <div className="mb-2">
              <div className="font-semibold mb-1">🛠️ What I Built</div>
              <ul className="text-base leading-relaxed list-disc pl-5">
                <li><span className="font-semibold">Financial Goals Tracker:</span> Created visual goal-setting tool that helps users plan around debt, emergency funds, and large purchases. Integrated with real-time progress and nudges</li>
                <li><span className="font-semibold">Loan & Savings Simulator:</span> Built a modular calculator to project loan repayment timelines, and hybrid savings strategies personalized to income volatility</li>
                <li><span className="font-semibold">Growth-Driven Product Roadmap:</span> Led GTM and product planning for features like gamified savings, financial literacy modules, and AI-powered nudges</li>
                <li><span className="font-semibold">Smart Income & Expense Dashboard:</span> Developing a categorized dashboard pulling user input and bank data to offer clear visibility into earnings, spend patterns, and suggested actions</li>
              </ul>
            </div>
            <div className="flex flex-wrap gap-2 mt-auto pt-2">
              <span className="bg-yellow-100 text-yellow-800 text-xs font-semibold px-2 py-1 rounded">CursorAI</span>
              <span className="bg-yellow-100 text-yellow-800 text-xs font-semibold px-2 py-1 rounded">Python</span>
              <span className="bg-yellow-100 text-yellow-800 text-xs font-semibold px-2 py-1 rounded">Google Sheets API</span>
              <span className="bg-yellow-100 text-yellow-800 text-xs font-semibold px-2 py-1 rounded">Lovable</span>
              <span className="bg-yellow-100 text-yellow-800 text-xs font-semibold px-2 py-1 rounded">OpenAI GPT-4 API</span>
            </div>
          </div>
          {/* Project Card 2.5: WallStreetOasis – Editorial Contributor */}
          <div className="bg-white dark:bg-gray-900 border-l-4 border-green-100 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300 h-full flex flex-col dark:text-gray-100">
            <span className="inline-block bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded-full mb-3">Financial Writing</span>
            <h3 className="font-bold text-lg mb-1">WallStreetOasis - Editorial</h3>
            <p className="text-sm text-text italic mb-2">Wrote articles on valuations, deal structures, and capital markets for a global finance audience.</p>
            <div className="border-t border-gray-200 my-3" />
            <div className="mb-2">
              <div className="font-semibold mb-1">🛠️ What I Built</div>
              <ul className="text-base leading-relaxed list-disc pl-5">
                <li>Published 20+ research articles on M&A, healthcare, oil and gas, and investment topics</li>
                <li>Created content for WSO&apos;s valuation, strategy, and investing libraries</li>
                <li>Articles averaged 20% higher engagement than peer forums</li>
              </ul>
            </div>
            <div className="mb-2">
              <div className="font-semibold mb-1">📚 Popular reads:</div>
              <div className="flex flex-wrap gap-2 text-sm text-gray-700">
                <a href="https://www.wallstreetoasis.com/resources/skills/strategy/organic-growth" target="_blank" rel="noopener noreferrer" className="underline hover:text-green-700">Organic Growth</a>
                <a href="https://www.wallstreetoasis.com/resources/skills/deals/mixed-offering" target="_blank" rel="noopener noreferrer" className="underline hover:text-green-700">Mixed Offering</a>
                <a href="https://www.wallstreetoasis.com/resources/skills/trading-investing/healthcare-sector" target="_blank" rel="noopener noreferrer" className="underline hover:text-green-700">Healthcare Sector</a>
                <a href="https://www.wallstreetoasis.com/resources/skills/valuation/breakup-value" target="_blank" rel="noopener noreferrer" className="underline hover:text-green-700">Breakup Value</a>
                <a href="https://www.wallstreetoasis.com/resources/skills/trading-investing/distressed-securities" target="_blank" rel="noopener noreferrer" className="underline hover:text-green-700">Distressed Securities</a>
              </div>
            </div>
            <div className="flex flex-wrap gap-2 mt-auto pt-2">
              <span className="bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded">Google Docs</span>
              <span className="bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded">SEO tools</span>
              <span className="bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded">WSO CMS</span>
            </div>
          </div>
          {/* Project Card 3: Custom Financial Sentiment GPT */}
          <div id="gpt" className="bg-white dark:bg-gray-900 border-l-4 border-purple-100 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300 h-full flex flex-col dark:text-gray-100">
            <span className="inline-block bg-purple-100 text-purple-800 text-xs font-semibold px-2 py-1 rounded-full mb-3">AI</span>
            <h3 className="font-bold text-lg mb-1">Custom Financial Sentiment GPT</h3>
            <p className="text-sm text-text italic mb-2">Built GPT-based tool to assist with early-stage investment research and memo drafting.</p>
            <div className="border-t border-gray-200 my-3" />
            <div className="mb-2">
              <div className="font-semibold mb-1">🛠️ What I Built</div>
              <ul className="text-base leading-relaxed list-disc pl-5">
                <li>Used GPT-4 to extract insights from startup profiles, news transcripts, and analyst reports</li>
                <li>Created templates to summarize deal rationale, surface red flags, and flag key metrics</li>
                <li>Designed the tool for early-stage diligence workflows, making it useful for quick memo drafts or VC screens</li>
              </ul>
            </div>
            <div className="flex flex-wrap gap-2 mt-auto pt-2">
              <span className="bg-purple-100 text-purple-800 text-xs font-semibold px-2 py-1 rounded">OpenAI GPT-4 API</span>
              <span className="bg-purple-100 text-purple-800 text-xs font-semibold px-2 py-1 rounded">Google Sheets API</span>
            </div>
          </div>
          {/* Project Card 4: Driver Profitability Dashboard */}
          <div id="driver-dashboard" className="bg-white dark:bg-gray-900 border-l-4 border-orange-100 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300 h-full flex flex-col dark:text-gray-100">
            <span className="inline-block bg-orange-100 text-orange-800 text-xs font-semibold px-2 py-1 rounded-full mb-3">Data Analytics</span>
            <h3 className="font-bold text-lg mb-1">Driver Profitability Dashboard</h3>
            <p className="text-sm text-text italic mb-2">Interactive dashboard analyzing Uber driver earnings after expenses across zones, times, and trip types.</p>
            <div className="border-t border-gray-200 my-3" />
            <div className="mb-2">
              <div className="font-semibold mb-1">🛠️ What I Built</div>
              <ul className="text-base leading-relaxed list-disc pl-5">
                <li><span className="font-semibold">Interactive Dashboard:</span> Built a comprehensive Streamlit app that analyzes 1000+ simulated trips across 6 zones with realistic cost modeling</li>
                <li><span className="font-semibold">Profitability Analysis:</span> Calculated driver net earnings after gas, time, and wait costs to identify truly profitable trips and zones</li>
                <li><span className="font-semibold">Business Intelligence:</span> Created automated insights engine that identifies worst/best performing zones and generates actionable recommendations</li>
                <li><span className="font-semibold">Interactive Visualizations:</span> Built earnings by region, time patterns, trip type comparisons, and cost breakdown charts using Plotly</li>
              </ul>
            </div>
            <div className="flex flex-wrap gap-2 mt-auto pt-2">
              <span className="bg-orange-100 text-orange-800 text-xs font-semibold px-2 py-1 rounded">Python</span>
              <span className="bg-orange-100 text-orange-800 text-xs font-semibold px-2 py-1 rounded">Streamlit</span>
              <span className="bg-orange-100 text-orange-800 text-xs font-semibold px-2 py-1 rounded">Pandas</span>
              <span className="bg-orange-100 text-orange-800 text-xs font-semibold px-2 py-1 rounded">Plotly</span>
              <span className="bg-orange-100 text-orange-800 text-xs font-semibold px-2 py-1 rounded">NumPy</span>
              <span className="bg-orange-100 text-orange-800 text-xs font-semibold px-2 py-1 rounded">CursorAI</span>
            </div>
            <div className="mt-3 pt-3 border-t border-gray-200">
              <a 
                href="https://driver-dashboard-nntngrim9pyjt9u8pwzrpf.streamlit.app/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 text-orange-600 hover:text-orange-700 font-medium text-sm"
              >
                🚀 Live Demo
                <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M7 17l9.2-9.2M17 17V7H7"/>
                </svg>
              </a>
            </div>
          </div>
          {/* Project Card 5: Renewable Energy Research */}
          <div id="research" className="bg-white dark:bg-gray-900 border-l-4 border-blue-100 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300 h-full flex flex-col dark:text-gray-100">
            <span className="inline-block bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded-full mb-3">Research</span>
            <h3 className="font-bold text-lg mb-1">Renewable Energy Research</h3>
            <p className="text-sm text-text italic mb-2">Research and policy analysis on low-emission energy solutions in emerging markets.</p>
            <div className="border-t border-gray-200 my-3" />
            <div className="mb-2">
              <div className="font-semibold mb-1">🛠️ What I Built</div>
              <ul className="text-base leading-relaxed list-disc pl-5">
                <li>Researched Alberta’s carbon pricing framework and its impact on renewable investment and emissions reduction</li>
                <li>Completed the <a href='https://studentenergy.org/fellowship-tiers-of-engagement/' target='_blank' rel='noopener noreferrer' className='underline hover:text-blue-700'>Student Energy Tier 1 Fellowship</a>, contributing to global projects on energy equity and access</li>
                <li>Conducted Master&apos;s level thesis on the feasibility of Small Modular Reactors (SMRs) in South Asia, focused on deployment potential in dense, underserved regions</li>
              </ul>
            </div>
            <div className="flex flex-wrap gap-2 mt-auto pt-2">
              <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded">Excel</span>
              <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded">Canva</span>
              <span className="bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded">Google Docs</span>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
} 