import influxdb_client_3 as influx
from influxdb_client_3 import WritePrecision
from .config import INFLUX_HOST, INFLUX_DB, INFLUX_TOKEN, MEASUREMENT, AWS_S3_BUCKET_JV


def register_in_influx(timestamp, s3_key, sepiv, tech):
    """
    Write metadata entry to InfluxDB using the timestamp extracted from filename.
    """

    point = (
        influx.Point(MEASUREMENT)
        .time(timestamp, write_precision=WritePrecision.S)  # <-- USE FILENAME TIMESTAMP
        .tag("sepiv", sepiv)
        .tag("panel_name", tech)
        .field("s3_bucket", AWS_S3_BUCKET_JV)
        .field("s3_object_key", s3_key)
    )

    # Write to InfluxDB
    with influx.InfluxDBClient3(
        host=INFLUX_HOST,
        token=INFLUX_TOKEN,
        database=INFLUX_DB,
    ) as client:
        client.write(point)
