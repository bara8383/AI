# Codex Subagents for AI Research and Model Improvement

This directory defines project-scoped Codex custom agents for an AI research and development workflow. The goal is not ordinary product delivery; it is a repeatable loop for proposing hypotheses, reviewing prior work, designing experiments, implementing only accepted plans, analyzing results, checking research quality, and packaging decisions for human review.

The files follow the Codex custom-agent convention: project-scoped custom agents live under `.codex/agents/`, and each TOML file defines a single agent with `name`, `description`, and `developer_instructions`.

## Design influences

This configuration is intentionally minimal and research-oriented. It uses the following design ideas from established agent and skill ecosystems without copying their content:

- **Narrow, opinionated agents:** Codex official guidance recommends focused custom agents with clear jobs, appropriate tool scope, and drift-prevention instructions.
- **Phase-based delegation:** Community subagent collections such as `VoltAgent/awesome-codex-subagents` and `VoltAgent/awesome-claude-code-subagents` organize agents around specialized responsibilities rather than one generic assistant.
- **Verification and scope discipline:** Agent-skill guidance from Addy Osmani emphasizes concrete evidence, quality gates, and touching only what was requested.
- **Decision-packaging for humans:** Product and PM skill libraries such as `product-on-purpose/pm-skills` emphasize structured outputs, decision points, and explicit reviewer questions.

## Human and Codex responsibilities

### Human responsibilities

Humans remain accountable for research direction and interpretation:

- Review research direction.
- Review hypothesis validity.
- Review experiment design.
- Review result interpretation.
- Review the next direction.
- Decide whether to adopt, reject, hold, rerun, or redesign an experiment.

### Codex responsibilities

Codex agents do the operational research work:

- Propose hypotheses.
- Survey prior work and existing implementations.
- Design experiments.
- Implement accepted experiments.
- Propose validation commands.
- Analyze results.
- Review reproducibility, quality, and likely mistakes.
- Propose next hypotheses or improvements.

Codex must not finalize major research-direction changes, metric changes, or baseline changes without human review.

## AI research development flow

1. Codex: `research-hypothesis-proposer` proposes hypotheses.
2. Codex: `literature-reviewer` summarizes related research, existing methods, and reference implementations.
3. Codex: `experiment-designer` creates an experiment plan.
4. Human: review the hypotheses, evidence, and experiment design.
5. Codex: `model-implementer` implements only the accepted experiment.
6. Codex: `research-quality-reviewer` reviews implementation, experiment setup, and evaluation mistakes.
7. Codex: `experiment-analyzer` analyzes results.
8. Codex: `research-review-packager` prepares human review material.
9. Human: review results, interpretation, and next direction.
10. Codex: `research-hypothesis-proposer` proposes the next hypotheses.
11. Return to step 1.

## Agent responsibilities

| Agent | Primary responsibility | May edit code? | Human review gate |
| --- | --- | --- | --- |
| `research-hypothesis-proposer` | Produce Hypothesis A/B/C with rationale, risk, validation method, and failure interpretation. | No | Before experiment design or implementation |
| `literature-reviewer` | Research papers, official docs, reference implementations, and benchmarks; separate claims from evidence. | No | Before relying on uncertain or high-impact claims |
| `experiment-designer` | Turn an accepted hypothesis into a minimal reproducible experiment plan. | No | Before implementation |
| `model-implementer` | Implement only the accepted experiment plan with minimal reproducible changes. | Yes | Requires accepted hypothesis and experiment plan |
| `experiment-analyzer` | Analyze logs, metrics, artifacts, and whether the hypothesis is supported, refuted, or inconclusive. | No | Before deciding the next direction |
| `research-quality-reviewer` | Review bugs, data leakage, evaluation mistakes, reproducibility, numerical stability, performance, maintainability, and unintended behavior. | No | Before human research review |
| `research-review-packager` | Package the research decision brief for human reviewers. | No | Supports final human review |

## When to spawn each agent

- Spawn `research-hypothesis-proposer` when the project needs new research options or the previous result produced new unknowns.
- Spawn `literature-reviewer` when hypotheses depend on prior methods, external benchmarks, model behavior claims, or official API/framework details.
- Spawn `experiment-designer` after a human accepts or shortlists a hypothesis for validation.
- Spawn `model-implementer` only after the accepted experiment plan is explicit.
- Spawn `research-quality-reviewer` after implementation and before trusting results or asking for human research review.
- Spawn `experiment-analyzer` after experiment logs, metrics, or artifacts exist.
- Spawn `research-review-packager` when a human needs a concise decision package.

Parallel spawning is useful when the tasks are independent. For example, after hypotheses are proposed, `literature-reviewer` can inspect prior work while `experiment-designer` drafts a tentative plan, but implementation should wait for human review.

## Prompt examples

### Example 1: propose next research hypotheses

```text
Spawn research-hypothesis-proposer.
Analyze the current repository, recent experiments, known issues, and research direction.
Do not implement anything.
Return hypotheses as A/B/C options with background, expected effect, risk, validation method, and failure interpretation.
Wait for human review.
```

### Example 2: review prior research

```text
Spawn literature-reviewer.
Research related papers, official documentation, known implementations, and benchmarks relevant to the proposed hypotheses.
Separate claims from evidence.
Prefer primary sources.
Do not edit code.
```

### Example 3: design an experiment

```text
Spawn experiment-designer.
Design a minimal reproducible experiment for the accepted hypothesis.
Define metrics, baselines, datasets, parameters, logging, success criteria, and failure criteria.
Do not implement anything.
Wait for human review.
```

### Example 4: implement only the accepted experiment

```text
Spawn model-implementer.
Implement only the accepted experiment plan:

- <accepted experiment>

Do not implement rejected or deferred hypotheses.
Keep changes minimal and reproducible.
After implementation, summarize changed files and validation commands.
```

### Example 5: run research quality review

```text
Spawn research-quality-reviewer.
Review the latest implementation and experiment setup before human research review.
Focus on bugs, data leakage, evaluation mistakes, reproducibility, numerical instability, performance, maintainability, and unintended behavior.
Do not edit code.
Return findings by severity with evidence and recommended fixes.
```

### Example 6: analyze experiment results

```text
Spawn experiment-analyzer.
Analyze the experiment results and logs.
Determine whether the result supports, refutes, or fails to evaluate the hypothesis.
Avoid overclaiming.
Return interpretation, limitations, and recommended next experiments.
```

### Example 7: package for human review

```text
Spawn research-review-packager.
Prepare a research review package for a human reviewer.
Include hypothesis, experiment purpose, implementation changes, conditions, results, interpretation, limitations, unresolved issues, and review questions.
Do not edit code.
```

## Notes and guardrails

- Keep hypotheses and experiments small enough to review and reproduce.
- Treat human review as a required gate before implementation and before major research-direction changes.
- Separate observations, assumptions, interpretations, and decisions.
- Prefer primary sources for literature review and official documentation checks.
- Do not implement speculative, rejected, or deferred ideas.
- Do not change evaluation metrics, datasets, baselines, or success criteria after seeing results without labeling the change as a proposal for human review.
- Avoid style-only review comments unless they reveal a real validity, safety, or maintainability issue.

## Difference from product-development subagents

Product-development subagents often optimize for shipping features, fixing bugs, improving UX, or reducing delivery risk. These research subagents optimize for hypothesis quality, experimental validity, reproducibility, measured evidence, and human interpretation.

The central output is not a shipped feature. The central output is a reviewed research decision: adopt, reject, hold, rerun, redesign, or propose the next hypothesis.
