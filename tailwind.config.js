/** @type {import('tailwindcss').Config} */
const { nextui } = require("@nextui-org/react");
export default {
  content: [
    "./src/*.tsx",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    colors: {
      turquoise: "#7FB5B5",
      blue: "#89cff0",
      purple: "#ca9bf7",
      blue_green: "#9adedb",
    },
    extend: {},
  },
  plugins: [nextui()],
};
