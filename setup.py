from setuptools import setup

setup(
    name="lambda_layer_whitelisting",
    version="0.0.3",
    description="Lambda layer registry whitelisting",
    url="http://github.com/hazurd/lambda_layer_whitelisting",
    author="Karl Dagenais",
    author_email="dagenaisx@gmail.com",
    license="Apache-2.0",
    packages=["lambda_layer_whitelisting"],
    install_requires=[
        'boto3', 'botocore', 'pytest'
    ],
    zip_safe=False,
)
