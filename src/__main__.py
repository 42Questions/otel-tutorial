from src.app import run
from src.telemetry import setup_telemetry

setup_telemetry()

def main():
    run()

if __name__=="__main__":
    main()
