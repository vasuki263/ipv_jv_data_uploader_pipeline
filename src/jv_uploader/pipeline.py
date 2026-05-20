from pathlib import Path
import datetime as dt
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

def process_jv_file(path: str):
    df = parse_jv_file(path)

    fname = Path(path).name
    date_str, time_str = fname.split("_")[0], fname.split("_")[1]
    timestamp = dt.datetime.strptime(date_str + time_str, "%Y%m%d%H%M%S")

    sepiv, tech = detect_sepiv_and_tech(path)

    s3_key = upload_to_s3(df, sepiv, tech, fname)
    register_in_influx(timestamp, s3_key, sepiv, tech)

    return s3_key
