from pathlib import Path

# Constants
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = BASE_DIR / "_projects"

def get_project_dirs()->list[Path]:
    """Return a list of all directories inside PROJECTS_DIR except those
    starting with an underscore."""
    return [
        path for path in PROJECTS_DIR.iterdir() 
        if 
        path.is_dir() 
        and 
        path.stem[0] != "_"
        ]
    
def check_authors_dot_text(dir):
    """Raise exception if dir does not contain authors.txt"""
    if not (dir/"authors.txt").exists():
        raise FileNotFoundError(f"authors.txt missing from project folder {dir}")
    
def check_index(dir):
    """Raise exception if dir does not contain index.md or index.html"""
    if not (dir/"index.md").exists() and not (dir/"index.html").exists():
        raise FileNotFoundError(f"index missing from project folder {dir}")
    
def run_checks(dir):
    check_authors_dot_text(dir)
    check_index(dir)
    
if __name__=="__main__":
    project_dirs = get_project_dirs()
    for dir in project_dirs:
        run_checks(dir)