### Mlflow Tracking Server
import mlflow

# Set the tracking URI to the local server
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Create a new experiment
experiment_name = "monitor_local_host"
mlflow.set_experiment(experiment_name)

# Start a new run
with mlflow.start_run():
    mlflow.log_metric("test1", 1)
    mlflow.log_metric("ahmed", 2) 