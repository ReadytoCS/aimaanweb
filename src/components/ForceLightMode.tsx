"use client";

import { useEffect } from "react";

export default function ForceLightMode() {
  useEffect(() => {
    const root = document.documentElement;
    const body = document.body;

    // Remove Tailwind dark mode trigger class if present
    root.classList.remove("dark");
    body?.classList.remove("dark");

    // Remove common theme attributes
    root.removeAttribute("data-theme");
    body?.removeAttribute("data-theme");

    // Clear common persisted theme keys
    try {
      localStorage.removeItem("theme");
      localStorage.removeItem("next-theme");
      localStorage.removeItem("color-theme");
    } catch {
      // ignore
    }
  }, []);

  return null;
} 