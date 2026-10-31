import React from "react";
import ReactDOM from "react-dom/client";
import "@fontsource/hind-siliguri/400.css";
import "@fontsource/hind-siliguri/500.css";
import "@fontsource/hind-siliguri/600.css";
import "@fontsource/hind-siliguri/700.css";
import "./index.css";
import App from "./App.jsx";
import { registerSW } from "virtual:pwa-register";

registerSW({ immediate: true });
ReactDOM.createRoot(document.getElementById("root")).render(<App />);
