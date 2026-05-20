from unittest.mock import MagicMock
from src.jv_uploader.influx import register_in_influx
from src.jv_uploader import config
import datetime as dt

def test_register_in_influx(monkeypatch):
    # Mock InfluxDB client context manager
    mock_client = MagicMock()
    mock_ctx = MagicMock()
    mock_ctx.__enter__.return_value = mock_client

    # Patch config token
    monkeypatch.setattr(config, "INFLUX_TOKEN", "FAKE_TOKEN")

    # Patch the InfluxDBClient3 constructor
    monkeypatch.setattr(
        "src.jv_uploader.influx.influx.InfluxDBClient3",
        lambda **kwargs: mock_ctx
    )

    # Call function
    ts = dt.datetime(2025, 7, 28, 7, 1, 49)
    register_in_influx(
        ts,
        "SEPIV3/Perovskite_5&6/file.csv",
        "SEPIV3",
        "Perovskite_5&6"
    )

    # Assert write was called
    assert mock_client.write.called
