WEBHOOK_URL=""

install:
	pipenv install

get_costs:
	pipenv run python lambda_function.py

test_endpoint:
	curl -X GET $(WEBHOOK_URL) | json_pp