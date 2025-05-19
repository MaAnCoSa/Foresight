# Foresight

<a href="https://cookiecutter-data-science.drivendata.org/" target="_blank">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>
<a href="https://github.com/MaAnCoSa/Foresight" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-hosted-181717?logo=github" />
</a>
<a href="https://github.com/MaAnCoSa/Foresight/tree/main/notebooks" target="_blank">
    <img src="https://img.shields.io/badge/Jupyter-enabled-F37626?logo=jupyter" />
</a>


The **Foresight** project aims to build a machine learning system for estimating the difficulty of encounters in *Dungeons & Dragons*. It leverages structured data from player parties and monsters, combining classification models, hyperparameter tuning, data balancing techniques (like SMOTE), and experiment tracking using MLflow.


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         foresight and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── foresight   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes foresight a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

## Environment Setup (Python 3.12.9)

To set up the development environment for this project, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/MaAnCoSa/Foresight.git
cd Foresight
```

## 2. Create and activate the virtual environment
Make sure you have Python **3.12.9** installed. You can manage multiple versions with pyenv or install it directly.


```bash
python3.12 -m venv foresight_env
source foresight_env/bin/activate
```

On Windows (PowerShell):

```bash
python -m venv foresight_env
.\foresight_env\Scripts\Activate.ps1
```

## 3. Upgrade pip and install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Verify the installation
```bash
python -V       # Should output Python 3.12.9
which python    # Should point to foresight_env/bin/python
```