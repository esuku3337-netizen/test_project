import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(name)s: %(message)s",
)

logger.info("openb started")

try:
    dataset_name = "test.csv"
    logger.info("Loading dataset: %s", dataset_name)

    # Simulate a missing dataset
    raise FileNotFoundError("Dataset file not found")

except FileNotFoundError as error:
    logger.error("Could not load dataset: %s", error)

logger.info("Program finished")
