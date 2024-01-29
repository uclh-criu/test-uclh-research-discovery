from pathlib import Path
import re

import yaml
from yaml import load, Loader


# Constants
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = BASE_DIR / "_projects"
STATUS_LIST = ["ongoing","completed"] # First value is default
FRONT_MATTER_REQS = {
    "layout": ["project"],
    "title": None,
    "status": STATUS_LIST,
    "authors": None
}
TABS_REQS = {
    "name": None,
    "type": ["md","html"],
    "source": None,
    "label": None
}

def get_project_dirs(name:str=None)->list[Path]:
    """Either return the path to the named project folder inside a list or, if no
    name is provided, return a list of all directories inside PROJECTS_DIR."""
    if name:
        project_dir = PROJECTS_DIR / name
        if project_dir.exists():
            return [project_dir]
        else:
            raise FileNotFoundError(f"No directory named {name} found under {PROJECTS_DIR}")
    else:
        return [
            path for path in PROJECTS_DIR.iterdir()
            if
              path.is_dir()
            and
              path.stem[0] != "_"
            ]

def get_index(dir):
    """Return Path to index.md or index.html if it exists in dir,
    or None if not"""
    if (index_file := dir/"index.md").exists():
        return index_file
    elif (index_file := dir/"index.html").exists():
        return index_file
    else:
        return None
    
def get_front_matter_yaml(index_file):
    with open(index_file,"r") as index:
        content = index.read()
    regex = "^---\n((.|\n)*|\n)---\n"  # Matches and captures front matter content
    fm_match = re.search(regex, content)
    if not fm_match:
        return None
    fm_text = fm_match.groups(0)[0]
    return load(fm_text, Loader=Loader)

def get_metadata_yaml(dir)->dict:
    """Find metadata.yml in project dir. If it exists, load and return
    metadata dictionary"""
    if (metadata_file := dir/"metadata.yml").exists():
        with open(metadata_file, "r") as f:
            metadata = yaml.safe_load(f)
        return metadata
    else:
        return {}
    
def check_metadata_content(metadata,dir:Path)->bool:
    # metadata must contain list of authors
    if authors := metadata.get("authors"):
        if type(authors) != list:
            raise ValueError(f"{dir/'metadata.yml'} authors is not a list")
    else:
        raise ValueError(f"{dir/'metadata.yml'} authors list required")
    # metadata contains optional title it should be str
    if title := metadata.get("title"):
        if type(title) != str:
            raise ValueError(f"{dir/'metadata.yml'}: title must be a string")
    # metadata contains optional status, one of STATUS_LIST
    if status := metadata.get("status"):
        if status not in STATUS_LIST:
            raise ValueError(f"{dir/'metadata.yml'} status is not one of {STATUS_LIST}")

def check_front_matter_from_metadata_dot_yaml(fm_yaml, index_file):
    for param, value_list in FRONT_MATTER_REQS.items():
        value = fm_yaml.get(param)
        if not value:
            raise ValueError(f"{index_file} front matter does not contain {param}")
        if value_list:  # If None, accept any value
            if value not in value_list:
                raise ValueError(f"{index_file} front matter contains illegal value for {param}: {value}")

def check_front_matter_tabs(fm_yaml, index_file):
    """For each tab item check format and confirm source exists"""
    tabs = fm_yaml.get("tabs")
    for tab in tabs:
        for param, value_list in TABS_REQS.items():
            value = tab.get(param)
            if not value:
                raise ValueError(f"Misconfigured tab data in {index_file}, missing {param}.")
            if value_list and value not in value_list:
                raise ValueError(f"Unrecognised value for tab:{param} in {index_file}: {value}.")
        source = tab.get("source")
        if not (index_file.parent / source).exists():
            raise FileNotFoundError(f"Source file {source} referenced in {index_file} not found.")

def check_front_matter(fm_yaml, index_file):
    """Check front matter content conforms to required values"""
    check_front_matter_from_metadata_dot_yaml(fm_yaml, index_file)
    check_front_matter_tabs(fm_yaml, index_file)
    
def check_project_meets_requirements(dir:Path) -> bool:
    """Given a directory path, check the content to determine if it
    meets requirements. Raise exception if required content is
    missing and raise_exception=True, otherwise return False.
    
    Requirements:
    
    * Project dir contains an index file: index.md or index.html
    * Index file must contain yaml front matter, or
    * Project dir must contain correctly formatted metadata.yml
    
    Only project dirs that meet the requirements, but don't already contain
    front matter should return True"""
    # Is there a file called index.md / index.html?
    if index_file := get_index(dir):
        # Index exists, but does it contain front matter?
        if front_matter := get_front_matter_yaml(index_file):
            check_front_matter(front_matter, index_file)
        # Front matter not present, so we need metadata.yml
        elif metadata := get_metadata_yaml(dir):
            # Is metadata formatted correctly?
            check_metadata_content(metadata, dir)
    else:
        # index file does not exist
        raise FileNotFoundError(f"index missing from project folder {dir}")
    return True
    
if __name__=="__main__":
    project_dirs = get_project_dirs()
    for dir in project_dirs:
        check_project_meets_requirements(dir)