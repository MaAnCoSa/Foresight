import os
import mlflow
from mlflow.tracking import MlflowClient
from datetime import datetime
from dotenv import load_dotenv

# --- Ruta base del proyecto ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# --- Cargar solo el token desde .env ---
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

# --- Configurar variables ---
os.environ["MLFLOW_TRACKING_USERNAME"] = "Jesolis14"
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/MaAnCoSa/Foresight.mlflow"
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])

client = MlflowClient()

def format_time(ts):
    return datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S") if ts else "N/A"

def export_all_experiments(output_filename="mlflow_experiments_report.md"):
    output_path = os.path.join(BASE_DIR, "reports", output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# MLflow Tracking Report (All Experiments)\n\n")

        experiments = client.search_experiments()
        if not experiments:
            f.write("No experiments found.\n")
            return

        for exp in experiments:
            f.write(f"## Experiment: {exp.name}\n")
            f.write(f"- ID: {exp.experiment_id}\n")
            f.write(f"- Artifact Location: {exp.artifact_location}\n")
            f.write(f"- Lifecycle Stage: {exp.lifecycle_stage}\n\n")

            runs = client.search_runs([exp.experiment_id], order_by=["attributes.start_time DESC"])
            if not runs:
                f.write("No runs found for this experiment.\n\n")
                continue

            for run in runs:
                info = run.info
                data = run.data

                f.write(f"### Run: {data.tags.get('mlflow.runName', '(no name)')}\n")
                f.write(f"- Run ID: {info.run_id}\n")
                f.write(f"- User: {info.user_id}\n")
                f.write(f"- Status: {info.status}\n")
                f.write(f"- Start Time: {format_time(info.start_time)}\n")
                f.write(f"- End Time: {format_time(info.end_time)}\n")

                if info.end_time and info.start_time:
                    duration = (info.end_time - info.start_time) / 1000
                    f.write(f"- Duration: {duration:.2f} seconds\n")
                else:
                    f.write("- Duration: Unknown\n")

                # Parámetros
                f.write("- Parameters:\n")
                if data.params:
                    for k, v in data.params.items():
                        f.write(f"  - {k}: {v}\n")
                else:
                    f.write("  - None\n")

                # Métricas
                f.write("- Metrics:\n")
                if data.metrics:
                    for k, v in data.metrics.items():
                        f.write(f"  - {k}: {v}\n")
                else:
                    f.write("  - None\n")

                # Artefactos
                artifacts = client.list_artifacts(info.run_id)
                f.write("- Artifacts:\n")
                if artifacts:
                    for art in artifacts:
                        f.write(f"  - {art.path}\n")
                else:
                    f.write("  - None\n")

                f.write("\n---\n\n")

    print(f"Report saved to: {output_path}")

# Ejecutar
export_all_experiments()



