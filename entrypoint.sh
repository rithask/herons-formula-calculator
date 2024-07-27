#!/bin/bash
exec gunicorn app:app -b 0.0.0.0:8000 --access-logfile /app/logs/access.log
