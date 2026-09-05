import logging
import os
from datetime import date
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = ROOT_DIR / "logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)


today = date.today()

log_file = LOG_DIR / f"pipeline_{today.year}-{today.month}-{today.day}.log"


logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("dse_pipeline")