# Feature Store Analysis

## 1. Feature Definitions

The Iris dataset contains both original measurements and engineered features.

### Original Features

- sepal length (cm)
- sepal width (cm)
- petal length (cm)
- petal width (cm)

### Engineered Features

- sepal_area
- petal_area
- sepal_to_petal_length_ratio
- petal_length_bin

These features are registered in Feast using two FeatureViews:

- `iris_measurements`
- `iris_engineered_features`

---

## 2. Entity

The entity used in the feature store is:

`sample_id`

It uniquely identifies each Iris sample.

The entity is defined as an INT64 join key.

---

## 3. Feature Source

The Feast data source is:

`data/iris_features.parquet`

The source contains 149 rows and includes:

- `sample_id`
- Iris measurements
- engineered features
- `event_timestamp`
- `created_timestamp`

---

## 4. Feature Views

### iris_measurements

Contains the original Iris measurements:

- sepal length
- sepal width
- petal length
- petal width

### iris_engineered_features

Contains the engineered features:

- sepal_area
- petal_area
- sepal_to_petal_length_ratio
- petal_length_bin

Both FeatureViews use a 365-day TTL.

---

## 5. Feature Service

The Feature Service is:

`iris_feature_service`

It combines both FeatureViews and allows consumers to request the registered feature set together.

---

## 6. Online Feature Retrieval

Online features were successfully retrieved for:

`sample_id = 1`

The retrieved values included both original and engineered features.

Example:

- sepal length = 4.9
- sepal width = 3.0
- petal length = 1.4
- petal width = 0.2
- sepal_area = 14.7
- petal_area = 0.28
- sepal_to_petal_length_ratio = 3.5
- petal_length_bin = short

---

## 7. Historical Feature Retrieval

Historical feature retrieval was performed using timestamped entity data.

The first 5 samples were successfully retrieved using Feast's historical retrieval API.

The result contained the entity ID, event timestamp, original features, and engineered features.

---

## 8. Feature Reusability

The registered features were reused through:

`iris_feature_service`

The Feature Service successfully returned the registered features for `sample_id = 1`.

This demonstrates that a downstream consumer can reuse the registered features without recreating the feature engineering logic.

---

## 9. Benefits of Using a Feature Store

### Feature Reusability

The same registered features can be reused by multiple models and applications.

### Consistency

Feature definitions are maintained centrally instead of being independently recreated by different consumers.

### Point-in-Time Retrieval

Historical features can be retrieved according to event timestamps.

### Online Serving

Features can be retrieved from the online store for low-latency inference.

### Reduced Feature Duplication

Feature engineering logic does not need to be repeatedly implemented for every model.

---

## 10. Experiment Result

The Feast feature store was successfully implemented for the Iris dataset.

The experiment demonstrated:

1. Feature definition
2. Feature registration
3. Online materialization
4. Online feature retrieval
5. Historical feature retrieval
6. Feature Service reuse

Therefore, the Iris feature store workflow was successfully completed.