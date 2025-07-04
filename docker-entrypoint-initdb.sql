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