import pytest
from botocore.stub import Stubber
from lambda_layer_whitelisting import lambda_layer_permission


@pytest.fixture(scope="function")
def lambda_stubber():
    lambda_stubber = Stubber(lambda_layer_permission.lambda_client)
    lambda_stubber.activate()
    yield lambda_stubber
    lambda_stubber.deactivate()


def test_layer_exists(lambda_stubber):
    list_layers_params = {

    }
    list_layers_response = {
        'NextMarker': 'string',
        'Layers': [
            {
                'LayerName': 'string',
                'LayerArn': 'string',
                'LatestMatchingVersion': {
                    'LayerVersionArn': 'string',
                    'Version': 123,
                    'Description': 'string',
                    'CreatedDate': 'string',
                    'CompatibleRuntimes': ['provided'],
                    'LicenseInfo': 'string'
                }
            },
        ]
    }

    lambda_stubber.add_response('list_layers', list_layers_response)
