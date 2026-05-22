import os
from dotenv import load_dotenv

load_dotenv()

AWS_S3_BUCKET_JV = "solar-park-jv"

AWS_ACCESS_KEY = os.getenv("SOLAR_PARK_JV_AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("SOLAR_PARK_JV_AWS_SECRET_ACCESS_KEY")

INFLUX_HOST = "https://eu-central-1-1.aws.cloud2.influxdata.com"
INFLUX_DB = "test_jv_upload"
INFLUX_TOKEN = os.getenv("INFLUXDB_TOKEN")

MEASUREMENT = "jv_measurements"
