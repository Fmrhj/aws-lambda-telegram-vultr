#!/bin/bash

set -a
source config.env
set +a

pipenv run python set_webhook.py