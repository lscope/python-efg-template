from fluent import handler
import logging
import time

# Configurazione del logger
logger = logging.getLogger("fluent.test")
logger.setLevel(logging.INFO)

# Configurazione dell'handler per Fluentd
fluent_handler = handler.FluentHandler("app.follow", host="fluentd", port=24224)
formatter = handler.FluentRecordFormatter({
    "host": "%(hostname)s",
    "where": "%(module)s.%(funcName)s",
    "type": "%(levelname)s",
    "stack_trace": "%(exc_text)s"
})
fluent_handler.setFormatter(formatter)
logger.addHandler(fluent_handler)



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
