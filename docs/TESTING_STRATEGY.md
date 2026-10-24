
# Testing Strategy — MLOps Iris Classifier

## Aim
Test data processing, feature engineering, data validation,
model training, and model outputs using pytest.

## Test Files

1. tests/test_preprocess.py
   Tests duplicate removal, missing numeric values,
   missing target labels, and empty datasets.

2. tests/test_features.py
   Tests sepal area, petal area, length ratio,
   petal length categories, and zero-division handling.

3. tests/test_validate.py
   Tests valid data, missing columns, invalid species,
   and out-of-range measurements.

4. tests/test_training_pipeline.py
   Tests model training, prediction shape,
   and probability sums.

5. tests/test_model_quality.py
   Tests valid predicted classes and the minimum
   accuracy threshold of 0.90.

## Execution Command
pytest --cov=src --cov-report=term-missing --junitxml=test-results.xml

## Actual Test Results
Tests passed: 16
Overall source-code coverage: 18%
Test report: test-results.xml
