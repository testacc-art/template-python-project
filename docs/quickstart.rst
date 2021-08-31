Quickstart
==========

In order to use this template you first need to clone this repo locally:

.. code-block:: bash

  $ git clone git@github.com:mundoalem/template-python-project.git
  $ cd template-python-project/

After you finish cloning the template you can start using it right away, however
it may be better to make the project your own by:

- Configure `setup.cfg` file with your project details.
- Configure in `tox.ini` file the `envlist` property with the Python versions you need.
- Add your license to `LICENSE` file.
- Update the license header in all Python files.
- Configure in `.coveragerc` the `source` property of your project (usually the name of the project).
- Update test files under `tests` directory.
- Make sure you are using the correct Python versions in the jobs configured in `.github/workflows`.
- Make sure to remove the `--noop` argumento in the `release` step of the pipeline in `.github/workflows/pipeline.yml`
- Update the `README.md` with your project information.

All pipeline jobs can be also run locally by invoking ``pipenv`` scripts, example:

.. code-block:: bash
  
  $ pipenv run build
  $ pipenv run lint
  $ pipenv run test
  $ pipenv run scan
  $ pipenv run release
