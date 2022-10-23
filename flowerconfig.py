import os

broker_api = os.getenv("RABBIT_API")
broker = os.getenv("RABBIT_URL", os.getenv("REDIS_URL"))

# Enable debug logging
logging = os.getenv("FLOWER_LOGGING_LEVEL")
