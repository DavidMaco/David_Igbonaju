# Portfolio Website

Professional portfolio showcasing data and analytics engineering projects, built with Streamlit.

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run locally
streamlit run app.py
```

The site opens at `http://localhost:8501`.

## Structure

```
portfolio-site/
├── app.py                  # Homepage (hero, featured projects, expertise)
├── data_loader.py          # YAML metadata reader
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Theme & server config
├── components/
│   ├── __init__.py
│   ├── project_card.py     # Card + detail renderers
│   └── styles.py           # Global CSS
├── data/
│   └── projects.yml        # Curated project metadata (single source of truth)
├── pages/
│   ├── 1_Projects.py       # Full catalog with filters + detail views
│   └── 2_About.py          # Skills, philosophy, contact
└── assets/                 # Visual assets (charts, screenshots)
```

## Content Management

All project content lives in `data/projects.yml`. To add or update a project:

1. Edit `data/projects.yml` to add a new entry following the existing schema
2. Restart the Streamlit app (or it hot-reloads automatically in dev)

Fields per project: `id`, `title`, `tagline`, `domain`, `icon`, `color`, `problem_statement`, `solution_summary`, `business_impact`, `architecture_summary`, `stack`, `key_features`, `status`, `highlights`, `repo_url`, `demo_url`.

## Deployment (Streamlit Community Cloud)

1. Push this folder to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select the repo, branch, and set **Main file path** to `app.py`
4. Deploy

Environment requirements are in `requirements.txt`. No secrets or database needed.

## Customization

- **Theme**: Edit `.streamlit/config.toml` (`primaryColor`, `backgroundColor`, etc.)
- **Styling**: Edit `components/styles.py` for all CSS
- **Layout**: Edit `app.py` (homepage) or pages for structure changes
- **Contact info**: Edit `pages/2_About.py` contact section

## Data Transparency

All project metrics are derived from synthetic demonstration data unless explicitly labelled otherwise. Each project's documentation includes full methodology, assumptions, and evidence classification details.
