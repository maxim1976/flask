# API Contracts: Hualien Breakfast Restaurant Landing Page

**Feature**: 001-i-need-a  
**Date**: 2025-10-15  
**Status**: Complete

## Overview

This document defines the Flask route contracts for the restaurant landing page. Since this is a static site with server-side rendering, the "API" consists of HTTP routes that return rendered HTML.

---

## Routes

### 1. Home Page / Landing Page

**Endpoint**: `GET /`

**Description**: Serves the main landing page with restaurant information, menu, and contact details.

**Request**:
- **Method**: GET
- **Path**: `/`
- **Query Parameters**: None
- **Headers**: 
  - `Accept-Language` (optional): Used for content negotiation (future enhancement)
- **Body**: None

**Response** (Success):
- **Status Code**: 200 OK
- **Content-Type**: `text/html; charset=utf-8`
- **Headers**:
  - `Content-Language: zh-TW` (primary language)
  - `Cache-Control: public, max-age=300` (5 minutes)
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: SAMEORIGIN`
- **Body**: Rendered HTML page

**Response** (Error):
- **Status Code**: 500 Internal Server Error
- **Content-Type**: `text/html; charset=utf-8`
- **Body**: Error page (500.html template)

**Template Data**:
```python
{
    'restaurant': {
        'name_zh': 'str',
        'name_en': 'str',
        'tagline_zh': 'str',
        'tagline_en': 'str',
        'address_zh': 'str',
        'address_en': 'str',
        'hours_zh': 'str',
        'hours_en': 'str',
        'phone': 'str | None',
        'social_media': {
            'facebook': 'str | None',
            'instagram': 'str | None',
            'line': 'str | None'
        }
    },
    'categories': [
        {
            'id': 'str',
            'name_zh': 'str',
            'name_en': 'str',
            'order': 'int',
            'items': [
                {
                    'id': 'str',
                    'name_zh': 'str',
                    'name_en': 'str | None',
                    'price': 'float',
                    'available': 'bool'
                }
            ]
        }
    ]
}
```

**Example Request**:
```http
GET / HTTP/1.1
Host: hualien-breakfast.example.com
Accept: text/html
Accept-Language: zh-TW,en;q=0.9
```

**Example Response**:
```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Language: zh-TW
Cache-Control: public, max-age=300
Content-Length: 12543

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>花蓮傳統早餐店 | Hualien Traditional Breakfast</title>
    ...
</head>
<body>
    ...
</body>
</html>
```

**Flask Implementation**:
```python
@app.route('/')
def index():
    """Render the landing page with restaurant and menu data"""
    # Load restaurant info
    restaurant = {
        'name_zh': '花蓮傳統早餐店',
        'name_en': 'Hualien Traditional Breakfast',
        # ... other fields
    }
    
    # Load and sort menu data
    categories = sorted(menu_data['categories'], key=lambda x: x['order'])
    for category in categories:
        category['items'] = sorted(
            [item for item in category['items'] if item.get('available', True)],
            key=lambda x: x.get('order', 999)
        )
    
    return render_template('index.html', 
                         restaurant=restaurant, 
                         categories=categories)
```

---

### 2. Static Assets

**Endpoint**: `GET /static/<path:filename>`

**Description**: Serves static files (images, CSS, JavaScript, data files).

**Request**:
- **Method**: GET
- **Path**: `/static/<filename>` (e.g., `/static/images/hero.jpg`)
- **Query Parameters**: None
- **Headers**: Standard browser headers
- **Body**: None

**Response** (Success):
- **Status Code**: 200 OK
- **Content-Type**: Varies by file type
  - `.jpg`, `.jpeg`: `image/jpeg`
  - `.png`: `image/png`
  - `.webp`: `image/webp`
  - `.css`: `text/css`
  - `.js`: `application/javascript`
  - `.json`: `application/json`
- **Headers**:
  - `Cache-Control: public, max-age=31536000, immutable` (for hashed assets)
  - `ETag: "<hash>"` (for cache validation)
- **Body**: File contents

**Response** (Not Found):
- **Status Code**: 404 Not Found
- **Content-Type**: `text/html; charset=utf-8`
- **Body**: Error page (404.html template)

**Example Requests**:
```http
GET /static/images/hero.jpg HTTP/1.1
GET /static/data/menu.json HTTP/1.1
GET /static/css/custom.css HTTP/1.1
```

**Flask Configuration**:
```python
app = Flask(__name__, 
            static_folder='static',
            static_url_path='/static')

# Custom cache headers for static files
@app.after_request
def add_header(response):
    if request.path.startswith('/static/'):
        response.cache_control.public = True
        response.cache_control.max_age = 31536000  # 1 year
        response.cache_control.immutable = True
    return response
```

---

### 3. Health Check / Status (Optional)

**Endpoint**: `GET /health`

**Description**: Simple health check endpoint for monitoring and deployment verification.

**Request**:
- **Method**: GET
- **Path**: `/health`
- **Query Parameters**: None
- **Headers**: None required
- **Body**: None

**Response** (Success):
- **Status Code**: 200 OK
- **Content-Type**: `application/json`
- **Headers**: `Cache-Control: no-cache, no-store, must-revalidate`
- **Body**:
```json
{
    "status": "healthy",
    "timestamp": "2025-10-15T12:00:00Z",
    "version": "1.0.0"
}
```

**Response** (Unhealthy):
- **Status Code**: 503 Service Unavailable
- **Content-Type**: `application/json`
- **Body**:
```json
{
    "status": "unhealthy",
    "timestamp": "2025-10-15T12:00:00Z",
    "error": "Menu data not loaded"
}
```

**Example Request**:
```http
GET /health HTTP/1.1
Host: hualien-breakfast.example.com
```

**Flask Implementation**:
```python
@app.route('/health')
def health():
    """Health check endpoint for monitoring"""
    try:
        # Verify menu data is loaded
        if not menu_data or 'categories' not in menu_data:
            raise ValueError("Menu data not loaded")
        
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'version': '1.0.0'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'error': str(e)
        }), 503
```

---

### 4. Sitemap (SEO)

**Endpoint**: `GET /sitemap.xml`

**Description**: XML sitemap for search engine indexing.

**Request**:
- **Method**: GET
- **Path**: `/sitemap.xml`
- **Query Parameters**: None
- **Headers**: None required
- **Body**: None

**Response**:
- **Status Code**: 200 OK
- **Content-Type**: `application/xml`
- **Headers**: `Cache-Control: public, max-age=86400` (24 hours)
- **Body**: XML sitemap

**Example Response**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://hualien-breakfast.example.com/</loc>
    <lastmod>2025-10-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

**Flask Implementation**:
```python
@app.route('/sitemap.xml')
def sitemap():
    """Generate XML sitemap"""
    from flask import make_response
    
    sitemap_xml = render_template('sitemap.xml', 
                                  base_url='https://hualien-breakfast.example.com')
    response = make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'
    return response
```

---

### 5. Robots.txt (SEO)

**Endpoint**: `GET /robots.txt`

**Description**: Robots exclusion protocol file.

**Request**:
- **Method**: GET
- **Path**: `/robots.txt`
- **Query Parameters**: None
- **Headers**: None required
- **Body**: None

**Response**:
- **Status Code**: 200 OK
- **Content-Type**: `text/plain`
- **Headers**: `Cache-Control: public, max-age=86400` (24 hours)
- **Body**: Robots.txt content

**Example Response**:
```
User-agent: *
Allow: /
Sitemap: https://hualien-breakfast.example.com/sitemap.xml
```

**Flask Implementation**:
```python
@app.route('/robots.txt')
def robots():
    """Serve robots.txt"""
    from flask import make_response
    
    robots_txt = "User-agent: *\nAllow: /\nSitemap: https://hualien-breakfast.example.com/sitemap.xml\n"
    response = make_response(robots_txt)
    response.headers['Content-Type'] = 'text/plain'
    return response
```

---

### 6. Error Pages

#### 404 Not Found

**Triggered by**: Accessing non-existent routes

**Response**:
- **Status Code**: 404 Not Found
- **Content-Type**: `text/html; charset=utf-8`
- **Body**: Custom 404 error page

**Flask Implementation**:
```python
@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    return render_template('404.html'), 404
```

#### 500 Internal Server Error

**Triggered by**: Unhandled exceptions in application code

**Response**:
- **Status Code**: 500 Internal Server Error
- **Content-Type**: `text/html; charset=utf-8`
- **Body**: Custom 500 error page

**Flask Implementation**:
```python
@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error page"""
    return render_template('500.html'), 500
```

---

## Route Summary Table

| Route | Method | Purpose | Cache | Auth Required |
|-------|--------|---------|-------|---------------|
| `/` | GET | Landing page | 5 min | No |
| `/static/<path>` | GET | Static assets | 1 year | No |
| `/health` | GET | Health check | No cache | No |
| `/sitemap.xml` | GET | SEO sitemap | 24 hours | No |
| `/robots.txt` | GET | SEO robots | 24 hours | No |
| (404 handler) | ANY | Not found error | No cache | No |
| (500 handler) | ANY | Server error | No cache | No |

---

## Security Headers

All HTML responses SHOULD include these security headers:

```python
@app.after_request
def set_security_headers(response):
    """Set security headers on all responses"""
    if response.content_type and 'text/html' in response.content_type:
        # Content Security Policy
        response.headers['Content-Security-Policy'] = (
            "default-src 'self'; "
            "style-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' https: data:; "
            "script-src 'self' https://cdn.tailwindcss.com;"
        )
        
        # Other security headers
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    
    return response
```

---

## Performance Optimizations

### Caching Strategy

1. **Static Assets** (images, CSS, JS):
   - Cache-Control: `public, max-age=31536000, immutable`
   - Rationale: Content-hashed filenames allow aggressive caching

2. **HTML Pages**:
   - Cache-Control: `public, max-age=300` (5 minutes)
   - Rationale: Allow quick menu updates without waiting hours

3. **SEO Files** (sitemap, robots):
   - Cache-Control: `public, max-age=86400` (24 hours)
   - Rationale: Rarely change, reduce server load

4. **Health Check**:
   - Cache-Control: `no-cache, no-store, must-revalidate`
   - Rationale: Always check current status

### Compression

Enable gzip/brotli compression for text responses:

```python
from flask_compress import Compress

app = Flask(__name__)
Compress(app)

# Compresses responses > 500 bytes with text/* or application/json MIME types
```

---

## Testing Contracts

### Unit Tests

```python
def test_home_page(client):
    """Test home page returns 200 and correct content"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'花蓮傳統早餐店' in response.data
    assert b'Hualien Traditional Breakfast' in response.data

def test_static_file(client):
    """Test static file serving"""
    response = client.get('/static/data/menu.json')
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_health_check(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_404_error(client):
    """Test 404 error handling"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
```

### Integration Tests

```python
def test_menu_data_loaded(client):
    """Test that menu data is properly loaded and displayed"""
    response = client.get('/')
    assert response.status_code == 200
    
    # Check all menu categories present
    assert b'主食' in response.data  # Main Dishes
    assert b'飲品' in response.data  # Drinks
    assert b'配菜' in response.data  # Sides
    
    # Check sample menu items
    assert b'燒餅夾油條' in response.data
    assert b'NT$ 44.00' in response.data

def test_bilingual_content(client):
    """Test bilingual content rendering"""
    response = client.get('/')
    
    # Chinese content
    assert '花蓮傳統早餐店'.encode('utf-8') in response.data
    
    # English content
    assert b'Hualien Traditional Breakfast' in response.data
```

---

## API Documentation Tools

While this is a simple Flask app with server-rendered HTML (not a REST API), we can document the routes using:

### Flask-RESTX (Optional)

For future API endpoints:
```python
from flask_restx import Api, Resource

api = Api(app, version='1.0', title='Restaurant Landing Page API',
          description='Simple landing page for Taiwanese breakfast restaurant')

ns = api.namespace('/', description='Main routes')

@ns.route('/')
class LandingPage(Resource):
    def get(self):
        """Render the landing page"""
        # Implementation
        pass
```

---

## Conclusion

The route contracts are intentionally minimal:
- ✅ Single main route (`/`) for the landing page
- ✅ Static file serving for assets
- ✅ Optional health check for monitoring
- ✅ SEO support (sitemap, robots.txt)
- ✅ Proper error handling (404, 500)
- ✅ Security headers configured
- ✅ Caching strategy defined

This aligns with the Static-First Architecture principle - no complex API needed, just simple HTTP routes serving pre-rendered HTML.
