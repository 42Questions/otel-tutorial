from typing import Final

APP_NAME: Final[str] = "otel-tutorial-app"
APP_VERSION: Final[str] = "0.0.1"

# TO MOVE INTO DOCKER COMPOSE
LOCAL_OTEL_EXPORTER_OTLP_METRICS_ENDPOINT: Final[str] = "http://otel-collector:4317"
