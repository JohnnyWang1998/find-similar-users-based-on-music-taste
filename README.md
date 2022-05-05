find-similar-users-based-on-music-taste
==============================

In this project, we recommend new friends and their favorite songs to users based on their similarity of music taste. We utilized the user listening habits dataset collected from last.fm

Project Organization
------------
.
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── data
│   ├── external
│   ├── interim
│   │   └── user-listen-count.csv
│   └── processed
│       └── user_track_df_reduced.csv
├── notebooks
│   ├── 0.1-johnny-data_sampling.ipynb
│   ├── 0.2-johnny-preprocess.ipynb
│   ├── 0.3-johnny-dimensionality_reduction.ipynb
│   ├── 1.0-johnny-similarity.ipynb
│   ├── 1.1-johnny-similarity-optimized.ipynb
│   └── 2.0-chams-recommendation.ipynb
├── references
│   └── HMT11-Finding-Structure-SIREV.pdf
├── reports
│   └── figures
│       ├── Histogram of track listened times.png
│       ├── dendrogram.png
│       ├── dendrogram1.png
│       ├── hourly count.png
│       ├── monthly count.png
│       ├── reconstruction error.png
│       ├── scatter after svd.png
│       ├── tsne after.png
│       └── tsne before.png
├── requirements.txt
├── setup.py
└── src
    ├── __init__.py
    ├── data
    │   ├── __init__.py
    │   ├── dimensionality_reduction.py
    │   └── preprocessor.py
    ├── models
    │   ├── __init__.py
    │   ├── predict_model.py
    │   └── train_model.py
    └── visualization
        ├── __init__.py
        └── visualize.py


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>
