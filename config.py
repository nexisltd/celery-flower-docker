import os

broker_api = os.getenv("REDIS_URL")

# Enable debug logging
logging = os.getenv("FLOWER_LOGGING_LEVEL")
