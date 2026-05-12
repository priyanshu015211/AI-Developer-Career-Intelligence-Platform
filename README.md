# AI Developer Career Intelligence Platform

> An AI-powered platform that analyzes GitHub profiles to evaluate technical skills, project quality, and career readiness — built on real code, not self-reported resumes.

---

## What This Is

The AI Developer Career Intelligence Platform is a full-stack analytics product that reads a developer's GitHub activity and turns it into actionable career intelligence. Instead of asking developers to manually describe their skills, the platform extracts them automatically from repositories, commit history, tech stacks, and project quality — then uses AI to benchmark those skills against real job roles.

The end goal is simple: a developer should be able to paste their GitHub username and walk away knowing exactly where they stand, what they're missing, and what to build next.

---

## Core Features

### GitHub Analysis
- Full public profile and repository ingestion
- Automatic filtering of forked vs. original work
- Commit frequency and contribution streak tracking
- Repository categorization (web dev, ML, DevOps, systems, etc.)

### Skill Extraction
- Automatic tech stack detection from repository contents and topics
- Language breakdown weighted by project size and recency
- Framework and tool identification beyond just language names
- Skill grouping into domains (frontend, backend, data, infrastructure)

### AI-Powered Insights
- Plain-English summarization of what each repository does
- README and documentation quality scoring
- Project complexity and completeness evaluation
- Semantic analysis using embeddings to understand project intent

### Career Readiness
- Skill gap analysis mapped to specific job roles (Backend Developer, Frontend Developer, ML Engineer, and more)
- Career readiness score with breakdown by category
- Identification of missing skills with evidence from the profile
- Personalized recommendations: what to build, what to learn, what to document better

### Analytics Dashboard
- Interactive visualizations of skill distribution and activity
- Timeline of growth and contribution patterns
- Shareable profile cards for recruiters or portfolio use
- Side-by-side comparison against job role requirements

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Tailwind CSS |
| Backend | FastAPI (Python) |
| Database | PostgreSQL |
| AI / NLP | OpenAI API, embeddings, semantic analysis |
| Visualization | Recharts / Plotly |
| Data source | GitHub REST API v3 |
| Deployment | Vercel (frontend) + Render (backend) |

---

## Project Objective

This platform is built as a placement-focused AI project that brings together three disciplines:

- **Software Engineering** — a production-grade full-stack application with a real API, database, and authenticated user flows
- **Data Analytics** — extracting structured insight from unstructured GitHub activity
- **Artificial Intelligence** — using language models and embeddings to generate career intelligence that goes beyond what simple metrics can tell you

The output is not a resume formatter or a generic portfolio tool. It is a career intelligence engine that tells a developer something they could not figure out on their own just by looking at their own profile.

---

## Target Users

- **Developers** preparing for job applications who want an honest assessment of their profile
- **Students** building their first portfolio who want to know what skills are missing
- **Career switchers** moving into a new domain who need to identify gaps fast

---

## Status

This is the final product specification. Development follows a phased roadmap:

- **Phase 1 (Complete):** GitHub profile fetch, repo listing, language breakdown
- **Phase 2:** Skill extraction from repo contents, topics, and file structure
- **Phase 3:** Commit activity analysis, README quality scoring, documentation evaluation
- **Phase 4:** AI summarization, skill gap analysis, career readiness scoring
- **Phase 5:** Full dashboard, user accounts, shareable profiles, recruiter view

---

## License

Apache License 2.0
