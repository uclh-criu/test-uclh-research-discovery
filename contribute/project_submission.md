---
layout: page
---

# Submitting a project for inclusion on this site
If you are a UCLH researcher, you can submit details about your own research project(s) and have them added to this site.

**Step 1**: [Upload datasets and code to a research data repository](#step-1-upload-datasets-and-code-to-a-research-data-repository)

**Step 2**: [Clone our repository on GitHub](#step-2-clone-our-repository-on-github)

**Step 3**: [Complete the project template](#step-3-complete-the-project-template)

**Step 4**: [Make a pull request](#step-4-make-a-pull-request)

## Step 1: Upload datasets and code to a research data repository

To help people who are interested in your research to better understand what data you have used and how you process it, it can be helpful to share example datasets together with any relevant computer code. We recommend using UCL's institutional [research data respository](https://rdr.ucl.ac.uk/) service as it is free for all UCL researchers to use and provides an embed link which can be used to include your data alongside details about your project on this site. Please read the guidance on the [UCL Library Researd Data Repository](https://www.ucl.ac.uk/library/open-science-research-support/research-data-management/ucl-research-data-repository) page for details on how to prepare and upload your data.

Once your submission has been approved, you can find the embed URL by navigating to your deposit's page and selecting 'Embed' from the menu. Copy the src url from the iframe tag and save this for step 3.

## Step 2: Clone our repository on GitHub

To complete the next steps you will need a GitHub account, which will enable you to take a copy of the site's code and later merge your changes back in. If you don't have one you can [sign up for free](https://github.com/join). You will also need to [install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your personal device.

The source code for this site can be found on GitHub: [{{site.data.github.url}}](https://{{site.data.github.url}}). To copy the code to work with on your own device, clone the repository with your git client or via the command line: 

`git clone https://{{site.data.github.url}}.git`

## Step 3: Complete the project template

Once you have cloned the repository, you will need to create a new branch as you will not be able to merge your changes directly back into the main branch (choose a name that identifies you or your group, and the name of the project):

`git switch -c group-a-project-x`

The pages for each project are kept in separate folders under `/_projects`, where you will also find a template for creating new projects: `_project_template`. Copy this folder and name it after your project (this folder name will form part of the url for your project pages). Now complete the following required steps:

### index.md
Every project folder must include a file called index.md, which serves two purposes:
1. It contains frontmatter where you can define variables which Jekyll uses when building your pages
2. It serves as the landing page for your project, where you can write an overview

Front matter at the top of the page starts and ends with triple dashes: '---'. This contains information about the project written in [YAML](https://en.wikipedia.org/wiki/YAML) format such as the project title, authors, and any additional content to include. To start with, enter a project title - we go into more detail about adding authors and extra content below.

Below the front matter you should write your project summary. This should be written in [markdown](https://en.wikipedia.org/wiki/Markdown) format and can be as long as you like. You have the option to add additional pages if you'd like to split things like discussion of the data analysis or how you protect sensitive data into separate sections (see extra content below). If you're new to markdown, have a look at this [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) to help you get started.

### Extra content
If you'd like to split content across several pages, or include an embed link for your data, you can add extra content in the form of tabs across the top of the page.

First, write your extra content in a separate markdown or html file (e.g. `_extras.md`) in the same folder as `index.md`. Then add the following to the tabs section in the frontmatter at the top of `index.md` for each tab you'd like to add:

```yaml
  - { 
    name: 'extra', # Two tabs cannot share the same name
    type: 'markdown', # embed/html/markdown
    source: '_extras.md', # filename or embed url
    label: 'Extra tab' # Optional: label for tab, defaults to capitalised name
    }
```

The options work as follows:
* `name`: determines the id used by the html elements - must begin with a letter followed by any number of letters, digits, hyphens or underscores (no spaces)
* `type`: specify whether your source file is written in markdown or html, or if it's a link to another page that you'd like to embed
* `source`: the source filename or url for the additional content
* `label`: the label you'd like to appear on the tab if different from capitalised name

This is how you can embed content from a research data repository, or even a page you have built with [Quarto](https://quarto.org/) to explain your analysis.

### Authors
You can also list all of the authors who have worked on the project in the frontmatter, and this list will appear at the top of the page and on the summary cards that appear on the main page of the site. To do this you will first need to add each authors' details to the site's people list. For each person you'd like to add to the site, create a new YAML file under `/_data/people/`; e.g. marie_curie.yml. Add the following fields:

* name: how the name should be displayed
* email: optional
* github_username: optional

Once this is done, you can include this person as an author on the project by adding the name of the YAML file (without the .yml suffix) to the author list:

```yaml
authors:
- marie_curie
- karl_popper
```

## Step 4: Make a pull request

When you're ready to publish your project, you can submit a pull request to merge your changes back into the main GitHub repository. If you originally cloned the code as described in step 2, you can push the branch you've created back up to GitHub as follows:

```bash
git push --set-upstream origin <name_of_your_branch>
```

If you open the repository in GitHub, you should be able to see your branch listed in the drop down menu labelled main at the top of the list of files. 

To open a pull request:
* Select Pull requests from the top navigation menu
* Click the green 'New pull request' button
* Select main from the left hand side dropdown labelled base (this should already be selected)
* Select your branch from the right hand side dropdown labelled compare
* Click 'Create pull request'
* Add a title and description, including and details you think may be relevant for somebody reviewing your changes
* Then click 'Create pull request'

Your pull request will then need to be approved by two reviewers who are chosen automatically. Reviewers may make comments or request changes before approving your submission so make sure you are able to receive notifications from GitHub in order to respond to their requests.