#!/usr/bin/env python3
"""Generate the Nexus42 AI 'AI Tech Lead' employment offer letter as a PDF.

Nexus42 is a fictional, G42-inspired Abu Dhabi AI company created for this
mock offer document. The brand mark is drawn as vector graphics directly on
the page canvas so the letterhead renders crisply at any zoom level.
"""
import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
    TableStyle, KeepTogether, HRFlowable, Flowable,
)

# ---- Brand palette ---------------------------------------------------------
NAVY     = HexColor(0x0B1F3A)
DEEPBLUE = HexColor(0x16406E)
MIDBLUE  = HexColor(0x0E2A52)
TEAL     = HexColor(0x12B5BC)
CYAN     = HexColor(0x35E0E6)
GOLD     = HexColor(0xC9A24B)
GREY     = HexColor(0x5A6B7B)
LGREY    = HexColor(0x9AA7B4)
RULE     = HexColor(0xD8DEE6)
INK      = HexColor(0x1B2733)

PAGE_W, PAGE_H = A4
LEFT = RIGHT = 1.9 * cm

# ---------------------------------------------------------------------------
def draw_spaced(c, x, y, text, font, size, extra):
    """drawString with manual letter-spacing (Canvas.setCharSpace is absent)."""
    c.setFont(font, size)
    cx = x
    for ch in text:
        c.drawString(cx, y, ch)
        cx += c.stringWidth(ch, font, size) + extra


def draw_logo(c, cx, cy, R, wordmark=True):
    """Draw the Nexus42 emblem centred at (cx, cy) with circumradius R."""
    # flat-top hexagon vertices (angles 0,60,...,300)
    pts = [(cx + R * math.cos(math.radians(a)),
            cy + R * math.sin(math.radians(a))) for a in range(0, 360, 60)]

    c.saveState()
    p = c.beginPath()
    p.moveTo(*pts[0])
    for x, y in pts[1:]:
        p.lineTo(x, y)
    p.close()
    c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(cx - R, cy + R, cx + R, cy - R,
                     (DEEPBLUE, MIDBLUE, NAVY), positions=(0.0, 0.55, 1.0),
                     extend=True)
    c.restoreState()

    # crisp edge
    c.saveState()
    c.setStrokeColor(CYAN)
    c.setLineWidth(R * 0.052)
    c.setLineJoin(1)
    p2 = c.beginPath()
    p2.moveTo(*pts[0])
    for x, y in pts[1:]:
        p2.lineTo(x, y)
    p2.close()
    c.drawPath(p2, stroke=1, fill=0)
    c.restoreState()

    # neural nodes (triangle) inside the hexagon
    nodes = [(cx,             cy + 0.41 * R, GOLD),
             (cx - 0.36 * R,  cy - 0.28 * R, CYAN),
             (cx + 0.36 * R,  cy - 0.28 * R, CYAN)]
    c.saveState()
    c.setStrokeColor(CYAN)
    c.setLineWidth(R * 0.04)
    c.setStrokeAlpha(0.7)
    for i in range(3):
        for j in range(i + 1, 3):
            c.line(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1])
    c.setStrokeAlpha(1)
    for x, y, col in nodes:
        c.setFillColor(col); c.setFillAlpha(0.28)
        c.circle(x, y, R * 0.205, stroke=0, fill=1)      # glow
        c.setFillAlpha(1)
        c.circle(x, y, R * 0.125, stroke=0, fill=1)       # node
    c.restoreState()

    if not wordmark:
        return
    # wordmark to the right of the emblem
    c.saveState()
    fs = R * 1.30
    base = cy - fs * 0.34
    x = cx + R + R * 0.72
    c.setFont("Helvetica-Bold", fs)
    c.setFillColor(NAVY)
    c.drawString(x, base, "NEXUS")
    w = c.stringWidth("NEXUS", "Helvetica-Bold", fs)
    c.setFillColor(GOLD)
    c.drawString(x + w, base, "42")
    # tagline
    tfs = R * 0.34
    c.setFillColor(GREY)
    draw_spaced(c, x + 1, base - tfs * 1.7, "SOVEREIGN INTELLIGENCE",
                "Helvetica-Bold", tfs, tfs * 0.42)
    c.restoreState()


def draw_signature(c, x, y, s=1.0):
    """A flowing, abstract cursive mark (not any real person's signature)."""
    c.saveState()
    c.setStrokeColor(HexColor(0x10305A))
    c.setLineWidth(1.7); c.setLineCap(1); c.setLineJoin(1)
    p = c.beginPath()
    p.moveTo(x, y)
    p.curveTo(x + 8 * s, y + 34 * s, x + 30 * s, y + 38 * s, x + 34 * s, y + 8 * s)
    p.curveTo(x + 37 * s, y - 12 * s, x + 20 * s, y - 6 * s, x + 26 * s, y + 10 * s)
    p.curveTo(x + 33 * s, y + 30 * s, x + 55 * s, y + 24 * s, x + 62 * s, y + 4 * s)
    p.curveTo(x + 70 * s, y - 14 * s, x + 80 * s, y + 22 * s, x + 94 * s, y + 12 * s)
    p.curveTo(x + 106 * s, y + 5 * s, x + 110 * s, y + 24 * s, x + 122 * s, y + 14 * s)
    p.curveTo(x + 134 * s, y + 6 * s, x + 144 * s, y + 18 * s, x + 156 * s, y + 5 * s)
    c.drawPath(p, stroke=1, fill=0)
    p2 = c.beginPath()
    p2.moveTo(x - 2 * s, y - 10 * s)
    p2.curveTo(x + 52 * s, y - 19 * s, x + 112 * s, y - 16 * s, x + 162 * s, y - 7 * s)
    c.drawPath(p2, stroke=1, fill=0)
    c.restoreState()


def draw_stamp(c, cx, cy, r, angle=-9):
    """A fictional round company seal for Nexus42."""
    ink = HexColor(0x15517F)
    c.saveState()
    c.translate(cx, cy); c.rotate(angle)
    c.setStrokeColor(ink); c.setFillColor(ink)
    c.setStrokeAlpha(0.72); c.setFillAlpha(0.72)
    c.setLineWidth(1.9); c.circle(0, 0, r, stroke=1, fill=0)
    c.setLineWidth(0.9); c.circle(0, 0, r * 0.72, stroke=1, fill=0)
    # divider with end dots
    c.setLineWidth(0.8)
    c.line(-r * 0.5, 0, r * 0.5, 0)
    c.circle(-r * 0.5, 0, r * 0.04, stroke=0, fill=1)
    c.circle(r * 0.5, 0, r * 0.04, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", r * 0.22)
    c.drawCentredString(0, r * 0.30, "NEXUS42")
    c.setFont("Helvetica", r * 0.135)
    c.drawCentredString(0, r * 0.14, "AI HOLDING PJSC")
    c.setFont("Helvetica-Bold", r * 0.16)
    c.drawCentredString(0, -r * 0.16, "ABU DHABI")
    c.setFont("Helvetica", r * 0.135)
    c.drawCentredString(0, -r * 0.34, "U.A.E.")
    c.setStrokeAlpha(1); c.setFillAlpha(1)
    c.restoreState()


class SignBlock(Flowable):
    """Inline signature mark + company stamp for the 'signed by the company' look."""
    def __init__(self, width, height=66):
        Flowable.__init__(self)
        self.width = width; self.height = height

    def wrap(self, aw, ah):
        return (self.width, self.height)

    def draw(self):
        draw_signature(self.canv, 6, 30, 1.0)
        draw_stamp(self.canv, 232, 33, 33, angle=-9)


def header_footer(c, doc):
    c.saveState()
    # ---- header ----
    draw_logo(c, LEFT + 17, PAGE_H - 50, 17)
    # company block, right aligned
    c.setFont("Helvetica-Bold", 8.2); c.setFillColor(NAVY)
    c.drawRightString(PAGE_W - RIGHT, PAGE_H - 40,
                      "Nexus42 Artificial Intelligence Holding PJSC")
    c.setFont("Helvetica", 7.4); c.setFillColor(GREY)
    for i, line in enumerate(["Capital Gate, 12th Floor, Al Khaleej Al Arabi St, Abu Dhabi, UAE",
                              "people@nexus42.ai  ·  +971 2 555 0042  ·  nexus42.ai"]):
        c.drawRightString(PAGE_W - RIGHT, PAGE_H - 51 - i * 10, line)
    # rule (navy + gold accent)
    y = PAGE_H - 72
    c.setStrokeColor(NAVY); c.setLineWidth(1.1)
    c.line(LEFT, y, PAGE_W - RIGHT, y)
    c.setStrokeColor(GOLD); c.setLineWidth(1.1)
    c.line(LEFT, y - 2.4, LEFT + 78, y - 2.4)

    # ---- footer ----
    fy = 52
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    c.line(LEFT, fy, PAGE_W - RIGHT, fy)
    c.setFont("Helvetica", 6.9); c.setFillColor(LGREY)
    c.drawString(LEFT, fy - 11,
                 "Nexus42 Artificial Intelligence Holding PJSC  ·  Licence CN-2310045  ·  Capital Gate, Al Khaleej Al Arabi Street, Abu Dhabi, UAE")
    c.drawString(LEFT, fy - 20,
                 "This document is private and confidential and is intended solely for the named addressee.")
    c.setFont("Helvetica-Bold", 6.9); c.setFillColor(GREY)
    c.drawRightString(PAGE_W - RIGHT, fy - 11, "Page %d" % doc.page)
    c.restoreState()


# ---- styles ----------------------------------------------------------------
body = ParagraphStyle("body", fontName="Helvetica", fontSize=9.3, leading=14.2,
                      textColor=INK, alignment=TA_JUSTIFY, spaceAfter=7)
small = ParagraphStyle("small", parent=body, fontSize=8.6, leading=12.6, spaceAfter=2)
h = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9.6, leading=13,
                   textColor=NAVY, spaceBefore=6, spaceAfter=3)
meta = ParagraphStyle("meta", fontName="Helvetica", fontSize=8.6, leading=12.6,
                      textColor=GREY)
confidential = ParagraphStyle("conf", fontName="Helvetica-Bold", fontSize=8,
                              textColor=GOLD, spaceAfter=2)
title = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=13.5,
                       leading=17, textColor=NAVY, spaceBefore=4, spaceAfter=8)
sig = ParagraphStyle("sig", fontName="Helvetica", fontSize=9.3, leading=13,
                     textColor=INK)


def bullet(txt):
    return Paragraph(
        '<font color="#12B5BC">▪</font>&nbsp;&nbsp;' + txt,
        ParagraphStyle("b", parent=body, leftIndent=12, spaceAfter=3,
                       alignment=TA_JUSTIFY))


def build(path):
    doc = BaseDocTemplate(
        path, pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
        topMargin=2.85 * cm, bottomMargin=2.45 * cm,
        title="Employment Offer — AI Tech Lead", author="Nexus42 AI")
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame],
                                       onPage=header_footer)])

    s = []
    s.append(Paragraph("PRIVATE &amp; CONFIDENTIAL", confidential))
    ref = Table([[Paragraph("Ref:&nbsp; NX42/HR/OFR/2026/0418", meta),
                  Paragraph("Date:&nbsp; 16 June 2026", ParagraphStyle(
                      "r", parent=meta, alignment=TA_RIGHT))]],
                colWidths=[doc.width * 0.5, doc.width * 0.5])
    ref.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                             ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                             ("TOPPADDING", (0, 0), (-1, -1), 0),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    s.append(ref)
    s.append(Spacer(1, 9))
    s.append(Paragraph("Diego Martín Maeso<br/>Avenida de Asturias 31, 1A<br/>"
                       "34880 Guardo (Palencia)<br/>España", meta))
    s.append(Spacer(1, 12))
    s.append(Paragraph("Dear Diego Martín Maeso,", body))
    s.append(Paragraph("RE: OFFER OF EMPLOYMENT — AI TECH LEAD", title))

    s.append(Paragraph(
        "We are delighted to extend to you an offer of employment with "
        "<b>Nexus42 Artificial Intelligence Holding PJSC</b> (“Nexus42” "
        "or the “Company”). Following our selection process, the "
        "Executive Committee has approved your appointment to a senior "
        "technical leadership role within our Foundation Models &amp; AI "
        "Platform division. This letter sets out the principal terms of our "
        "offer.", body))

    s.append(Paragraph("1.&nbsp; Position and Reporting", h))
    s.append(Paragraph(
        "You will be employed as <b>AI Tech Lead</b>, reporting to the Vice "
        "President, AI Engineering. You will lead a multidisciplinary team "
        "responsible for the design, training and large-scale deployment of "
        "the Company’s foundation models and applied AI platforms, and "
        "will set technical direction, architecture and engineering standards "
        "across the division.", body))

    s.append(Paragraph("2.&nbsp; Nature and Term of Contract", h))
    s.append(Paragraph(
        "Your employment is offered on a fixed-term basis for an <b>initial "
        "period of eighteen (18) months</b> (the “Initial Term”), "
        "commencing on the Commencement Date and renewable by mutual written "
        "agreement. The contract is governed by UAE Federal Decree-Law No. 33 "
        "of 2021 (the UAE Labour Law) and its implementing regulations.", body))

    s.append(Paragraph("3.&nbsp; Commencement Date and Place of Work", h))
    s.append(Paragraph(
        "Your Commencement Date is anticipated to be <b>1 September 2026</b>, "
        "or such other date as may be mutually agreed in writing. Your "
        "principal place of work will be the Company’s headquarters at "
        "Capital Gate, Al Khaleej Al Arabi Street, Abu Dhabi, United Arab "
        "Emirates, with hybrid working "
        "available in accordance with Company policy.", body))

    s.append(Paragraph("4.&nbsp; Probationary Period", h))
    s.append(Paragraph(
        "The first six (6) months of the Initial Term shall constitute a "
        "probationary period, during which either party may terminate the "
        "employment in accordance with the UAE Labour Law.", body))

    s.append(Paragraph("5.&nbsp; Remuneration", h))
    s.append(Paragraph(
        "Your <b>annual base salary</b> will be <b>AED 3,000,000</b> "
        "(three million United Arab Emirates Dirhams), equivalent to "
        "approximately <b>EUR 750,000</b> per annum at an indicative "
        "reference rate of EUR 1.00 = AED 4.00. <b>In addition to your base "
        "salary, and separately from it</b>, you will receive the cash "
        "allowances set out below. All amounts are paid in UAE Dirhams "
        "(AED), free of UAE personal income tax.", body))

    hdr = ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=8.6,
                         textColor=HexColor(0xFFFFFF), leading=11)
    cell = ParagraphStyle("td", fontName="Helvetica", fontSize=8.8,
                          textColor=INK, leading=11)
    cellr = ParagraphStyle("tdr", parent=cell, alignment=TA_RIGHT)
    cellb = ParagraphStyle("tb", parent=cell, fontName="Helvetica-Bold")
    cellbr = ParagraphStyle("tbr", parent=cellb, alignment=TA_RIGHT)
    data = [
        [Paragraph("Component", hdr),
         Paragraph("Annual (AED)", ParagraphStyle("hr", parent=hdr, alignment=TA_RIGHT)),
         Paragraph("Monthly (AED)", ParagraphStyle("hr2", parent=hdr, alignment=TA_RIGHT))],
        [Paragraph("Base salary", cell), Paragraph("3,000,000", cellr), Paragraph("250,000", cellr)],
        [Paragraph("Housing allowance <i>(in addition to salary)</i>", cell), Paragraph("600,000", cellr), Paragraph("50,000", cellr)],
        [Paragraph("Transport allowance <i>(in addition to salary)</i>", cell), Paragraph("120,000", cellr), Paragraph("10,000", cellr)],
        [Paragraph("Total annual cash package", cellb), Paragraph("3,720,000", cellbr), Paragraph("310,000", cellbr)],
    ]
    t = Table(data, colWidths=[doc.width * 0.5, doc.width * 0.25, doc.width * 0.25])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("BACKGROUND", (0, 4), (-1, 4), HexColor(0xEFF3F7)),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, NAVY),
        ("LINEBELOW", (0, 1), (-1, 3), 0.4, RULE),
        ("LINEABOVE", (0, 4), (-1, 4), 0.8, GOLD),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    s.append(t)
    s.append(Spacer(1, 4))
    s.append(Paragraph(
        "Your base salary and allowances are payable monthly in arrears by "
        "bank transfer to a UAE account nominated by you. The total annual "
        "cash package above (AED 3,720,000, approximately EUR 930,000) is "
        "exclusive of the benefits set out in clause 7, which are provided "
        "in addition.", small))

    s.append(Paragraph("6.&nbsp; Performance Bonus and Long-Term Incentive", h))
    s.append(Paragraph(
        "You will be eligible for a discretionary annual performance bonus of "
        "up to 30% of your basic salary, subject to Company and individual "
        "performance, and will be invited to participate in the Company’s "
        "Long-Term Incentive Plan, details of which will be provided "
        "separately.", body))

    s.append(Paragraph("7.&nbsp; Benefits", h))
    s.append(bullet("30 calendar days of paid annual leave per year, in addition to UAE public holidays;"))
    s.append(bullet("comprehensive private medical insurance for you and your eligible dependents;"))
    s.append(bullet("annual return air tickets to your home country for you and your eligible dependents;"))
    s.append(bullet("a one-time relocation allowance and assistance with relocation to Abu Dhabi;"))
    s.append(bullet("UAE residence visa sponsorship for you and your eligible dependents;"))
    s.append(bullet("end-of-service gratuity calculated in accordance with the UAE Labour Law."))

    s.append(Paragraph("8.&nbsp; Working Hours", h))
    s.append(Paragraph(
        "Standard working hours are 40 hours per week, Monday to Friday, "
        "exclusive of breaks, together with the flexibility expected of a "
        "senior leadership position.", body))

    s.append(Paragraph("9.&nbsp; Confidentiality, Intellectual Property and Restrictive Covenants", h))
    s.append(Paragraph(
        "Your employment is conditional upon execution of the Company’s "
        "standard Confidentiality and Intellectual Property Assignment "
        "Agreement. All intellectual property created in the course of your "
        "employment shall vest in the Company. Reasonable post-termination "
        "confidentiality and non-solicitation obligations will apply.", body))

    s.append(Paragraph("10.&nbsp; Conditions Precedent", h))
    s.append(Paragraph(
        "This offer is conditional upon: (a) satisfactory completion of "
        "background, reference and security checks; (b) evidence of your right "
        "to be sponsored and to work in the UAE; (c) a satisfactory medical "
        "fitness examination; and (d) provision of attested copies of your "
        "academic and professional certificates.", body))

    s.append(Paragraph("11.&nbsp; Validity and Acceptance", h))
    s.append(Paragraph(
        "This offer is open for acceptance until <b>30 June 2026</b>. To "
        "accept, please sign and return the duplicate of this letter. This "
        "letter constitutes the principal terms of our offer and supersedes "
        "any prior discussions; a full employment contract will be issued upon "
        "acceptance.", body))

    s.append(Paragraph(
        "We are confident that your expertise will make a significant "
        "contribution to Nexus42’s mission to build sovereign, world-class "
        "artificial intelligence, and we look forward to welcoming you to the "
        "team.", body))

    s.append(Spacer(1, 10))
    sigblock = [
        Paragraph("Yours sincerely,", sig),
        SignBlock(doc.width, height=64),
        Paragraph("<b>Khalid Al Nuaimi</b>", sig),
        Paragraph("Group Chief Executive Officer", meta),
        Paragraph("For and on behalf of Nexus42 Artificial Intelligence Holding PJSC", meta),
    ]
    s.append(KeepTogether(sigblock))

    s.append(Spacer(1, 16))
    accept = [
        HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=6),
        Paragraph("<b>ACCEPTANCE</b>", ParagraphStyle("a", parent=h, spaceBefore=0)),
        Paragraph("I, <b>Diego Martín Maeso</b>, accept the offer of "
                  "employment on the terms set out in this letter.", body),
        Spacer(1, 14),
    ]
    acc_tbl = Table([[Paragraph("Signature: _____________________________", sig),
                      Paragraph("Date: ___________________", sig)]],
                    colWidths=[doc.width * 0.6, doc.width * 0.4])
    acc_tbl.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                                 ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    accept.append(acc_tbl)
    s.append(KeepTogether(accept))

    doc.build(s)
    print("wrote", path)


if __name__ == "__main__":
    build("/home/user/segment-anything-2/job-offer/Nexus42_Offer_AI-Tech-Lead.pdf")
