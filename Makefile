include config.env

install:
	pipenv install

deploy:
	zip $(HANDLER_NAME).zip $(HANDLER_NAME).py constants.py
	aws lambda update-function-code --function-name $(FUNCTION_NAME) \
		--zip-file fileb://$(HANDLER_NAME).zip

get_costs:
	bash run_function.sh

set_webhook:
	bash run_set_webhook.sh

test_endpoint:
	curl -X GET $(WEBHOOK_URL) | json_pp