import boto3


def botoClient(access_key, secret_key, base_url, user):
    session = boto3.session.Session()
    client = session.client('s3', region_name='alpha', endpoint_url=base_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key, verify=False)
    return client


def botoResource(access_key, secret_key, base_url, user):
    session = boto3.session.Session()
    resource = session.resource('s3', region_name='alpha', endpoint_url=base_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key, verify=False)
    return resource
