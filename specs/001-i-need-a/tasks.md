---
description: "Task list for Hualien Breakfast Restaurant Landing Page implementation"
---

# Tasks: Hualien Breakfast Restaurant Landing Page

**Input**: Design documents from `/specs/001-i-need-a/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL and not included in this task list as they were not explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions
- **Web app**: `templates/`, `static/`, `app.py` at repository root
- Paths shown assume Flask project structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic Flask application structure

- [ ] T001 [P] Create Python virtual environment and activate it in project root
- [ ] T002 [P] Create requirements.txt with Flask==3.0.0, pytest==7.4.0, pytest-flask==1.3.0
- [ ] T003 Install dependencies from requirements.txt using pip
- [ ] T004 [P] Create directory structure: templates/, templates/components/, static/images/, static/css/, static/data/, tests/
- [ ] T005 [P] Create base Flask application file app.py with basic route structure and imports
- [ ] T006 [P] Create base.html template in templates/ with Tailwind CSS CDN, Google Fonts (Noto Sans TC), and custom typography styles
- [ ] T007 [P] Create .gitignore file with Python, Flask, and IDE-specific entries

**Checkpoint**: Basic project structure ready - can run Flask development server

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T008 Create menu.json data file in static/data/ with complete menu structure (categories: Main Dishes, Drinks, Sides) and sample items
- [ ] T009 Add menu data loading logic to app.py (load JSON on app startup, handle file errors)
- [ ] T010 [P] Define restaurant information dictionary in app.py with bilingual fields (name_zh, name_en, address, hours, etc.)
- [ ] T011 [P] Configure Flask static file serving with cache headers for static/ directory
- [ ] T012 Create index.html template in templates/ that extends base.html and includes component placeholders

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View Restaurant Information (Priority: P1) 🎯 MVP

**Goal**: Display essential restaurant information (name, tagline, location, hours) so customers can learn about the restaurant

**Independent Test**: Visit the homepage URL and verify all restaurant information (name in Chinese and English, location as "Hualien, Taiwan", opening hours) is visible and readable

### Implementation for User Story 1

- [ ] T013 [P] [US1] Create header.html component in templates/components/ displaying bilingual restaurant name and tagline with amber-800 background
- [ ] T014 [P] [US1] Create hero.html component in templates/components/ with hero image placeholder and proper sizing (1200x400)
- [ ] T015 [P] [US1] Create footer.html component in templates/components/ displaying bilingual opening hours and address in two-column grid layout
- [ ] T016 [US1] Update index.html to include header, hero, and footer components using Jinja2 {% include %} tags
- [ ] T017 [US1] Update app.py index route to pass restaurant_info dictionary to index.html template
- [ ] T018 [US1] Add hero image to static/images/ (download from Unsplash or use placeholder, optimize to < 200KB)
- [ ] T019 [US1] Verify bilingual content displays correctly (Traditional Chinese characters render properly, English text is readable)
- [ ] T020 [US1] Test responsive layout on mobile (320px) and desktop (1920px) - verify no horizontal scrolling

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently - basic restaurant information page complete

---

## Phase 4: User Story 2 - Browse Menu Items (Priority: P2)

**Goal**: Display menu items with prices organized by categories (Main Dishes, Drinks, Sides) so customers can see what's available

**Independent Test**: Scroll to the menu section and verify that breakfast items are displayed with names and prices in NT$ organized by categories

### Implementation for User Story 2

- [ ] T021 [US2] Populate menu.json with complete menu data (at least 20+ items across 3 categories: Main Dishes, Drinks, Sides)
- [ ] T022 [US2] Create menu.html component in templates/components/ with category sections and grid layout
- [ ] T023 [US2] Implement menu rendering logic in menu.html: loop through categories, display category headers (bilingual), loop through items in grid
- [ ] T024 [US2] Add menu item cards with Tailwind styling: white background, shadow-sm, hover:shadow-md, rounded-lg
- [ ] T025 [US2] Format prices in menu items using Jinja2 filter (NT$ with 2 decimal places: "%.2f"|format)
- [ ] T026 [US2] Update index.html to include menu.html component between hero and footer
- [ ] T027 [US2] Update app.py index route to sort categories by order field and items by order field within categories
- [ ] T028 [US2] Add section title "菜單 Menu" with amber accent line above menu component
- [ ] T029 [US2] Verify menu displays in 2-column grid on desktop (md: breakpoint) and 1-column on mobile
- [ ] T030 [US2] Verify all menu items show Chinese names and NT$ prices correctly

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - customers can view restaurant info and browse menu

---

## Phase 5: User Story 3 - View Location and Contact Options (Priority: P3)

**Goal**: Provide easy access to contact methods (phone, address, social media) so customers can reach the restaurant

**Independent Test**: Find and click contact information elements (phone link, address display) and verify they work correctly

### Implementation for User Story 3

- [ ] T031 [US3] Add phone number to restaurant_info dictionary in app.py (format: +886-3-XXX-XXXX or placeholder)
- [ ] T032 [US3] Update footer.html to include phone number with tel: link for mobile click-to-call
- [ ] T033 [US3] Add social media links to restaurant_info dictionary in app.py (Facebook, Instagram, or placeholders)
- [ ] T034 [US3] Update footer.html to display social media links with icons or text links in footer
- [ ] T035 [US3] Make address in footer clickable (wrap in link to Google Maps search or copy-to-clipboard)
- [ ] T036 [US3] Add aria-label attributes to phone and social media links for accessibility
- [ ] T037 [US3] Test phone link on mobile device (or mobile emulator) - verify it initiates call
- [ ] T038 [US3] Test address link - verify it copies address or opens map service
- [ ] T039 [US3] Test social media links - verify they open in new tab (target="_blank" rel="noopener")

**Checkpoint**: All user stories should now be independently functional - full landing page experience complete

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final quality checks

- [ ] T040 [P] Create 404.html error page template with bilingual "Page Not Found" message and "Return Home" link
- [ ] T041 [P] Add 404 error handler to app.py using @app.errorhandler(404)
- [ ] T042 [P] Create /health endpoint in app.py returning JSON with status and timestamp
- [ ] T043 [P] Add security headers to app.py using @app.after_request (CSP, X-Content-Type-Options, X-Frame-Options)
- [ ] T044 [P] Create robots.txt route in app.py serving "User-agent: * Allow: /" with sitemap link
- [ ] T045 Optimize hero image: convert to WebP format with JPEG fallback, ensure < 200KB size
- [ ] T046 Add image dimensions (width, height) to hero image tag in hero.html to prevent CLS
- [ ] T047 Verify color contrast ratios meet WCAG AA standards (amber-800 on white: 4.5:1 minimum)
- [ ] T048 Add lang="zh-TW" attribute to html tag in base.html, add lang="en" spans where needed
- [ ] T049 Verify semantic HTML structure: proper heading hierarchy (h1 → h2 → h3), landmarks (header, main, footer)
- [ ] T050 Test keyboard navigation: verify all links are tabbable with visible focus indicators
- [ ] T051 Add meta description tag to base.html with bilingual restaurant description
- [ ] T052 Add favicon link to base.html (create or use placeholder favicon.ico in static/)
- [ ] T053 [P] Create README.md with project description, setup instructions, and run commands
- [ ] T054 Run Lighthouse audit - verify Performance > 90, Accessibility = 100, SEO = 100
- [ ] T055 Verify total page size < 500KB (check Network tab in browser DevTools)
- [ ] T056 Verify page load time < 3 seconds on 3G network simulation
- [ ] T057 Test on multiple browsers: Chrome, Firefox, Safari (latest 2 versions)
- [ ] T058 Test responsive design at breakpoints: 320px (mobile), 768px (tablet), 1024px (desktop), 1920px (large desktop)
- [ ] T059 Run quickstart.md validation - verify all steps in quickstart guide work correctly
- [ ] T060 Final code review: verify no hardcoded secrets, proper UTF-8 encoding, consistent code style

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Independent of US1 (but builds on same page)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Independent of US1/US2 (enhances existing footer from US1)

**Note**: While stories are technically independent, they all modify the same landing page, so parallel development would require coordination on template files. Sequential implementation (P1 → P2 → P3) is recommended.

### Within Each User Story

- **User Story 1**: Header → Hero → Footer → Integration → Testing → Complete
- **User Story 2**: Menu data → Menu component → Integration → Testing → Complete
- **User Story 3**: Contact data → Footer updates → Testing → Complete

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T001, T002, T004, T005, T006, T007)
- All Foundational tasks marked [P] can run in parallel (T008, T010, T011)
- Within User Story 1: Header and Hero components can be built in parallel (T013, T014)
- Polish tasks marked [P] can run in parallel (T040, T041, T042, T043, T044, T053)

---

## Parallel Example: User Story 1

```bash
# Launch all independent components for User Story 1 together:
Task: "Create header.html component in templates/components/ displaying bilingual restaurant name"
Task: "Create hero.html component in templates/components/ with hero image placeholder"
Task: "Create footer.html component in templates/components/ displaying opening hours"

# Then integrate sequentially:
Task: "Update index.html to include header, hero, and footer components"
Task: "Update app.py index route to pass restaurant_info dictionary"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (T013-T020)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Run Lighthouse, verify responsive design, test accessibility
6. Deploy/demo if ready - you now have a working landing page with basic info

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (T013-T020) → Test independently → Deploy/Demo (MVP with basic restaurant info!)
3. Add User Story 2 (T021-T030) → Test independently → Deploy/Demo (now with full menu)
4. Add User Story 3 (T031-T039) → Test independently → Deploy/Demo (now with contact options)
5. Complete Polish (T040-T060) → Final quality checks → Production deployment
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (restaurant info components)
   - Developer B: User Story 2 (menu data and component)
   - Developer C: User Story 3 (contact enhancements)
   - Developer D: Polish tasks (error pages, optimization)
3. **Coordination needed**: All modify index.html, so merge conflicts likely
4. **Recommended approach**: Sequential implementation by priority to avoid conflicts

---

## Task Count Summary

- **Phase 1 (Setup)**: 7 tasks
- **Phase 2 (Foundational)**: 5 tasks (BLOCKING)
- **Phase 3 (User Story 1 - P1)**: 8 tasks
- **Phase 4 (User Story 2 - P2)**: 10 tasks
- **Phase 5 (User Story 3 - P3)**: 9 tasks
- **Phase 6 (Polish)**: 21 tasks

**Total**: 60 tasks

**Parallel Opportunities**: 14 tasks marked [P]

**Estimated Effort**:
- Setup + Foundational: 1-2 hours
- User Story 1 (MVP): 2-3 hours
- User Story 2: 2-3 hours
- User Story 3: 1-2 hours
- Polish: 3-4 hours
- **Total**: 9-14 hours for complete implementation

---

## Success Criteria Verification

After completing all tasks, verify against spec.md success criteria:

- [ ] **SC-001**: Users can find the restaurant's address and opening hours within 10 seconds of landing on the page
- [ ] **SC-002**: The landing page loads completely in under 3 seconds on a standard broadband connection
- [ ] **SC-003**: The page displays correctly across all screen sizes from 320px mobile to 1920px desktop without horizontal scrolling
- [ ] **SC-004**: All menu items across all categories (Main Dishes, Drinks, Sides) are visible with names and prices in NT$
- [ ] **SC-005**: Both Chinese and English text are readable and properly rendered across all sections
- [ ] **SC-006**: The page meets accessibility standards with proper heading hierarchy and semantic HTML structure
- [ ] **SC-007**: Users can navigate to any section of the page via smooth scrolling
- [ ] **SC-008**: The page design visually communicates "traditional Taiwanese breakfast restaurant" within 3 seconds of viewing

---

## Notes

- Tasks use absolute file paths relative to project root
- All templates use Jinja2 syntax and extend base.html
- Tailwind CSS classes are applied inline (no separate CSS build process for MVP)
- Menu data in JSON format allows easy updates without code changes
- Each user story is independently testable and deployable
- No database required - all data is static (JSON and hardcoded in app.py)
- Tests are not included as they were not requested in the feature specification
- For production deployment, consider migrating Tailwind from CDN to build process for optimal performance
- Follow quickstart.md for detailed implementation guidance on each task

---

## Validation Checkpoints

After each phase, run these checks:

**After Setup (Phase 1)**:
```bash
python app.py  # Should start Flask dev server without errors
```

**After Foundational (Phase 2)**:
```bash
python app.py  # Navigate to http://localhost:5000
# Should see basic page structure (even if incomplete)
```

**After Each User Story**:
```bash
# Manual testing checklist:
1. Visit homepage
2. Verify story-specific functionality works
3. Test responsive design (resize browser)
4. Check both Chinese and English text render correctly
```

**After Polish (Phase 6)**:
```bash
# Run Lighthouse audit in Chrome DevTools
# Verify all success criteria met
# Test on multiple devices/browsers
```

---

**Ready to implement!** Start with Phase 1 (Setup) and work through sequentially, or use parallel strategies where marked.
