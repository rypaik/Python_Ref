# Poetry Guide

```other
project
   ├── poetry.lock
   └── pyproject.toml



# From inside Project Directory
# Initialize Poetry 
poetry init

# Install the Python virtualenv
poetry install

# Add Python Packages
poetry add <PACKAGE_NAME>

# Activate virtualenv
poetry shell



link virtualenv to Jupyter
python -m ipykernel install --user --name=<ENV_NAME>

# TO EXPORT POETRY SETUP
# Poetry makes it easy to share deterministic builds of Python environments. To do so, all you need to do is share or push # the poetry.lock and pyproject.toml file to a repository
# with poetry.lock and pyproject.toml in project directory
poetry install



# installing poetry addons from requirements.txt
poetry add `cat requirements.txt`

#or 
cat requirements.txt|xargs poetry add
```

