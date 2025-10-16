# Deployment Guide

This guide provides step-by-step instructions for deploying the 無名台式早餐店 (Wuming Taiwanese Breakfast) web application to production.

## Deployment Platform: Render.com

We recommend using [Render.com](https://render.com) for deployment due to its:
- Free tier with automatic HTTPS
- Easy GitHub integration
- Zero-configuration Flask deployment
- Custom domain support

## Prerequisites

- GitHub account
- Render.com account (free)
- Your code pushed to a GitHub repository

## Step 1: Prepare Your Application

1. **Ensure all dependencies are in `requirements.txt`**:
   ```
   Flask==3.0.0
   pytest==7.4.0
   pytest-flask==1.3.0
   ```

2. **Verify your app runs locally**:
   ```bash
   python app.py
   ```

3. **Push your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

## Step 2: Deploy to Render

1. **Sign in to Render.com**
   - Go to https://render.com
   - Sign in with your GitHub account

2. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository containing your Flask app

3. **Configure the Web Service**
   - **Name**: `wuming-breakfast` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: `Free`

4. **Environment Variables** (if needed)
   - Click "Advanced" → "Add Environment Variable"
   - Add any necessary environment variables:
     - `FLASK_ENV=production`
     - `PORT=5000` (Render will override this automatically)

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - Wait for the deployment to complete (usually 2-5 minutes)

## Step 3: Verify Deployment

1. **Check the deployment logs** in the Render dashboard
2. **Visit your app** at: `https://<your-service-name>.onrender.com`
3. **Test critical functionality**:
   - Homepage loads correctly
   - Menu displays all items
   - Contact information is visible
   - Google Maps embed works
   - Mobile responsive design works
   - Phone and WhatsApp links work

## Step 4: Custom Domain (Optional)

1. **Purchase a domain** from a registrar (e.g., Namecheap, GoDaddy)

2. **Add custom domain in Render**:
   - Go to your service settings
   - Click "Custom Domains"
   - Add your domain (e.g., `wumingbreakfast.com`)

3. **Update DNS records** at your registrar:
   - Add a CNAME record:
     - Name: `www` or `@`
     - Value: `<your-service-name>.onrender.com`

4. **Enable HTTPS**:
   - Render automatically provisions SSL certificates
   - Wait for DNS propagation (up to 24 hours)

## Step 5: Enable Auto-Deploy

1. In Render dashboard, go to your service
2. Under "Settings" → "Build & Deploy"
3. Enable "Auto-Deploy" for `main` branch
4. Now every push to `main` will automatically deploy

## Production Checklist

Before going live, verify:

- [ ] All tests passing (`pytest tests/`)
- [ ] Menu data is accurate and up-to-date
- [ ] Restaurant contact information is correct
- [ ] Google Maps location is accurate
- [ ] Phone numbers work correctly
- [ ] WhatsApp link is functional
- [ ] Business hours are current
- [ ] 404 page displays correctly
- [ ] SEO meta tags are present
- [ ] Structured data (JSON-LD) is valid
- [ ] Mobile responsive design works
- [ ] Page load time is acceptable (<3 seconds)
- [ ] robots.txt and sitemap.xml are accessible

## Monitoring and Maintenance

### Check Application Health
- Visit `/health` endpoint to verify server status
- Monitor Render dashboard for uptime and errors

### Update Menu
1. Edit `static/data/menu.json`
2. Commit and push changes
3. Auto-deploy will update production

### Update Restaurant Information
1. Edit `static/data/menu.json` → `restaurant` object
2. Update templates if needed
3. Commit, push, and deploy

## Troubleshooting

### App won't start
- Check Render logs for errors
- Verify `requirements.txt` is complete
- Ensure `app.py` has correct Flask app configuration

### Static files not loading
- Verify files are in `static/` directory
- Check file paths in templates use `url_for('static', filename='...')`

### Google Maps not showing
- Verify iframe src URL is correct
- Check if maps are blocked by browser extensions
- Ensure HTTPS is enabled (required for maps embed)

### Performance issues
- Consider upgrading from Render free tier
- Enable Tailwind CLI build process (see `docs/CSS_OPTIMIZATION.md`)
- Optimize images (compress, use WebP format)

## Alternative Deployment Options

### Heroku
- Similar to Render, with paid plans
- Requires `Procfile`: `web: python app.py`

### DigitalOcean App Platform
- More control, slightly more complex
- Good for scaling beyond free tier

### Traditional VPS (DigitalOcean, AWS, etc.)
- Full control, requires more setup
- Use Gunicorn + Nginx for production
- Example: `gunicorn -w 4 -b 0.0.0.0:8000 app:app`

## Security Considerations

1. **Keep dependencies updated**:
   ```bash
   pip list --outdated
   pip install --upgrade Flask
   ```

2. **Use environment variables** for sensitive data:
   - API keys
   - Database credentials (if added later)

3. **Enable HTTPS** (automatic on Render)

4. **Monitor for vulnerabilities**:
   ```bash
   pip install safety
   safety check
   ```

## Support

For issues or questions:
- Check Render documentation: https://render.com/docs
- Review Flask documentation: https://flask.palletsprojects.com/
- Contact repository maintainer

---

**Last Updated**: January 2025
