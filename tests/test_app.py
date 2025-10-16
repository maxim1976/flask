import pytest
import json
import sys
import os

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, load_menu, menu_data, restaurant_info


@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            load_menu()
        yield client


def test_index_route_returns_200(client):
    """Test that the index route returns a 200 status code"""
    response = client.get('/')
    assert response.status_code == 200


def test_index_route_contains_restaurant_name(client):
    """Test that the index page contains the restaurant name"""
    response = client.get('/')
    # Check for English text
    assert b'Hualien' in response.data or b'Menu' in response.data


def test_health_endpoint_returns_json(client):
    """Test that the health endpoint returns valid JSON"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert 'status' in data
    assert data['status'] == 'healthy'
    assert 'timestamp' in data


def test_menu_data_loads_correctly():
    """Test that menu data loads correctly from JSON file"""
    with app.app_context():
        load_menu()
    
    assert 'restaurant' in menu_data
    assert 'categories' in menu_data
    assert len(menu_data['categories']) > 0
    
    # Check restaurant info
    assert restaurant_info.get('name_zh') is not None
    assert restaurant_info.get('name_en') is not None


def test_menu_categories_structure():
    """Test that menu categories have the correct structure"""
    with app.app_context():
        load_menu()
    
    categories = menu_data.get('categories', [])
    assert len(categories) > 0
    
    for category in categories:
        assert 'id' in category
        assert 'name_zh' in category
        assert 'name_en' in category
        assert 'items' in category
        assert isinstance(category['items'], list)


def test_menu_items_structure():
    """Test that menu items have the correct structure"""
    with app.app_context():
        load_menu()
    
    categories = menu_data.get('categories', [])
    for category in categories:
        for item in category['items']:
            assert 'id' in item
            assert 'name_zh' in item
            assert 'name_en' in item
            assert 'price' in item
            assert isinstance(item['price'], (int, float))


def test_404_handler(client):
    """Test that the 404 handler works"""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404


def test_static_files_accessible(client):
    """Test that static files are accessible"""
    # Test that we can access the menu.json file
    response = client.get('/static/data/menu.json')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_header_component_renders(client):
    """Test that the header component renders with restaurant name"""
    response = client.get('/')
    assert response.status_code == 200
    # Check for header element and restaurant name
    assert b'<header' in response.data
    assert b'Wuming' in response.data or b'Order Now' in response.data


def test_hero_component_renders(client):
    """Test that the hero component renders with key information"""
    response = client.get('/')
    assert response.status_code == 200
    # Check for hero section
    assert b'hero' in response.data
    # Check for business hours
    assert b'5:30' in response.data or b'10:30' in response.data
    assert b'Business Hours' in response.data


def test_footer_component_renders(client):
    """Test that the footer component renders with contact info"""
    response = client.get('/')
    assert response.status_code == 200
    # Check for footer element
    assert b'<footer' in response.data
    # Check for phone number
    assert b'+886' in response.data or b'tel:' in response.data
    # Check for address
    assert b'Zhongshan' in response.data or b'Hualien' in response.data


def test_bilingual_content_present(client):
    """Test that both Chinese and English content are present"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for English content
    assert 'Business Hours' in html or 'Menu' in html
    assert 'Contact' in html or 'Wuming' in html
    
    # Check for Traditional Chinese content (encoded in HTML)
    assert '營業時間' in html or '菜單' in html or '無名' in html


def test_responsive_meta_tag(client):
    """Test that responsive viewport meta tag is present"""
    response = client.get('/')
    assert b'viewport' in response.data
    assert b'width=device-width' in response.data


def test_tailwind_css_loaded(client):
    """Test that Tailwind CSS CDN is loaded"""
    response = client.get('/')
    assert b'tailwindcss.com' in response.data


def test_noto_sans_font_loaded(client):
    """Test that Noto Sans TC font is loaded"""
    response = client.get('/')
    assert b'Noto+Sans+TC' in response.data or b'Noto Sans TC' in response.data


def test_menu_section_renders(client):
    """Test that the menu section renders on the page"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    assert 'id="menu"' in html or 'class="menu"' in html


def test_menu_categories_render(client):
    """Test that all menu categories are displayed"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for category names (updated to match new menu)
    assert '燒餅系列' in html or 'Sesame Flatbread Series' in html
    assert '豆漿系列' in html or 'Soy Milk Series' in html
    assert '配菜小點' in html or 'Side Dishes' in html


def test_menu_items_display(client):
    """Test that menu items are displayed with correct information"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for specific menu items (updated to match new menu)
    assert '燒餅' in html or 'Sesame Flatbread' in html
    assert '蛋餅' in html or 'Egg Crepe' in html
    assert '豆漿' in html or 'Soy Milk' in html


def test_menu_prices_display(client):
    """Test that menu item prices are displayed with NT$ prefix"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for NT$ currency prefix
    assert 'NT$' in html
    # Check for some actual prices from our menu
    assert '45' in html  # 飯糰 price
    assert '35' in html  # 蛋餅 price


def test_vegetarian_badges_display(client):
    """Test that vegetarian badges appear for vegetarian items"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for vegetarian indicator
    assert '素食' in html or 'vegetarian' in html.lower()


def test_menu_item_descriptions(client):
    """Test that menu item descriptions are displayed (note: new menu doesn't have descriptions)"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for menu items presence instead since descriptions were removed
    assert '油條' in html or 'Fried Dough' in html
    assert '蔥' in html or 'Scallion' in html


def test_menu_has_add_to_order_buttons(client):
    """Test that menu items have 'Add to Order' buttons"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for order button text
    assert '加入訂單' in html or 'Add' in html


def test_menu_grid_layout_classes(client):
    """Test that menu uses responsive grid layout"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for Tailwind grid classes
    assert 'grid' in html
    assert 'md:grid-cols-2' in html or 'lg:grid-cols-3' in html


def test_phone_links_in_footer(client):
    """Test that phone links are clickable"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for tel: protocol
    assert 'tel:' in html
    assert '03-8335408' in html or '038335408' in html


def test_google_maps_embed(client):
    """Test that Google Maps iframe is present"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for Google Maps embed
    assert 'google.com/maps' in html
    assert 'iframe' in html


def test_whatsapp_link(client):
    """Test that WhatsApp link is present"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for WhatsApp link
    assert 'wa.me' in html or 'WhatsApp' in html


def test_address_display(client):
    """Test that restaurant address is displayed"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for address components
    assert 'Dean' in html or '德安' in html
    assert 'Hualien' in html or '花蓮' in html


def test_structured_data_json_ld(client):
    """Test that structured data (JSON-LD) is present"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for JSON-LD structured data
    assert 'application/ld+json' in html
    assert 'schema.org' in html
    assert 'Restaurant' in html


def test_robots_txt_endpoint(client):
    """Test that robots.txt is accessible"""
    response = client.get('/robots.txt')
    assert response.status_code == 200
    assert response.content_type == 'text/plain; charset=utf-8'
    assert b'User-agent' in response.data
    assert b'Sitemap' in response.data


def test_sitemap_xml_endpoint(client):
    """Test that sitemap.xml is accessible"""
    response = client.get('/sitemap.xml')
    assert response.status_code == 200
    assert response.content_type == 'application/xml; charset=utf-8'
    assert b'<?xml version' in response.data
    assert b'<urlset' in response.data
    assert b'<loc>' in response.data


# ===== Phase 6: Polish & Optimization Tests =====

def test_favicon_endpoint(client):
    """Test that favicon endpoint returns 204 No Content"""
    response = client.get('/favicon.ico')
    assert response.status_code == 204


def test_smooth_scrolling_css(client):
    """Test that smooth scrolling CSS is loaded"""
    response = client.get('/static/css/custom.css')
    assert response.status_code == 200
    assert b'scroll-behavior: smooth' in response.data


def test_print_styles_present(client):
    """Test that print styles are present in CSS"""
    response = client.get('/static/css/custom.css')
    assert response.status_code == 200
    assert b'@media print' in response.data


def test_mobile_menu_toggle_script(client):
    """Test that mobile menu toggle JavaScript is present"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'mobile-menu-button' in response.data
    assert b'addEventListener' in response.data


def test_skip_to_content_link(client):
    """Test that skip to content link for accessibility is present"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    assert 'Skip to main content' in html or '跳至主要內容' in html
    assert 'main-content' in html


def test_social_meta_tags(client):
    """Test that Open Graph and Twitter meta tags are present"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'og:title' in response.data
    assert b'og:description' in response.data
    assert b'twitter:card' in response.data
    assert b'twitter:title' in response.data


def test_aria_labels_present(client):
    """Test that ARIA labels are present for accessibility"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    assert 'aria-label' in html
    assert 'aria-expanded' in html or 'role="navigation"' in html


def test_lazy_loading_enabled(client):
    """Test that lazy loading is enabled on iframe"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    
    # Check for lazy loading on Google Maps iframe
    assert 'loading="lazy"' in html

