# lambda_layer_whitelisting

Respecting the AWS API contract, ensure your credentials are properly exported to your env or in ~/.aws/ or equivalent

Usage:

- pip install layer_whitelisting
- export LAYER_PERMISSION_ACCOUNT_ID to be equal to the requesting customer's AWS account ID
- python layer_whitelisting/lambda_layer_permission.py
