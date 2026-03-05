"""
Data loader — reads curated project metadata from YAML.
"""

import os
from pathlib import Path
from typing import List, Dict, Any

import yaml


DATA_DIR = Path(__file__).resolve().parent / "data"
PROJECTS_FILE = DATA_DIR / "projects.yml"


def load_projects() -> List[Dict[str, Any]]:
    """Load all projects from the curated YAML file."""
    with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
        projects = yaml.safe_load(f)
    return projects or []


def get_project_by_id(project_id: str) -> Dict[str, Any] | None:
    """Return a single project dict by its id, or None."""
    for p in load_projects():
        if p["id"] == project_id:
            return p
    return None


def get_domains() -> List[str]:
    """Return sorted list of unique project domains."""
    return sorted({p.get("domain", "Other") for p in load_projects()})
