#  Install virtual environment
> pip install virtualenv

# Create virtual Environment
> python -m venv .venv

# Activate 
> .venv\Scripts\Activate.ps1

# Deactivate
> deactivate

# Best practices 
* Do not commit .venv
* Make seperate .venv for every project
* To save and install all the dependencies
* >>> pip freeze > requirements.txt
* >>> pip install -r requirements.txt




