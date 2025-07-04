import React from "react";
import Image from "next/image";

interface PostModalProps {
  postKey: 'narayana' | 'taobao' | 'mpesa';
  onClose: () => void;
}

function getPostContent(postKey: 'narayana' | 'taobao' | 'mpesa') {
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
          <p className="text-sm text-gray-700 dark:text-gray-300">
            Founded by heart surgeon Dr. Devi Shetty, Narayana Health is a chain of Indian hospitals that delivers world-class cardiac surgeries at ultra-low costs. It&apos;s not just a hospital, it&apos;s a lesson in operational brilliance. By combining scale, process discipline, and smart pricing, they have figured out how to treat millions without breaking the system or the patient.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🚀 Why it’s a standout</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
            Dr. Shetty basically turned surgery into a high-volume, high-efficiency service. Think of it like a life-saving assembly line, where surgeons perform more procedures, faster, and with better outcomes. The more they operate, the more affordable and effective it gets. Quality and affordability are not opposites here, they fuel each other!
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🛠️ Playbook Breakdown</h3>
          <ul className="list-disc pl-6 text-sm text-gray-700 dark:text-gray-300 space-y-1">
            <li>Centralized purchasing & standardized care pathways</li>
            <li>Tiered pricing so wealthier patients help subsidize the rest</li>
            <li>Nurses and assistants take on more frontline roles (task-shifting)</li>
            <li>Focused on high-demand specialties like cardiac and cancer care</li>
          </ul>
          <h3 className="text-lg font-semibold mt-4 mb-1">🔑 Key Learnings (Aimaan’s POV)</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
            Narayana flipped how I think about cost: It&apos;s not the barrier, it&apos;s the unlock. They have shown that with smart systems thinking, you can scale affordable care without cutting corners. It made me rethink public sector constraints, not as a money problem, but as a design problem.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🌍 Adoption Potential</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
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
          <p className="text-sm text-gray-700 dark:text-gray-300">
            Tao Bao Villages are a wild success story from rural China. With help from Alibaba, these once isolated communities turned into thriving e-commerce hubs. Villagers went from offline to online, allowing them to get access to tools, training, and storefronts to sell everything from handmade crafts to furniture across the country.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🚀 Why it’s innovative</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
            Instead of moving people to cities for jobs, Alibaba flipped the model and brought digital jobs to the people. This wasn&apos;t philanthropy, it was platform-building! Think: digital literacy, micro-loans, logistics, and payments all working together to create economic inclusion at scale.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🛠️ Playbook Breakdown</h3>
          <ul className="list-disc pl-6 text-sm text-gray-700 dark:text-gray-300 space-y-1">
            <li>Trained “e-leaders” in each village to onboard others</li>
            <li>Built local logistics systems in hard-to-reach areas</li>
            <li>Offered zero-interest loans and seller incentives to reduce barriers</li>
            <li>Bundled payments, storefronts, and delivery tools into one smooth setup</li>
          </ul>
          <h3 className="text-lg font-semibold mt-4 mb-1">🔑 Key Learnings (Aimaan’s POV)</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
            What blew me away is how Tao Bao Villages turned digital equity into infrastructure. It is not just about giving people internet, it&apos;s about building a repeatable ecosystem that unlocks economic agency. It made me rethink inclusion as not just as a fairness issue, but as a growth strategy.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🌍 Adoption Potential</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
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
          <p className="text-sm text-gray-700 dark:text-gray-300">
            M-Pesa flipped the financial system on its head in Kenya. It let people send and receive money over SMS, no bank account or internet needed. What started as a simple mobile money service is now deeply woven into Kenya&apos;s economy, powering everything from daily transactions to business loans.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🚀 Why it’s innovative</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
            While banks were busy building branches, M-Pesa leapfrogged the entire system. It brought financial access to millions who were previously excluded, all through basic phones and SIM cards. The magic? Simplicity, trust, and distribution.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🛠️ Playbook Breakdown</h3>
          <ul className="list-disc pl-6 text-sm text-gray-700 dark:text-gray-300 space-y-1">
            <li>Used telecom agents, not banks, to sign people up</li>
            <li>Ran on SMS, so it worked on basic feature phones</li>
            <li>Focused on high-density, cash-heavy communities</li>
            <li>Layered in more products (savings, loans) as trust grew</li>
          </ul>
          <h3 className="text-lg font-semibold mt-4 mb-1">🔑 Key Learnings (Aimaan’s POV)</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
            M-Pesa made me rethink what fintech really means. It is not just about flashy apps, it&apos;s about building something people trust and actually use. They nailed product-market fit by grounding everything in local behaviors and needs.
          </p>
          <h3 className="text-lg font-semibold mt-4 mb-1">🌍 Adoption Potential</h3>
          <p className="text-sm text-gray-700 dark:text-gray-300">
            Places like Pakistan, Haiti, or underserved regions facing institutional gaps where formal banking is limited or mistrusted could benefit hugely. M-Pesa&apos;s model is also a powerful blueprint for building inclusive digital public infrastructure from the ground up.
          </p>
        </>
      );
    default:
      return <p className="text-gray-700 dark:text-gray-200">(Full post content will go here.)</p>;
  }
}

const PostModal: React.FC<PostModalProps> = ({ postKey, onClose }) => {
  return (
    <div className="fixed inset-0 backdrop-blur-sm bg-black/10 z-40 flex items-center justify-center">
      <div className="bg-white dark:bg-gray-900 p-6 rounded-xl shadow-lg z-50 relative max-w-2xl w-full mx-4 pt-2 max-h-[90vh] overflow-y-auto">
        <button
          className="absolute top-2 left-2 text-3xl text-black hover:text-accent dark:hover:text-accent focus:outline-none"
          onClick={onClose}
          aria-label="Close modal"
        >
          &times;
        </button>
        {getPostContent(postKey)}
      </div>
    </div>
  );
};

export default PostModal; 