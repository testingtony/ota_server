# python poetry devcontainer

Python project using [Poetry](https://python-poetry.org/) for a developing in a devcontainer.

It contains GitHub action workflows for trunk-based development. i.e. always work and push on "trunk". Pushes that fail either flake8 or pytest will
be rolled back.

## How to configure

* update [pyproject.toml](pyproject.toml)
  * change `name` and `description` sections
  * update/remove the `tool.poetry.scripts` section
* rename the `template` folder to match the project name
* make a thing

### Optional

Set up git and dynamic versions
```shell
git init -b trunk
poetry dynamic-versioning enable
git add .
git commit -m "Base"
```
