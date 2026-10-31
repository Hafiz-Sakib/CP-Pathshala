import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { VitePWA } from "vite-plugin-pwa";

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: "autoUpdate",
      includeAssets: ["icon.svg", "favicon-32.png", "apple-touch-icon.png"],
      workbox: { globPatterns: ["**/*.{js,css,html,svg,png,woff2,json}"], maximumFileSizeToCacheInBytes: 5 * 1024 * 1024 },
      manifest: {
        name: "সি++ শিখি বাংলায়",
        short_name: "সি++ বাংলা",
        id: "/",
        scope: "/",
        categories: ["education", "books"],
        description: "Competitive Programming Beginner দের জন্য — STL, বিট, নাম্বার থিওরি, রিকার্সন ও গ্রাফ থিওরি বাংলায়",
        lang: "bn",
        theme_color: "#0a3631",
        background_color: "#0a3631",
        display: "standalone",
        start_url: "/",
        icons: [
          { src: "icon-192.png", sizes: "192x192", type: "image/png" },
          { src: "icon-512.png", sizes: "512x512", type: "image/png" },
          { src: "icon-maskable-192.png", sizes: "192x192", type: "image/png", purpose: "maskable" },
          { src: "icon-maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
          { src: "icon.svg", sizes: "any", type: "image/svg+xml", purpose: "any" }
        ],
        shortcuts: [
          { name: "STL", url: "/?tab=stl" },
          { name: "বিটের মজা", url: "/?tab=bits" },
          { name: "নাম্বার থিওরি", url: "/?tab=nt" },
          { name: "রিকার্সন ও DP", url: "/?tab=rec" },
          { name: "গ্রাফ থিওরি", url: "/?tab=graph" }
        ]
      }
    })
  ]
});
