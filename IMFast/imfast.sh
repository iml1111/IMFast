#!/bin/bash
if [ "$1" = "run" ] ; then
    uvicorn main:application \
    --reload \
    --port 5000 --env-file dev.env \
    --log-config uvicorn_log_config.yaml
elif [ "$1" = "prod-run" ] ; then
    uvicorn main:application \
    --port 5000 \
    --env-file prod.env \
    --host=0.0.0.0 \
    --log-config uvicorn_log_config.yaml
elif [ "$1" = "test" ] ; then
    pytest "$*" \
    -o log_cli=true \
    -o log_cli_level=INFO \
    -o log_cli_format="%(message)s"
elif [ "$1" = "" ] ; then
    python main.py
else
    python main.py "$*"
fi