import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { VitePWA } from "vite-plugin-pwa";

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: "autoUpdate",
      includeAssets: ["icon.svg"],
      manifest: {
        name: "সি++ শিখি বাংলায়",
        short_name: "সি++ বাংলা",
        description: "STL, বিটের মজা ও বেসিক নাম্বার থিওরি — বাংলায় টিউটোরিয়াল",
        lang: "bn",
        theme_color: "#0a3631",
        background_color: "#0a3631",
        display: "standalone",
        start_url: "/",
        icons: [
          { src: "icon-192.png", sizes: "192x192", type: "image/png" },
          { src: "icon-512.png", sizes: "512x512", type: "image/png" },
          { src: "icon-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" }
        ],
        shortcuts: [
          { name: "STL", url: "/?tab=stl" },
          { name: "বিটের মজা", url: "/?tab=bits" },
          { name: "নাম্বার থিওরি", url: "/?tab=nt" }
        ]
      }
    })
  ]
});
