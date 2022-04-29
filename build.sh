#!/bin/bash
docker build -t herons-calculator . &&
docker run -d -p 8000:8000 herons-calculator