# Quickstart Guide: Hualien Breakfast Restaurant Landing Page

**Feature**: 001-i-need-a  
**Date**: 2025-10-15  
**For**: Developers implementing this feature

## Overview

This guide walks you through setting up, developing, and deploying the Hualien breakfast restaurant landing page from scratch.

**Prerequisites**:
- Python 3.11 or higher
- Git
- Text editor (VS Code recommended)
- Web browser (Chrome/Firefox for testing)

**Estimated Time**: 2-3 hours for complete implementation

---

## Quick Setup (5 minutes)

### 1. Clone and Navigate

```powershell
# If starting fresh, create project directory
mkdir flask
cd flask

# Initialize git (if not already done)
git init
git checkout -b 001-i-need-a
```

### 2. Create Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Verify activation (should show (venv) in prompt)
# If activation fails due to execution policy:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies

```powershell
# Create requirements.txt
@"
Flask==3.0.0
pytest==7.4.0
pytest-flask==1.3.0
"@ | Out-File -Encoding utf8 requirements.txt

# Install dependencies
pip install -r requirements.txt

# Verify installation
flask --version  # Should show Flask 3.0.0
```

### 4. Create Project Structure

```powershell
# Create directory structure
New-Item -ItemType Directory -Path templates, static, tests -Force
New-Item -ItemType Directory -Path templates/components -Force
New-Item -ItemType Directory -Path static/images, static/css, static/data -Force

# Create empty files
New-Item -ItemType File -Path app.py, templates/base.html, templates/index.html -Force
New-Item -ItemType File -Path templates/components/header.html -Force
New-Item -ItemType File -Path templates/components/hero.html -Force
New-Item -ItemType File -Path templates/components/menu.html -Force
New-Item -ItemType File -Path templates/components/footer.html -Force
New-Item -ItemType File -Path static/data/menu.json -Force
New-Item -ItemType File -Path tests/test_routes.py -Force
```

**Verify Structure**:
```
flask/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── components/
│       ├── header.html
│       ├── hero.html
│       ├── menu.html
│       └── footer.html
├── static/
│   ├── images/
│   ├── css/
│   └── data/
│       └── menu.json
├── tests/
│   └── test_routes.py
└── requirements.txt
```

---

## Implementation Steps

### Step 1: Create Menu Data (10 minutes)

**File**: `static/data/menu.json`

```json
{
  "categories": [
    {
      "id": "main-dishes",
      "name_zh": "主食",
      "name_en": "Main Dishes",
      "order": 1,
      "items": [
        {"id": "shaobing-youtiao", "name_zh": "燒餅夾油條", "price": 44.00, "order": 1},
        {"id": "shaobing", "name_zh": "燒餅", "price": 22.00, "order": 2},
        {"id": "danbing-youtiao", "name_zh": "蛋餅夾油條", "price": 54.00, "order": 3},
        {"id": "youtiao", "name_zh": "油條", "price": 22.00, "order": 4},
        {"id": "danbing", "name_zh": "蛋餅", "price": 32.00, "order": 5},
        {"id": "hongdoubing", "name_zh": "红豆餅", "price": 27.00, "order": 6}
      ]
    },
    {
      "id": "drinks",
      "name_zh": "飲品",
      "name_en": "Drinks",
      "order": 2,
      "items": [
        {"id": "iced-black-tea", "name_zh": "冰紅茶", "price": 22.00, "order": 1},
        {"id": "soy-milk-sweet", "name_zh": "甜豆漿.熱.溫.冰", "price": 27.00, "order": 2},
        {"id": "soy-milk-salty", "name_zh": "鹹豆漿", "price": 32.00, "order": 3},
        {"id": "soy-milk-salty-egg", "name_zh": "鹹豆漿加蛋", "price": 47.00, "order": 4}
      ]
    },
    {
      "id": "sides",
      "name_zh": "配菜",
      "name_en": "Sides",
      "order": 3,
      "items": [
        {"id": "scallion-egg", "name_zh": "蔥蛋", "price": 22.00, "order": 1},
        {"id": "fried-egg", "name_zh": "荷包蛋.半熟.全熟", "price": 15.00, "order": 2}
      ]
    }
  ]
}
```

### Step 2: Create Flask Application (15 minutes)

**File**: `app.py`

```python
import json
from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Load menu data on startup
with open('static/data/menu.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

# Restaurant information
restaurant_info = {
    'name_zh': '花蓮傳統早餐店',
    'name_en': 'Hualien Traditional Breakfast',
    'tagline_zh': '來自花蓮的傳統美味，每日新鮮現做，品嘗最道地的台式早餐',
    'address_zh': '花蓮縣花蓮市',
    'address_en': 'Hualien City, Hualien County, Taiwan',
    'hours_zh': '週一至週日 早上 6:00 - 中午 12:00',
    'hours_en': 'Monday - Sunday: 6:00 AM - 12:00 PM'
}

@app.route('/')
def index():
    """Render the landing page"""
    # Sort categories and items
    categories = sorted(menu_data['categories'], key=lambda x: x['order'])
    for category in categories:
        category['items'] = sorted(
            category['items'],
            key=lambda x: x.get('order', 999)
        )
    
    return render_template('index.html',
                         restaurant=restaurant_info,
                         categories=categories)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Step 3: Create Base Template (10 minutes)

**File**: `templates/base.html`

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}花蓮傳統早餐店 | Hualien Traditional Breakfast{% endblock %}</title>
    <meta name="description" content="來自花蓮的傳統美味，每日新鮮現做，品嘗最道地的台式早餐">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts - Noto Sans TC -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        h1 { font-size: 1.875rem; font-weight: 500; line-height: 1.5; }
        h2 { font-size: 1.5rem; font-weight: 500; line-height: 1.5; }
        h3 { font-size: 1.25rem; font-weight: 500; line-height: 1.5; }
        p, span { font-size: 1rem; font-weight: 400; line-height: 1.5; }
    </style>
</head>
<body class="min-h-screen bg-gradient-to-b from-amber-50 to-white">
    {% block content %}{% endblock %}
</body>
</html>
```

### Step 4: Create Landing Page Template (15 minutes)

**File**: `templates/index.html`

```html
{% extends "base.html" %}

{% block content %}
    {% include 'components/header.html' %}
    {% include 'components/hero.html' %}
    
    <main class="max-w-6xl mx-auto px-6 py-12">
        {% include 'components/menu.html' %}
    </main>
    
    {% include 'components/footer.html' %}
{% endblock %}
```

### Step 5: Create Header Component (5 minutes)

**File**: `templates/components/header.html`

```html
<header class="bg-amber-800 text-white py-8 px-6 shadow-lg">
    <div class="max-w-6xl mx-auto text-center">
        <h1 class="mb-2">{{ restaurant.name_zh }}</h1>
        <p class="opacity-90">{{ restaurant.name_en }}</p>
        <p class="mt-4 max-w-2xl mx-auto opacity-95">
            {{ restaurant.tagline_zh }}
        </p>
    </div>
</header>
```

### Step 6: Create Hero Component (5 minutes)

**File**: `templates/components/hero.html`

```html
<div class="max-w-6xl mx-auto px-6 py-8">
    <div class="rounded-2xl overflow-hidden shadow-2xl">
        <img 
            src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200&h=400&fit=crop" 
            alt="Restaurant storefront" 
            class="w-full h-96 object-cover"
            width="1200"
            height="400"
        />
    </div>
</div>
```

### Step 7: Create Menu Component (20 minutes)

**File**: `templates/components/menu.html`

```html
<div class="text-center mb-12">
    <h2 class="mb-2">菜單 Menu</h2>
    <div class="w-24 h-1 bg-amber-600 mx-auto rounded-full"></div>
</div>

{% for category in categories %}
<section class="mb-12">
    <h3 class="mb-6 text-amber-800 border-b-2 border-amber-200 pb-3">
        {{ category.name_zh }} {{ category.name_en }}
    </h3>
    <div class="grid md:grid-cols-2 gap-4">
        {% for item in category.items %}
        <div class="flex justify-between items-center bg-white p-4 rounded-lg shadow-sm hover:shadow-md transition-shadow">
            <span class="flex-1">{{ item.name_zh }}</span>
            <span class="ml-4 text-amber-700">NT$ {{ "%.2f"|format(item.price) }}</span>
        </div>
        {% endfor %}
    </div>
</section>
{% endfor %}
```

### Step 8: Create Footer Component (10 minutes)

**File**: `templates/components/footer.html`

```html
<footer class="bg-amber-900 text-white py-12 px-6 mt-16">
    <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-8">
        <div>
            <h3 class="mb-4">營業時間 Opening Hours</h3>
            <div class="space-y-2 opacity-90">
                <p>{{ restaurant.hours_zh }}</p>
                <p>{{ restaurant.hours_en }}</p>
            </div>
        </div>
        <div>
            <h3 class="mb-4">地址 Address</h3>
            <div class="space-y-2 opacity-90">
                <p>{{ restaurant.address_zh }}</p>
                <p>{{ restaurant.address_en }}</p>
            </div>
        </div>
    </div>
    <div class="max-w-6xl mx-auto mt-8 pt-8 border-t border-amber-700 text-center opacity-75">
        <p>&copy; 2025 {{ restaurant.name_zh }} {{ restaurant.name_en }}. All rights reserved.</p>
    </div>
</footer>
```

### Step 9: Create 404 Error Page (5 minutes)

**File**: `templates/404.html`

```html
{% extends "base.html" %}

{% block title %}404 - Page Not Found{% endblock %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gradient-to-b from-amber-50 to-white">
    <div class="text-center px-6">
        <h1 class="text-6xl font-bold text-amber-800 mb-4">404</h1>
        <h2 class="text-2xl text-gray-700 mb-4">找不到頁面 Page Not Found</h2>
        <p class="text-gray-600 mb-8">抱歉，您訪問的頁面不存在。<br>Sorry, the page you're looking for doesn't exist.</p>
        <a href="/" class="inline-block bg-amber-600 text-white px-6 py-3 rounded-lg hover:bg-amber-700 transition-colors">
            返回首頁 Return Home
        </a>
    </div>
</div>
{% endblock %}
```

### Step 10: Create Tests (15 minutes)

**File**: `tests/test_routes.py`

```python
import pytest
from app import app

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert '花蓮傳統早餐店'.encode('utf-8') in response.data
    assert b'Hualien Traditional Breakfast' in response.data

def test_menu_content(client):
    """Test menu data is displayed"""
    response = client.get('/')
    assert response.status_code == 200
    # Check category headers
    assert '主食'.encode('utf-8') in response.data
    assert b'Main Dishes' in response.data
    assert '飲品'.encode('utf-8') in response.data
    assert b'Drinks' in response.data
    # Check sample menu item
    assert '燒餅夾油條'.encode('utf-8') in response.data
    assert b'44.00' in response.data

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data

def test_404_page(client):
    """Test 404 error handling"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'404' in response.data
```

---

## Running the Application

### Development Server

```powershell
# Make sure virtual environment is activated
# Run the Flask app
python app.py

# Output should show:
# * Running on http://0.0.0.0:5000
# * Debug mode: on

# Open browser to http://localhost:5000
```

### Run Tests

```powershell
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test
pytest tests/test_routes.py::test_home_page -v
```

### Manual Testing Checklist

- [ ] Homepage loads without errors
- [ ] Restaurant name displays in both Chinese and English
- [ ] Hero image loads properly
- [ ] Menu categories display: Main Dishes, Drinks, Sides
- [ ] Menu items show Chinese names and prices in NT$
- [ ] Footer shows opening hours and address
- [ ] Responsive design works on mobile (resize browser to 320px)
- [ ] 404 page shows when accessing `/nonexistent`
- [ ] Health check works at `/health`

---

## Performance Validation

### Lighthouse Test

1. Open Chrome DevTools (F12)
2. Go to "Lighthouse" tab
3. Select "Desktop" or "Mobile"
4. Click "Analyze page load"
5. **Target Scores**:
   - Performance: > 90
   - Accessibility: 100
   - Best Practices: > 90
   - SEO: 100

### Performance Budget Check

```powershell
# Check page size (should be < 500KB total)
# Use browser DevTools Network tab:
# 1. Open DevTools (F12)
# 2. Go to Network tab
# 3. Reload page
# 4. Check "Transferred" column total at bottom
```

**Expected Sizes**:
- HTML: ~10-15 KB
- Tailwind CSS (CDN): ~50-100 KB
- Google Fonts: ~20-30 KB
- Hero image: ~150-200 KB
- **Total**: < 400 KB ✅

---

## Accessibility Validation

### Automated Testing

```powershell
# Install axe-core (if using Node.js)
npm install -g @axe-core/cli

# Run accessibility test
axe http://localhost:5000

# Should show 0 violations
```

### Manual Testing

1. **Keyboard Navigation**:
   - Tab through all links (should have visible focus)
   - No keyboard traps

2. **Screen Reader** (Windows - NVDA):
   - Download NVDA: https://www.nvaccess.org/download/
   - Start NVDA
   - Navigate page with arrow keys
   - Verify all content is announced correctly

3. **Color Contrast**:
   - Use WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
   - Test: White on amber-800 (should be > 4.5:1 ratio)

---

## Deployment

### Option 1: Render.com (Recommended)

1. **Create `render.yaml`**:
```yaml
services:
  - type: web
    name: hualien-breakfast
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

2. **Add Gunicorn** to `requirements.txt`:
```
Flask==3.0.0
gunicorn==21.2.0
```

3. **Deploy**:
   - Push code to GitHub
   - Connect GitHub repo to Render.com
   - Render auto-deploys on push to main branch

### Option 2: Local Production Server

```powershell
# Install Gunicorn
pip install gunicorn

# Run production server
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# -w 4: 4 worker processes
# -b 0.0.0.0:8000: Bind to all interfaces on port 8000
```

---

## Troubleshooting

### Issue: Virtual environment won't activate

**Solution**:
```powershell
# Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then retry activation
.\venv\Scripts\Activate.ps1
```

### Issue: Flask not found

**Solution**:
```powershell
# Verify venv is activated (should see (venv) in prompt)
# Reinstall Flask
pip install --upgrade Flask
```

### Issue: Menu items not displaying

**Solution**:
1. Check `menu.json` is valid JSON (use https://jsonlint.com/)
2. Verify file encoding is UTF-8
3. Check Flask console for errors

### Issue: Chinese characters showing as boxes

**Solution**:
1. Verify file saved as UTF-8 encoding
2. Check Google Fonts link is loading (Network tab in DevTools)
3. Clear browser cache and reload

### Issue: Page loading slowly

**Solution**:
1. Check hero image size (should be < 200KB)
2. Use image optimization tools (TinyPNG, ImageOptim)
3. Convert to WebP format for better compression

---

## Next Steps

After completing quickstart:

1. **Replace placeholder hero image** with actual restaurant photo
2. **Add more menu items** to `menu.json` (full menu from spec)
3. **Optimize images** (WebP conversion, responsive sizes)
4. **Set up CI/CD** (GitHub Actions for automated testing)
5. **Configure custom domain** (if deploying to production)
6. **Add analytics** (Google Analytics or similar)

---

## Development Workflow

```powershell
# Daily workflow
1. Activate venv:           .\venv\Scripts\Activate.ps1
2. Run tests:               pytest tests/ -v
3. Start dev server:        python app.py
4. Make changes to templates/data
5. Browser auto-reloads (Flask debug mode)
6. Verify changes
7. Run tests again:         pytest tests/ -v
8. Commit:                  git add .; git commit -m "feat: add menu items"
9. Push:                    git push origin 001-i-need-a
```

---

## Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Tailwind CSS Docs**: https://tailwindcss.com/docs
- **Jinja2 Template Docs**: https://jinja.palletsprojects.com/
- **WCAG Guidelines**: https://www.w3.org/WAI/WCAG21/quickref/
- **Lighthouse CI**: https://github.com/GoogleChrome/lighthouse-ci

---

## Success Criteria Checklist

Verify implementation meets all success criteria from spec:

- [ ] **SC-001**: Users can find address and hours within 10 seconds
- [ ] **SC-002**: Page loads in under 3 seconds
- [ ] **SC-003**: Responsive from 320px to 1920px (no horizontal scroll)
- [ ] **SC-004**: All menu items visible with names and prices in NT$
- [ ] **SC-005**: Both Chinese and English text readable
- [ ] **SC-006**: Proper heading hierarchy and semantic HTML
- [ ] **SC-007**: Smooth scrolling navigation works
- [ ] **SC-008**: Design communicates "traditional Taiwanese breakfast" within 3 seconds

---

**Congratulations!** 🎉 You've completed the quickstart and have a working restaurant landing page.

For task breakdown and implementation details, proceed to `/speckit.tasks` command.
