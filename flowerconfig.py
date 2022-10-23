import os

try:
  broker_api = os.getenv("RABBIT_API")
except:
  broker = os.getenv("RABBIT_URL", os.getenv("REDIS_URL"))

# Enable debug logging
logging = os.getenv("FLOWER_LOGGING_LEVEL")
