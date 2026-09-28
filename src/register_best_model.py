import os
import mlflow
from mlflow.tracking import MlflowClient


# ---------------------------------------------------------
# 1. MLflow configuration
# ---------------------------------------------------------

mlflow.set_tracking_uri(
    os.getenv(
        "MLFLOW_TRACKING_URI",
        "http://127.0.0.1:5000"
    )
)

EXPERIMENT_NAME = "iris-classification-baseline"
MODEL_NAME = "iris-classifier-prod"


# ---------------------------------------------------------
# 2. Get experiment
# ---------------------------------------------------------

client = MlflowClient()

experiment = client.get_experiment_by_name(
    EXPERIMENT_NAME
)

if experiment is None:
    raise RuntimeError(
        f"Experiment '{EXPERIMENT_NAME}' not found."
    )


# ---------------------------------------------------------
# 3. Find best run using F1 score
# ---------------------------------------------------------

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.f1_macro DESC"],
    max_results=1
)

if not runs:
    raise RuntimeError("No MLflow runs found.")


best_run = runs[0]

run_id = best_run.info.run_id
f1_score = best_run.data.metrics["f1_macro"]

print("Best run:")
print("Run ID:", run_id)
print("F1 Score:", f1_score)


# ---------------------------------------------------------
# 4. Register the model
# ---------------------------------------------------------

model_uri = f"runs:/{run_id}/model"

print("Model URI:", model_uri)

registered_model = mlflow.register_model(
    model_uri=model_uri,
    name=MODEL_NAME
)

print("\nModel registered successfully!")
print("Model Name:", registered_model.name)
print("Model Version:", registered_model.version)