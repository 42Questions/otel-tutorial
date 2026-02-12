from opentelemetry.metrics import set_meter_provider
from opentelemetry.trace import set_tracer_provider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import MetricExporter, MetricReader, PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.trace import set_tracer_provider
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

from src.constants import LOCAL_OTEL_EXPORTER_OTLP_METRICS_ENDPOINT, LOCAL_OTEL_EXPORTER_OTLP_TRACES_ENDPOINT

def setup_metrics():
    metric_exporter: MetricExporter = OTLPMetricExporter(endpoint=LOCAL_OTEL_EXPORTER_OTLP_METRICS_ENDPOINT)
    metric_reader: MetricReader = PeriodicExportingMetricReader(metric_exporter)
    meter_provider: MeterProvider = MeterProvider(metric_readers=[metric_reader])
    set_meter_provider(meter_provider=meter_provider)

def setup_traces():
    trace_provider: TracerProvider = TracerProvider()
    span_processor: SimpleSpanProcessor = SimpleSpanProcessor(OTLPSpanExporter(endpoint=LOCAL_OTEL_EXPORTER_OTLP_TRACES_ENDPOINT))
    trace_provider.add_span_processor(span_processor=span_processor)
    set_tracer_provider(trace_provider)

def setup_telemetry():
    setup_metrics()
    setup_traces()
