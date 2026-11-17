# Page generators

Service pages and blog posts are generated from content in these scripts.
Edit the content here, then rebuild from the repo root:

    python _tools/build_pages.py .
    python _tools/build_blog.py .

Hand edits to the generated `index.html` files will be overwritten on rebuild.
New blog posts also need a `<url>` entry in `sitemap.xml`.
Folders starting with `_` are not published by GitHub Pages.
