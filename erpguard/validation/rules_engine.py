import json
from database.connection import get_connection

conn = get_connection()
cur = conn.cursor()

def log_failure(rule, record_key):
    cur.execute("""
        INSERT INTO rule_results (table_name, record_key, rule_name, status, message)
        VALUES (%s, %s, %s, %s, %s)
    """, (rule['table'], str(record_key), rule['rule'], 'FAIL', rule['message']))

def run_rules(rules_file):
    with open(rules_file) as f:
        rules = json.load(f)
    for rule in rules:
        if rule['rule'] == 'must_not_be_null':
            cur.execute(f"SELECT id FROM {rule['table']} WHERE {rule['field']} IS NULL")
            for row in cur.fetchall():
                log_failure(rule, row[0])
        elif rule['rule'] == 'must_be_true':
            cur.execute(f"SELECT id FROM {rule['table']} WHERE {rule['field']} IS NOT TRUE")
            for row in cur.fetchall():
                log_failure(rule, row[0])
        elif rule['rule'] == 'numeric_positive':
            cur.execute(f"SELECT id FROM {rule['table']} WHERE {rule['field']} <= 0 OR {rule['field']} IS NULL")
            for row in cur.fetchall():
                log_failure(rule, row[0])
        elif rule['rule'] == 'not_expired':
            cur.execute(f"SELECT id FROM {rule['table']} WHERE {rule['field']} < CURRENT_DATE")
            for row in cur.fetchall():
                log_failure(rule, row[0])
        elif rule['rule'] == 'date_in_future':
            days = rule.get('days', 0)
            cur.execute(f"SELECT id FROM {rule['table']} WHERE {rule['field']} < (CURRENT_DATE + interval '{days} days')")
            for row in cur.fetchall():
                log_failure(rule, row[0])
        elif rule['rule'] == 'unique_combination':
            fields = ', '.join(rule['field'])
            cur.execute(f"SELECT {fields}, COUNT(*) FROM {rule['table']} GROUP BY {fields} HAVING COUNT(*) > 1")
            for row in cur.fetchall():
                composite_key = '|'.join(map(str, row[:-1]))
                log_failure(rule, composite_key)
        elif rule['rule'] == 'must_exist_in':
            field = rule['field']
            ref_table = rule['reference_table']
            ref_field = rule['reference_field']
            cur.execute(f"SELECT DISTINCT {field} FROM {rule['table']} WHERE {field} IS NOT NULL AND {field} NOT IN (SELECT {ref_field} FROM {ref_table})")
            for row in cur.fetchall():
                log_failure(rule, row[0])
        elif rule['rule'] == 'enum_in_list':
            values = tuple(rule['values'])
            cur.execute(f"SELECT id FROM {rule['table']} WHERE {rule['field']} NOT IN {values}")
            for row in cur.fetchall():
                log_failure(rule, row[0])
        elif rule['rule'] == 'numeric_above':
            min_val = rule.get('min', 0)
            cur.execute(f"SELECT id FROM {rule['table']} WHERE {rule['field']} < {min_val}")
            for row in cur.fetchall():
                log_failure(rule, row[0])
        elif rule['rule'] == 'conditional_boolean':
            cur.execute(f"SELECT id FROM {rule['table']} WHERE {rule.get('condition_field')} IS TRUE AND {rule['field']} IS NOT TRUE")
            for row in cur.fetchall():
                log_failure(rule, row[0])
    conn.commit()

if __name__ == "__main__":
    run_rules('validation/rules/full_compliance_rules.json')