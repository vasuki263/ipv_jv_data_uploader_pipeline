import pandas as pd
from src.jv_uploader.parser import parse_jv_file

def test_parse_jv_file(tmp_path):
    content = """Temperature : 13.172C;
1;0.00%;27.281;0.079;13.125;
2;0.11%;90.059;0.043;35.437;
"""

    file = tmp_path / "sample_jv.txt"
    file.write_text(content)

    df = parse_jv_file(str(file))

    # Basic structure
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 6)

    # Temperature column
    assert df["temperature"].iloc[0] == 13.172

    # Parsed numeric values
    assert df["serial"].tolist() == [1, 2]
    assert df["sweep_percent"].tolist() == [0.00, 0.11]
    assert df["voltage"].iloc[0] == 27.281
    assert df["current"].iloc[1] == 0.043
    assert df["irradiance"].iloc[1] == 35.437
