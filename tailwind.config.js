export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      fontFamily: { sans: ["Hind Siliguri", "system-ui", "sans-serif"], mono: ["ui-monospace", "Menlo", "Consolas", "monospace"] },
      colors: { brand: { ink: "#0a3631", green: "#00694d", red: "#c8283a" } },
      keyframes: {
        "fade-up": { from: { opacity: 0, transform: "translateY(14px)" }, to: { opacity: 1, transform: "none" } },
        "fade-in": { from: { opacity: 0 }, to: { opacity: 1 } },
        "slide-down": { from: { opacity: 0, transform: "translateY(-8px)" }, to: { opacity: 1, transform: "none" } },
        "pop-in": { from: { opacity: 0, transform: "scale(.92)" }, to: { opacity: 1, transform: "none" } }
      },
      animation: {
        "fade-up": "fade-up .5s ease both",
        "fade-in": "fade-in .35s ease both",
        "slide-down": "slide-down .2s ease both",
        "pop-in": "pop-in .25s ease both"
      }
    }
  },
  plugins: []
};
