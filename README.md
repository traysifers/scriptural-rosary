# Scriptural Rosary

A one-screen phone app for praying the scriptural Rosary. It opens to the day's mysteries:

| Day | Mysteries |
| --- | --- |
| Monday, Saturday | Joyful |
| Tuesday, Friday | Sorrowful |
| Wednesday, Sunday | Glorious |
| Thursday | Luminous |

Each mystery shows its title, the fruit of the mystery (with the alternate naming in parentheses), and the Douay-Rheims scripture. When a mystery has more than one passage, the first is shown and buttons switch between them. Swipe left and right to move between mysteries, or tap the beads at the bottom. "Change" picks a different set.

## Files

- `public/` — the website. Only this folder is published.
  - `index.html` — the app (mysteries, fruits, passage references, layout).
  - `scripture.js` — Douay-Rheims verse text for the passages the app uses (generated).
  - `manifest.webmanifest`, icons — let the phone open it full screen from the home screen.
- `tools/import_dra.py` — regenerates `scripture.js`. It reads the passage list from `public/index.html`,
  so after changing a reference run: `python3 tools/import_dra.py`
- `tools/build_preview.py` — builds a single self-contained HTML file.

## Scripture text

Douay-Rheims Bible, Challoner revision (the text of the 1899 American edition), which is in the public domain.
The importer downloads it from the scrollmapper/bible_databases project on GitHub (`DRC.json`).

Douay-Rheims numbering follows the Vulgate, so some references differ from modern Bibles:
Judith 13:23, 25, 31 and Sirach (Ecclesiasticus) 24:24–27 for the Coronation, and John 6:51–59 for the Eucharist.

## Hosting

**GitHub Pages:** `.github/workflows/pages.yml` publishes `public/` on every push to `main`
(Settings → Pages → Source: GitHub Actions).

### Cloudflare (alternative)

Either setup publishes only `public/`, and `public/index.html` is what opens at the site's address.

- **Pages (Connect to Git):** framework preset None, build command empty, build output directory `public`.
- **Workers (Import a repository):** uses `wrangler.jsonc`; deploy command `npx wrangler deploy`, no build command.

Optionally protect it with Cloudflare Access (Zero Trust → Access → Applications) so only you can open it.
