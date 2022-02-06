# AWS Lambda for Vultr costs

## Usage

```bash

# Install dependencies
make install

# Local test
make get_costs

# Test deployed lambda endpoint (from AWS API Gateway)
make test_endpoint
```

## Configuration/ Environmental Variables

```bash
VULTR_API_KEY=<vutlr_api_key>
END_POINT=<vultr_endpoint>
TELEGRAM_API_KEY=<key>
```

## Set webhook

```bash
make set_webohook

# or
bash run_set_webhook.sh
```

## Deploy to AWS

Dependencies:

- AWS account
- [AWS CLI](https://aws.amazon.com/de/cli/)
- Create a custom role to deploy directly to AWS Lambda

```bash
make deploy
```

> Note: HTTP deployment option is cheaper and sufficient for this use case.
