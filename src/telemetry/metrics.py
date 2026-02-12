from functools import wraps

import logging
from opentelemetry.metrics import Counter, get_meter_provider, Meter

from src.constants import APP_NAME, APP_VERSION

_LOGGER = logging.getLogger(__name__)

def get_meter() -> Meter:
    return get_meter_provider().get_meter(name=APP_NAME, version=APP_VERSION)

def increment_counter(func, increment: int=1):
    @wraps(func)
    def wrapper(*args, **kwargs):
        counter_name: str = f"{func.__module__}.{func.__name__}"
        if increment>0:
            meter: Meter = get_meter()
            counter: Counter = meter.create_counter(counter_name)
            counter.add(increment)
        else:
            _LOGGER.warning(counter_name)
        return func(*args, **kwargs)
    return wrapper

