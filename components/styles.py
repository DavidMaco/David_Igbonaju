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

        /* ── About Page ── */
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
            font-size: 0.7rem;
            font-weight: 600;
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
