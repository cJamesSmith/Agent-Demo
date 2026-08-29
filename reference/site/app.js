const markets = [
  {
    name: "Vietnam",
    size: 720,
    growth: 24,
    cac: 18,
    margin: 62,
    competition: 58,
    regulation: 55,
    execution: 48,
    confidence: 84,
    summary: "Fast growth and low estimated acquisition cost",
    counter: "Market education and bilingual customer-success investment may push actual acquisition costs above the research estimate."
  },
  {
    name: "Indonesia",
    size: 1350,
    growth: 19,
    cac: 27,
    margin: 57,
    competition: 72,
    regulation: 68,
    execution: 64,
    confidence: 76,
    summary: "Largest scale and broad demand",
    counter: "Geographic dispersion, integration work, and channel requirements may significantly lengthen the payback period."
  },
  {
    name: "Thailand",
    size: 610,
    growth: 12,
    cac: 22,
    margin: 68,
    competition: 61,
    regulation: 39,
    execution: 35,
    confidence: 90,
    summary: "High margin and more predictable execution",
    counter: "Slower market growth and entrenched vendors require clearer product differentiation."
  }
];

const dimensions = [
  { key: "growthPotential", label: "Growth Potential" },
  { key: "profitability", label: "Profitability" },
  { key: "competitionEnvironment", label: "Competitive Environment" },
  { key: "regulatorySafety", label: "Regulatory Risk" },
  { key: "executionFeasibility", label: "Execution Feasibility" }
];

const scenarios = {
  growth: { label: "Growth-first", weights: [40, 20, 15, 10, 15] },
  profit: { label: "Profit-first", weights: [15, 40, 10, 15, 20] },
  risk: { label: "Risk-first", weights: [10, 20, 10, 35, 25] },
  cashflow: { label: "Cash-flow-first", weights: [10, 35, 10, 20, 25] }
};

let activeScenario = "growth";
let currentWeights = [...scenarios[activeScenario].weights];

function normalize(values, reverse = false) {
  const min = Math.min(...values);
  const max = Math.max(...values);
  if (max === min) return values.map(() => 50);
  return values.map((value) => {
    const normalized = reverse
      ? ((max - value) / (max - min)) * 100
      : ((value - min) / (max - min)) * 100;
    return Number(normalized.toFixed(1));
  });
}

function buildDimensionScores() {
  const size = normalize(markets.map((market) => market.size));
  const growth = normalize(markets.map((market) => market.growth));
  const cac = normalize(markets.map((market) => market.cac), true);
  const margin = normalize(markets.map((market) => market.margin));
  const competition = normalize(markets.map((market) => market.competition), true);
  const regulation = normalize(markets.map((market) => market.regulation), true);
  const execution = normalize(markets.map((market) => market.execution), true);

  return markets.map((market, index) => ({
    ...market,
    dimensionScores: {
      growthPotential: (size[index] + growth[index]) / 2,
      profitability: (cac[index] + margin[index]) / 2,
      competitionEnvironment: competition[index],
      regulatorySafety: regulation[index],
      executionFeasibility: execution[index]
    }
  }));
}

const scoredMarkets = buildDimensionScores();

function calculateRanking() {
  return scoredMarkets
    .map((market) => {
      const score = dimensions.reduce((sum, dimension, index) => {
        return sum + market.dimensionScores[dimension.key] * (currentWeights[index] / 100);
      }, 0);
      return { ...market, score: Number(score.toFixed(1)) };
    })
    .sort((a, b) => b.score - a.score);
}

function strongestAdvantages(leader, runnerUp) {
  return dimensions
    .map((dimension) => ({
      label: dimension.label,
      gap: leader.dimensionScores[dimension.key] - runnerUp.dimensionScores[dimension.key],
      score: leader.dimensionScores[dimension.key]
    }))
    .filter((item) => item.gap > 0)
    .sort((a, b) => b.gap - a.gap)
    .slice(0, 3);
}

function recommendationSentence(leader, advantages) {
  const advantageText = advantages.slice(0, 2).map((item) => item.label).join(" and ");
  if (activeScenario === "cashflow") {
    return `${leader.name} better meets cash-flow predictability requirements on ${advantageText || "the current weights"}; compared with the growth scenario, the model places more emphasis on profitability, regulation, and execution.`;
  }
  return `${leader.name} offers the best balance across ${advantageText || "the currently weighted dimensions"} in this scenario.`;
}

function renderSummary(ranking) {
  const leader = ranking[0];
  const runnerUp = ranking[1];
  const gap = Number((leader.score - runnerUp.score).toFixed(1));
  const advantages = strongestAdvantages(leader, runnerUp);
  const sensitive = gap < 5 || leader.confidence < 80;

  document.querySelector("#active-scenario-label").textContent = scenarios[activeScenario]?.label || "Custom weights";
  document.querySelector("#recommended-market").textContent = leader.name;
  document.querySelector("#recommended-score").textContent = leader.score.toFixed(1);
  document.querySelector("#recommendation-copy").textContent = recommendationSentence(leader, advantages);
  document.querySelector("#score-gap").textContent = `${gap.toFixed(1)} points ahead of second place`;
  document.querySelector("#counter-argument").textContent = leader.counter;

  const badge = document.querySelector("#sensitivity-badge");
  badge.textContent = sensitive ? "Sensitive conclusion" : "Relatively robust";
  badge.className = `status ${sensitive ? "sensitive" : "stable"}`;

  const reasons = advantages.length
    ? advantages.map((item) => `${item.label} leads second place by ${item.gap.toFixed(1)} points.`)
    : ["Performance is similar across the current dimensions; gather more evidence before making an irreversible investment."];
  document.querySelector("#top-reasons").innerHTML = reasons.map((reason) => `<li>${reason}</li>`).join("");
}

function renderMarketCards(ranking) {
  const cards = ranking.map((market, index) => {
    const strongest = dimensions
      .map((dimension) => ({ label: dimension.label, score: market.dimensionScores[dimension.key] }))
      .sort((a, b) => b.score - a.score)[0];

    return `
      <article class="market-card ${index === 0 ? "is-first" : ""}">
        <div class="market-rank"><span>RANK 0${index + 1}</span><strong>${market.score.toFixed(1)}</strong></div>
        <h3>${market.name}</h3>
        <p>${market.summary}</p>
        <div class="score-track" aria-hidden="true"><div class="score-fill" style="width:${market.score}%"></div></div>
        <div class="dimension-mini"><span>Strongest dimension</span><strong>${strongest.label} ${strongest.score.toFixed(0)}</strong></div>
        <div class="dimension-mini"><span>Data confidence</span><strong>${market.confidence}%</strong></div>
      </article>`;
  });
  document.querySelector("#market-cards").innerHTML = cards.join("");
}

function renderMetrics() {
  document.querySelector("#metrics-body").innerHTML = markets.map((market) => `
    <tr>
      <th scope="row">${market.name}</th>
      <td>$${market.size}M</td>
      <td>${market.growth}%</td>
      <td>$${market.cac}</td>
      <td>${market.margin}%</td>
      <td>${market.competition}</td>
      <td>${market.regulation}</td>
      <td>${market.confidence}%</td>
    </tr>`).join("");
}

function renderWeightControls() {
  document.querySelector("#weights-grid").innerHTML = dimensions.map((dimension, index) => `
    <div class="weight-control">
      <label for="weight-${dimension.key}">
        <span>${dimension.label}</span>
        <output id="output-${dimension.key}" for="weight-${dimension.key}">${currentWeights[index]}%</output>
      </label>
      <input id="weight-${dimension.key}" data-index="${index}" type="range" min="0" max="80" step="1" value="${currentWeights[index]}" aria-label="${dimension.label} weight">
    </div>`).join("");

  document.querySelectorAll(".weight-control input").forEach((input) => {
    input.addEventListener("input", handleWeightChange);
  });
}

function rebalanceWeights(changedIndex, requestedValue) {
  const value = Math.max(0, Math.min(80, Number(requestedValue)));
  const remaining = 100 - value;
  const otherIndexes = currentWeights.map((_, index) => index).filter((index) => index !== changedIndex);
  const previousOtherTotal = otherIndexes.reduce((sum, index) => sum + currentWeights[index], 0);
  const next = [...currentWeights];
  next[changedIndex] = value;

  if (previousOtherTotal === 0) {
    const base = Math.floor(remaining / otherIndexes.length);
    otherIndexes.forEach((index) => { next[index] = base; });
  } else {
    otherIndexes.forEach((index) => {
      next[index] = Math.round((currentWeights[index] / previousOtherTotal) * remaining);
    });
  }

  const total = next.reduce((sum, weight) => sum + weight, 0);
  if (total !== 100) {
    const largestOther = otherIndexes.reduce((best, index) => next[index] > next[best] ? index : best, otherIndexes[0]);
    next[largestOther] += 100 - total;
  }
  return next;
}

function handleWeightChange(event) {
  const index = Number(event.currentTarget.dataset.index);
  currentWeights = rebalanceWeights(index, event.currentTarget.value);
  activeScenario = "custom";
  updateScenarioButtons();
  updateWeightControls();
  renderDashboard();
}

function updateWeightControls() {
  dimensions.forEach((dimension, index) => {
    const input = document.querySelector(`#weight-${dimension.key}`);
    const output = document.querySelector(`#output-${dimension.key}`);
    input.value = currentWeights[index];
    output.value = `${currentWeights[index]}%`;
    output.textContent = `${currentWeights[index]}%`;
  });
  document.querySelector("#weight-total").textContent = `${currentWeights.reduce((sum, weight) => sum + weight, 0)}%`;
}

function updateScenarioButtons() {
  document.querySelectorAll(".scenario-button").forEach((button) => {
    const isActive = button.dataset.scenario === activeScenario;
    button.classList.toggle("is-active", isActive);
    button.setAttribute("aria-pressed", String(isActive));
  });
}

function selectScenario(scenarioKey) {
  activeScenario = scenarioKey;
  currentWeights = [...scenarios[scenarioKey].weights];
  updateScenarioButtons();
  updateWeightControls();
  renderDashboard();
}

function renderDashboard() {
  const ranking = calculateRanking();
  renderSummary(ranking);
  renderMarketCards(ranking);
}

function init() {
  renderMetrics();
  renderWeightControls();
  document.querySelectorAll(".scenario-button").forEach((button) => {
    button.addEventListener("click", () => selectScenario(button.dataset.scenario));
  });
  renderDashboard();
}

document.addEventListener("DOMContentLoaded", init);
