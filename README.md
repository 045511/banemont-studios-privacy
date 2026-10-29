# BANEMONT STUDIOS privacy website

Prepared 28 October 2026. Publication-ready static notices for BANEMONT STUDIOS,
also published in app stores as BANEMONT. Contact: **info@banemont.org**.

## Live website

Published on GitHub Pages on 28 October 2026, with HTTPS enforced:

- [BANEMONT STUDIOS Privacy Policy](https://045511.github.io/banemont-studios-privacy/)
- [Astro Exit game notice](https://045511.github.io/banemont-studios-privacy/games/astro-exit.html)
- [Account and data deletion requests](https://045511.github.io/banemont-studios-privacy/delete-data.html)

The first Pages deployment completed successfully. All three pages and their
CSS/favicon returned HTTP 200 without authentication and exactly matched their
committed source. The email request page is active; this does not claim the
separate prepared automatic deletion backend has been deployed.

## Pages

- `index.html`: studio-wide privacy policy for games that link to it.
- `games/astro-exit.html`: current Astro Exit notice (`com.astroexit.game`).
- `delete-data.html`: prominent email account/data deletion request pathway.

This website contains only public notices, styling and their source. Keep it in
a **separate public repository**, never make the private game repository public
to obtain free Pages hosting. GitHub Pages is free for public repositories and
does not require a custom domain. The dedicated public repository is
[`045511/banemont-studios-privacy`](https://github.com/045511/banemont-studios-privacy).

## Publish with GitHub Pages

1. Create the separate public repository. Do not add secrets or game source.
2. Upload this directory's contents to its `main` branch. Keep `index.html` at
   the repository root, and preserve `games/` and `.nojekyll`.
3. In **Settings → Pages**, select **Deploy from a branch**, **main**, **/(root)**,
   then save. Use the default GitHub domain; enforce HTTPS where the control is
   available. No paid plan, custom domain or additional service is needed.
4. After GitHub reports a successful deployment, open all three public URLs and
   check links and email buttons in a signed-out browser. Only then use the actual
   URLs in Play Console or an app. This local package is not evidence of hosting.

The live URLs are:

```
https://045511.github.io/banemont-studios-privacy/
https://045511.github.io/banemont-studios-privacy/games/astro-exit.html
https://045511.github.io/banemont-studios-privacy/delete-data.html
```

Verify these addresses after enabling Pages. For Astro Exit's Play
privacy-policy field, use the game notice, which links the full studio policy;
for the separate deletion-resource field, use `delete-data.html` after publication.
The optional developer-website field can remain blank as previously requested.

Publication must be confirmed from the Pages deployment status and an actual
public page load. A local commit or repository upload alone does not prove the
site is available. This project does not change DNS or game-source visibility.

## Maintain

Edit `policy-content.json`, then regenerate the HTML:

```powershell
python build_site.py
python check_site.py
python -m http.server 8795 --bind 127.0.0.1 --directory .
```

Open `http://127.0.0.1:8795/` for local review. Generated files are committed so
Pages needs no custom build, external package, script runtime or paid service.
`PRIVACY_POLICY.md` is a readable review/export copy generated from the same
content. Update the revision date and notices when practices change. Review the
actual providers, audience, permissions and retention of each new game before
adding its notice; this policy is not blanket authorization for undisclosed
future data collection.

There are no analytics, third-party scripts, external fonts, tracking cookies,
browser storage or recovery-key forms added to this site. The deletion page uses
email links; it does not claim that the prepared automatic deletion API is live.
Email requests still require secure verification and actual fulfillment. GitHub
Pages logs connection information such as visitor IP addresses for security.

Security uses HTTPS from the host, local static assets, a restrictive CSP in HTML
and no-referrer metadata. GitHub Pages does not apply a Netlify-style `_headers`
file; no unsupported server header configuration is included or claimed.
The package deliberately excludes the earlier recovery-key web client until its
backend is deployed and verified.

## Source review

The wording was checked against the existing Astro Exit implementation and these
primary references on 28 October 2026:

- [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)
- [Google Play account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en)
- [Google Mobile Ads Android disclosure](https://developers.google.com/admob/android/next-gen/privacy/play-data-disclosure)
- [GitHub Pages hosting and connection logging](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Pages creation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [GitHub Pages HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)
- [Canadian meaningful consent guidance](https://www.priv.gc.ca/en/privacy-topics/privacy-for-businesses/appropriate-handling-of-personal-information/collecting-personal-information-and-consent/consent/gl_omc_201805/)

The notices identify the supplied studio/publisher brand and email. They do not
invent a registered legal entity, address, registration, representative, provider
retention deadline or legal compliance certification.
