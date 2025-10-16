# Implementation Plan: Hualien Breakfast Restaurant Landing Page

**Branch**: `001-i-need-a` | **Date**: 2025-10-15 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-i-need-a/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create a static landing page for a traditional Taiwanese breakfast restaurant in Hualien using Flask as the web framework. The page will display bilingual content (Traditional Chinese and English), showcase menu items with prices in NT$, and provide restaurant information including location and opening hours. The design follows a traditional aesthetic with Tailwind CSS, featuring an amber/brown color scheme, Noto Sans TC font, and responsive card-based layout.

## Technical Context

**Language/Version**: Python 3.11+  
**Primary Dependencies**: Flask 3.0+, Tailwind CSS (CDN), Jinja2 (templating)  
**Storage**: Static JSON file for menu data (no database required for static content)  
**Testing**: pytest (for Flask routes), Lighthouse CI (performance), axe-core (accessibility)  
**Target Platform**: Web browsers (Chrome, Firefox, Safari, Edge - latest 2 versions), mobile-responsive (320px to 1920px)  
**Project Type**: Web application (single-page static site served via Flask)  
**Performance Goals**: < 3s page load, < 1.5s FCP, < 2.5s LCP, < 0.1 CLS, < 3.5s TTI  
**Constraints**: < 50KB HTML gzipped, < 500KB total page weight, WCAG 2.1 Level AA compliance, no JavaScript required for core functionality  
**Scale/Scope**: Single landing page, ~30-40 menu items, bilingual content, static content updates via code deployment

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### I. Component-First Architecture ✅ PASS

**Requirement**: All UI elements MUST be developed as reusable, self-contained components with clear responsibilities.

**Compliance**: 
- Landing page will use component-based structure (Header, Hero, Menu, Footer components)
- Each component will be a Jinja2 template partial with co-located styles via Tailwind classes
- Components are independently demonstrable (can be rendered in isolation)
- No global CSS affecting component internals (Tailwind utility classes are scoped)

### II. Static-First Approach ✅ PASS

**Requirement**: Default to static HTML generation; dynamic features MUST justify their necessity and weight.

**Compliance**:
- Content pre-rendered to HTML via Flask/Jinja2 at request time (server-side rendering)
- No client-side JavaScript required for core functionality (menu display, contact info viewing)
- Static fallback content available (all content visible without JS)
- Tailwind CSS loaded via CDN but core content remains accessible if CSS fails
- Progressive enhancement only (smooth scrolling is enhancement, not requirement)

### III. Performance Budget (NON-NEGOTIABLE) ✅ PASS

**Requirement**: All pages MUST meet strict performance criteria.

**Compliance**:
- Initial HTML target: < 50KB gzipped (bilingual content + menu inline)
- Total page weight: < 500KB (HTML + Tailwind CSS CDN + hero image optimized)
- FCP < 1.5s: Static HTML renders immediately, critical CSS inlined
- LCP < 2.5s: Hero image lazy-loaded with proper sizing
- CLS < 0.1: Fixed layouts, no dynamic content shifts, image dimensions specified
- TTI < 3.5s: Minimal JS (only for smooth scroll enhancement if added)
- Images: WebP format with JPEG fallback, responsive srcset
- Critical CSS: Tailwind purged to only used classes

**Validation**: Lighthouse CI in build pipeline, performance budget enforced

### IV. Accessibility Standards ✅ PASS

**Requirement**: All components and pages MUST meet WCAG 2.1 Level AA compliance.

**Compliance**:
- Semantic HTML: `<header>`, `<main>`, `<footer>`, `<section>`, proper heading hierarchy (h1 → h2 → h3)
- Keyboard accessible: All navigation links tabbable, focus indicators visible
- Color contrast: Amber/brown scheme tested for 4.5:1 ratio on normal text, 3:1 on large text
- Images: Alt text for hero image, decorative images with empty alt
- Bilingual content: Clear language switching via `lang` attribute on elements
- ARIA: Only used where semantic HTML insufficient (none required for this static page)
- Screen reader testing: Required for acceptance

**Validation**: axe-core automated tests in build pipeline

### V. Build Optimization ✅ PASS

**Requirement**: Build processes MUST automate quality checks and optimize output.

**Compliance**:
- HTML validation: W3C validator check in CI/CD
- Accessibility: axe-core automated checks (must pass for deployment)
- Performance budget: Lighthouse CI (must meet thresholds)
- CSS: Tailwind purged of unused classes, minified via CDN
- Images: Optimized at build time (WebP conversion, responsive sizes)
- No JavaScript bundling needed (minimal/no JS)
- Sitemap.xml and robots.txt generated

**Build Pipeline**: GitHub Actions or similar CI/CD with quality gates

### Summary

**Status**: ✅ ALL GATES PASS - No constitution violations. Proceeding to Phase 0 research.

## Project Structure

### Documentation (this feature)

```
specs/001-i-need-a/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
│   └── api.md          # Flask route contracts
├── checklists/
│   └── requirements.md  # Specification quality checklist
└── spec.md             # Feature specification
```

### Source Code (repository root)

```
flask/
├── app.py                      # Flask application entry point
├── templates/                  # Jinja2 templates
│   ├── base.html              # Base template with head, meta tags
│   ├── index.html             # Landing page template
│   └── components/            # Reusable component partials
│       ├── header.html        # Restaurant header/navigation
│       ├── hero.html          # Hero section with image
│       ├── menu.html          # Menu display component
│       └── footer.html        # Footer with contact info
├── static/                     # Static assets
│   ├── images/                # Restaurant and food images
│   │   └── hero.jpg           # Hero section image
│   ├── css/                   # Custom CSS (if needed beyond Tailwind)
│   │   └── custom.css         # Additional styles
│   └── data/                  # Static data files
│       └── menu.json          # Menu items data
├── tests/                      # Test files
│   ├── test_routes.py         # Flask route tests
│   ├── test_accessibility.py  # Accessibility tests (axe-core)
│   └── test_performance.py    # Performance tests (Lighthouse)
├── requirements.txt            # Python dependencies
├── .github/
│   └── workflows/
│       └── ci.yml             # CI/CD pipeline (quality gates)
└── README.md                   # Project documentation
```

**Structure Decision**: Web application structure with Flask serving static HTML. Using Jinja2 templating for component-based architecture. Static data in JSON format for menu items (easily editable without code changes for future menu updates). Components separated into partials for reusability and independent testing.

## Complexity Tracking

*No constitution violations - this section is empty.*
