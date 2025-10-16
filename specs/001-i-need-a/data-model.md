# Data Model: Hualien Breakfast Restaurant Landing Page

**Feature**: 001-i-need-a  
**Date**: 2025-10-15  
**Status**: Complete

## Overview

This document defines the data structures for the restaurant landing page. Since this is a static site, data is stored in JSON format and loaded by the Flask application.

## Entities

### 1. Restaurant

Represents the breakfast restaurant's core information.

**Storage**: Hardcoded in template or configuration file

**Attributes**:

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `name_zh` | String | Yes | Restaurant name in Traditional Chinese | "花蓮傳統早餐店" |
| `name_en` | String | Yes | Restaurant name in English | "Hualien Traditional Breakfast" |
| `tagline_zh` | String | No | Tagline/slogan in Traditional Chinese | "來自花蓮的傳統美味，每日新鮮現做，品嘗最道地的台式早餐" |
| `tagline_en` | String | No | Tagline/slogan in English | "Traditional flavors from Hualien, freshly made daily" |
| `address_zh` | String | Yes | Full address in Traditional Chinese | "花蓮縣花蓮市" |
| `address_en` | String | Yes | Full address in English | "Hualien City, Hualien County, Taiwan" |
| `hours_zh` | String | Yes | Opening hours in Traditional Chinese | "週一至週日 早上 6:00 - 中午 12:00" |
| `hours_en` | String | Yes | Opening hours in English | "Monday - Sunday: 6:00 AM - 12:00 PM" |
| `phone` | String | No | Contact phone number | "+886-3-XXX-XXXX" |
| `email` | String | No | Contact email | "info@example.com" |
| `social_media` | Object | No | Social media links | See SocialMedia entity |

**Validation Rules**:
- `name_zh` and `name_en` must not be empty
- `phone` must match Taiwan phone number format if provided
- `email` must be valid email format if provided

**Example**:
```json
{
  "name_zh": "花蓮傳統早餐店",
  "name_en": "Hualien Traditional Breakfast",
  "tagline_zh": "來自花蓮的傳統美味，每日新鮮現做，品嘗最道地的台式早餐",
  "tagline_en": "Traditional flavors from Hualien, freshly made daily",
  "address_zh": "花蓮縣花蓮市",
  "address_en": "Hualien City, Hualien County, Taiwan",
  "hours_zh": "週一至週日 早上 6:00 - 中午 12:00",
  "hours_en": "Monday - Sunday: 6:00 AM - 12:00 PM",
  "phone": "+886-3-XXX-XXXX",
  "social_media": {
    "facebook": "https://facebook.com/example",
    "instagram": "https://instagram.com/example"
  }
}
```

---

### 2. MenuCategory

Represents a grouping of menu items (Main Dishes, Drinks, Sides).

**Storage**: `static/data/menu.json` (array of categories)

**Attributes**:

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | String | Yes | Unique identifier (kebab-case) | "main-dishes" |
| `name_zh` | String | Yes | Category name in Traditional Chinese | "主食" |
| `name_en` | String | Yes | Category name in English | "Main Dishes" |
| `order` | Integer | Yes | Display order (lower = first) | 1 |
| `items` | Array[MenuItem] | Yes | Menu items in this category | See MenuItem entity |

**Validation Rules**:
- `id` must be unique across all categories
- `order` must be positive integer
- `items` array must contain at least one MenuItem

**Example**:
```json
{
  "id": "main-dishes",
  "name_zh": "主食",
  "name_en": "Main Dishes",
  "order": 1,
  "items": [...]
}
```

---

### 3. MenuItem

Represents an individual dish or drink on the menu.

**Storage**: Nested within MenuCategory in `static/data/menu.json`

**Attributes**:

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | String | Yes | Unique identifier within category | "shaobing-youtiao" |
| `name_zh` | String | Yes | Dish name in Traditional Chinese | "燒餅夾油條" |
| `name_en` | String | No | Dish name in English (optional) | "Sesame Flatbread with Fried Dough" |
| `description_zh` | String | No | Description in Traditional Chinese | "" |
| `description_en` | String | No | Description in English | "" |
| `price` | Decimal | Yes | Price in New Taiwan Dollars (NT$) | 44.00 |
| `available` | Boolean | No | Whether item is currently available | true |
| `order` | Integer | No | Display order within category | 1 |

**Validation Rules**:
- `id` must be unique within the category
- `name_zh` must not be empty
- `price` must be positive decimal (2 decimal places)
- `price` must be >= 0
- `available` defaults to `true` if not specified

**Example**:
```json
{
  "id": "shaobing-youtiao",
  "name_zh": "燒餅夾油條",
  "name_en": "Sesame Flatbread with Fried Dough",
  "price": 44.00,
  "available": true,
  "order": 1
}
```

---

### 4. SocialMedia

Represents social media links for the restaurant.

**Storage**: Nested within Restaurant data

**Attributes**:

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `facebook` | String (URL) | No | Facebook page URL | "https://facebook.com/example" |
| `instagram` | String (URL) | No | Instagram profile URL | "https://instagram.com/example" |
| `line` | String (URL) | No | LINE official account URL | "https://line.me/R/ti/p/@example" |
| `google_maps` | String (URL) | No | Google Maps location URL | "https://maps.google.com/?q=..." |

**Validation Rules**:
- All URLs must be valid HTTPS URLs if provided
- At least one social media link recommended (not enforced)

**Example**:
```json
{
  "facebook": "https://facebook.com/hualienbreakfast",
  "instagram": "https://instagram.com/hualienbreakfast",
  "line": "https://line.me/R/ti/p/@hualienbreakfast"
}
```

---

## Complete Data Structure Example

### File: `static/data/menu.json`

```json
{
  "categories": [
    {
      "id": "main-dishes",
      "name_zh": "主食",
      "name_en": "Main Dishes",
      "order": 1,
      "items": [
        {
          "id": "shaobing-youtiao",
          "name_zh": "燒餅夾油條",
          "name_en": "Sesame Flatbread with Fried Dough",
          "price": 44.00,
          "available": true,
          "order": 1
        },
        {
          "id": "shaobing",
          "name_zh": "燒餅",
          "name_en": "Sesame Flatbread",
          "price": 22.00,
          "available": true,
          "order": 2
        },
        {
          "id": "danbing-youtiao",
          "name_zh": "蛋餅夾油條",
          "name_en": "Egg Crepe with Fried Dough",
          "price": 54.00,
          "available": true,
          "order": 3
        }
      ]
    },
    {
      "id": "drinks",
      "name_zh": "飲品",
      "name_en": "Drinks",
      "order": 2,
      "items": [
        {
          "id": "iced-black-tea",
          "name_zh": "冰紅茶",
          "name_en": "Iced Black Tea",
          "price": 22.00,
          "available": true,
          "order": 1
        },
        {
          "id": "soy-milk-sweet",
          "name_zh": "甜豆漿.熱.溫.冰",
          "name_en": "Sweet Soy Milk (Hot/Warm/Iced)",
          "price": 27.00,
          "available": true,
          "order": 2
        }
      ]
    },
    {
      "id": "sides",
      "name_zh": "配菜",
      "name_en": "Sides",
      "order": 3,
      "items": [
        {
          "id": "scallion-egg",
          "name_zh": "蔥蛋",
          "name_en": "Scallion Egg",
          "price": 22.00,
          "available": true,
          "order": 1
        },
        {
          "id": "fried-egg",
          "name_zh": "荷包蛋.半熟.全熟",
          "name_en": "Fried Egg (Soft/Hard)",
          "price": 15.00,
          "available": true,
          "order": 2
        }
      ]
    }
  ]
}
```

---

## Data Access Patterns

### Loading Menu Data (Flask)

```python
import json
from flask import Flask

app = Flask(__name__)

# Load menu data on application startup
with open('static/data/menu.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

@app.route('/')
def index():
    # Sort categories by order
    categories = sorted(menu_data['categories'], key=lambda x: x['order'])
    
    # Sort items within each category
    for category in categories:
        category['items'] = sorted(category['items'], key=lambda x: x.get('order', 999))
    
    return render_template('index.html', categories=categories)
```

### Template Usage (Jinja2)

```jinja2
{% for category in categories %}
  <section>
    <h3>{{ category.name_zh }} {{ category.name_en }}</h3>
    <div class="grid">
      {% for item in category.items %}
        {% if item.available %}
          <div class="menu-item">
            <span>{{ item.name_zh }}</span>
            <span class="price">NT$ {{ "%.2f"|format(item.price) }}</span>
          </div>
        {% endif %}
      {% endfor %}
    </div>
  </section>
{% endfor %}
```

---

## Data Lifecycle

### Creation
- Menu data created manually by editing `menu.json`
- Restaurant data hardcoded in template or config file
- No create operations needed in application

### Read
- Menu data loaded once on application startup (cached in memory)
- Re-read on server restart or reload
- No dynamic reads from file during request handling (performance)

### Update
- Manual updates to `menu.json` file
- Requires application restart to pick up changes
- Alternative: Implement file watcher for auto-reload in development

### Delete
- Items can be marked `"available": false` to hide without deleting
- Physical deletion requires editing JSON file
- No soft-delete mechanism needed for this simple use case

---

## State Transitions

### MenuItem Availability

```
[Created] → available: true (default)
    ↓
[Hidden] → available: false (temporarily unavailable)
    ↓
[Restored] → available: true (back in stock)
```

**Business Rules**:
- Unavailable items are not displayed on the page
- No historical tracking of availability changes
- Price changes require manual JSON edit

---

## Data Validation

### JSON Schema (menu.json)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["categories"],
  "properties": {
    "categories": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["id", "name_zh", "name_en", "order", "items"],
        "properties": {
          "id": { "type": "string", "pattern": "^[a-z0-9-]+$" },
          "name_zh": { "type": "string", "minLength": 1 },
          "name_en": { "type": "string", "minLength": 1 },
          "order": { "type": "integer", "minimum": 1 },
          "items": {
            "type": "array",
            "minItems": 1,
            "items": {
              "type": "object",
              "required": ["id", "name_zh", "price"],
              "properties": {
                "id": { "type": "string", "pattern": "^[a-z0-9-]+$" },
                "name_zh": { "type": "string", "minLength": 1 },
                "name_en": { "type": "string" },
                "price": { "type": "number", "minimum": 0 },
                "available": { "type": "boolean", "default": true },
                "order": { "type": "integer", "minimum": 1 }
              }
            }
          }
        }
      }
    }
  }
}
```

### Validation Implementation

```python
import json
import jsonschema

def validate_menu_data(menu_file='static/data/menu.json', schema_file='static/data/menu.schema.json'):
    """Validate menu.json against JSON schema"""
    with open(menu_file, 'r', encoding='utf-8') as f:
        menu_data = json.load(f)
    
    with open(schema_file, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    try:
        jsonschema.validate(menu_data, schema)
        return True, "Menu data is valid"
    except jsonschema.ValidationError as e:
        return False, f"Menu data validation error: {e.message}"

# Run validation on startup
is_valid, message = validate_menu_data()
if not is_valid:
    raise ValueError(message)
```

---

## Relationships

```
Restaurant (1) --- (0..1) SocialMedia
                 |
                 +--- (displayed on) Landing Page

MenuCategory (1) --- (1..*) MenuItem
    |
    +--- (displayed on) Landing Page
```

**Notes**:
- No foreign key relationships (not a relational database)
- Menu structure is hierarchical (categories contain items)
- All relationships are in-memory only (loaded from JSON)

---

## Performance Considerations

### Data Size Estimates

| Entity | Count | Size per Item | Total Size |
|--------|-------|---------------|------------|
| Restaurant | 1 | ~500 bytes | 500 bytes |
| MenuCategory | 3 | ~100 bytes | 300 bytes |
| MenuItem | ~30-40 | ~150 bytes | 4.5-6 KB |
| **Total** | | | **~7 KB** |

**Impact**:
- Entire menu dataset fits in < 10KB JSON
- Loaded once on startup, cached in memory
- Negligible memory footprint
- No database queries or I/O during request handling
- Extremely fast read performance

### Optimization Strategies

1. **Caching**: Menu data loaded once, stored in application memory
2. **Pre-sorting**: Sort categories and items on load, not on each request
3. **Lazy Loading**: Not needed (data is small enough to load all at once)
4. **Compression**: JSON can be gzipped if served as API (not applicable for template rendering)

---

## Future Extensibility

### Potential Additions (Not in MVP)

1. **Images per MenuItem**:
   ```json
   {
     "image_url": "/static/images/menu/shaobing-youtiao.jpg",
     "image_alt_zh": "燒餅夾油條照片",
     "image_alt_en": "Photo of sesame flatbread with fried dough"
   }
   ```

2. **Allergen Information**:
   ```json
   {
     "allergens": ["gluten", "soy"],
     "dietary_tags": ["vegetarian"]
   }
   ```

3. **Nutritional Information**:
   ```json
   {
     "calories": 350,
     "protein_g": 12,
     "carbs_g": 45
   }
   ```

4. **Multi-language Support** (beyond Chinese/English):
   ```json
   {
     "name_ja": "焼餅夾油条",
     "name_ko": "샤오빙 요우티아오"
   }
   ```

5. **Dynamic Pricing** (time-based, seasonal):
   ```json
   {
     "price_regular": 44.00,
     "price_weekend": 48.00,
     "price_effective_from": "2025-01-01"
   }
   ```

**Note**: These extensions are not needed for MVP but can be added by updating the JSON structure and templates.

---

## Conclusion

The data model is intentionally simple and flat, optimized for:
- ✅ Static content serving (no database overhead)
- ✅ Easy manual editing (restaurant staff can update menu.json)
- ✅ Fast read performance (in-memory caching)
- ✅ Clear bilingual structure (separate fields for Chinese and English)
- ✅ Extensibility (JSON structure easily expandable)

This model aligns with the Static-First Architecture principle and meets all requirements from the feature specification.
