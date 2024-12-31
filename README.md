# Tristan McKinney's Python package template

Use this to quickly start new Python projects with [Hatchling](https://hatch.pypa.io/latest/), [Ruff](https://docs.astral.sh/ruff/), [tox](https://tox.wiki/en/4.23.2/), [pytest](https://docs.pytest.org/en/stable/), and [mypy](https://mypy-lang.org/index.html). [This](https://github.com/ndjenkins85/ndj_cookie) is similar. 

## Usage

Follow the [cookiecutter](https://github.com/cookiecutter/cookiecutter) instructions to use the template to create your project. Once you've created the project, I recommend creating a virtual environment, then installing your new package with dependencies for local development with

```bash
pip install -e '.[dev]'
```

You can then run formatting, type checking, and tests for different Python versions with

```bash
tox -p
```

(the `-p` runs them in parallel) and you can build for distribution with

```bash
hatch build
```
