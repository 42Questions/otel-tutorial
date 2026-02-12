from functools import wraps

import logging
from opentelemetry.metrics import Counter, get_meter_provider, Meter

from src.constants import APP_NAME, APP_VERSION

_COUNTERS: dict[str, Counter] = {}
_LOGGER = logging.getLogger(__name__)

def get_meter() -> Meter:
    return get_meter_provider().get_meter(name=APP_NAME, version=APP_VERSION)

def increment_counter(increment: int=1):
    def decorator(func):
        counter_name: str = f"{func.__module__}.{func.__name__}"
        if increment>0:
            meter: Meter = get_meter()
            if _COUNTERS.get(counter_name) is None:
                _COUNTERS[counter_name] = meter.create_counter(counter_name)
            _COUNTERS.get(counter_name).add(increment)
        else:
            _LOGGER.warning("%s must be incremented by > 0",counter_name)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
