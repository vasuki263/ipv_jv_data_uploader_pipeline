from pathlib import Path
import datetime as dt
import re

from .parser import parse_jv_file
from .s3_upload import upload_to_s3
from .influx import register_in_influx


def detect_sepiv_and_tech(path: str):
    p = Path(path)
    sepiv = p.parent.name

    if "Psk_raw" in str(p):
        tech = "Perovskite_5&6"
    elif "Si_raw" in str(p):
        tech = "SunPower_5-1"
    else:
        tech = "Unknown"

    return sepiv, tech


def extract_timestamp_from_filename(filename: str) -> dt.datetime:
    """
    Extract timestamps from filenames like:
        20250725_070051_SEPIV1.txt

    Pattern:
        YYYYMMDD_HHMMSS_<anything>.txt

    Returns a timezone-aware UTC datetime.
    """
    pattern = r"(\d{8})_(\d{6})"
    match = re.search(pattern, filename)

    if not match:
        raise ValueError(f"No timestamp found in filename: {filename}")

    date_str, time_str = match.groups()

    # Parse into datetime
    ts = dt.datetime.strptime(date_str + time_str, "%Y%m%d%H%M%S")

    # Make timezone-aware (UTC)
    return ts.replace(tzinfo=dt.timezone.utc)


def process_jv_file(path: str):
    """
    Full JV pipeline:
    - Parse JV file
    - Extract timestamp from filename
    - Detect SEPIV + technology
    - Upload CSV to S3
    - Register metadata in InfluxDB
    """
    df = parse_jv_file(path)

    fname = Path(path).name

    # NEW: extract timestamp from filename
    timestamp = extract_timestamp_from_filename(fname)

    sepiv, tech = detect_sepiv_and_tech(path)

    s3_key = upload_to_s3(df, sepiv, tech, fname)

    # Use filename timestamp instead of current time
    register_in_influx(timestamp, s3_key, sepiv, tech)

    return s3_key
