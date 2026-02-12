from functools import wraps
from opentelemetry.trace import get_tracer, Tracer
import logging

from src.constants import APP_NAME, APP_VERSION

_LOGGER = logging.getLogger(__name__)

def trace():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tracer: Tracer = get_tracer(instrumenting_module_name=APP_NAME, instrumenting_library_version=APP_VERSION)
            with tracer.start_as_current_span(func.__name__) as span:
                _LOGGER.debug("Starting span for %s", func.__name__)
                return func(*args, **kwargs)
        return wrapper
    return decorator
