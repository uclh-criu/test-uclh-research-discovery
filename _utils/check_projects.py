from pathlib import Path
import re

from jekyllify import STATUS_LIST

# Constants
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = BASE_DIR / "_projects"
FRONT_MATTER_REQS = {
    "layout": ["project"],
    "title": None,
    "status": STATUS_LIST,
    "authors": None
}

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
     
def check_front_matter(fm, index_file):
    """Check front matter content conforms to required values"""
    for param, value_list in FRONT_MATTER_REQS.items():
        fm_item = re.search(f"{param}:(.*)\n", fm)
        if not fm_item:
            raise ValueError(f"{index_file} front matter does not contain {param}")
        if value_list:  # If None, accept any value
            fm_item_value = fm_item.groups(0)[0].strip()
            if fm_item_value not in value_list:
                raise ValueError(f"{index_file} front matter contains illegal value for {param}: {fm_item_value}")
    
def check_index(dir):
    """Raise exception if:
    - dir does not contain index.md or index.html
    - index does not contain front matter"""
    if (dir/"index.md").exists():
        index_file = dir/"index.md"
    elif (dir/"index.html").exists():
        index_file = dir/"index.html"
    else:
        raise FileNotFoundError(f"index missing from project folder {dir}")
    with open(index_file,"r") as index:
        content = index.read()
        regex = "^---\n((.|\n)*|\n)---\n"  # Matches and captures front matter content
        front_matter = re.search(regex, content)
        if not front_matter:
            raise Exception(f"{index_file} missing front-matter")
        check_front_matter(front_matter.groups(0)[0], index_file)
    
def run_checks(dir):
    check_index(dir)
    
if __name__=="__main__":
    project_dirs = get_project_dirs()
    for dir in project_dirs:
        run_checks(dir)