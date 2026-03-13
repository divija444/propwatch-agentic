# Multi-Agent Real Estate Analytics — Folder Structure

Overview of the repository layout for the agentic real estate analytics system.

## Root

| Path | Purpose |
|------|--------|
| `app.py` | Application entrypoint / orchestration runner |
| `requirements.txt` | Python dependencies |

---

## `agents/`

**Specialized agents** in the multi-agent graph (LangGraph/agent framework).

| File / Role | Purpose |
|-------------|--------|
| `controller.py` | Top-level controller / router |
| `graph.py` | Agent graph definition and wiring |
| `state.py` | Shared agent state schema |
| `constitution.py` | Guardrails and policy constraints |
| `affordability.py` | Affordability analysis agent |
| `fairness.py` | Fairness / equity analysis agent |
| `drift.py` | Data/model drift monitoring agent |
| `spatial.py` | Geospatial analysis agent |
| `hotspot.py` | Hotspot / trend detection agent |
| `inventory.py` | Inventory / listing analysis agent |
| `insight.py` | Insight synthesis and reporting agent |

Add new agents here and register them in `graph.py`.

---

## `config/`

**Configuration** for agents, pipelines, and environment.

- Agent prompts, model settings, tool bindings
- Feature flags, environment-specific settings
- Optional: YAML/JSON config files loaded at runtime

---

## `analytics/`

**Analytics logic** used by agents and pipelines (not agent definitions).

| Subfolder | Purpose |
|-----------|--------|
| `metrics/` | Computed metrics (e.g. affordability indices, equity metrics) |
| `models/` | Valuation, forecasting, or other ML/statistical models |
| `pipelines/` | ETL or analysis pipelines (data → metrics → outputs) |

---

## `tools/`

**Shared tools** callable by agents (APIs, geo, valuation).

| Subfolder | Purpose |
|-----------|--------|
| `geo/` | Geocoding, boundaries, spatial queries |
| `valuation/` | Valuation helpers, AVM-related logic |

Add other tool modules (e.g. `mls/`, `demographics/`) as needed.

---

## `utils/`

**General utilities** (logging, run tracking, helpers).

- e.g. `runlog.py` for run logging
- Cross-cutting helpers used by agents and pipelines

---

## `data/`

**Data layout** for inputs and outputs.

| Subfolder | Purpose |
|-----------|--------|
| `raw/` | Ingested or downloaded raw data (immutable) |
| `processed/` | Cleaned, normalized, or feature-engineered datasets |
| `outputs/` | Reports, exports, and generated artifacts |

---

## `runs/`

**Runtime artifacts** from agent runs and pipelines.

| Subfolder | Purpose |
|-----------|--------|
| `artifacts/` | Saved outputs, cached results, serialized state |
| `logs/` | Run logs, traces, debug output |

---

## `api/`

**Optional API layer** (REST or internal) for:

- Triggering runs
- Querying results
- Serving metrics or reports

---

## `storage/`

**Persistence** for state, cache, or DB access.

- DB clients, migrations, or schema definitions
- Optional: vector store or cache for agent context

---

## `tests/`

**Tests** for agents, tools, and pipelines.

| Subfolder | Purpose |
|-----------|--------|
| `unit/` | Unit tests for agents, tools, metrics |
| `integration/` | Integration tests (graph, pipelines, APIs) |

---

## `scripts/`

**CLI and one-off scripts.**

- Data ingestion, backfills
- Local run scripts
- Deployment or maintenance helpers

---

## `docs/`

**Documentation.**

- `architecture.md` — system and agent architecture
- `STRUCTURE.md` — this file

---

## Quick reference (tree)

```
propwatch-agentic/
├── app.py
├── requirements.txt
├── README.md
├── agents/           # Multi-agent definitions (graph, state, specialist agents)
├── config/           # Agent & system configuration
├── analytics/        # Metrics, models, pipelines
│   ├── metrics/
│   ├── models/
│   └── pipelines/
├── tools/            # Shared agent tools (geo, valuation, …)
│   ├── geo/
│   └── valuation/
├── utils/            # Cross-cutting utilities
├── data/
│   ├── raw/
│   ├── processed/
│   └── outputs/
├── runs/
│   ├── artifacts/
│   └── logs/
├── api/              # Optional API layer
├── storage/          # Persistence / DB
├── tests/
│   ├── unit/
│   └── integration/
├── scripts/          # CLI and one-off scripts
└── docs/
```
