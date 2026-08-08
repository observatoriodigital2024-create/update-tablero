const repository = process.env.GITHUB_REPOSITORY?.split("/")[1];
const base = process.env.GITHUB_ACTIONS && repository ? `/${repository}/` : "/";

export default {
  root: "src",
  output: "dist",
  title: "Plan anual OMD 2026–2027",
  base,
  theme: "light",
  pages: [],
  footer: false
};
