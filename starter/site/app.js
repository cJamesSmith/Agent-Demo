// 学生起点：请让 Claude Code 从 inputs/ 提取虚构数据并实现交互。

const markets = [];
const scenarios = {};

function normalizeMetric() {
  // TODO: 根据 data-dictionary.md 实现正向/反向 min-max 归一化。
}

function calculateScores() {
  // TODO: 根据五个维度和当前权重计算排名。
}

function rebalanceWeights() {
  // TODO: 一个滑块变化后，按比例调整其他维度并保持总和 100%。
}

function renderDashboard() {
  // TODO: 同步更新推荐、排名、解释、风险和来源。
}

function init() {
  // TODO: 绑定情景按钮、滑块和初始渲染。
}

document.addEventListener("DOMContentLoaded", init);
