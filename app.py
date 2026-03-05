"""
Portfolio Website — Homepage
============================
Professional landing page showcasing projects built by David Maco.
"""

import streamlit as st

st.set_page_config(
    page_title="David Maco — Portfolio",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

from components.styles import get_global_css
from components.project_card import render_project_card
from data_loader import load_projects

# ── Inject Global CSS ──
st.markdown(get_global_css(), unsafe_allow_html=True)

# ── Sidebar ──
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    st.markdown(
        """
        <div style="font-size:0.85rem; color:#64748B; line-height:1.8;">
            <strong>Home</strong> — You are here<br>
            <strong>Projects</strong> — Full catalog + detail views<br>
            <strong>About</strong> — Background & contact
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        '<div style="font-size:0.75rem; color:#94A3B8;">Built with Streamlit · 2026</div>',
        unsafe_allow_html=True,
    )


# ── Load Data ──
projects = load_projects()

# ── Hero Section ──
st.markdown(
    f"""
    <div class="hero-container">
        <div class="hero-title">David Maco</div>
        <div class="hero-subtitle">
            Data & Analytics Engineer building investment-grade procurement intelligence
            platforms — from Monte Carlo simulations and ML risk models to full-stack
            executive dashboards. Every project here solves a real business problem
            with production-quality code, transparent methodology, and quantified outcomes.
        </div>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="hero-stat-value">{len(projects)}</div>
                <div class="hero-stat-label">Projects</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-value">16</div>
                <div class="hero-stat-label">Analytics Engines</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-value">500+</div>
                <div class="hero-stat-label">Tests</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-value">5</div>
                <div class="hero-stat-label">Live Dashboards</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Featured Projects ──
st.markdown('<div class="section-header">Featured Projects</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subheader">Flagship platforms with the deepest technical scope and business impact.</div>',
    unsafe_allow_html=True,
)

# Show top 3 featured projects in columns
featured_ids = ["aegis-procurement", "procurement-intelligence-engine", "tco-comparison-model"]
featured = [p for p in projects if p["id"] in featured_ids]

cols = st.columns(len(featured))
for col, proj in zip(cols, featured):
    with col:
        clicked = render_project_card(proj, show_details_button=True)
        if clicked:
            st.session_state["selected_project"] = proj["id"]
            st.switch_page("pages/1_Projects.py")

# ── All Projects Quick Grid ──
st.markdown('<div class="spacer-lg"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Complete Portfolio</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subheader">All projects spanning procurement analytics, sustainability, supply chain ML, and business intelligence.</div>',
    unsafe_allow_html=True,
)

remaining = [p for p in projects if p["id"] not in featured_ids]
cols = st.columns(2)
for i, proj in enumerate(remaining):
    with cols[i % 2]:
        clicked = render_project_card(proj, show_details_button=True)
        if clicked:
            st.session_state["selected_project"] = proj["id"]
            st.switch_page("pages/1_Projects.py")

# ── Domain Expertise Ribbon ──
st.markdown('<div class="spacer-lg"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">Domain Expertise</div>', unsafe_allow_html=True)

expertise_cols = st.columns(4)
expertise = [
    ("📊", "Procurement Analytics", "Spend analysis, supplier scoring, cost leakage, FX risk"),
    ("🤖", "ML & Simulation", "Monte Carlo, Random Forest, game theory, optimization"),
    ("🏗️", "Full-Stack Platforms", "Streamlit, FastAPI, MySQL, Docker, CI/CD, Power BI"),
    ("🌿", "Sustainability", "GHG Protocol, carbon tracking, ROI quantification"),
]
for col, (icon, title, desc) in zip(expertise_cols, expertise):
    with col:
        st.markdown(
            f"""
            <div class="about-card">
                <div style="font-size:2rem; margin-bottom:0.5rem;">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Footer ──
st.markdown(
    """
    <div class="footer">
        Portfolio of David Maco · Data & Analytics Engineer<br>
        All project metrics derived from documented methodologies · 2026
    </div>
    """,
    unsafe_allow_html=True,
)
