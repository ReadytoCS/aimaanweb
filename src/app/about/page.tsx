"use client";
import React from "react";
import Image from "next/image";

// About page for Aimaan Shergill
// Sections: Career Overview, Experience Timeline, Education
export default function AboutPage() {
  return (
    <main className="max-w-3xl mx-auto px-4 py-10 flex flex-col gap-8">
      {/* Title */}
      <h1 className="text-3xl font-semibold mb-2">About Me</h1>
      {/* Human Headline */}
      <p className="text-xl font-light text-accent mb-10">Restless strategist. Global builder. People-first problem solver.</p>
      {/* Career Overview */}
      <section className="py-10 bg-white">
        <h2 className="text-3xl font-semibold mb-6">Career Overview</h2>
        <p className="text-base text-gray-600">
          I am a strategist who enjoys working across messy problems where data meets decision-making. I have contributed to projects spanning megacity finance systems in the Middle East, healthcare funding reform in Ontario, and infrastructure due diligence under Canada’s Zero Emission Program. Now, I work on global growth and investor strategy at RapidSOS, a public safety technology company connecting emergency data at scale. Outside work, I run Grassroot Ideas, a newsletter that spotlights breakthrough innovations from countries often ignored by Silicon Valley. I believe the next great solutions will rise from Lagos as easily as London, and I want my career, writing, and future ventures to help make that happen.
        </p>
      </section>
      <hr className="my-12 border-gray-300" />
      {/* Experience Timeline or Cards */}
      <section className="py-10 bg-gray-50">
        <h2 className="text-3xl font-semibold mb-6">Experience</h2>
        <div className="flex flex-col gap-4">
          {/* RapidSOS */}
          <div className="bg-white border rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-200 flex items-start dark:bg-gray-900 dark:text-gray-100">
            <Image src="/logos/rapidsos.jpg" alt="RapidSOS logo" width={64} height={64} className="w-16 h-16 mr-6 object-contain mt-1" />
            <div className="space-y-2">
              <h3 className="text-lg font-medium text-gray-700">RapidSOS</h3>
              <p className="text-base text-gray-600">Strategy & Corporate Development</p>
              <p className="text-base text-gray-700">
                At RapidSOS, I worked at the intersection of public safety, growth, and finance, helping shape strategy for a platform that connects real-time emergency data to 911. I built long-range plans, supported a live Series D fundraise, and evaluated acquisitions in a space where saving seconds truly saves lives.
              </p>
              <div className="border-l-4 border-gray-200 pl-4 mt-2">
                <p className="text-sm font-medium text-gray-700 mb-1">Key Takeaways:</p>
                <ul className="list-disc list-inside text-sm text-gray-600">
                  <li>Strategy feels different when lives are at stake, I learned how to balance scale with impact</li>
                  <li>The most meaningful partnerships are the ones that move the needle, not just logos</li>
                  <li>Saw how to position growth strategy to resonate with institutional investors</li>
                </ul>
              </div>
            </div>
          </div>
          {/* Deloitte */}
          <div className="bg-white border rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-200 flex items-start dark:bg-gray-900 dark:text-gray-100">
            <Image src="/logos/deloitte.jpg" alt="Deloitte logo" width={64} height={64} className="w-16 h-16 mr-6 object-contain mt-1" />
            <div className="space-y-2">
              <h3 className="text-lg font-medium text-gray-700">Deloitte</h3>
              <p className="text-base text-gray-600">Infrastructure M&A</p>
              <p className="text-base text-gray-700">
                At Deloitte, I worked on the kind of projects that shape entire regions like Electric Vehicle networks and infrastructure rollouts. It was my first exposure to how governments, capital, and strategy collide. I built models, presented findings, and helped clients see the financial side of long-term impact.
              </p>
              <div className="border-l-4 border-gray-200 pl-4 mt-2">
                <p className="text-sm font-medium text-gray-700 mb-1">Key Takeaways:</p>
                <ul className="list-disc list-inside text-sm text-gray-600">
                  <li>Learned to ask: what does success look like in 10 years, not just next quarter</li>
                  <li>Found value in visual storytelling, seeing how dashboards can simplify the complex</li>
                  <li>Understood how ESG and infrastructure go hand-in-hand when scale meets sustainability</li>
                </ul>
              </div>
            </div>
          </div>
          {/* Ontario Health */}
          <div className="bg-white border rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-200 flex items-start dark:bg-gray-900 dark:text-gray-100">
            <Image src="/logos/ontariohealth.jpg" alt="Ontario Health logo" width={64} height={64} className="w-16 h-16 mr-6 object-contain mt-1" />
            <div className="space-y-2">
              <h3 className="text-lg font-medium text-gray-700">Ontario Health</h3>
              <p className="text-base text-gray-600">Strategic Funding & Financial Modelling Intern</p>
              <p className="text-base text-gray-700">
                At Ontario Health, I worked on long-term funding strategy, analyzing international disease and spending data to better allocate healthcare dollars across Ontario. 
              </p>
              <div className="border-l-4 border-gray-200 pl-4 mt-2">
                <p className="text-sm font-medium text-gray-700 mb-1">Key Takeaways:</p>
                <ul className="list-disc list-inside text-sm text-gray-600">
                  <li>Saw how cross-country data informs smarter funding decisions</li>
                  <li>Gained experience linking economic indicators to public health budgeting</li>
                  <li>Realized that behind every data-driven recommendation is a story and a trade-off</li>
                </ul>
              </div>
            </div>
          </div>
          {/* PwC Dubai */}
          <div className="bg-white border rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-200 flex items-start dark:bg-gray-900 dark:text-gray-100">
            <Image src="/logos/pwc.jpg" alt="PwC Dubai logo" width={64} height={64} className="w-16 h-16 mr-6 object-contain mt-1" />
            <div className="space-y-2">
              <h3 className="text-lg font-medium text-gray-700">PwC Dubai</h3>
              <p className="text-base text-gray-600">Finance Transformation Consulting</p>
              <p className="text-base text-gray-700">
                At PwC Middle East, I worked on designing the financial backbone of a $500B smart city project. We weren’t just creating models we were mapping organizational leadership in a city that doesn’t exist yet. I also got to advise a sovereign wealth fund on digital dashboard to map their assets.
              </p>
              <div className="border-l-4 border-gray-200 pl-4 mt-2">
                <p className="text-sm font-medium text-gray-700 mb-1">Key Takeaways:</p>
                <ul className="list-disc list-inside text-sm text-gray-600">
                  <li>Learned how to navigate high-stakes strategy with sovereign clients and shifting priorities</li>
                  <li>Saw how storytelling through models can shape how governments plan for the future</li>
                  <li>Got a front-row seat to the scale transformation in the Gulf region</li>
                </ul>
              </div>
            </div>
          </div>
          {/* Markid */}
          <div className="bg-white border rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-200 flex items-start dark:bg-gray-900 dark:text-gray-100">
            <Image src="/logos/markid.png" alt="Markid logo" width={64} height={64} className="w-16 h-16 mr-6 object-contain mt-1" />
            <div className="space-y-2">
              <h3 className="text-lg font-medium text-gray-700">Markid</h3>
              <p className="text-base text-gray-600">Strategy & Operations</p>
              <p className="text-base text-gray-700">
                At Markid, a kids’ resale startup, I helped turn messy ideas into real products. From interviews to building a GTM roadmap, I learned to move fast, test assumptions, and find clarity in early chaos working closely with founders and engineers to get the product into users’ hands.
              </p>
              <div className="border-l-4 border-gray-200 pl-4 mt-2">
                <p className="text-sm font-medium text-gray-700 mb-1">Key Takeaways:</p>
                <ul className="list-disc list-inside text-sm text-gray-600">
                  <li>Product strategy is about choosing what not to do just as much as what to build</li>
                  <li>Fast feedback beats perfect answers, as interviews taught me more than data ever could</li>
                  <li>Being embedded in a startup showed me how vision meets execution, day by day</li>
                </ul>
              </div>
            </div>
          </div>
          {/* Coca-Cola */}
          <div className="bg-white border rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-200 flex items-start dark:bg-gray-900 dark:text-gray-100">
            <Image src="/logos/cocacola.jpg" alt="Coca-Cola logo" width={64} height={64} className="w-16 h-16 mr-6 object-contain mt-1" />
            <div className="space-y-2">
              <h3 className="text-lg font-medium text-gray-700">Coca-Cola India</h3>
              <p className="text-base text-gray-600">Strategy & Operations</p>
              <p className="text-base text-gray-700">
                In North India, I worked on go-to-market strategies for Coca-Cola, analyzing how socio-economic factors shaped demand, and how we could better respond to competitors like Pepsi. From grassroots incentives to price-pack design, it was all about understanding what really drives choice.
              </p>
              <div className="border-l-4 border-gray-200 pl-4 mt-2">
                <p className="text-sm font-medium text-gray-700 mb-1">Key Takeaways:</p>
                <ul className="list-disc list-inside text-sm text-gray-600">
                  <li>Saw how pricing is shaped by regional context, and not just demand curves</li>
                  <li>Proposed region-specific promotions based on consumption habits</li>
                  <li>Realized that even global brands win on the ground, through trust, timing, and relevance</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>
      <hr className="my-12 border-gray-300" />
      {/* Education */}
      <section className="py-10 bg-white">
        <h2 className="text-3xl font-semibold mb-6">Education</h2>
        <div className="flex flex-col gap-4">
          {/* Ivey Business School */}
          <div className="bg-gray-50 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-200 mb-4 flex items-start dark:bg-gray-800 dark:text-gray-100">
            <Image src="/logos/ivey.jpg" alt="Ivey Business School logo" width={96} height={96} className="w-24 h-24 mr-6 object-contain mt-1" />
            <div className="space-y-2">
              <h3 className="text-lg font-medium text-gray-700">Western University - Ivey Business School</h3>
              <p className="text-base text-gray-600">Master of Management in Analytics | London, Ontario</p>
              <p className="text-base mt-2 text-gray-700">
                Studied how data and strategy intersect, from predictive modelling to applied AI. Worked on projects across healthcare, finance, and retail using Python, SQL, R-Studio & Tableau while learning to move from code to context.
              </p>
              <div className="border-l-4 border-gray-200 pl-4 mt-2">
                <p className="text-sm font-medium text-gray-700 mb-1">Key Takeaways:</p>
                <ul className="list-disc list-inside text-sm text-gray-600">
                  <li>Applied analytics to real-world business and policy challenges</li>
                  <li>Built end-to-end data pipelines and AI tools on large-scale datasets</li>
                  <li>Found that good questions drive better data outcomes than good models alone</li>
                </ul>
              </div>
            </div>
          </div>
          {/* University of Toronto (Rotman) */}
          <div className="bg-gray-50 rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-200 mb-4 flex items-start dark:bg-gray-800 dark:text-gray-100">
            <Image src="/logos/rotman.jpg" alt="Rotman/University of Toronto logo" width={96} height={96} className="w-24 h-24 mr-6 object-contain mt-1" />
            <div className="space-y-2">
              <h3 className="text-lg font-medium text-gray-700">University of Toronto - Rotman Commerce</h3>
              <p className="text-base text-gray-600">Bachelor of Commerce (Finance, Economics & Data Science) | Toronto, Ontario</p>
              <p className="text-base mt-2 text-gray-700">
                Explored how markets, policy, and technology shape economic systems, and how data connects it all. Led student organizations, launched conferences, and built communities around innovation, consulting, and impact.
              </p>
              <div className="border-l-4 border-gray-200 pl-4 mt-2">
                <p className="text-sm font-medium text-gray-700 mb-1">Key Takeaways:</p>
                <ul className="list-disc list-inside text-sm text-gray-600">
                  <li>Developed a strong foundation in finance, economics, and data analysis</li>
                  <li>Learned to lead by organizing teams, events, and partnerships</li>
                  <li>Discovered how storytelling, systems thinking, and student voice create real impact</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
} 