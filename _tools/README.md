# Page generators

Service pages and blog posts are generated from content in these scripts.
Edit the content here, then rebuild from the repo root:

    python _tools/build_pages.py .
    python _tools/build_blog.py .

Hand edits to the generated `index.html` files will be overwritten on rebuild.
New blog posts also need a `<url>` entry in `sitemap.xml`.
Folders starting with `_` are not published by GitHub Pages.

## Blog posts

- Give each new post `date="YYYY-MM-DD"` (defaults to 2026-11-17). The blog lists newest first.
- A post's filter topic comes from its `service` argument (see `TOPICS` in build_blog.py).

## Shared pieces

- `common.py` holds the nav, footer, contact form, fonts, phone/email and Web3Forms key used by every generated page.
- `build_pages.py` also writes `privacy/index.html`.
- `build_blog.py` also refreshes the "From the Blog" section on the homepage (between the LATEST-POSTS markers in index.html).
- `assets/site.js` handles the menu, all contact forms and analytics. Turn analytics on by setting `GOATCOUNTER_CODE` at the top of that file.
