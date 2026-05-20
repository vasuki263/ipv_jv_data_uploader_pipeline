import influxdb_client_3 as influx
from influxdb_client_3 import WritePrecision
from .config import INFLUX_HOST, INFLUX_DB, INFLUX_TOKEN, MEASUREMENT, AWS_S3_BUCKET_JV
import datetime as dt

def register_in_influx(timestamp, s3_key, sepiv, tech):
    point = (
        influx.Point(MEASUREMENT)
        .time(timestamp, write_precision=WritePrecision.S)
        .tag("sepiv", sepiv)
        .tag("panel_name", tech)
        .field("s3_bucket", AWS_S3_BUCKET_JV)
        .field("s3_object_key", s3_key)
    )
    now = dt.datetime.utcnow()

    point = (
        influx.Point("jv_measurements")
        .time(now, write_precision=influx.WritePrecision.S)
        .tag("sepiv", sepiv)
        .tag("panel_name", tech)
        .field("s3_bucket", AWS_S3_BUCKET_JV)
        .field("s3_object_key", s3_key)
    )

    with influx.InfluxDBClient3(
        host=INFLUX_HOST,
        token=INFLUX_TOKEN,
        database=INFLUX_DB,
    ) as client:
        client.write(point)
