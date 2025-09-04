import React from "react";
import Image from "next/image";

interface PostModalProps {
  postKey: 'narayana' | 'taobao' | 'mpesa' | 'zipline' | 'grameen';
  onClose: () => void;
}

function getPostContent(postKey: 'narayana' | 'taobao' | 'mpesa' | 'zipline' | 'grameen') {
  switch (postKey) {
    case 'narayana':
      return (
        <>
          <Image src="/stock/narayana-health.jpg" alt="Narayana Health" width={800} height={400} className="w-full rounded-md mb-4 mt-10" />
          <h2 className="text-2xl font-bold mb-2 flex items-center gap-2">
            <span role="img" aria-label="diamond">🔷</span> Narayana Health
          </h2>
          <div className="mb-4">
            <span className="inline-block bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded mr-2">Case Study</span>
            <span className="inline-block bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded">Healthcare Innovation</span>
          </div>
          <h3 className="text-lg font-semibold mt-4 mb-1">💡 What’s the story?</h3>
          <p className="text-sm">
            Founded by heart surgeon Dr. Devi Shetty, Narayana Health is a chain of Indian hospitals that delivers world-class cardiac surgeries at ultra-low costs. It&apos;s not just a hospital, it&apos;s a lesson in operational brilliance. By combining scale, process discipline, and smart pricing, they have figured out how to treat millions without breaking the system or the patient.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🚀 Why it’s a standout</h3>
          <p className="text-sm">
            Dr. Shetty basically turned surgery into a high-volume, high-efficiency service. Think of it like a life-saving assembly line, where surgeons perform more procedures, faster, and with better outcomes. The more they operate, the more affordable and effective it gets. Quality and affordability are not opposites here, they fuel each other!
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🛠️ Playbook Breakdown</h3>
          <ul className="list-disc pl-6 text-sm space-y-1">
            <li>Centralized purchasing & standardized care pathways</li>
            <li>Tiered pricing so wealthier patients help subsidize the rest</li>
            <li>Nurses and assistants take on more frontline roles (task-shifting)</li>
            <li>Focused on high-demand specialties like cardiac and cancer care</li>
          </ul>
          <h3 className="text-lg font-semibold mt-4 mb-1">🔑 Key Learnings (Aimaan’s POV)</h3>
          <p className="text-sm">
            Narayana flipped how I think about cost: It&apos;s not the barrier, it&apos;s the unlock. They have shown that with smart systems thinking, you can scale affordable care without cutting corners. It made me rethink public sector constraints, not as a money problem, but as a design problem.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🌍 Adoption Potential</h3>
          <p className="text-sm">
            This model has legs in Nigeria, Bangladesh, and even underserved parts of the U.S. Any place with young populations, high disease burdens, and weak insurance coverage. Pair it with telemedicine, and you&apos;ve got a game plan for reaching the last mile.
          </p>
        </>
      );
    case 'taobao':
      return (
        <>
          <Image src="/stock/taobao-village.jpg" alt="Tao Bao Villages" width={800} height={400} className="w-full rounded-md mb-4 mt-10" />
          <h2 className="text-2xl font-bold mb-2 flex items-center gap-2">
            <span role="img" aria-label="village">🏘️</span> Tao Bao Villages
          </h2>
          <div className="mb-4">
            <span className="inline-block bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded mr-2">Case Study</span>
            <span className="inline-block bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded">Rural E-Commerce</span>
          </div>
          <h3 className="text-lg font-semibold mt-4 mb-1">💡 What’s the story?</h3>
          <p className="text-sm">
            Tao Bao Villages are a wild success story from rural China. With help from Alibaba, these once isolated communities turned into thriving e-commerce hubs. Villagers went from offline to online, allowing them to get access to tools, training, and storefronts to sell everything from handmade crafts to furniture across the country.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🚀 Why it’s innovative</h3>
          <p className="text-sm">
            Instead of moving people to cities for jobs, Alibaba flipped the model and brought digital jobs to the people. This wasn&apos;t philanthropy, it was platform-building! Think: digital literacy, micro-loans, logistics, and payments all working together to create economic inclusion at scale.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🛠️ Playbook Breakdown</h3>
          <ul className="list-disc pl-6 text-sm space-y-1">
            <li>Trained “e-leaders” in each village to onboard others</li>
            <li>Built local logistics systems in hard-to-reach areas</li>
            <li>Offered zero-interest loans and seller incentives to reduce barriers</li>
            <li>Bundled payments, storefronts, and delivery tools into one smooth setup</li>
          </ul>
          <h3 className="text-lg font-semibold mt-4 mb-1">🔑 Key Learnings (Aimaan’s POV)</h3>
          <p className="text-sm">
            What blew me away is how Tao Bao Villages turned digital equity into infrastructure. It is not just about giving people internet, it&apos;s about building a repeatable ecosystem that unlocks economic agency. It made me rethink inclusion as not just as a fairness issue, but as a growth strategy.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🌍 Adoption Potential</h3>
          <p className="text-sm">
            This model feels ripe for places like rural Indonesia, Nepal, or even Indigenous communities in Canada. With the right mix of localized commerce platforms, mobile payments, and digital training, you could turn rural populations into a distributed workforce, and do it profitably.
          </p>
        </>
      );
    case 'mpesa':
      return (
        <>
          <Image src="/stock/mpesa.jpg" alt="M-Pesa" width={800} height={400} className="w-full rounded-md mb-4 mt-10" />
          <h2 className="text-2xl font-bold mb-2 flex items-center gap-2">
            <span role="img" aria-label="diamond">📲</span> M-Pesa
          </h2>
          <div className="mb-4">
            <span className="inline-block bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded mr-2">Case Study</span>
            <span className="inline-block bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded">Fintech & Financial Inclusion</span>
          </div>
          <h3 className="text-lg font-semibold mt-4 mb-1">💡 What’s the story?</h3>
          <p className="text-sm">
            M-Pesa flipped the financial system on its head in Kenya. It let people send and receive money over SMS, no bank account or internet needed. What started as a simple mobile money service is now deeply woven into Kenya&apos;s economy, powering everything from daily transactions to business loans.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🚀 Why it’s innovative</h3>
          <p className="text-sm">
            While banks were busy building branches, M-Pesa leapfrogged the entire system. It brought financial access to millions who were previously excluded, all through basic phones and SIM cards. The magic? Simplicity, trust, and distribution.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🛠️ Playbook Breakdown</h3>
          <ul className="list-disc pl-6 text-sm space-y-1">
            <li>Used telecom agents, not banks, to sign people up</li>
            <li>Ran on SMS, so it worked on basic feature phones</li>
            <li>Focused on high-density, cash-heavy communities</li>
            <li>Layered in more products (savings, loans) as trust grew</li>
          </ul>
          <h3 className="text-lg font-semibold mt-4 mb-1">🔑 Key Learnings (Aimaan’s POV)</h3>
          <p className="text-sm">
            M-Pesa made me rethink what fintech really means. It is not just about flashy apps, it&apos;s about building something people trust and actually use. They nailed product-market fit by grounding everything in local behaviors and needs.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🌍 Adoption Potential</h3>
          <p className="text-sm">
            Places like Pakistan, Haiti, or underserved regions facing institutional gaps where formal banking is limited or mistrusted could benefit hugely. M-Pesa&apos;s model is also a powerful blueprint for building inclusive digital public infrastructure from the ground up.
          </p>
        </>
      );
    case 'zipline':
      return (
        <>
          <Image src="/stock/zipline.jpg" alt="Zipline" width={800} height={400} className="w-full rounded-md mb-4 mt-10" />
          <h2 className="text-2xl font-bold mb-2 flex items-center gap-2">
            <span role="img" aria-label="airplane">✈️</span> Zipline
          </h2>
          <div className="mb-4">
            <span className="inline-block bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded mr-2">Case Study</span>
            <span className="inline-block bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded">Logistics Innovation & Public Health</span>
          </div>
          <span className="text-xs text-gray-500 mb-2 block">July 7th, 2025</span>
          <h3 className="text-lg font-semibold mt-4 mb-1">💡 What’s the story?</h3>
          <p className="text-sm">
            Zipline started in Rwanda with a big, yet simple idea: use drones to deliver life-saving medical supplies to remote areas. Think blood, vaccines, insulin—anything time-sensitive and hard to get to. Today, they’ve grown into a full-blown automated logistics network, operating in countries like Ghana, Nigeria, Kenya, and even the U.S.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🚀 Why it’s a stand-out</h3>
          <p className="text-sm">
            Zipline turned a classic bottleneck like poor infrastructure into an opportunity. Where roads were unreliable, they flew over the problem. Their drone-based system cuts delivery times from hours (or days) to under 30 minutes, saving lives in emergencies and making rural healthcare more reliable.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🛠️ Playbook Breakdown</h3>
          <ul className="list-disc pl-6 text-sm space-y-1">
            <li>Focused on high-impact, hard-to-serve use cases (e.g., rural blood banks)</li>
            <li>Partnered directly with governments and health systems</li>
            <li>Built end-to-end logistics hubs to handle storage, packing, and autonomous delivery</li>
            <li>Designed ultra-efficient fixed-wing drones to handle scale and distance</li>
            <li>Now expanding into e-commerce and home delivery with precision-drop tech</li>
          </ul>
          <h3 className="text-lg font-semibold mt-4 mb-1">🔑 Key Learnings (Aimaan’s POV)</h3>
          <p className="text-sm">
            Zipline showed me that infrastructure does not always have to be physical. In places where roads cannot be fixed anytime soon, they built something better and faster. It reframed logistics for me as a layered system, not just trucks and warehouses. Because they are solving a public health problem, not just a delivery one, Zipline feels less like a tech company and more like a lifeline!
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🌍 Adoption Potential</h3>
          <p className="text-sm">
            High-need, hard-to-reach regions in Indonesia, the Philippines, or the Amazon basin could benefit from this model. In general, anywhere with geographic barriers and critical supply gaps is fair game. With growing applications beyond healthcare, Zipline could become the FedEx for frontier markets.
          </p>
        </>
      );
    case 'grameen':
      return (
        <>
          <Image src="/stock/grameen.jpg" alt="Grameen Bank" width={800} height={400} className="w-full rounded-md mb-4 mt-10" />
          <h2 className="text-2xl font-bold mb-2 flex items-center gap-2">
            <span role="img" aria-label="bank">🏦</span> Grameen Bank
          </h2>
          <div className="mb-4">
            <span className="inline-block bg-blue-100 text-blue-800 text-xs font-semibold px-2 py-1 rounded mr-2">Case Study</span>
            <span className="inline-block bg-green-100 text-green-800 text-xs font-semibold px-2 py-1 rounded">Microfinance & Economic Empowerment</span>
          </div>
          <span className="text-xs text-gray-500 mb-2 block">June 18th, 2025</span>
          <h3 className="text-lg font-semibold mt-4 mb-1">💡 What’s the story?</h3>
          <p className="text-sm">
            Grameen Bank, founded by Nobel laureate Muhammad Yunus in Bangladesh, pioneered the concept of micro-loans for the poor, particularly for women with no credit history or collateral. By lending tiny amounts to help people start or grow small businesses, Grameen proved that the poor were not un-bankable, they were just underserved.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🚀 Why it’s innovative</h3>
          <p className="text-sm">
            Instead of relying on credit scores or traditional collateral, Grameen built a system based on community trust and group accountability. It flipped the banking model by betting on those most excluded and in doing so, sparked a global micro-finance revolution.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🛠️ Playbook Breakdown</h3>
          <ul className="list-disc pl-6 text-sm space-y-1">
            <li>Offered small loans without collateral, often to women-led households</li>
            <li>Used group lending circles to create built-in support and repayment incentives</li>
            <li>Focused on income-generating activities like livestock, crafts, and farming</li>
            <li>Reinvested profits into expanding outreach and social programs</li>
          </ul>
          <h3 className="text-lg font-semibold mt-4 mb-1">🔑 Key Learnings (Aimaan’s POV)</h3>
          <p className="text-sm">
            Grameen taught me that empowerment and finance were not mutually exclusive. By trusting borrowers and designing for their realities the model created real upward mobility. It reshaped how I think about risk, especially in emerging markets.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🌍 Adoption Potential</h3>
          <p className="text-sm">
            This approach is tailor-made for rural parts of India, Sub-Saharan Africa, or Southeast Asia, where people live outside the formal credit system. With a layer of digital onboarding and mobile repayment tools, Grameen’s model could thrive in today’s fintech ecosystem, allowing people to bridge inclusion with dignity.
          </p>
        </>
      );
    default:
      return <p className="text-sm">(Full post content will go here.)</p>;
  }
}

const PostModal: React.FC<PostModalProps> = ({ postKey, onClose }) => {
  return (
    <div className="fixed inset-0 backdrop-blur-sm bg-black/10 z-40 flex items-center justify-center">
      <div className="bg-white text-slate-900 p-6 rounded-2xl shadow-lg z-50 relative max-w-3xl w-full mx-4 pt-2 max-h-[90vh] overflow-y-auto border border-slate-200">
        <button
          className="absolute top-2 left-2 text-3xl text-black hover:text-accent focus:outline-none"
          onClick={onClose}
          aria-label="Close modal"
        >
          &times;
        </button>
        <div className="post-content">
          {getPostContent(postKey)}
        </div>
        <style jsx>{`
          .post-content, .post-content * {
            color: #111827; /* slate-900 */
          }
        `}</style>
      </div>
    </div>
  );
};

export default PostModal; 