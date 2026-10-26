# CI Pipeline Documentation

## Overview

The GitHub Actions workflow in [`.github/workflows/ci.yml`](../.github/workflows/ci.yml)
runs for pushes to `main` or `develop` and pull requests targeting either branch.
It uses Python 3.11 and performs compilation, linting, automated tests, and a
model-accuracy check.

## Jobs and execution order

The workflow has three sequential jobs. Each job runs on a fresh Ubuntu runner;
the `needs` relationship stops downstream jobs when an upstream job fails.

| Job | Dependency | Purpose |
|---|---|---|
| `build-and-lint` | None | Installs the requirements and CI tools, compiles `src` and `tests`, and runs Flake8 on `src/` with a 100-character line limit. |
| `test-suite` | `build-and-lint` | Recreates the Iris raw, preprocessed, and feature datasets; runs all tests with coverage; and uploads JUnit and coverage XML reports. |
| `model-quality-gate` | `test-suite` | Recreates the feature dataset and runs `tests/test_model_quality.py` independently as a dedicated quality check. |

The test job uploads an artifact named `test-and-coverage-reports`, containing
`test-results.xml` and `coverage.xml` when those reports are generated. The
upload step uses `if: always()` so reports are retained when tests fail, if the
files exist.

The model-quality test uses `MIN_ACCEPTABLE_ACCURACY = 0.90`. Since the full
test suite also includes this test, a model-quality regression fails
`test-suite`; by design, `model-quality-gate` is then skipped because it depends
on the test job. The dedicated job runs after a successful full test suite as an
additional explicit CI check.

## Branch protection and pull-request verification

To enforce the workflow on GitHub, a repository administrator must configure a
ruleset or branch protection rule for `main`. Require pull requests and require
the `build-and-lint`, `test-suite`, and `model-quality-gate` status checks to
pass before merging. These are GitHub repository settings and cannot be enabled
by committing this workflow file.

After pushing the workflow, open a pull request targeting `main` and verify that
all three checks appear. A successful run should expose the downloadable
`test-and-coverage-reports` artifact on the Actions run summary.

## Regression demonstration

The practical's regression exercise temporarily raises the threshold in
`tests/test_model_quality.py` from `0.90` to `0.999` on a separate branch and
opens a pull request without merging it. The supplied practical reports model
accuracy of approximately `0.9667`, so the accuracy assertion fails in
`test-suite` and the dependent `model-quality-gate` is skipped. Close the
demonstration pull request without merging, then confirm the normal `0.90`
threshold remains on `main`.

The regression demonstration and branch-protection settings require GitHub
repository access. In this workspace, the normal local suite was verified with
16 passing tests; no claim is made here that a GitHub Actions run or branch
ruleset was configured from this local change.
