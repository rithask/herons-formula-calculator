#!/bin/bash
exec gunicorn -w 4 app:app -b 0.0.0.0:8000