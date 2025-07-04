-- === EXISTING TABLES ===
CREATE TABLE IF NOT EXISTS items_master (
    id SERIAL PRIMARY KEY,
    item_id TEXT NOT NULL,
    description TEXT,
    revision TEXT,
    lot_flag BOOLEAN,
    shelf_life_days INT,
    default_supplier TEXT,
    change_control_ref TEXT,
    rework_flag BOOLEAN,
    special_process BOOLEAN
);

CREATE TABLE IF NOT EXISTS boms (
    id SERIAL PRIMARY KEY,
    bom_id TEXT NOT NULL,
    parent_item TEXT,
    component_item TEXT,
    quantity NUMERIC,
    uom TEXT,
    e_sign_approval BOOLEAN
);

CREATE TABLE IF NOT EXISTS suppliers (
    id SERIAL PRIMARY KEY,
    supplier_id TEXT NOT NULL,
    name TEXT,
    cert_expiry DATE,
    approved_flag BOOLEAN,
    audit_score INT
);

CREATE TABLE IF NOT EXISTS equipment (
    id SERIAL PRIMARY KEY,
    equipment_id TEXT NOT NULL,
    calibration_next_due DATE,
    calibration_freq TEXT
);

CREATE TABLE IF NOT EXISTS rule_results (
    id SERIAL PRIMARY KEY,
    table_name TEXT,
    record_key TEXT,
    rule_name TEXT,
    status TEXT,
    message TEXT,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- === NEW TABLES FOR FULL COMPLIANCE ===
CREATE TABLE IF NOT EXISTS audit_trail (
    id SERIAL PRIMARY KEY,
    record_table TEXT,
    record_id TEXT,
    action TEXT,
    user_id TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    old_value JSONB,
    new_value JSONB
);

CREATE TABLE IF NOT EXISTS capa (
    id SERIAL PRIMARY KEY,
    capa_id TEXT NOT NULL,
    description TEXT,
    root_cause TEXT,
    effectiveness_review TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    closed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    doc_id TEXT NOT NULL,
    title TEXT,
    current_revision TEXT,
    revision_history TEXT,
    approved_by TEXT,
    approved_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS data_records (
    id SERIAL PRIMARY KEY,
    data_id TEXT NOT NULL,
    activity_date DATE,
    created_by TEXT,
    created_at TIMESTAMP,
    raw_data JSONB
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    name TEXT,
    active_flag BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP,
    password_expiry DATE
);

CREATE TABLE IF NOT EXISTS training_records (
    id SERIAL PRIMARY KEY,
    user_id TEXT,
    course_id TEXT,
    course_name TEXT,
    completed_on DATE
);

CREATE TABLE IF NOT EXISTS process_runs (
    id SERIAL PRIMARY KEY,
    batch_id TEXT,
    process_step TEXT,
    outcome TEXT,
    deviations TEXT
);

CREATE TABLE IF NOT EXISTS deviations (
    id SERIAL PRIMARY KEY,
    deviation_id TEXT NOT NULL,
    description TEXT,
    linked_capa TEXT
);

CREATE TABLE IF NOT EXISTS batches (
    id SERIAL PRIMARY KEY,
    batch_id TEXT NOT NULL,
    product_code TEXT,
    start_date DATE,
    closed_at TIMESTAMP
);
