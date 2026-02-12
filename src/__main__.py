from src.constants import APP_NAME
from src.app import run
from src.telemetry import setup_telemetry

def main():
    run()

if __name__=="__main__":
    setup_telemetry()
    main()
