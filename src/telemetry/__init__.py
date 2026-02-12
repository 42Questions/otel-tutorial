from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import MetricExporter, MetricReader, PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

def setup_metrics():
    metric_exporter: MetricExporter = OTLPMetricExporter(endpoint=)
    metric_reader: MetricReader = PeriodicExportingMetricReader(metric_exporter)
    meter_provider: MeterProvider = MeterProvider(metric_readers=[metric_reader])
    metrics.set_meter_provider(meter_provider=meter_provider)

def setup_telemetry():
    setup_metrics()
