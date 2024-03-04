import time
import logging
import logstash


# Logstash configuration
host = "logstash"

logger = logging.getLogger("python-logstash-logger") # Logger name
logger.setLevel(logging.INFO) # Log level
logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1)) # Logstash handler






if __name__ == "__main__":
    n_message = 0

    try:
        # Keep sending logs to logstash
        while True:
            logger.info(f"Printed test message {n_message}")
            n_message += 1

            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
        exit(0)
