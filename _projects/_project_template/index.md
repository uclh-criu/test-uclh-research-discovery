---
title: # project title
tags: # space separated list
layout: project
# Add author data to _data/people and list here:
authors:
- author_1
# Add additional tabs by linking to other sources
tabs:
  - { 
    name: 'extra', # Two tabs cannot share the same name
    type: 'html', # Optional: embed/html/markdown
    source: 'extra.html', # filename or embed url
    label: 'Extra tab' # Optional: label for tab, defaults to capitalised name
    }
  - { 
    name: 'data', 
    type: 'embed',
    source: 'https://www.explainxkcd.com/wiki/images/d/d7/flawed_data.png',
    label: 'Data and Code' # Optional: label for tab, defaults to capitalised name
    }
---

Write your project overview in markdown format here