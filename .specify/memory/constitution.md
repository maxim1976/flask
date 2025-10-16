<!--
═══════════════════════════════════════════════════════════════════════════
SYNC IMPACT REPORT
═══════════════════════════════════════════════════════════════════════════
Version Change: Initial → 1.0.0
Constitution Type: Static Web App

Modified Principles:
  • NEW: I. Component-First Architecture
  • NEW: II. Static-First Approach
  • NEW: III. Performance Budget (NON-NEGOTIABLE)
  • NEW: IV. Accessibility Standards
  • NEW: V. Build Optimization

Added Sections:
  • Core Principles (5 principles defined)
  • Deployment & Hosting
  • Development Workflow
  • Governance

Removed Sections: None (initial creation)

Templates Status:
  ✅ plan-template.md - Compatible (Constitution Check section will validate principles)
  ✅ spec-template.md - Compatible (Requirements section aligns with principles)
  ✅ tasks-template.md - Compatible (Task structure supports component-based development)

Follow-up TODOs: None

Rationale for v1.0.0:
  - Initial constitution ratification for static web app project
  - Establishes foundational governance for HTML/CSS/JS development
  - Defines non-negotiable performance and accessibility requirements
═══════════════════════════════════════════════════════════════════════════
-->

# Static Web App Constitution

## Core Principles

### I. Component-First Architecture

All UI elements MUST be developed as reusable, self-contained components with clear responsibilities.

**Rules**:
- Each component lives in its own directory with HTML, CSS, and JS co-located
- Components MUST be independently demonstrable (via example/demo page)
- Component APIs (props, events, styling hooks) MUST be documented before implementation
- No global CSS that affects component internals (components own their styles)
- Component dependencies MUST be explicitly declared and minimized

**Rationale**: Component isolation enables independent development, testing, and reuse. Co-location reduces cognitive load. Clear APIs prevent coupling and enable safe refactoring.

### II. Static-First Approach

Default to static HTML generation; dynamic features MUST justify their necessity and weight.

**Rules**:
- Content MUST be pre-rendered to HTML at build time whenever possible
- Client-side JavaScript MUST be progressive enhancement only (site functional without JS)
- Any dynamic data loading MUST have static fallback content
- Third-party scripts MUST be evaluated for necessity and deferred/async loaded
- No client-side rendering of initial page content (SSG over CSR)

**Rationale**: Static HTML ensures maximum performance, accessibility, SEO, and resilience. Progressive enhancement maintains functionality for all users regardless of JavaScript support or network conditions.

### III. Performance Budget (NON-NEGOTIABLE)

All pages MUST meet strict performance criteria measured on representative devices.

**Rules**:
- Initial HTML MUST be < 50KB gzipped
- Total page weight (HTML + CSS + JS + critical assets) MUST be < 500KB
- First Contentful Paint (FCP) MUST be < 1.5s on 3G networks
- Largest Contentful Paint (LCP) MUST be < 2.5s
- Cumulative Layout Shift (CLS) MUST be < 0.1
- Time to Interactive (TTI) MUST be < 3.5s
- All images MUST be optimized and served in modern formats (WebP/AVIF with fallbacks)
- Critical CSS MUST be inlined; non-critical CSS MUST be deferred

**Rationale**: Performance is a feature and an accessibility concern. Strict budgets prevent degradation over time. Metrics are based on real-world user expectations and Core Web Vitals standards.

### IV. Accessibility Standards

All components and pages MUST meet WCAG 2.1 Level AA compliance minimum.

**Rules**:
- Semantic HTML MUST be used (proper heading hierarchy, landmarks, lists)
- All interactive elements MUST be keyboard accessible (tab order, focus indicators)
- Color contrast MUST meet 4.5:1 ratio for normal text, 3:1 for large text
- All images MUST have descriptive alt text; decorative images MUST have empty alt
- Forms MUST have associated labels and clear error messages
- ARIA attributes MUST be used only when semantic HTML insufficient
- Pages MUST be tested with screen readers (NVDA/JAWS on Windows, VoiceOver on Mac/iOS)

**Rationale**: Accessibility is a legal requirement and moral imperative. Designing for accessibility improves usability for all users. Semantic HTML provides accessibility by default.

### V. Build Optimization

Build processes MUST automate quality checks and optimize output for production.

**Rules**:
- Build MUST fail on HTML validation errors (W3C validator)
- Build MUST fail on accessibility violations (automated axe-core checks)
- Build MUST fail if performance budget exceeded (Lighthouse CI)
- CSS MUST be purged of unused selectors and minified
- JavaScript MUST be bundled, tree-shaken, and minified
- Images MUST be automatically optimized and responsive sizes generated
- Build output MUST include integrity hashes for subresource integrity (SRI)
- Build MUST generate sitemap.xml and robots.txt

**Rationale**: Automated quality gates prevent regressions. Build-time optimization removes manual steps and ensures consistency. Production builds MUST be deployment-ready with no manual intervention.

## Deployment & Hosting

**Static Hosting Requirements**:
- MUST use CDN for global distribution and caching
- MUST serve all assets over HTTPS only
- MUST set appropriate cache headers (immutable for hashed assets, short-lived for HTML)
- MUST implement proper 404 handling and redirects
- SHOULD use HTTP/2 or HTTP/3 for multiplexing
- SHOULD implement security headers (CSP, X-Frame-Options, etc.)

**Deployment Process**:
- All deployments MUST pass build validation (performance, accessibility, HTML validation)
- Preview deployments MUST be generated for all pull requests
- Production deployments MUST be atomic (no partial updates)
- Rollback capability MUST be available (previous version accessible)

## Development Workflow

**Code Quality Gates**:
- HTML MUST validate against W3C standards (no errors, warnings acceptable with justification)
- CSS MUST pass linting (Stylelint with standard config)
- JavaScript MUST pass linting (ESLint with standard config) and type checking (if TypeScript used)
- All PRs MUST include before/after Lighthouse scores for affected pages
- All new components MUST include usage documentation and demo page

**Review Requirements**:
- UI changes MUST include screenshots/videos in PR description
- Accessibility changes MUST include screen reader testing notes
- Performance-sensitive changes MUST include bundle size comparison
- Breaking changes to component APIs MUST document migration path

**Testing Strategy** (if tests explicitly requested):
- Visual regression tests for critical user journeys
- Accessibility automated tests (axe-core) for all components
- Performance regression tests (Lighthouse CI) on key pages
- Manual cross-browser testing on latest 2 versions (Chrome, Firefox, Safari, Edge)
- Manual mobile testing on iOS and Android

## Governance

This constitution supersedes all other development practices and guidelines. Any deviation from core principles MUST be documented with clear justification in the implementation plan's Complexity Tracking section.

**Amendment Process**:
- Amendments require documentation in `.specify/memory/constitution.md`
- Version MUST be incremented following semantic versioning
- All affected templates and documentation MUST be updated to reflect changes
- Amendment rationale MUST be captured in Sync Impact Report

**Compliance Verification**:
- All PRs and code reviews MUST verify compliance with core principles
- Build system MUST enforce non-negotiable requirements (performance budgets, accessibility minimums)
- Quarterly audits SHOULD review adherence to static-first and component-first principles
- Any justified complexity MUST be re-evaluated quarterly for simplification opportunities

**Runtime Development Guidance**:
For detailed development workflows, refer to template files in `.specify/templates/` and command prompts in `.github/prompts/speckit.*.prompt.md`.

**Version**: 1.0.0 | **Ratified**: 2025-10-15 | **Last Amended**: 2025-10-15