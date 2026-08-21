from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

PAPER = HexColor("#F8F8F4")
INK = HexColor("#21272E")
STONE = HexColor("#5C6570")
ACCENT = HexColor("#196E6A")
LINE = HexColor("#DCDFD6")

W, H = letter
M = 0.6 * inch
c = canvas.Canvas("/home/claude/site/downloads/john-lague-resume.pdf", pagesize=letter)
c.setTitle("John LaGue — Resume")
c.setAuthor("John LaGue")

c.setFillColor(PAPER)
c.rect(0, 0, W, H, fill=1, stroke=0)

y = H - 0.72 * inch
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 25)
c.drawString(M, y, "John LaGue")
c.setFillColor(ACCENT)
c.setFont("Helvetica-Bold", 10)
c.drawRightString(W - M, y + 3, "COO at Trainwell")
y -= 15
c.setFillColor(STONE)
c.setFont("Courier", 8.3)
c.drawString(M, y, "Pittsburgh, PA  |  john@johnlague.com  |  johnlague.com  |  linkedin.com/in/john-lague")
y -= 14
c.setStrokeColor(LINE); c.setLineWidth(0.9); c.line(M, y, W - M, y)
y -= 16

# summary
c.setFillColor(STONE)
c.setFont("Helvetica", 9.2)
c.drawString(M, y, "Operator and growth leader with a data science background. Open to helping early stage companies with acquisition.")
y -= 22

def section(title, yy):
    c.setFillColor(ACCENT)
    c.setFont("Courier-Bold", 8.2)
    c.drawString(M, yy, title.upper())
    c.setStrokeColor(LINE); c.setLineWidth(0.6)
    tw = c.stringWidth(title.upper(), "Courier-Bold", 8.2)
    c.line(M + tw + 8, yy + 3, W - M, yy + 3)
    return yy - 16

# --- results strip ---
y = section("Selected results", y)
metrics = [("$1k \u2192 $10M ARR", "as first growth leader; $30M+ revenue since"),
           ("3 \u2192 125 employees", "scaled as COO at Trainwell")]
mx = M
for num, lab in metrics:
    c.setFillColor(INK); c.setFont("Courier-Bold", 13.5)
    c.drawString(mx, y, num)
    c.setFillColor(STONE); c.setFont("Helvetica", 8.4)
    c.drawString(mx, y - 12, lab)
    mx += (W - 2 * M) / 2
y -= 30

# --- experience ---
y = section("Experience", y)
JOBS = [
    ("Chief Operating Officer", "Trainwell", "Feb 2021 \u2013 Present", [
        "Drove B2C ARR from $1k to $10M as growth leader; company reached $30M+ revenue in the years since.",
        "Scaled the company from 3 to 125 employees.",
        "Acquired customers on both $0 and $6.5M marketing budgets.",
        "Supported execution of a large-scale partnership with Peloton.",
        "Own all marketing and growth, customer support, and operations.",
    ]),
    ("VP of Business Development", "Trainwell", "Feb 2020 \u2013 Nov 2021", [
        "First full-time hire. Found initial user traction using the Bullseye framework (Gabriel Weinberg, DuckDuckGo).",
    ]),
    ("Data Analyst", "PNC Bank", "Feb \u2013 Sep 2020", [
        "Analyzed millions of data points across home equity, mortgage, and credit products (Python, T-SQL, Hadoop).",
        "Key resource for the SBA Paycheck Protection Program; processed and approved hundreds of small-business loans.",
    ]),
    ("Founder", "PocketPosture", "Jul 2019 \u2013 Aug 2020", [
        "Ecommerce store for posture devices; broke even. A sandbox for unconventional marketing experiments.",
    ]),
    ("Co-founder & COO", "Community Phone (Y Combinator W19)", "Dec 2017 \u2013 Jul 2019", [
        "Affordable cell service (MVNO). Bootstrapped $0 \u2192 $300K ARR in year one. Front-page Boston Globe coverage.",
        "Wore many hats: sales, customer success, marketing, BD, analytics, retail management, and recruiting.",
    ]),
    ("Data Science Practicum Lead", "LA County Elections Dept.", "Nov 2017 \u2013 May 2018", [
        "Cut ballot collection times 12% in the 2018 primaries using the Google Maps API and k-means clustering.",
    ]),
    ("Teaching Assistant", "University of San Francisco", "Jan 2015 \u2013 Dec 2017", [
        "TA'd statistics, calculus, data science, and bioinformatics; lectured a graduate course as an undergraduate.",
    ]),
]
for role, org, when, bullets in JOBS:
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 10.6)
    c.drawString(M, y, role)
    rw = c.stringWidth(role, "Helvetica-Bold", 10.6)
    c.setFillColor(ACCENT); c.setFont("Helvetica", 9.6)
    c.drawString(M + rw + 6, y, "\u00b7 " + org)
    c.setFillColor(STONE); c.setFont("Courier", 7.8)
    c.drawRightString(W - M, y + 1, when)
    y -= 14
    c.setFont("Helvetica", 9.3)
    for b in bullets:
        c.setFillColor(ACCENT); c.drawString(M + 3, y, "\u2022")
        c.setFillColor(STONE); c.drawString(M + 12, y, b)
        y -= 13.4
    y -= 10

# --- bottom columns ---
y -= 2
col_y = y
c.setFillColor(ACCENT); c.setFont("Courier-Bold", 8.2)
c.drawString(M, col_y, "EDUCATION")
c.drawString(M + (W - 2 * M) * 0.36, col_y, "SKILLS")
c.drawString(M + (W - 2 * M) * 0.72, col_y, "PUBLICATIONS & AWARDS")
col_y -= 13

def wrapped(text, x, yy, width, font="Helvetica", size=8.6, leading=10.8):
    words, line = text.split(), ""
    for w in words:
        t = (line + " " + w).strip()
        if c.stringWidth(t, font, size) > width:
            c.drawString(x, yy, line); yy -= leading; line = w
        else:
            line = t
    if line:
        c.drawString(x, yy, line); yy -= leading
    return yy

c.setFont("Helvetica", 8.6)
colw = (W - 2 * M) * 0.33
c.setFillColor(INK); c.setFont("Helvetica-Bold", 8.4)
c.drawString(M, col_y, "Y Combinator \u2014 W19")
c.setFillColor(STONE); c.setFont("Helvetica", 8.6)
yy1 = wrapped("University of San Francisco \u2014 B.S. Data Science, Summa Cum Laude, GPA 3.85", M, col_y - 11, colw)

x2 = M + (W - 2 * M) * 0.36
c.setFillColor(STONE); c.setFont("Helvetica", 8.6)
yy2 = wrapped("Growth strategy, performance marketing, funnel optimization, SEO, Python, SQL, R, predictive modeling.", x2, col_y, colw)

x3 = M + (W - 2 * M) * 0.72
c.setFillColor(STONE); c.setFont("Helvetica", 8.6)
yy3 = wrapped("Towards Data Science (2019); IEEE IEMCON (2018). Most Impactful Graduate Research, USF 2017.", x3, col_y, colw)

# footer
c.setStrokeColor(LINE); c.setLineWidth(0.9)
c.line(M, M + 18, W - M, M + 18)
c.setFillColor(STONE); c.setFont("Courier", 7.4)
c.drawString(M, M + 8, "johnlague.com")
c.drawRightString(W - M, M + 8, "Last updated August 2026")

c.showPage()
c.save()
print("resume PDF written")
