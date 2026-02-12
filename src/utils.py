import time
import random
from src.telemetry.traces import trace

@trace()
def foo():
    time.sleep(random.randint(1,3))
