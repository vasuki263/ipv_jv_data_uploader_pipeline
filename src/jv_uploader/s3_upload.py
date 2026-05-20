import boto3
import posixpath
import tempfile
from .config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_S3_BUCKET_JV

def upload_to_s3(df, sepiv, tech, filename):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
    )

    object_key = posixpath.join(sepiv, tech, filename.replace(".txt", ".csv"))

    with tempfile.NamedTemporaryFile(delete=False) as f:
        df.to_csv(f.name, index=False)
        s3.upload_file(f.name, AWS_S3_BUCKET_JV, object_key)

    return object_key
