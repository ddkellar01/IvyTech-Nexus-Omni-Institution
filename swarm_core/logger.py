import logging
import json
import sys

class SwarmJsonFormatter(logging.Formatter):
    """Formats swarm node logs into structured JSON for centralized observability."""
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage()
        }
        return json.dumps(log_record)

def get_swarm_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(SwarmJsonFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
