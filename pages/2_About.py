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

# ── Hero ──
st.markdown(
    """
    <div class="hero-container" style="padding: 2.5rem 2.5rem;">
        <div class="hero-title" style="font-size: 2.2rem;">About Me</div>
        <div class="hero-subtitle">
            Data & Analytics Engineer focused on building production-quality procurement
            intelligence platforms that translate complex analytics into clear business decisions.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Professional Summary ──
st.markdown('<div class="section-header">Professional Summary</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="detail-section">
        <p style="font-size: 0.95rem; color: #334155; line-height: 1.8;">
            I build end-to-end analytics platforms that help procurement and supply chain teams
            make better decisions with data. My work spans the full stack, from MySQL schema
            design and ETL pipelines through Monte Carlo simulation engines and ML risk models,
            to executive dashboards in Streamlit and Power BI.
        </p>
        <p style="font-size: 0.95rem; color: #334155; line-height: 1.8; margin-top: 0.8rem;">
            Every project in this portfolio follows a consistent engineering philosophy:
            <strong>transparent methodology</strong> (every metric traces to code),
            <strong>evidence classification</strong> (simulated vs. observed vs. production data),
            <strong>production-quality code</strong> (typed contracts, CI/CD, comprehensive tests),
            and <strong>business-first design</strong> (analytics only matter if they drive action).
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Technical Skills ──
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Technical Skills</div>', unsafe_allow_html=True)

skills = {
    "Languages & Frameworks": [
        "Python 3.10+", "SQL (MySQL, SQL Server, SQLite, PostgreSQL)",
        "T-SQL (stored procedures, DDL)", "DAX / Power Query M",
    ],
    "Analytics & ML": [
        "Monte Carlo Simulation (GBM)", "scikit-learn (Random Forest, classification)",
        "MCDA (TOPSIS, PROMETHEE-II)", "Game Theory (Nash, auctions)",
        "Optimization (SciPy, LP)", "Time Series & FX Modeling",
    ],
    "Data Engineering": [
        "MySQL 8.0 (schema design, ETL)", "Star-Schema Warehousing (SCD Type 2)",
        "SQLAlchemy ORM", "pandas / NumPy",
        "ETL Pipelines", "Data Validation (Pydantic)",
    ],
    "Platforms & DevOps": [
        "Streamlit (multi-page apps)", "FastAPI (REST APIs, JWT auth)",
        "Power BI (DAX, themes, semantic views)", "Docker / Docker Compose",
        "GitHub Actions CI/CD", "Kubernetes (k8s manifests)",
    ],
}

cols = st.columns(2)
for idx, (category, items) in enumerate(skills.items()):
    with cols[idx % 2]:
        items_html = "".join(f'<span class="stack-tag">{item}</span>' for item in items)
        st.markdown(
            f"""
            <div class="detail-section">
                <div class="skill-category">{category}</div>
                <div class="project-card-stack">{items_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Engineering Philosophy ──
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Engineering Philosophy</div>', unsafe_allow_html=True)

principles = [
    ("🎯", "Business-First Design",
     "Analytics exist to drive decisions. Every dashboard page, every metric, every model output connects to a specific business action."),
    ("🔍", "Transparent Methodology",
     "Every number in every report traces to source code. No black boxes. Stakeholders can verify methodology and assumptions."),
    ("🏷️", "Evidence Classification",
     "Every output carries explicit data provenance tags: simulated estimate, then pilot observed, then production realized."),
    ("✅", "Production Quality",
     "Typed contracts (Pydantic), comprehensive test suites (500+ tests across portfolio), CI/CD pipelines, Docker deployment, and security scanning."),
]

cols = st.columns(2)
for idx, (icon, title, desc) in enumerate(principles):
    with cols[idx % 2]:
        st.markdown(
            f"""
            <div class="about-card" style="text-align: left; margin-bottom: 1rem;">
                <div style="font-size: 1.5rem; margin-bottom: 0.3rem;">{icon}</div>
                <h3 style="text-align:left;">{title}</h3>
                <p style="text-align:left;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Portfolio Stats ──
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Portfolio at a Glance</div>', unsafe_allow_html=True)

stat_cols = st.columns(5)
portfolio_stats = [
    ("Total Projects", str(len(projects))),
    ("Analytics Engines", "16"),
    ("Total Tests", "500+"),
    ("Live Demos", "2"),
    ("Tech Stack Depth", "25+ tools"),
]
for col, (label, value) in zip(stat_cols, portfolio_stats):
    col.metric(label=label, value=value)

# ── Contact ──
st.markdown('<div class="spacer-lg"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Get in Touch</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="detail-section" style="text-align: center; padding: 2rem;">
        <p style="font-size: 1rem; color: #334155; margin-bottom: 1.5rem;">
            Interested in collaboration, have questions about methodology, or want to
            discuss procurement analytics? I'd love to hear from you.
        </p>
        <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
            <div>
                <div style="font-size: 0.75rem; color:#94A3B8; text-transform:uppercase; letter-spacing:0.05em;">Email</div>
                <div style="font-size: 0.95rem; color:#0066CC; font-weight:500;">david.igbonaju@email.com</div>
            </div>
            <div>
                <div style="font-size: 0.75rem; color:#94A3B8; text-transform:uppercase; letter-spacing:0.05em;">GitHub</div>
                <div style="font-size: 0.95rem; color:#0066CC; font-weight:500;">github.com/DavidMaco</div>
            </div>
            <div>
                <div style="font-size: 0.75rem; color:#94A3B8; text-transform:uppercase; letter-spacing:0.05em;">LinkedIn</div>
                <div style="font-size: 0.95rem; color:#0066CC; font-weight:500;">linkedin.com/in/david-igbonaju-a202821a0</div>
            </div>
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
