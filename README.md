# HABits Lab Website design

This is the repo to edit the github.io page for the lab.
Uses the Hugo [Academinc Theme](https://themes.gohugo.io/academic/)
[Hugo Commands](https://gohugo.io/commands/)

The deployed page is a submodule of this repository.

## Overview:
1. Download and install all prerequisites:
    - https://wowchemy.com/docs/getting-started/install-hugo-extended/

2. Clone this repository with all submodules:
    - `git clone --recurse-submodules https://github.com/HAbitsLab/habits_lab_webpage.git`

3. Test and develop locally:
    - cd into repository
    - use command `hugo server`
    - you can visit local server at localhost:1313

4. Build:
    - To build static page with hugo use command `hugo`
    - This builds site to the "public" directory where the github.io submodule is located

4. Deploy:
    - Commit changes to webpage edit repo
    - cd into public directory, this is the submodule for the deployable page and add and commit changes.
    - after a few minutes to changes should propagate to habitslab.github.io

## Edit pages:
1. Create new content with hugo commands
    - To create a new project use the command: `hugo new  --kind project project/TestProject`
    - To create a new publication `hugo new  --kind publication publication/TestPublication`
    - To create a new team member `hugo new  --kind authors authors/Test`
      - This creates the directory and the index markdown that can be edited.
      - To add an image, add a jpg named "featured.jpg" to the directory
      - In the index.md edit content, i.e authors, tags
2. Can edit existing content by editing the markdown

> REMEMBER TO BUILD WITH `hugo` COMMAND AND PUSH TO SUBMODULE TO DEPLOY CHANGES
