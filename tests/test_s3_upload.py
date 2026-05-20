import pandas as pd
from unittest.mock import MagicMock
from src.jv_uploader.s3_upload import upload_to_s3
from src.jv_uploader import config

def test_upload_to_s3(monkeypatch):
    df = pd.DataFrame({"a": [1], "b": [2]})

    # Fake AWS credentials
    monkeypatch.setattr(config, "AWS_ACCESS_KEY", "FAKE")
    monkeypatch.setattr(config, "AWS_SECRET_KEY", "FAKE")
    monkeypatch.setattr(config, "AWS_S3_BUCKET_JV", "test-bucket")

    # Mock boto3 client
    mock_s3 = MagicMock()
    monkeypatch.setattr(
        "src.jv_uploader.s3_upload.boto3.client",
        lambda *args, **kwargs: mock_s3
    )

    key = upload_to_s3(df, "SEPIV3", "Perovskite_5&6", "test.txt")

    # Correct object key
    assert key == "SEPIV3/Perovskite_5&6/test.csv"

    # Ensure upload_file was called with correct args
    mock_s3.upload_file.assert_called_once()
    args, kwargs = mock_s3.upload_file.call_args

    # args = (local_temp_file, bucket, object_key)
    assert args[1] == "solar-park-jv"
    assert args[2] == "SEPIV3/Perovskite_5&6/test.csv"
