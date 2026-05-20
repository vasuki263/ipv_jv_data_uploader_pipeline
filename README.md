📘 JV Uploader Pipeline
A modular Python pipeline for parsing JV measurement files, converting them to CSV, uploading them to AWS S3, and registering metadata in InfluxDB.
Supports both single‑file uploads and batch uploads with progress indicators.


🚀 Features
- Parse JV .txt files into structured Pandas DataFrames
- Convert JV data to CSV and upload to AWS S3
- Register upload metadata in InfluxDB (jv_measurements)
- CLI interface:
  ° upload-one — upload a single JV file
  ° upload-all — upload an entire directory
- Automatic timestamping using UTC now
- Clean modular architecture (parser, pipeline, s3_upload, influx, batch, cli)
- Unit tests for all components
- Progress indicators for batch processing


📂 Project Structure
**'''**
src/jv_uploader/
│
├── parser.py          # Parse JV text files → DataFrame
├── s3_upload.py       # Upload CSV to AWS S3
├── influx.py          # Register metadata in InfluxDB
├── pipeline.py        # Full JV → S3 → Influx pipeline
├── batch.py           # Batch directory processing
├── cli.py             # Command-line interface
├── config.py          # Environment variable loading
└── __init__.py
'''

🔧 Installation
1. Clone the repository
   git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
2. Create a virtual environment
   python -m venv .venv
  source .venv/bin/activate   # Linux/Mac
  .venv\Scripts\activate      # Windows
3. Install dependencies
   pip install -r requirements.txt


🔐 Environment Variables
Create a .env file in the project root:
SOLAR_PARK_JV_AWS_ACCESS_KEY_ID=your_key
SOLAR_PARK_JV_AWS_SECRET_ACCESS_KEY=your_secret
SOLAR_PARK_SPECTRA_INFLUXDB_TOKEN=your_influx_token


🧪 Running Unit Tests
pytest -q
All core modules have dedicated tests:
- parser
- S3 upload
- Influx registration
- pipeline
- batch processing


🖥️ CLI Usage
▶️ Upload a single JV file
python -m src.jv_uploader.cli upload-one --file path/to/file.txt

▶️ Upload all JV files in a directory
python -m src.jv_uploader.cli upload-all --root path/to/folder

Progress bars appear automatically.


🔄 Pipeline Overview
1. Parse JV file
Extracts:
- temperature
- serial
- sweep percent
- voltage
- current
- irradiance

2. Upload CSV to S3
Stored under:
<SEPIV>/<panel_name>/<filename>.csv

3. Register metadata in InfluxDB
Fields stored:
- s3_bucket
- s3_object_key
- sepiv
- technology
- timestamp = UTC now


🛠️ Development Notes
All timestamps use UTC now for consistency
.env is loaded globally to avoid token mismatch
S3 uploads use temporary files for safe writes
InfluxDB writes use InfluxDBClient3 context manager
