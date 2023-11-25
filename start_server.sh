#!/bin/bash
HOST=${1:-'127.0.0.1'}
uvicorn aviasales_bot_admin.main:app --host $HOST --reload