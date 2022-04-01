# Steps to reproduce this poetry project

1. Install pyenv to install and manage different versions of python: `brew install pyenv` (on macOS)
	- Run: `echo 'eval "$(pyenv init --path)"' >> ~/.zprofile`
	- Run: `echo eval "$(pyenv init -)"' >> ~/.zshrc`
	- or in general follow this guide: https://github.com/pyenv/pyenv

2. Install python 3.7.9: `pyenv install 3.7.9`
3. Switch to the new version: `pyenv local 3.7.9`
	- Test the version: `python -V`
5. Create a new poetry project: `poetry new zenml-project`
6. Check the `.toml` file if the python version is set correctly
7. Install dependencies and create virtual environment: `poetry install`
8. Activate virtual environment: `poetry shell`
	- This creates a new virtual shell inside your running shell (you can exit it: `exit` when needed)
9. It is important that the virtual environment uses python >= 3.7.1 and less than 3.9 for _zenml_ to work
10. Add zenml package: `poetry add zenml`
11. Change directory: `cd zenml-project`
12. Initialize zenml: `zenml init`
13. Install sklearn: `zenml integration install sklearn`


# Setup environment using PyCharm
1. Clone repo and open this folder `zenml-project` as a PyCharm project
2. Make sure the Poetry plugin is installed or update to Professional
3. Say yes when PyCharm opens the project and asks to setup Poetry environment based on the pyproject.toml file 
4. Alternatively, go to File > Settings > Project and add the Poetry environment manually and run `poetry install`. Make sure to select Python 3.7.
5. Initialize zenml: `zenml init`
6. Install sklearn: `zenml integration install sklearn`


# Run the test script

1. cd into zenml-project
2. Run `python3 gettingstarted.py`
	- Pipeline that contains:
		- Importer (imports MNIST digit data set with a predefined model)
		- Trainer (trains the model)
		- Evaluator (evaluates the model on a test set)


