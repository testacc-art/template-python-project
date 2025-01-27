<div align="center">

<img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="320px" />

# Template Python Project

![Python Version](https://img.shields.io/github/pipenv/locked/python-version/mundoalem/template-python-project)
![Release Version](https://img.shields.io/github/v/release/mundoalem/template-python-project)
![Pipeline Status](https://github.com/mundoalem/template-python-project/actions/workflows/pipeline.yml/badge.svg)
[![codecov](https://codecov.io/gh/mundoalem/template-python-project/branch/main/graph/badge.svg?token=R0HJ0SAOC0)](https://codecov.io/gh/mundoalem/template-python-project)
![Contributors](https://img.shields.io/github/issues/mundoalem/template-python-project)

A DevOps centric template to bootstrap Python projects.

</div>

## Introduction

This project is a template anyone can use in order to bootstrap a project using the Python programming language. The
template has a full featured pipeline following the latest DevOps practices.

You can control the project through the use of [pipenv](https://pipenv.pypa.io/), it accepts the following targets:

| Argument | Description                                           |
| -------- | ----------------------------------------------------- |
| build    | Build source and wheel packages                       |
| clean    | Remove build files and directories                    |
| docs     | Build documentation                                   |
| install  | Install the project inside the virtual environment    |
| lint     | Check the code for syntax issues and style            |
| release  | Release the package to PyPi                           |
| reset    | Removes build files, directories and test environment |
| scan     | Scan the project for security vulnerabilities         |
| test     | Test the project                                      |
| test37   | Test the project using Python 3.7                     |
| test38   | Test the project using Python 3.8                     |
| test39   | Test the project using Python 3.9                     |

## License

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Tech Stack

These are the software baked in this template:

- [Python](https://www.python.org/) 3.7, 3.8 and 3.9
- [black](https://github.com/psf/black)
- [coverage](https://github.com/nedbat/coveragepy)
- [invoke](http://docs.pyinvoke.org/en/stable/)
- [mypy](http://www.mypy-lang.org/)
- [pytest](https://pypi.org/project/pytest/)
- [Sphinx](https://www.sphinx-doc.org/en/master/)
- [tox](https://tox.readthedocs.io/en/latest/)
- [twine](https://twine.readthedocs.io/en/latest/)

## Usage

In order to use this template you first need to clone this repo locally:

```
$ git clone git@github.com:mundoalem/template-python-project.git
$ cd template-python-project/
```

After you finish cloning the template you can start using it right away, however
it may be better to make the project your own by:

- Configure `setup.cfg` file with your project details.
- Configure in `tox.ini` file the `envlist` property with the Python versions you need.
- Add your license to `LICENSE` file.
- Update the license header in all Python files.
- Configure in `.coveragerc` the `source` property of your project (usually the name of the project).
- Update test files under `tests` directory.
- Make sure you are using the correct Python versions in the jobs configured in `.github/workflows`.
- Make sure to remove the `--noop` argument in the `release` step of the pipeline in `.github/workflows/pipeline.yml`.
- Update the `README.md` with your project information.

All pipeline jobs can be also run locally by invoking `pipenv` scripts, example:

```
$ pipenv run build
$ pipenv run lint
$ pipenv run test
$ pipenv run scan
$ pipenv run release
```

## Environment Variables

To run this project, you will need to add the following environment variables to your environment:

| Variable           | Description                                                           |
| ------------------ | --------------------------------------------------------------------- |
| CODECOV_TOKEN      | Token used to calculate and report test coverage from codecov.io      |
| SNYK_TOKEN         | Token used during the security vulnerabilities scan task from snyk.io |
| PYPI_PASSWORD      | PyPi Password used during the release process                         |
| PYPI_USERNAME      | PyPi User Name used during the release process                        |
| PYPI_PASSWORD_TEST | PyPi Test Password used during the release process                    |
| PYPI_USERNAME_TEST | PyPi Test Password used during the release process                    |

## Feedback

If you have any feedback, please open an [issue](https://github.com/mundoalem/template-python-project/issues).

## Contributing

Please contribute to this repository if any of the following is true:

- You have expertise in community development, communication, or education
- You want open source communities to be more collaborative and inclusive
- You want to help lower the burden to first time contributors

The Prerequisites to contribute:

- Familiarity with pull [requests](https://help.github.com/articles/using-pull-requests) and [issues](https://guides.github.com/features/issues/).
- Knowledge of [Markdown](https://help.github.com/articles/markdown-basics/) for editing `.md` documents.
- Knowledge of [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) for editing `.rst` documents.
- Knowledge of [Python](https://www.python.org) and its ecosystem.

In particular, this community seeks the following types of contributions:

- Ideas: participate in an issue thread or start your own to have your voice heard.
- Resources: submit a pull request to add to `RESOURCES.md` with links to related content.
- Outline sections: help us ensure that this repository is comprehensive. if there is a topic that is overlooked,
  please add it, even if it is just a stub in the form of a header and single sentence. Initially, most things fall into
  this category.
- Writing: contribute your expertise in an area by helping us expand the included content.
- Copy editing: fix typos, clarify language, and generally improve the quality of the content.
- Formatting: help keep content easy to read with consistent formatting.
- Features: add new features to the project.
- Bugfixes: fix open issues.

## Conduct

We are committed to providing a friendly, safe and welcoming environment for all, regardless of gender, sexual
orientation, disability, ethnicity, religion, income or similar personal characteristic.

Please be kind and courteous. There's no need to be mean or rude. Respect that people have differences of opinion and
that every design or implementation choice carries a trade-off and numerous costs. There is seldom a right answer,
merely an optimal answer given a set of values and circumstances.

Please keep unstructured critique to a minimum. If you have solid ideas you want to experiment with, make a fork and see
how it works.

We will exclude you from interaction if you insult, demean or harass anyone. That is not welcome behavior. We interpret
the term "harassment" as including the definition in the [Citizen Code of Conduct](http://citizencodeofconduct.org/);
if you have any lack of clarity about what might be included in that concept, please read their definition. In
particular, we don't tolerate behavior that excludes people in socially marginalized groups.

Whether you're a regular contributor or a newcomer, we care about making this community a safe place for you and we've
got your back.

Likewise any spamming, trolling, flaming, baiting or other attention-stealing behavior is not welcome.

## Communication

GitHub issues are the primary way for communicating about specific proposed changes to this project.

In both contexts, please follow the conduct guidelines above. Language issues are often contentious and we'd like to
keep discussion brief, civil and focused on what we're actually doing, not wandering off into too much imaginary stuff.

## FAQ

### Will there ever be support for other continuous integration platforms?

Right now I have no plans to support other platforms like TravisCI, CircleCI or Gitlab. Anyway, it should be quite
easy for you to port the GitHub Actions to any platform you like.

The reason for that is that I don't want to have a `.travis.yml`, a `circleci.yml` and a `.gitlab-ci.yml` all together
in the same place when only one would actually be used. So I want to avoid (for now) cluttering the template with too
many files that might or might not be useful.
