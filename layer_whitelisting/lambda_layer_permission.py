import os
import boto3

aws_region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
lambda_client = boto3.client("lambda", region_name=aws_region)


def list_latest_layer_version_arns():
    layers = []
    c = 0
    for i in lambda_client.list_layers():
        layers.append(
            lambda_client.list_layers()
            .get("Layers")[c]
            .get("LatestMatchingVersion")
            .get("LayerVersionArn")
        )
        c = c + 1
    return layers


def add_layer_version_permission(principal):
    action = "lambda:GetLayerVersion"
    for arn in list_latest_layer_version_arns():
        layer_name = arn.split(":")[6]
        version_num = int(arn.split(":")[7])
        lambda_client.add_layer_version_permission(
            LayerName=layer_name,
            VersionNumber=version_num,
            StatementId=f"Allow-{principal}-on-{layer_name}-v{version_num}",
            Action=action,
            Principal=principal,
        )


def main():
    customer_aws_account_id = os.getenv("LAYER_PERMISSION_ACCOUNT_ID", "noID")
    if "noID" in customer_aws_account_id:
        print("No customer account provided")
    else:
        add_layer_version_permission(customer_aws_account_id)


if __name__ == "__main__":
    main()
