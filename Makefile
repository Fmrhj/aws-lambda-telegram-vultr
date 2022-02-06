WEBHOOK_URL=""

install:
	pipenv install

get_costs:
	bash run_function.sh

set_webhook:
	bash run_set_webhook.sh

test_endpoint:
	curl -X GET $(WEBHOOK_URL) | json_pp