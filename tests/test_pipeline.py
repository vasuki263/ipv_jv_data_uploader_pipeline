import pandas as pd
from unittest.mock import MagicMock
from src.jv_uploader.pipeline import process_jv_file

def test_process_jv_file(monkeypatch, tmp_path):
    # Create sample JV file
    content = """Temperature : 13.172C;
1;0.00%;27.281;0.079;13.125;
"""
    file = tmp_path / "20250728_070149_SEPIV3.txt"
    file.write_text(content)

    # Mock parser to return a valid DataFrame
    mock_df = pd.DataFrame({"dummy": [1]})
    monkeypatch.setattr(
        "src.jv_uploader.pipeline.parse_jv_file",
        lambda p: mock_df
    )

    # Mock S3 upload
    monkeypatch.setattr(
        "src.jv_uploader.pipeline.upload_to_s3",
        lambda df, s, t, f: "mock/key.csv"
    )

    # Mock Influx
    mock_register = MagicMock()
    monkeypatch.setattr(
        "src.jv_uploader.pipeline.register_in_influx",
        mock_register
    )

    # Run pipeline
    key = process_jv_file(str(file))

    # Assertions
    assert key == "mock/key.csv"
    assert mock_register.called
