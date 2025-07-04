# ERPGuard

**ERPGuard** is an ERP-agnostic compliance validation platform for regulated industries, automating checks for FDA 21 CFR, ISO 13485, ICH Q10, and ALCOA data integrity.

It connects to your ERP data, runs a configurable JSON-driven rules engine, and generates dashboards, compliance summaries, and audit-ready PDF reports.

## Features
- Validates ERP master data for traceability, supplier compliance, calibration, electronic signatures, and more
- JSON rule configs aligned to regulatory standards (FDA, ISO, ICH)
- Streamlit dashboards and detailed audit reports
- Secure environment-variable database connections
- Dockerized Postgres setup for local or cloud deployments

## Usage
```bash
pip install -r requirements.txt
export PGDATABASE=compliance_db
export PGUSER=youruser
export PGPASSWORD=yourpass
export PGHOST=localhost
python ingestion/csv_loader.py
python validation/rules_engine.py
python compliance_summary.py
python reporting/generate_report.py
streamlit run dashboard/app.py
```

## Docker
`docker-compose.yml` included for easy Postgres startup.

## License
MIT or proprietary — your choice.