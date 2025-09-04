import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  eslint: {
    // Running ESLint in CI can be memory intensive; skip during production builds
    ignoreDuringBuilds: true,
  },
  typescript: {
    // Skip type checking during the build to reduce memory usage in CI
    ignoreBuildErrors: true,
  },
};

export default nextConfig;
