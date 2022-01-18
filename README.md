# python-boilerplate
Python Boilerplate Project Structure

## Folder Structure

```
.github/workflows/     # Workflows
    production.yml     # Production workflow
    development.yml    # Development workflow
config/
    env.py             # Environment variables
libs/
    __init__.py
    my_libs.py         # Utility libraries
notebook/
    test.ipynb         # Test notebook (for development)
scripts/
    __init__.py        
    job.py             # Job script 
tests/
    __init__.py
    test_my_libs.py    # Test libraries
    test_job.py        # Test job script              
.dockerignore          # Docker ignore file
.env-example           # Environment variables example
.gitignore             # Git ignore file
conftest.py            # Test configuration file
Dockerfile.kubernetes  # Dockerfile for kubernetes
Dockerfile.lambda      # Dockerfile for lambda
main.job.py            # Main job script
main.service.py        # Main service script
Makefile               # Makefile
poetry.lock            # Poetry lock file
pyproject.toml         # Pyproject.toml
README.md              # Readme
```

## How to Fork
- Create new repository on GitHub (`new-repository-name`)
- Create another folder on local machine
- Clone bare this repository\
    ```bash
    git clone --bare https://github.com/kgmedia-data/python-boilerplate.git
    ```
- CD to this folder (with .git suffix) and push mirror to GitHub
    ```bash
    cd python-boilerplate.git
    git push --mirror https://github.com/kgmedia-data/new-repository-name.git
    ```
- Remove `python-biolerplate.git` folder from local folder
- Clone `new-repository-name` to local folder


## How to Code
- Create a new branch from Boards/dev
- Branch Name:
  ```
  # For story:
  story/ID-BOARD/STORY-TITLE 

  # For task:
  task/ID-BOARD/STORY-ID/TASK-TITLE
  ```
  story and task name are automatically generated using Board.
- Install Poetry
    - Run `poetry install`
    - Run `poetry shell`

## How to Commit
- Commit on the branch
- PR if it should be merged
- Specify the type of commit:
    - feat: The new feature you're adding to a particular application
    - fix: A bug fix
    - style: Feature and updates related to styling
    - refactor: Refactoring a specific section of the codebase
    - test: Everything related to testing
    - docs: Everything related to documentation
    - chore: Regular code maintenance.[ You can also use emojis to represent commit types]
