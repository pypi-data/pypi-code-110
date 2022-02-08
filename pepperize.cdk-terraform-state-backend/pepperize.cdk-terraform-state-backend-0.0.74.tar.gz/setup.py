import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "pepperize.cdk-terraform-state-backend",
    "version": "0.0.74",
    "description": "This project provides a CDK construct bootstrapping an AWS account with a S3 Bucket and a DynamoDB table as terraform state backend.",
    "license": "MIT",
    "url": "https://github.com/pepperize/cdk-terraform-state-backend.git",
    "long_description_content_type": "text/markdown",
    "author": "Patrick Florek<patrick.florek@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/pepperize/cdk-terraform-state-backend.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "pepperize_cdk_terraform_state_backend",
        "pepperize_cdk_terraform_state_backend._jsii"
    ],
    "package_data": {
        "pepperize_cdk_terraform_state_backend._jsii": [
            "cdk-terraform-state-backend@0.0.74.jsii.tgz"
        ],
        "pepperize_cdk_terraform_state_backend": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk-lib>=2.8.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.52.1, <2.0.0",
        "pepperize.cdk-private-bucket>=0.0.16, <0.0.17",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
