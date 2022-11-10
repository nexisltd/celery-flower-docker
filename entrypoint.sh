#!/bin/sh

python3 getip.py

celery -b amqp://$BROKER_USER:$BROKER_PASS@$BROKER_API:5672 flower