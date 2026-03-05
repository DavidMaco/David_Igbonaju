"""
About: Background, Skills and Contact
======================================
"""

import streamlit as st
from components.styles import get_global_css
from data_loader import load_projects

st.set_page_config(
    page_title="About: David Igbonaju Portfolio",
    page_icon="👤",
    layout="wide",
)

st.markdown(get_global_css(), unsafe_allow_html=True)

projects = load_projects()
live_demos = sum(1 for p in projects if p.get("demo_url"))
production_ready = sum(1 for p in projects if "production" in p.get("status", "").lower())

# ── Profile Hero Banner ──
st.markdown(
    f"""
    <div class="profile-hero">
        <div class="profile-avatar-col">
            <div class="profile-avatar">DI</div>
            <div class="profile-available-badge">🟢 Open to Opportunities</div>
        </div>
        <div class="profile-info-col">
            <div class="profile-name">David Igbonaju</div>
            <div class="profile-title">Data &amp; Analytics Engineer</div>
            <div class="profile-location">📍 Nigeria &nbsp;·&nbsp; Remote-Ready</div>
            <div class="profile-tags">
                <span class="profile-tag">Procurement Intelligence</span>
                <span class="profile-tag">Supply Chain Analytics</span>
                <span class="profile-tag">ML Pipelines</span>
                <span class="profile-tag">Dashboard Engineering</span>
                <span class="profile-tag">Full-Stack Python</span>
            </div>
            <div class="profile-stats-row">
                <div class="profile-stat">
                    <div class="profile-stat-val">{len(projects)}</div>
                    <div class="profile-stat-lbl">Projects</div>
                </div>
                <div class="profile-stat">
                    <div class="profile-stat-val">16</div>
                    <div class="profile-stat-lbl">Analytics Engines</div>
                </div>
                <div class="profile-stat">
                    <div class="profile-stat-val">500+</div>
                    <div class="profile-stat-lbl">Tests Written</div>
                </div>
                <div class="profile-stat">
                    <div class="profile-stat-val">{live_demos}</div>
                    <div class="profile-stat-lbl">Live Demos</div>
                </div>
                <div class="profile-stat">
                    <div class="profile-stat-val">{production_ready}</div>
                    <div class="profile-stat-lbl">Production-Ready</div>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── What I Solve ──
st.markdown('<div class="section-header">What I Solve</div>', unsafe_allow_html=True)
st.markdown('<div style="height:0.6rem"></div>', unsafe_allow_html=True)

domains = [
    (
        "💸", "#0066CC", "Cost Leakage &amp; Spend Visibility",
        "Turning thousands of PO lines into clear savings maps: price variance, maverick buying, "
        "supplier concentration risk, and should-cost gap analysis with executive reporting.",
        ["SQLite", "pandas", "Plotly", "Power BI DAX"],
    ),
    (
        "📉", "#DC2626", "FX &amp; Market Risk Quantification",
        "Regime-weighted Monte Carlo simulation with 10K–50K GBM paths, P5/P95 uncertainty "
        "bands, and live FX monitoring for 150+ currencies with dual-API failover.",
        ["NumPy", "SciPy", "Monte Carlo", "GBM"],
    ),
    (
        "🔮", "#7C3AED", "Predictive Supply Chain Intelligence",
        "ML early-warning systems that flag late-delivery risk, supplier deterioration, "
        "and inventory imbalances — before they cause production stoppages.",
        ["scikit-learn", "Random Forest", "18 Features", "SHA-256"],
    ),
    (
        "🌿", "#059669", "Sustainability &amp; Total Cost of Ownership",
        "Converting ESG programs into defensible business cases with quantified carbon "
        "reduction, payback periods, and full 8-layer lifecycle TCO by sourcing region.",
        ["Pydantic", "TCO Engine", "GHG Protocol", "Scenario Analysis"],
    ),
]

dom_cols = st.columns(2)
for i, (icon, color, title, desc, tags) in enumerate(domains):
    tag_html = "".join(
        f'<span class="domain-tag" style="border-color:{color}30; color:{color}; background:{color}12;">{t}</span>'
        for t in tags
    )
    with dom_cols[i % 2]:
        st.markdown(
            f"""
            <div class="domain-card" style="border-top: 3px solid {color};">
                <div class="domain-card-icon" style="background:{color}18;">{icon}</div>
                <div class="domain-card-title">{title}</div>
                <div class="domain-card-desc">{desc}</div>
                <div class="domain-tags">{tag_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Professional Summary ──
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Professional Summary</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="detail-section" style="border-left: 4px solid #0066CC;">
        <p style="font-size: 0.97rem; color: #334155; line-height: 1.85; margin:0 0 0.8rem 0;">
            I build end-to-end analytics platforms that help procurement and supply chain teams
            make better decisions with data. My work spans the full stack, from MySQL schema
            design and ETL pipelines through Monte Carlo simulation engines and ML risk models,
            to executive dashboards in Streamlit and Power BI.
        </p>
        <p style="font-size: 0.97rem; color: #334155; line-height: 1.85; margin:0;">
            Every project follows a disciplined engineering philosophy:
            <strong>every metric traces to code</strong>, evidence is always classified
            (simulated vs. observed vs. production), and every output is tied to a
            specific business decision. Analytics only matter if they drive action.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Technical Skills ──
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Technical Skills</div>', unsafe_allow_html=True)

skills = {
    "🐍  Languages & Frameworks": [
        "Python 3.10+",
        "SQL (MySQL · SQL Server · SQLite · PostgreSQL)",
        "T-SQL (stored procedures, DDL)",
        "DAX / Power Query M",
    ],
    "📐  Analytics & ML": [
        "Monte Carlo Simulation (GBM)",
        "scikit-learn (Random Forest, classification)",
        "MCDA (TOPSIS · PROMETHEE-II)",
        "Game Theory (Nash · Vickrey auctions)",
        "Optimization (SciPy · LP)",
        "Time Series & FX Modeling",
    ],
    "🏗️  Data Engineering": [
        "MySQL 8.0 (schema design, ETL)",
        "Star-Schema Warehousing (SCD Type 2)",
        "SQLAlchemy ORM",
        "pandas / NumPy",
        "ETL Pipelines",
        "Data Validation (Pydantic)",
    ],
    "☁️  Platforms & DevOps": [
        "Streamlit (multi-page apps)",
        "FastAPI (REST APIs, JWT auth)",
        "Power BI (DAX, themes, semantic views)",
        "Docker / Docker Compose",
        "GitHub Actions CI/CD",
        "Kubernetes (k8s manifests)",
    ],
}

sk_cols = st.columns(2)
for idx, (category, items) in enumerate(skills.items()):
    with sk_cols[idx % 2]:
        items_html = "".join(f'<span class="stack-tag">{item}</span>' for item in items)
        st.markdown(
            f"""
            <div class="detail-section" style="margin-bottom:1rem;">
                <div class="skill-category">{category}</div>
                <div class="project-card-stack" style="margin-top:0.5rem;">{items_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Engineering Philosophy ──
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Engineering Philosophy</div>', unsafe_allow_html=True)

principles = [
    (
        "🎯", "#0066CC", "Business-First Design",
        "Analytics exist to drive decisions. Every dashboard page, every metric, every "
        "model output connects to a specific business action — no vanity metrics.",
    ),
    (
        "🔍", "#7C3AED", "Transparent Methodology",
        "Every number in every report traces to source code. No black boxes. "
        "Stakeholders can verify methodology and assumptions at any time.",
    ),
    (
        "🏷️", "#059669", "Evidence Classification",
        "Every output carries explicit data provenance: simulated estimate, then pilot "
        "observed, then production realized. No ambiguity about confidence level.",
    ),
    (
        "✅", "#DC2626", "Production Quality",
        "Typed contracts (Pydantic), 500+ tests across portfolio, CI/CD pipelines, "
        "Docker deployment, and automated security scanning on every PR.",
    ),
]

ph_cols = st.columns(2)
for idx, (icon, color, title, desc) in enumerate(principles):
    with ph_cols[idx % 2]:
        st.markdown(
            f"""
            <div class="philosophy-card" style="border-left: 4px solid {color};">
                <div style="display:flex; align-items:center; gap:0.7rem; margin-bottom:0.5rem;">
                    <div style="font-size:1.5rem; line-height:1;">{icon}</div>
                    <div style="font-size:0.97rem; font-weight:700; color:#1A1A2E;">{title}</div>
                </div>
                <div style="font-size:0.88rem; color:#475569; line-height:1.65;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Portfolio at a Glance ──
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Portfolio at a Glance</div>', unsafe_allow_html=True)

glance_items = [
    ("🏛️", str(len(projects)), "Projects Built",       "#0066CC"),
    ("⚙️", "16",               "Analytics Engines",     "#7C3AED"),
    ("✅", "500+",             "Automated Tests",       "#059669"),
    ("🚀", str(live_demos),    "Live Demos",            "#F59E0B"),
    ("🛠️", "25+",             "Tools & Libraries",     "#DC2626"),
]

gc = st.columns(len(glance_items))
for col, (icon, value, label, color) in zip(gc, glance_items):
    with col:
        st.markdown(
            f"""
            <div class="glance-card" style="border-top: 3px solid {color};">
                <div style="font-size:1.5rem;">{icon}</div>
                <div class="glance-value" style="color:{color};">{value}</div>
                <div class="glance-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Get in Touch ──
st.markdown('<div class="spacer-lg"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Get in Touch</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="contact-section">
        <p class="contact-intro">
            Interested in collaboration, have questions about methodology, or want to
            discuss procurement analytics? I would love to hear from you.
        </p>
        <div class="contact-items">
            <a class="contact-card" href="mailto:davidigbonaju@email.com">
                <div class="contact-icon">✉️</div>
                <div class="contact-label">Email</div>
                <div class="contact-value">davidigbonaju@email.com</div>
            </a>
            <a class="contact-card" href="https://github.com/DavidMaco" target="_blank">
                <div class="contact-icon">💻</div>
                <div class="contact-label">GitHub</div>
                <div class="contact-value">github.com/DavidMaco</div>
            </a>
            <a class="contact-card" href="https://linkedin.com/in/david-igbonaju-a202821a0" target="_blank">
                <div class="contact-icon">🔗</div>
                <div class="contact-label">LinkedIn</div>
                <div class="contact-value">david-igbonaju</div>
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Footer ──
st.markdown(
    """
    <div class="footer">
        Portfolio of David Igbonaju · Data and Analytics Engineer<br>
        All project metrics derived from documented methodologies · 2026
    </div>
    """,
    unsafe_allow_html=True,
)
