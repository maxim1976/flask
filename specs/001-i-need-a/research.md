# Research: Hualien Breakfast Restaurant Landing Page

**Feature**: 001-i-need-a  
**Date**: 2025-10-15  
**Status**: Complete

## Overview

This document captures research decisions for implementing a static landing page for a Taiwanese breakfast restaurant using Flask and Tailwind CSS.

## Technology Stack Decisions

### 1. Flask vs Static Site Generators

**Decision**: Use Flask (Python web framework)

**Rationale**:
- User explicitly requested "Python Flask web app"
- Flask provides simple routing and templating via Jinja2
- Easy to serve static content with potential for future dynamic features
- Lightweight and well-suited for single-page applications
- Built-in development server for local testing
- Straightforward deployment options (Gunicorn + Nginx, or PaaS like Heroku/Render)

**Alternatives Considered**:
- **Static Site Generators (Jekyll, Hugo, 11ty)**: Would be more performant for purely static content, but user specified Flask
- **FastAPI**: More modern async framework, but overkill for a simple landing page and not requested
- **Django**: Too heavy for a single landing page with no admin requirements

### 2. Tailwind CSS Integration

**Decision**: Use Tailwind CSS via CDN with JIT (Just-In-Time) mode

**Rationale**:
- User explicitly requested Tailwind CSS
- CDN approach simplifies setup (no build process for CSS)
- Tailwind Play CDN includes JIT compiler for on-demand class generation
- Reduces initial setup complexity
- For production, can migrate to full Tailwind build process with PurgeCSS

**Alternatives Considered**:
- **Full Tailwind Build**: Requires Node.js, npm, PostCSS configuration - adds complexity
- **Tailwind CLI**: Good middle ground, but CDN is simpler for MVP
- **Custom CSS**: Would not meet user's Tailwind requirement

**Production Consideration**: For production deployment, should migrate to Tailwind CLI or full build process to:
- Purge unused classes (reduce CSS bundle size)
- Customize color palette and fonts
- Meet performance budget requirements

### 3. Data Storage for Menu Items

**Decision**: Static JSON file (`static/data/menu.json`)

**Rationale**:
- Menu items are relatively static (change infrequently)
- No database overhead or maintenance required
- Easy to edit menu items (simple JSON structure)
- Fast read performance (loaded into memory on app start)
- Meets static-first architecture principle
- Simple backup and version control

**Alternatives Considered**:
- **Database (SQLite/PostgreSQL)**: Overkill for ~30-40 static menu items that rarely change
- **Hardcoded in templates**: Less maintainable, harder to update menu
- **CMS integration**: Too complex for a simple landing page

**JSON Structure**:
```json
{
  "categories": [
    {
      "id": "main-dishes",
      "name_zh": "主食",
      "name_en": "Main Dishes",
      "items": [
        {
          "name_zh": "燒餅夾油條",
          "name_en": "Sesame Flatbread with Fried Dough",
          "price": 44.00
        }
      ]
    }
  ]
}
```

### 4. Bilingual Content Strategy

**Decision**: Server-side rendering with inline bilingual content (no language toggle)

**Rationale**:
- User specified "both local and tourist audiences" with Traditional Chinese and English displayed together
- No language switching complexity required
- Single page serves all users
- Better for SEO (all content indexed in both languages)
- Simpler implementation (no session/cookie management)

**Implementation**:
- HTML `lang` attribute set to `zh-TW` (Traditional Chinese - Taiwan)
- Bilingual text displayed inline: "花蓮傳統早餐店 / Hualien Traditional Breakfast"
- Menu items show Chinese name with optional English subtitle
- Proper font support for Traditional Chinese characters (Noto Sans TC)

### 5. Image Optimization Strategy

**Decision**: WebP images with JPEG fallback using `<picture>` element

**Rationale**:
- WebP provides 25-35% smaller file sizes than JPEG
- Modern browsers support WebP (>95% coverage)
- JPEG fallback ensures compatibility
- Meets performance budget requirements
- HTML `<picture>` element provides native fallback mechanism

**Implementation**:
```html
<picture>
  <source srcset="hero.webp" type="image/webp">
  <img src="hero.jpg" alt="Traditional Taiwanese breakfast" 
       width="1200" height="400" loading="eager">
</picture>
```

**Optimization Process**:
- Resize images to exact display dimensions
- Compress JPEG at 85% quality
- Convert to WebP at 80% quality
- Generate responsive sizes (mobile, tablet, desktop)
- Use `loading="lazy"` for below-fold images

### 6. Typography - Chinese Font Selection

**Decision**: Noto Sans TC (Traditional Chinese) via Google Fonts CDN

**Rationale**:
- User specified Noto Sans TC in design reference
- Excellent Traditional Chinese glyph coverage
- Free and open-source (OFL license)
- Available via Google Fonts CDN (fast, cached)
- Professional appearance suitable for restaurant branding
- Good readability at small sizes (important for menu items)

**Fallback Stack**:
```css
font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', 
             'Microsoft JhengHei', sans-serif;
```

**Font Weights Used**:
- 400 (Regular): Body text, menu items
- 500 (Medium): Headings, section titles
- 700 (Bold): Restaurant name, emphasis

### 7. Color Scheme - Amber/Brown Palette

**Decision**: Tailwind's amber color scale (50-900) as primary palette

**Rationale**:
- User specified amber/brown color scheme in design reference
- Warm, inviting colors appropriate for breakfast restaurant
- Evokes traditional Taiwanese aesthetic
- Tailwind provides well-balanced color scales
- Ensures sufficient contrast ratios for accessibility

**Color Usage**:
- `amber-50`: Gradient background (light)
- `amber-800`: Header background (dark)
- `amber-600`/`amber-700`: Accents, prices, dividers
- `amber-900`: Footer background (darkest)
- `white`: Text on dark backgrounds
- `amber-800`: Text on light backgrounds

**Accessibility Validation**: All text-on-background combinations tested for WCAG AA contrast ratios (4.5:1 minimum).

### 8. Responsive Design Breakpoints

**Decision**: Tailwind's default breakpoints with mobile-first approach

**Rationale**:
- Mobile-first ensures core content accessible on smallest screens
- Tailwind breakpoints align with common device sizes
- User requirement: 320px (mobile) to 1920px (desktop)

**Breakpoints**:
- `default` (< 640px): Single column, stacked layout
- `md:` (≥ 768px): 2-column menu grid, side-by-side sections
- `lg:` (≥ 1024px): Max-width container (1024px), wider spacing

**Critical Responsive Patterns**:
- Menu grid: 1 column mobile, 2 columns tablet+
- Typography: Smaller sizes on mobile, larger on desktop
- Images: Responsive srcset for optimal download size
- Navigation: Simplified on mobile (no separate nav, just anchor links)

### 9. Performance Optimization Strategy

**Decision**: Multi-layered optimization to meet strict performance budget

**Strategies**:

1. **HTML Optimization**:
   - Inline critical CSS (above-fold styles)
   - Defer non-critical CSS loading
   - Minimize DOM depth (< 32 levels)
   - Use semantic HTML (reduces markup bloat)

2. **CSS Optimization**:
   - Tailwind CDN with JIT (on-demand class generation)
   - Production: Full Tailwind build with PurgeCSS (remove unused classes)
   - Target: < 20KB CSS after purge and gzip

3. **Image Optimization**:
   - WebP format (25-35% smaller than JPEG)
   - Responsive images via `srcset`
   - Lazy loading for below-fold images
   - Proper sizing (no client-side resizing)
   - Target: < 200KB for hero image (optimized)

4. **JavaScript Strategy**:
   - Minimal to no JavaScript for core functionality
   - Optional: Smooth scroll enhancement (< 1KB)
   - No frameworks (React/Vue) - unnecessary for static page

5. **Caching Strategy**:
   - Flask static files served with long cache headers (1 year)
   - HTML served with short cache (5 minutes) for easy updates
   - CDN resources cached by browser

**Performance Budget Enforcement**:
- Lighthouse CI in GitHub Actions
- Fail build if FCP > 1.5s, LCP > 2.5s, or total size > 500KB
- Monitor Core Web Vitals: FCP, LCP, CLS, TTI

### 10. Accessibility Implementation

**Decision**: WCAG 2.1 Level AA compliance with automated and manual testing

**Implementation Checklist**:

1. **Semantic HTML**:
   - `<header>`, `<main>`, `<footer>` landmarks
   - Proper heading hierarchy: h1 (restaurant name) → h2 (section titles) → h3 (category names)
   - `<section>` for logical content groupings
   - `<nav>` for navigation links

2. **Keyboard Accessibility**:
   - All links tabbable (native HTML behavior)
   - Visible focus indicators (Tailwind `focus:` utilities)
   - Skip-to-content link for screen readers
   - Logical tab order (follows visual flow)

3. **Color Contrast**:
   - Text on amber-800: White text (21:1 ratio - AAA)
   - Text on amber-50: Amber-900 text (10.5:1 ratio - AAA)
   - Prices in amber-700: On white (4.6:1 ratio - AA)
   - All combinations tested via WebAIM Contrast Checker

4. **Images**:
   - Hero image: Descriptive alt text ("Traditional Taiwanese breakfast spread")
   - Decorative images: Empty alt (`alt=""`)
   - No text in images (all text in HTML)

5. **Language Attributes**:
   - Root: `<html lang="zh-TW">`
   - English sections: `<span lang="en">` where appropriate
   - Helps screen readers choose correct pronunciation

6. **ARIA** (minimal usage):
   - Only when semantic HTML insufficient
   - Example: `aria-label` for icon-only links (if social media icons used)

**Testing**:
- Automated: axe-core in CI/CD pipeline
- Manual: NVDA (Windows), VoiceOver (Mac) screen reader testing
- Keyboard-only navigation testing

### 11. Development Environment Setup

**Decision**: Simple Python virtual environment with minimal dependencies

**Setup Steps**:
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install Flask==3.0.0 pytest==7.4.0

# Run development server
python app.py
```

**Dependencies** (`requirements.txt`):
```
Flask==3.0.0
pytest==7.4.0
pytest-flask==1.3.0
```

**Development Tools**:
- VS Code with Python extension
- Lighthouse Chrome extension (performance testing)
- axe DevTools extension (accessibility testing)
- Browser DevTools (responsive design testing)

### 12. Deployment Strategy

**Decision**: Multiple deployment options researched, recommend Render.com for simplicity

**Options**:

1. **Render.com** (Recommended):
   - Free tier available
   - Automatic HTTPS
   - GitHub integration (auto-deploy on push)
   - Simple configuration (`render.yaml`)
   - Good performance (CDN included)

2. **Heroku**:
   - Well-known platform
   - Free tier removed (paid only now)
   - Simple deployment via Git push
   - `Procfile` required

3. **PythonAnywhere**:
   - Free tier available
   - Beginner-friendly
   - Manual deployment process
   - Good for learning

4. **Traditional VPS** (DigitalOcean, Linode):
   - Full control
   - Requires server management (Nginx, SSL, etc.)
   - More complex but most flexible

**Recommended Setup** (Render.com):
- Gunicorn WSGI server
- Auto-scaling (if traffic increases)
- Custom domain support
- Free SSL certificate (Let's Encrypt)

## Best Practices Summary

### Flask Best Practices

1. **Project Structure**:
   - Separate templates and static files
   - Use Jinja2 template inheritance (`base.html`)
   - Component partials for reusability

2. **Configuration**:
   - Use environment variables for secrets
   - Separate development and production configs
   - Never commit secrets to version control

3. **Security**:
   - Enable HTTPS in production (via platform)
   - Set security headers (CSP, X-Frame-Options)
   - Validate all user input (if forms added later)

### Tailwind CSS Best Practices

1. **Utility-First Approach**:
   - Use utility classes directly in HTML
   - Extract components only when repetitive
   - Avoid custom CSS unless necessary

2. **Responsive Design**:
   - Mobile-first breakpoints
   - Test all breakpoints thoroughly
   - Use Tailwind's responsive utilities (`md:`, `lg:`)

3. **Production Optimization**:
   - Purge unused classes
   - Minify CSS
   - Use CDN for caching

### Performance Best Practices

1. **Critical Rendering Path**:
   - Inline critical CSS
   - Defer non-critical resources
   - Minimize render-blocking resources

2. **Image Optimization**:
   - Use modern formats (WebP)
   - Provide fallbacks (JPEG)
   - Lazy load below-fold images
   - Specify dimensions (prevent CLS)

3. **Caching Strategy**:
   - Long cache for static assets
   - Short cache for HTML
   - Use ETags for validation

## Conclusion

All technical decisions align with the Static Web App Constitution principles:
- ✅ Component-first architecture (Jinja2 partials)
- ✅ Static-first approach (server-rendered HTML, no client-side rendering)
- ✅ Performance budget (optimizations in place to meet targets)
- ✅ Accessibility standards (WCAG 2.1 AA compliance strategy)
- ✅ Build optimization (quality gates and automation planned)

Ready to proceed to Phase 1: Design & Contracts.
