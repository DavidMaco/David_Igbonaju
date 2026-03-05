"""
Projects — Full Catalog + Detail Views
=======================================
Browse all projects with filtering, or view detailed breakdowns.
"""

import streamlit as st
from components.styles import get_global_css
from components.project_card import render_project_card, render_project_detail
from data_loader import load_projects, get_project_by_id, get_domains

st.set_page_config(
    page_title="Projects — David Maco Portfolio",
    page_icon="📂",
    layout="wide",
)

st.markdown(get_global_css(), unsafe_allow_html=True)

projects = load_projects()

# ── Sidebar Filters ──
with st.sidebar:
    st.markdown("### 🔍 Filter Projects")

    domains = ["All"] + get_domains()
    selected_domain = st.selectbox("Domain", domains, index=0)

    statuses = ["All"] + sorted({p.get("status", "") for p in projects})
    selected_status = st.selectbox("Status", statuses, index=0)

    search_query = st.text_input("Search", placeholder="e.g. Monte Carlo, FastAPI...")

    st.markdown("---")
    st.markdown(
        '<div style="font-size:0.75rem; color:#94A3B8;">Built with Streamlit · 2026</div>',
        unsafe_allow_html=True,
    )

# ── Check if a project detail is selected ──
selected_id = st.session_state.get("selected_project", None)

if selected_id:
    project = get_project_by_id(selected_id)
    if project:
        # Back button
        if st.button("← Back to All Projects"):
            st.session_state["selected_project"] = None
            st.rerun()

        render_project_detail(project)
    else:
        st.warning(f"Project '{selected_id}' not found.")
        st.session_state["selected_project"] = None
else:
    # ── Catalog View ──
    st.markdown(
        """
        <div class="hero-container" style="padding: 2rem 2.5rem;">
            <div class="hero-title" style="font-size: 2rem;">Project Catalog</div>
            <div class="hero-subtitle">
                Browse all projects with full detail views including problem statements,
                architecture summaries, business impact, and technology stacks.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Apply Filters ──
    filtered = projects

    if selected_domain != "All":
        filtered = [p for p in filtered if p.get("domain") == selected_domain]

    if selected_status != "All":
        filtered = [p for p in filtered if p.get("status") == selected_status]

    if search_query:
        q = search_query.lower()
        filtered = [
            p
            for p in filtered
            if q in p.get("title", "").lower()
            or q in p.get("tagline", "").lower()
            or q in p.get("domain", "").lower()
            or any(q in tech.lower() for tech in p.get("stack", []))
            or any(q in feat.lower() for feat in p.get("key_features", []))
        ]

    # ── Results Summary ──
    st.markdown(
        f'<div class="section-subheader">Showing {len(filtered)} of {len(projects)} projects</div>',
        unsafe_allow_html=True,
    )

    if not filtered:
        st.info("No projects match your current filters. Try broadening your search.")
    else:
        # Render in two-column grid
        cols = st.columns(2)
        for i, proj in enumerate(filtered):
            with cols[i % 2]:
                clicked = render_project_card(proj, show_details_button=True)
                if clicked:
                    st.session_state["selected_project"] = proj["id"]
                    st.rerun()
