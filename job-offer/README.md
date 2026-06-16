# Nexus42 AI — Sample Employment Offer (AI Tech Lead)

A realistic, professionally formatted **mock job-offer letter** with a custom logo.

> **Important — this is a mock/template, not a real offer.**
> **"Nexus42 AI"** is a **fictional, G42-inspired company** invented for this sample, with
> its **own original name and logo**. It is **not** the real G42 and deliberately does **not**
> use G42's name, logo, branding, or any real executive's name or signature. The signatory
> ("Khalid Al Nuaimi"), licence number, phone, seal and signature are all illustrative and
> fictional. Use this only as a template / design mockup — not to represent a genuine offer
> from any real organisation or to impersonate any real company or person.

## The offer at a glance
| | |
|---|---|
| **Company** | Nexus42 Artificial Intelligence Holding PJSC (fictional) — Capital Gate, Abu Dhabi, UAE |
| **Role** | AI Tech Lead — Foundation Models & AI Platform |
| **Contract** | Fixed-term, initial **18 months**, renewable |
| **Base salary** | **AED 3,000,000 / year** (≈ **EUR 750,000**, at an indicative EUR 1 = AED 4.00) |
| **Allowances (on top)** | Housing AED 600,000 + Transport AED 120,000 → **total cash package AED 3,720,000** (≈ EUR 930,000) |
| **Governing law** | UAE Federal Decree-Law No. 33 of 2021 (UAE Labour Law) |

## Files
| File | What it is |
|------|------------|
| `Nexus42_Offer_AI-Tech-Lead.pdf` | The finished, print-ready offer letter (3 pages). |
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
The **base salary** is AED 3,000,000 (≈ EUR 750,000 at an indicative **EUR 1 = AED 4.00**).
Housing (AED 600,000) and transport (AED 120,000) allowances are paid **on top of** the base
salary, for a total annual cash package of AED 3,720,000 (≈ EUR 930,000); the clause-7
benefits (medical, flights, relocation, visa, gratuity, leave) are additional again. Adjust
any figure or the exchange rate to taste.
