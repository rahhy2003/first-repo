# Build Plan

We will iterate with small commits. If anything is ambiguous, we pick a safe default and proceed.

## Milestones
1. Repo scaffolding (docs, license, formatting, Node/PNPM setup)
2. Backend API scaffold (TypeScript, Fastify)
3. Database setup (SQLite via Prisma for simplicity)
4. Basic products CRUD
5. Frontend scaffold (Vite + React + TypeScript)
6. Basic product list/detail UI
7. Integration: frontend ↔ backend
8. Auth (email/password, session cookies)
9. Cart & checkout flow (mock payments)
10. Tests, linting, CI

## Current Step
Step 1: Initialize repository scaffolding with package manager and tooling defaults.

### Step 1 Tasks
- Initialize Node project with PNPM (fallback: NPM)
- Add editor configuration and basic linting/formatting (Prettier + ESLint)
- Add TypeScript config
- Add workspace structure

### Acceptance
- `pnpm install` or `npm install` succeeds
- `pnpm lint` and `pnpm format` runnable (even if no files yet)


