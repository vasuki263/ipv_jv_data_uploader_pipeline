import pandas as pd

def parse_jv_file(path: str) -> pd.DataFrame:
    with open(path, "r") as f:
        lines = f.readlines()

    temp_line = lines[0].strip().replace("Temperature :", "").replace("C;", "")
    temperature = float(temp_line)

    rows = []
    for line in lines[1:]:
        line = line.strip().rstrip(";")
        if not line:
            continue
        parts = line.split(";")
        if len(parts) < 5:
            continue
        rows.append(parts[:5])

    df = pd.DataFrame(rows, columns=["serial", "sweep_percent", "voltage", "current", "irradiance"])
    df["serial"] = df["serial"].astype(int)
    df["sweep_percent"] = df["sweep_percent"].str.replace("%", "").astype(float)
    df["voltage"] = df["voltage"].astype(float)
    df["current"] = df["current"].astype(float)
    df["irradiance"] = df["irradiance"].astype(float)
    df["temperature"] = temperature

    return df
