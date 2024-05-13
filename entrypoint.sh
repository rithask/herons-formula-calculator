#!/bin/bash
exec gunicorn -w 4 app:app -b 0.0.0.0:5000 --access-logfile /app/logs/access.log