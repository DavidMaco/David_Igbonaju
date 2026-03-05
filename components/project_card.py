"""
Reusable project card and detail renderers.
"""

import streamlit as st
from components.styles import get_status_class


def render_project_card(project: dict, show_details_button: bool = True) -> bool:
    """
    Render a summary card for a project.
    Returns True if the user clicks 'View Details'.
    """
    color = project.get("color", "#0066CC")
    icon = project.get("icon", "📦")
    status_cls = get_status_class(project.get("status", ""))

    # Build stack tags HTML
    stack_html = "".join(
        f'<span class="stack-tag">{tech}</span>' for tech in project.get("stack", [])[:8]
    )

    # Build metrics HTML
    highlights = project.get("highlights", {})
    metrics_html = ""
    if highlights:
        items = list(highlights.items())[:4]
        metrics_html = '<div class="project-card-metrics">' + "".join(
            f'<div class="metric-item">'
            f'<div class="metric-value">{v}</div>'
            f'<div class="metric-label">{k.replace("_", " ").title()}</div>'
            f"</div>"
            for k, v in items
        ) + "</div>"

    card_html = f"""
    <div class="project-card">
        <div class="project-card-accent" style="background: {color};"></div>
        <div style="padding-left: 0.8rem;">
            <span class="status-badge {status_cls}">{project.get('status', 'N/A')}</span>
            <div class="project-card-header">
                <div class="project-card-icon">{icon}</div>
                <div>
                    <div class="project-card-title">{project['title']}</div>
                    <div class="project-card-domain">{project.get('domain', '')}</div>
                </div>
            </div>
            <div class="project-card-tagline">{project.get('tagline', '')}</div>
            <div class="project-card-stack">{stack_html}</div>
            {metrics_html}
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

    if show_details_button:
        return st.button(
            f"View Details →",
            key=f"btn_{project['id']}",
            use_container_width=True,
        )
    return False


def render_project_detail(project: dict):
    """Render a full detail view for a project."""
    color = project.get("color", "#0066CC")
    icon = project.get("icon", "📦")

    # ── Header ──
    st.markdown(
        f"""
        <div class="detail-header">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
            <div class="detail-title">{project['title']}</div>
            <div class="detail-tagline">{project.get('tagline', '')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Quick Stats Row ──
    highlights = project.get("highlights", {})
    if highlights:
        cols = st.columns(len(highlights))
        for col, (key, val) in zip(cols, highlights.items()):
            col.metric(label=key.replace("_", " ").title(), value=val)

    # ── Links ──
    link_cols = st.columns(3)
    demo_url = project.get("demo_url", "")
    repo_url = project.get("repo_url", "")
    if demo_url:
        link_cols[0].link_button("🚀 Live Demo", demo_url, use_container_width=True)
    if repo_url:
        link_cols[1].link_button("💻 Source Code", repo_url, use_container_width=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # ── Two-Column Layout ──
    left, right = st.columns([1, 1])

    with left:
        # Problem
        st.markdown(
            f"""
            <div class="detail-section">
                <div class="detail-section-title">🎯 Problem</div>
                <p style="font-size:0.9rem; color:#334155; line-height:1.7;">
                    {project.get('problem_statement', '')}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Architecture
        st.markdown(
            f"""
            <div class="detail-section">
                <div class="detail-section-title">🏗️ Architecture</div>
                <p style="font-size:0.9rem; color:#334155; line-height:1.7;">
                    {project.get('architecture_summary', '')}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        # Solution
        st.markdown(
            f"""
            <div class="detail-section">
                <div class="detail-section-title">💡 Solution</div>
                <p style="font-size:0.9rem; color:#334155; line-height:1.7;">
                    {project.get('solution_summary', '')}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Business Impact
        impact_items = project.get("business_impact", [])
        impact_html = "".join(
            f'<div class="impact-item"><span class="impact-bullet">▸</span> {item}</div>'
            for item in impact_items
        )
        st.markdown(
            f"""
            <div class="detail-section">
                <div class="detail-section-title">📈 Business Impact</div>
                {impact_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Key Features ──
    features = project.get("key_features", [])
    if features:
        features_html = "".join(
            f'<span class="feature-tag">{f}</span>' for f in features
        )
        st.markdown(
            f"""
            <div class="detail-section">
                <div class="detail-section-title">⚡ Key Features</div>
                <div style="display: flex; flex-wrap: wrap; gap: 0.3rem;">
                    {features_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Tech Stack ──
    stack = project.get("stack", [])
    if stack:
        stack_html = "".join(f'<span class="stack-tag">{t}</span>' for t in stack)
        st.markdown(
            f"""
            <div class="detail-section">
                <div class="detail-section-title">🛠️ Technology Stack</div>
                <div class="project-card-stack">{stack_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Dashboard Preview ──
    dashboard_pages = project.get("dashboard_pages", [])
    if dashboard_pages:
        st.markdown(
            """
            <div class="detail-section">
                <div class="detail-section-title">🖥️ Dashboard Pages</div>
                <div style="font-size:0.8rem; color:#64748B; margin-bottom:0.8rem;">
                    Key screens and analytical panels in this project's dashboard.
                </div>
            """,
            unsafe_allow_html=True,
        )
        dp_cols = st.columns(min(len(dashboard_pages), 2))
        for i, page in enumerate(dashboard_pages):
            chips_html = "".join(
                f'<span class="dp-chip">{m}</span>'
                for m in page.get("key_metrics", [])
            )
            with dp_cols[i % 2]:
                st.markdown(
                    f"""
                    <div class="dp-card">
                        <div class="dp-card-top">
                            <div class="dp-icon">{page.get('icon', '📄')}</div>
                            <div class="dp-page-name">{page.get('page', '')}</div>
                        </div>
                        <div class="dp-desc">{page.get('description', '')}</div>
                        <div class="dp-metrics">{chips_html}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Data Transparency Note ──
    st.markdown(
        """
        <div style="background:#FFFBEB; border:1px solid #FDE68A; border-radius:8px;
                     padding:0.8rem 1rem; margin-top:1rem; font-size:0.8rem; color:#92400E;">
            <strong>📋 Data Note:</strong> All metrics shown above are derived from synthetic
            demonstration data unless explicitly labelled otherwise. Each project's documentation
            includes full methodology, assumptions, and evidence classification details.
        </div>
        """,
        unsafe_allow_html=True,
    )
