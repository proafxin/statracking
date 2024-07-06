# Statracking

[![Build, test with Tox and publish to Pypi](https://github.com/proafxin/statracking/actions/workflows/test_release.yaml/badge.svg)](https://github.com/proafxin/statracking/actions/workflows/test_release.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/proafxin/statracking/develop.svg)](https://results.pre-commit.ci/latest/github/proafxin/statracking/develop)

Extract stats from scoreboard screenshots.

## How to use locally

Only use it in linux systems with GPU support for [pytorch](https://pytorch.org/get-started/locally/). Steps to run the server:

* Install poetry: `curl -sSL https://install.python-poetry.org | python3 -`
* Install tox: `python3 -m pip install -U tox`
* Run the server: `tox -e runserver`
