---
title: "SyncWISE: Window Induced Shift Estimation for Synchronization ofVideo and Accelerometry from Wearable Sensors"
authors:
- shibo
- nabil
author_notes:
- ""
date: "2020-09-01T00:00:00Z"
doi: "https://dl.acm.org/doi/10.1145/3411824"

# Schedule page publish date (NOT publication's date).
publishDate: "2020-10-11T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "2020 ACM International Joint Conference on Pervasive and Ubiquitous Computing (ubicomp 2020)."
publication_short: ""

abstract: "The development and validation of computational models to detect daily human behaviors (e.g., eating, smoking, brushing)
using wearable devices requires labeled data collected from the natural field environment, with tight time synchronization
of the micro-behaviors (e.g., start/end times of hand-to-mouth gestures during a smoking puff or an eating gesture) and
the associated labels. Video data is increasingly being used for such label collection. Unfortunately, wearable devices and
video cameras with independent (and drifting) clocks make tight time synchronization challenging. To address this issue,
we present the Window Induced Shift Estimation method for Synchronization (SyncWISE) approach. We demonstrate the
feasibility and effectiveness of our method by synchronizing the timestamps of a wearable camera and wearable accelerometer
from 163 videos representing 45.2 hours of data from 21 participants enrolled in a real-world smoking cessation study. Our
approach shows significant improvement over the state-of-the-art, even in the presence of high data loss, achieving 90%
synchronization accuracy given a synchronization tolerance of 700 milliseconds. Our method also achieves state-of-the-art
synchronization performance on the CMU-MMAC dataset.
"

# Summary. An optional shortened abstract.
summary: ""


tags:
- health
- wearable
- eating
- sensor
- machinelearning

featured: true

# links:
# - name: ""
#   url: ""
url_pdf: media/papers/68.pdf
url_code: 'https://github.com/HAbitsLab/SyncWISE/'
url_dataset: 'https://doi.org/10.5281/zenodo.4029502'
url_poster: ''
url_project: 'http://syncwiseproject.info/'
url_slides: ''
url_source: 'http://ubicomp.org/ubicomp2020/'
url_video: 'https://www.youtube.com/watch?v=QA1srp0Iv64'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: [syncwise]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---