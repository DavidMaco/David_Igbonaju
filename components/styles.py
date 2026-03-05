"""
Shared CSS styles for the portfolio website.
"""


def get_global_css() -> str:
    """Return global CSS to inject into every page."""
    return """
    <style>
        /* ── Global Reset & Typography ── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        .block-container {
            padding-top: 2rem;
            max-width: 1200px;
        }

        /* ── Hero Section ── */
        .hero-container {
            background: linear-gradient(135deg, #0a1628 0%, #1a365d 50%, #0d2847 100%);
            border-radius: 16px;
            padding: 3.5rem 3rem;
            margin-bottom: 2.5rem;
            position: relative;
            overflow: hidden;
        }
        .hero-container::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(0,102,204,0.15) 0%, transparent 70%);
            border-radius: 50%;
        }
        .hero-container::after {
            content: '';
            position: absolute;
            bottom: -30%;
            left: -10%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(0,168,107,0.1) 0%, transparent 70%);
            border-radius: 50%;
        }
        .hero-title {
            font-size: 2.8rem;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 0.5rem;
            line-height: 1.15;
            position: relative;
            z-index: 1;
        }
        .hero-subtitle {
            font-size: 1.15rem;
            color: #94A3B8;
            line-height: 1.7;
            max-width: 700px;
            position: relative;
            z-index: 1;
        }
        .hero-stats {
            display: flex;
            gap: 2.5rem;
            margin-top: 2rem;
            position: relative;
            z-index: 1;
        }
        .hero-stat {
            text-align: center;
        }
        .hero-stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: #60A5FA;
        }
        .hero-stat-label {
            font-size: 0.8rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.2rem;
        }

        /* ── Section Headers ── */
        .section-header {
            font-size: 1.5rem;
            font-weight: 700;
            color: #1A1A2E;
            margin: 2rem 0 0.5rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid #0066CC;
            display: inline-block;
        }
        .section-subheader {
            font-size: 0.95rem;
            color: #64748B;
            margin-bottom: 1.5rem;
        }

        /* ── Project Cards ── */
        .project-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 1.8rem;
            margin-bottom: 1.2rem;
            transition: all 0.25s ease;
            position: relative;
            overflow: hidden;
        }
        .project-card:hover {
            border-color: #0066CC;
            box-shadow: 0 4px 20px rgba(0,102,204,0.1);
            transform: translateY(-2px);
        }
        .project-card-accent {
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
        }
        .project-card-header {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 0.8rem;
        }
        .project-card-icon {
            font-size: 2rem;
            line-height: 1;
        }
        .project-card-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #1A1A2E;
            margin: 0;
            line-height: 1.3;
        }
        .project-card-domain {
            font-size: 0.75rem;
            font-weight: 600;
            color: #0066CC;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.15rem;
        }
        .project-card-tagline {
            font-size: 0.92rem;
            color: #475569;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        .project-card-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 1rem;
        }
        .stack-tag {
            background: #F1F5F9;
            color: #475569;
            font-size: 0.72rem;
            font-weight: 500;
            padding: 0.25rem 0.65rem;
            border-radius: 100px;
            white-space: nowrap;
        }
        .project-card-metrics {
            display: flex;
            gap: 1.5rem;
            padding-top: 0.8rem;
            border-top: 1px solid #F1F5F9;
        }
        .metric-item {
            text-align: center;
        }
        .metric-value {
            font-size: 1.1rem;
            font-weight: 700;
            color: #1A1A2E;
        }
        .metric-label {
            font-size: 0.68rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .status-badge {
            font-size: 0.7rem;
            font-weight: 600;
            padding: 0.2rem 0.7rem;
            border-radius: 100px;
            display: inline-block;
            margin-bottom: 0.5rem;
        }
        .status-production {
            background: #DCFCE7;
            color: #166534;
        }
        .status-pilot {
            background: #FEF9C3;
            color: #854D0E;
        }
        .status-mvp {
            background: #FEE2E2;
            color: #991B1B;
        }

        /* ── Detail View ── */
        .detail-header {
            background: linear-gradient(135deg, #0a1628 0%, #1a365d 100%);
            border-radius: 12px;
            padding: 2.5rem 2rem;
            margin-bottom: 2rem;
            color: white;
        }
        .detail-title {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 0.3rem;
        }
        .detail-tagline {
            font-size: 1rem;
            color: #94A3B8;
            line-height: 1.6;
        }
        .detail-section {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }
        .detail-section-title {
            font-size: 1rem;
            font-weight: 700;
            color: #1A1A2E;
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .impact-item {
            display: flex;
            align-items: flex-start;
            gap: 0.6rem;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
            color: #334155;
            line-height: 1.5;
        }
        .impact-bullet {
            color: #0066CC;
            font-weight: bold;
            flex-shrink: 0;
            margin-top: 0.15rem;
        }
        .feature-tag {
            background: #EFF6FF;
            color: #1E40AF;
            font-size: 0.82rem;
            font-weight: 500;
            padding: 0.5rem 0.9rem;
            border-radius: 8px;
            margin: 0.3rem;
            display: inline-block;
            line-height: 1.4;
        }

        /* ── About Page — Profile Hero ── */
        .profile-hero {
            background: linear-gradient(135deg, #0a1628 0%, #1a365d 50%, #0d2847 100%);
            border-radius: 16px;
            padding: 2.5rem 2.5rem;
            margin-bottom: 2.5rem;
            display: flex;
            gap: 2.5rem;
            align-items: center;
            flex-wrap: wrap;
            position: relative;
            overflow: hidden;
        }
        .profile-hero::before {
            content: '';
            position: absolute;
            top: -40%;
            right: -10%;
            width: 400px; height: 400px;
            background: radial-gradient(circle, rgba(0,102,204,0.18) 0%, transparent 70%);
            border-radius: 50%;
        }
        .profile-avatar-col {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.8rem;
            position: relative;
            z-index: 1;
        }
        .profile-avatar {
            width: 96px; height: 96px;
            border-radius: 50%;
            background: linear-gradient(135deg, #0066CC, #00A86B);
            display: flex; align-items: center; justify-content: center;
            font-size: 2rem; font-weight: 800; color: #FFFFFF;
            border: 3px solid rgba(255,255,255,0.25);
            box-shadow: 0 4px 24px rgba(0,102,204,0.4);
        }
        .profile-available-badge {
            background: rgba(5,150,105,0.2);
            border: 1px solid rgba(5,150,105,0.5);
            color: #6EE7B7;
            font-size: 0.7rem;
            font-weight: 600;
            padding: 0.25rem 0.7rem;
            border-radius: 100px;
            white-space: nowrap;
        }
        .profile-info-col {
            flex: 1;
            min-width: 260px;
            position: relative;
            z-index: 1;
        }
        .profile-name {
            font-size: 2.2rem;
            font-weight: 800;
            color: #FFFFFF;
            line-height: 1.2;
            margin-bottom: 0.2rem;
        }
        .profile-title {
            font-size: 1.05rem;
            font-weight: 500;
            color: #60A5FA;
            margin-bottom: 0.3rem;
        }
        .profile-location {
            font-size: 0.85rem;
            color: #94A3B8;
            margin-bottom: 1rem;
        }
        .profile-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 1.4rem;
        }
        .profile-tag {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            color: #CBD5E1;
            font-size: 0.72rem;
            font-weight: 500;
            padding: 0.25rem 0.7rem;
            border-radius: 100px;
        }
        .profile-stats-row {
            display: flex;
            gap: 1.8rem;
            flex-wrap: wrap;
        }
        .profile-stat {
            text-align: center;
        }
        .profile-stat-val {
            font-size: 1.6rem;
            font-weight: 800;
            color: #60A5FA;
            line-height: 1.1;
        }
        .profile-stat-lbl {
            font-size: 0.68rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.15rem;
        }

        /* ── Domain Cards ── */
        .domain-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.2rem;
            transition: box-shadow 0.2s ease;
        }
        .domain-card:hover {
            box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        }
        .domain-card-icon {
            width: 44px; height: 44px;
            border-radius: 10px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.4rem;
            margin-bottom: 0.7rem;
        }
        .domain-card-title {
            font-size: 1rem;
            font-weight: 700;
            color: #1A1A2E;
            margin-bottom: 0.4rem;
        }
        .domain-card-desc {
            font-size: 0.87rem;
            color: #64748B;
            line-height: 1.65;
            margin-bottom: 0.8rem;
        }
        .domain-tags { display: flex; flex-wrap: wrap; gap: 0.35rem; }
        .domain-tag {
            font-size: 0.68rem;
            font-weight: 600;
            padding: 0.2rem 0.55rem;
            border-radius: 100px;
            border: 1px solid;
            background: transparent;
        }

        /* ── Philosophy Cards ── */
        .philosophy-card {
            background: #FAFBFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 1.3rem 1.4rem;
            margin-bottom: 1rem;
        }

        /* ── Glance Cards ── */
        .glance-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 1.2rem 0.8rem;
            text-align: center;
            margin-bottom: 0.8rem;
        }
        .glance-value {
            font-size: 1.8rem;
            font-weight: 800;
            line-height: 1.2;
            margin: 0.3rem 0 0.15rem 0;
        }
        .glance-label {
            font-size: 0.72rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        /* ── Contact Section ── */
        .contact-section {
            background: linear-gradient(135deg, #F8FAFF 0%, #F0F7FF 100%);
            border: 1px solid #DBEAFE;
            border-radius: 14px;
            padding: 2rem 2rem 2rem 2rem;
            text-align: center;
            margin-top: 0.5rem;
        }
        .contact-intro {
            font-size: 0.97rem;
            color: #334155;
            line-height: 1.75;
            max-width: 600px;
            margin: 0 auto 1.6rem auto;
        }
        .contact-items {
            display: flex;
            justify-content: center;
            gap: 1.2rem;
            flex-wrap: wrap;
        }
        .contact-card {
            background: #FFFFFF;
            border: 1px solid #DBEAFE;
            border-radius: 12px;
            padding: 1.1rem 1.5rem;
            text-decoration: none;
            min-width: 160px;
            transition: box-shadow 0.2s ease, transform 0.15s ease;
            display: block;
        }
        .contact-card:hover {
            box-shadow: 0 4px 16px rgba(0,102,204,0.12);
            transform: translateY(-2px);
            text-decoration: none;
        }
        .contact-icon { font-size: 1.6rem; margin-bottom: 0.3rem; }
        .contact-label {
            font-size: 0.68rem;
            font-weight: 600;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.2rem;
        }
        .contact-value {
            font-size: 0.88rem;
            font-weight: 600;
            color: #0066CC;
        }

        /* ── Dashboard Preview (Project Detail) ── */
        .dp-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
            gap: 0.9rem;
            margin-top: 0.6rem;
        }
        .dp-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 1.1rem 1.2rem;
            position: relative;
            overflow: hidden;
            transition: box-shadow 0.2s ease;
        }
        .dp-card:hover {
            box-shadow: 0 3px 14px rgba(0,0,0,0.07);
        }
        .dp-card-top {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin-bottom: 0.5rem;
        }
        .dp-icon {
            width: 32px; height: 32px;
            border-radius: 8px;
            background: #F1F5F9;
            display: flex; align-items: center; justify-content: center;
            font-size: 1rem;
            flex-shrink: 0;
        }
        .dp-page-name {
            font-size: 0.9rem;
            font-weight: 700;
            color: #1A1A2E;
            line-height: 1.3;
        }
        .dp-desc {
            font-size: 0.82rem;
            color: #64748B;
            line-height: 1.55;
            margin-bottom: 0.7rem;
        }
        .dp-metrics {
            display: flex;
            flex-wrap: wrap;
            gap: 0.3rem;
        }
        .dp-chip {
            background: #EFF6FF;
            color: #1E40AF;
            font-size: 0.68rem;
            font-weight: 600;
            padding: 0.2rem 0.55rem;
            border-radius: 100px;
        }

        /* ── About Page ── (legacy, kept for backward compat) */
        .about-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
        }
        .about-card h3 {
            font-size: 1.1rem;
            font-weight: 700;
            color: #1A1A2E;
            margin-bottom: 0.5rem;
        }
        .about-card p {
            font-size: 0.88rem;
            color: #64748B;
            line-height: 1.6;
        }
        .skill-category {
            font-size: 0.72rem;
            font-weight: 700;
            color: #0066CC;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
        }

        /* ── Footer ── */
        .footer {
            text-align: center;
            color: #94A3B8;
            font-size: 0.78rem;
            padding: 2rem 0 1rem 0;
            border-top: 1px solid #E2E8F0;
            margin-top: 3rem;
        }

        /* ── Utility ── */
        .spacer { height: 1rem; }
        .spacer-lg { height: 2rem; }

        /* Hide Streamlit default elements for cleaner look */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { visibility: hidden; }
    </style>
    """


def get_status_class(status: str) -> str:
    """Return CSS class for a project status string."""
    s = status.lower()
    if "production" in s:
        return "status-production"
    elif "pilot" in s or "beta" in s:
        return "status-pilot"
    else:
        return "status-mvp"
