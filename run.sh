#!/bin/bash

set -a
source config.env
set +a

pipenv run python lambda_function.py