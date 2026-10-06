# Benton Caldwell — personal portfolio

A concise professional portfolio for Benton Caldwell, a Tulane economics student and founder of Biowalk. Built for a class assignment using his résumé, public LinkedIn information, and supplied photos.

## What visitors see

- A personal introduction and real portrait.
- Biowalk: purpose, founder responsibilities, $4,000 raised, working prototype, and 2026 Tulane Hult Prize win.
- Construction experience, led by Suffolk's summer 2026 internship.
- Practical skills supported by actual experience.
- Education, leadership, interests, email, LinkedIn, and a downloadable résumé.

## How the site works

`index.html` contains the words, images, links, and page sections. HTML gives them meaning: a main heading, navigation, articles, and a footer.

`style.css` controls the fonts, colors, spacing, and layout. Media queries change the layout on narrower screens so the columns stack on a phone.

`assets/` stores the four photos and original résumé PDF. The photos are served locally so the site does not depend on someone else's image hosting.

The Biowalk disclosure uses the browser's native `details` and `summary` elements. It works with a keyboard and needs no JavaScript. Contact links open an email app or LinkedIn; there is no form pretending to send a message.

## Why GitHub is useful

Git records snapshots called **commits**, including what changed and why. A **repository** is the project plus that history. GitHub hosts the repository online so work can be reviewed, shared, and restored. A **push** sends local commits to GitHub. A **pull request** lets someone review proposed changes before they join the main version.

GitHub Pages serves the website publicly. GitHub Actions runs the checks and publication steps in `.github/workflows/pages.yml` whenever a change is pushed to `main`. Pull requests run checks without publishing.

## Run and check locally

No package installation or build system is required.

```sh
python3 -m http.server 8765
python3 scripts/check_site.py
```

Open `http://localhost:8765` for the preview. The check validates local files and anchors, image attributes, basic metadata, and page landmarks. It is not a full accessibility audit.

## Publish on GitHub Pages

1. Create a new **public**, empty repository in your own GitHub account. `benton-caldwell-portfolio` is a suggested name. Do not add a generated README if pushing this existing repository.
2. Connect the local repository to the exact GitHub repository URL and push `main`. Preserve the existing commits so the history shows the original portfolio and the assignment improvements.
3. In the repository, go to **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Run **Check and publish portfolio** from Actions, or push a new change.
5. Wait for the workflow to finish, then open the public URL shown in Settings → Pages. Check it while signed out and on your phone.
6. Submit both the public repository URL and the published website URL through the course's submission system.

All website asset links are relative, so the site works beneath a repository path on GitHub Pages. The workflow publishes only the HTML, CSS, images, and résumé; the guide and scripts stay in the repository.

## Editing workflow

Make one meaningful change, preview it, run the checker, and commit with a short description of the actual change. Push to update the site. Keep real changes in history; don't manufacture commits to suggest work that never happened.

The initial local commits were created by Codex and are labeled accordingly. Future commits can use your own configured Git identity.

## Design and accessibility choices

- Editorial serif headings, forest green accents, and a consistent spacing system.
- One main heading, meaningful sections, a skip link, image descriptions, and visible keyboard focus.
- At least 44px-high principal navigation and action targets.
- Responsive layouts, reduced-motion support, image dimensions, lazy loading below the opening portrait, and no external fonts or scripts.
- Descriptive page title and search/social description metadata.
- Real content; no fabricated testimonials, employers, or project results.

## Sources and inspiration

- User-provided résumé and photos.
- [Benton Caldwell on LinkedIn](https://www.linkedin.com/in/benton-caldwell/).
- [Satz portfolio design reference](https://frame-supply.framer.website/templates/satz) and [Framer minimal templates](https://www.framer.com/marketplace/templates/categories/minimal/?page=1). The implementation is original; no paid template code was copied.
- [W3C accessibility checks](https://www.w3.org/WAI/test-evaluate/preliminary/).
- [GitHub Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

Photos and résumé belong to their respective owners. The Suffolk mark identifies a past employer and does not imply endorsement. No general reuse license is granted for personal assets.
