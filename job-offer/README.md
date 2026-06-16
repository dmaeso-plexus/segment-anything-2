# Nexus42 AI — Sample Employment Offer (AI Tech Lead)

A realistic, professionally formatted **mock job-offer letter** with a custom logo.

> **Note:** **"Nexus42 AI"** is a **fictional, G42-inspired company** invented for this
> sample (own name, own logo, own branding). It is **not** the real G42 and does not use
> G42's name or marks. Use this as a template / mockup, not as a genuine offer from any
> real organisation. The signatory, licence number, phone and address are illustrative.

## The offer at a glance
| | |
|---|---|
| **Company** | Nexus42 Artificial Intelligence Holding PJSC (fictional) — Abu Dhabi, UAE |
| **Role** | AI Tech Lead — Foundation Models & AI Platform |
| **Contract** | Fixed-term, initial **18 months**, renewable |
| **Compensation** | **AED 3,000,000 / year** (≈ **EUR 750,000**, at an indicative EUR 1 = AED 4.00) |
| **Governing law** | UAE Federal Decree-Law No. 33 of 2021 (UAE Labour Law) |

## Files
| File | What it is |
|------|------------|
| `Nexus42_Offer_AI-Tech-Lead.pdf` | The finished, print-ready offer letter (2 pages). |
| `offer-letter.html` | Editable version. Open in a browser, replace the `[ ... ]` fields, then **Print → Save as PDF**. |
| `assets/nexus42-logo.svg` | The logo as scalable vector (for editing / reuse). |
| `assets/nexus42-logo.png` | High-resolution transparent PNG of the logo. |
| `build_offer.py` | Script that generates the PDF (logo drawn as vector). |

## Editing
- **Quick edits** (candidate name, dates, numbers): edit `offer-letter.html` and re-print to PDF.
- **Regenerate the PDF** after changing `build_offer.py`:
  ```bash
  pip install reportlab
  python3 build_offer.py
  ```

## Compensation note
The package is quoted in **AED** as requested. AED 3,000,000 ≈ EUR 750,000 at an indicative
rate of **EUR 1 = AED 4.00**; adjust the figures if you want to pin them to a specific
exchange rate on the offer date.
