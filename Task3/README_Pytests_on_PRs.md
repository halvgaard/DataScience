## Adding more tests to be run on PRs in GitHub Action

The GitHub workflow `pytests-on-PRs.yml` in the directory `.github/workflows` runs all tests in `Task3/tests/` 
on all PRs.

If you wish to add more tests for the workflow, simply add another file to the directory (or in a subdirectory)
and make sure it is of format **test_x.py** or **x_test.py**, where x is arbitrary.
Pytest requires the test function names to start with **test**.
