from src.jv_uploader.batch import upload_all_jv
from unittest.mock import MagicMock
from pathlib import Path

def test_upload_all_jv(monkeypatch, tmp_path):
    # Create fake JV files with minimal valid content
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"

    f1.write_text(
        "Temperature : 10C;\n"
        "1;10%;0.5;0.1;1000;\n"
    )
    f2.write_text(
        "Temperature : 20C;\n"
        "2;20%;0.6;0.2;900;\n"
    )

    # Mock process_jv_file so we don't actually parse/upload
    mock_process = MagicMock()
    monkeypatch.setattr("src.jv_uploader.batch.process_jv_file", mock_process)

    upload_all_jv(str(tmp_path))

    # Expect both files to be processed
    assert mock_process.call_count == 2
