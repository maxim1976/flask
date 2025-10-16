# 無名台式早餐店 | Wuming Taiwanese Breakfast

A modern, bilingual web application for a traditional Taiwanese breakfast restaurant in Hualien, Taiwan.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Tests](https://img.shields.io/badge/tests-38%20passing-brightgreen.svg)

## 🌟 Features

### Core Functionality
- **Bilingual Support**: Traditional Chinese (zh-TW) and English throughout
- **Responsive Design**: Mobile-first design using Tailwind CSS
- **Menu Display**: 33 authentic Taiwanese breakfast items across 7 categories
- **Contact Information**: Phone, address, Google Maps integration
- **WhatsApp Integration**: Direct messaging for orders and inquiries

### SEO & Accessibility
- **Structured Data**: JSON-LD schema for search engines
- **SEO Optimized**: robots.txt and sitemap.xml
- **Accessibility**: WCAG 2.1 Level AA compliant
  - Skip-to-content link
  - ARIA labels
  - Keyboard navigation support
  - Screen reader friendly

### Performance & UX
- **Smooth Scrolling**: Enhanced navigation experience
- **Lazy Loading**: Optimized resource loading
- **Print Styles**: Menu optimized for printing
- **Mobile Menu**: Animated toggle with JavaScript
- **Fast Load Times**: <3 second target

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd flask
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open in browser**:
   Navigate to `http://127.0.0.1:5000`

## 🧪 Testing

Run the complete test suite (38 tests):

```bash
pytest tests/ -v
```

Run specific test categories:

```bash
# Basic functionality tests
pytest tests/test_app.py::test_index_route_returns_200 -v

# Menu display tests
pytest tests/test_app.py -k "menu" -v

# Accessibility tests
pytest tests/test_app.py -k "aria" -v
```

Test coverage:
```bash
pytest --cov=app tests/
```

## 📁 Project Structure

```
flask/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── static/                     # Static assets
│   ├── css/
│   │   └── custom.css         # Custom styles (smooth scrolling, print, etc.)
│   └── data/
│       └── menu.json          # Restaurant and menu data
├── templates/                  # Jinja2 templates
│   ├── base.html              # Base template with meta tags
│   ├── index.html             # Landing page
│   ├── 404.html               # Error page
│   └── components/
│       ├── header.html        # Navigation header
│       ├── hero.html          # Hero section
│       ├── menu.html          # Menu display
│       ├── menu_item.html     # Menu item card
│       └── footer.html        # Contact footer
├── tests/                      # Test suite
│   └── test_app.py            # 38 comprehensive tests
├── docs/                       # Documentation
│   └── DEPLOYMENT.md          # Deployment guide
└── specs/                      # Feature specifications
    └── 001-i-need-a/
        ├── spec.md            # Feature specification
        ├── plan.md            # Implementation plan
        ├── tasks.md           # Task breakdown
        └── ...
```

## 🍜 Menu Categories

The application features 33 authentic Taiwanese breakfast items:

1. **燒餅系列** (Shaobing Series) - 10 items
2. **蛋餅系列** (Egg Pancake Series) - 2 items
3. **蔥油餅系列** (Scallion Pancake Series) - 3 items
4. **饅頭包子系列** (Steamed Bun Series) - 5 items
5. **豆漿系列** (Soy Milk Series) - 7 items
6. **飲料** (Beverages) - 1 item
7. **配菜小點** (Side Dishes) - 5 items

Price range: NT$12 - NT$66

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.0**: Python web framework
- **Jinja2**: Templating engine
- **pytest 7.4.0**: Testing framework

### Frontend
- **Tailwind CSS**: Utility-first CSS framework (CDN)
- **Noto Sans TC**: Google Font for Traditional Chinese
- **Vanilla JavaScript**: Mobile menu toggle

### Data Storage
- **JSON**: Static file storage (`static/data/menu.json`)

### Deployment
- **Render.com**: Recommended platform (free tier)
- **GitHub**: Version control and auto-deploy

## 📍 Restaurant Information

**無名台式早餐店 | Wuming Taiwanese Breakfast**

- **Address**: No. 59, Dean 1st St (德安一街59號), Hualien City, Hualien County 970, Taiwan
- **Phone**: 03-8335408
- **WhatsApp**: +886-3-8335408
- **Hours**: 5:30 AM - 10:30 AM (Closed Mondays)
- **Cuisine**: Traditional Taiwanese Breakfast

## 🌐 API Endpoints

- `GET /` - Landing page
- `GET /health` - Health check (JSON)
- `GET /robots.txt` - SEO robots file
- `GET /sitemap.xml` - SEO sitemap
- `GET /favicon.ico` - Favicon endpoint
- `GET /static/*` - Static assets

## 🎨 Customization

### Update Menu
Edit `static/data/menu.json`:

```json
{
  "restaurant": {
    "name_zh": "餐廳名稱",
    "name_en": "Restaurant Name",
    ...
  },
  "categories": [
    {
      "name_zh": "分類名稱",
      "name_en": "Category Name",
      "items": [...]
    }
  ]
}
```

### Update Styles
Edit `static/css/custom.css` for custom styles beyond Tailwind.

### Update Colors
Modify Tailwind config in `templates/base.html`:

```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        'brand': { /* your color palette */ }
      }
    }
  }
}
```

## 📱 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🚀 Deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed deployment instructions.

Quick deploy to Render.com:
1. Push code to GitHub
2. Connect repository to Render
3. Configure build: `pip install -r requirements.txt`
4. Configure start: `python app.py`
5. Deploy!

## 📊 Test Coverage

Current test suite: **38 tests, 100% passing**

Test categories:
- ✅ Basic routes (3 tests)
- ✅ Menu data structure (3 tests)
- ✅ Component rendering (3 tests)
- ✅ Menu display (8 tests)
- ✅ Contact features (4 tests)
- ✅ SEO features (3 tests)
- ✅ Polish & optimization (8 tests)
- ✅ Accessibility (6 tests)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest tests/`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 Development Workflow

This project follows a structured development approach:

1. **Constitution** - Static Web App principles
2. **Specification** - Feature requirements
3. **Planning** - Implementation plan
4. **Execution** - 6-phase development:
   - Phase 1: Setup
   - Phase 2: Foundational
   - Phase 3: MVP
   - Phase 4: Menu Display
   - Phase 5: Contact Features
   - Phase 6: Polish & Optimization ✅

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Restaurant: 無名台式早餐店, Hualien, Taiwan
- Tailwind CSS for the excellent utility-first framework
- Flask team for the robust web framework
- Google Fonts for Noto Sans TC

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Email: [your-email@example.com]
- Phone: 03-8335408 (Restaurant)

---

**Built with ❤️ for authentic Taiwanese breakfast culture**

*Last Updated: January 2025*
