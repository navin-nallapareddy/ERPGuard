# ERPGuard

**ERPGuard** is an ERP-agnostic compliance validation platform for regulated industries. It automates checks for FDA 21 CFR, ISO 13485, ICH Q10 and ALCOA data integrity.

It connects to your ERP data, runs a configurable JSON-driven rules engine and generates dashboards, compliance summaries and audit-ready PDF reports.

## Features
- Validates ERP master data for traceability, supplier compliance and calibration
- JSON rule configs aligned to regulatory standards
- Streamlit dashboards and PDF reports
- Secure environment variable database connections
- Dockerized Postgres setup for local or cloud deployments

## Usage
```bash
poetry install
export DATABASE_URL=postgres://user:pass@localhost:5432/compliance_db
python erpguard/validation/rules_engine.py
python erpguard/compliance_summary.py
python erpguard/reporting/generate_report.py
streamlit run erpguard/dashboard/app.py
```

### Upload sample data
Use the dashboard sidebar to upload CSV files for the `items_master`,
`suppliers` and `equipment` tables. Click **Load and Run** to populate
the database and execute the validation rules. A set of example CSVs is
provided in the `samples` directory for quick testing.
For convenience `items_master_columns.csv` and `suppliers_columns.csv`
list every column in their respective tables so the headers always match
the database schema.

### Render deployment
ERPGuard is also ready for [Render](https://render.com) hosting. The `render.yaml`
file provisions a free PostgreSQL 16 database named `api-db` and injects its
connection string into the `DATABASE_URL` environment variable. When deploying
to Render no extra configuration is needed&mdash;the app will automatically use
this connection string.

## Docker
`docker-compose.yml` included for easy Postgres 16 startup.

## License
MIT or proprietary — your choice.

## 🚀 Local development instructions
1. Copy `sample.env` to `.env` and update with your Postgres credentials.
   Set `PGSSLMODE=disable` if connecting to a local database.
2. Load environment variables:
```bash
export $(cat .env | xargs)
```
3. Run your compliance checks as shown in the usage section.
