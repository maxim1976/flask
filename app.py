import json
import os
from urllib.parse import quote
from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Custom Jinja2 filter for datetime formatting
@app.template_filter('datetime_format')
def datetime_format(value, format='%Y-%m-%d'):
    """Format a datetime or string to a specific format"""
    if value == 'now':
        return datetime.now().strftime(format)
    return value

# Custom Jinja2 filter for URL encoding
@app.template_filter('urlencode')
def urlencode_filter(s):
    """URL encode a string for use in URLs"""
    if s is None:
        return ''
    return quote(str(s))

# Load menu data on startup
menu_data = {}
restaurant_info = {}

def load_menu():
    """Load menu data from JSON file"""
    global menu_data, restaurant_info
    menu_file = os.path.join(app.static_folder, 'data', 'menu.json')
    try:
        with open(menu_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            menu_data = data
            restaurant_info = data.get('restaurant', {})
            app.logger.info(f"Loaded menu with {len(data.get('categories', []))} categories")
    except FileNotFoundError:
        app.logger.error(f"Menu file not found: {menu_file}")
        menu_data = {'restaurant': {}, 'categories': []}
        restaurant_info = {}
    except json.JSONDecodeError as e:
        app.logger.error(f"Invalid JSON in menu file: {e}")
        menu_data = {'restaurant': {}, 'categories': []}
        restaurant_info = {}

# Load menu on startup
with app.app_context():
    load_menu()

@app.route('/')
def index():
    """Render the landing page"""
    return render_template('index.html',
                         restaurant=restaurant_info,
                         categories=menu_data.get('categories', []))

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })

@app.route('/robots.txt')
def robots():
    """Robots.txt for search engine crawlers"""
    content = """User-agent: *
Allow: /
Sitemap: {}/sitemap.xml

# Disallow admin and api paths
Disallow: /admin
Disallow: /api
""".format(request.url_root.rstrip('/'))
    return content, 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/sitemap.xml')
def sitemap():
    """Sitemap.xml for search engines"""
    from flask import request
    pages = []
    
    # Add homepage
    pages.append({
        'loc': request.url_root,
        'lastmod': datetime.now().strftime('%Y-%m-%d'),
        'changefreq': 'daily',
        'priority': '1.0'
    })
    
    # Build XML
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for page in pages:
        sitemap_xml.append('  <url>')
        sitemap_xml.append(f'    <loc>{page["loc"]}</loc>')
        sitemap_xml.append(f'    <lastmod>{page["lastmod"]}</lastmod>')
        sitemap_xml.append(f'    <changefreq>{page["changefreq"]}</changefreq>')
        sitemap_xml.append(f'    <priority>{page["priority"]}</priority>')
        sitemap_xml.append('  </url>')
    
    sitemap_xml.append('</urlset>')
    
    return '\n'.join(sitemap_xml), 200, {'Content-Type': 'application/xml; charset=utf-8'}

@app.route('/favicon.ico')
def favicon():
    """Serve favicon"""
    # Return a simple response for now - can be replaced with actual favicon file
    return '', 204

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
