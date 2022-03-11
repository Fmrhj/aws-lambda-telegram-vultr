# AWS Lambda for Vultr costs
[![AWS Deployment](https://github.com/Fmrhj/aws-lambda-telegram-vultr/actions/workflows/ci.yaml/badge.svg)](https://github.com/Fmrhj/aws-lambda-telegram-vultr/actions/workflows/ci.yaml)
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

It requires a `config.env` file to debug the function locally. The AWS deployment requires the following
environmental variables:

```text
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
