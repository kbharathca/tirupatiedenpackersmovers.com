# Tirupati Eden Packers Cloudflare Pages Deployment

This project is ready to publish as a static site on Cloudflare Pages.

## Cloudflare Pages Settings

- Framework preset: `None`
- Build command: leave blank
- Build output directory: `.`
- Root directory: `/`

If Cloudflare Pages requires a non-empty build command in your workflow, you can use:

```sh
echo "No build step required"
```

The site uses:

- folder-based pages for clean URLs such as `/about-us/`, `/services/`, `/gallery/`, and `/contact/`
- `_redirects` to permanently redirect old `.html` URLs to clean URLs
- `_headers` for basic cache and security headers
- `sitemap.xml` and `robots.txt` for search engine discovery

## Publish Steps

1. Push this repository to GitHub.
2. In Cloudflare Pages, create a new project from this repository.
3. Set the build options shown above.
4. Deploy.
5. Connect the custom domain `tirupatiedenpackersmovers.com` in Cloudflare Pages.

## Output Structure

- Home page: [index.html](./index.html)
- Clean URL pages:
  - [about-us/index.html](./about-us/index.html)
  - [services/index.html](./services/index.html)
  - [gallery/index.html](./gallery/index.html)
  - [contact/index.html](./contact/index.html)
