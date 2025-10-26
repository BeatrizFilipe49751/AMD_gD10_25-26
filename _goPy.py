import os

# Database credentials
db_name = "postgres"
db_user = "postgres"

# Paths
sql_script = "create_view.sql"
output_file_orange = "dataset_3row_orange.tab"
output_file = "dataset.csv"

# Command: run SQL + export both formats
cmd = f'''
psql -d {db_name} -U {db_user} -v ON_ERROR_STOP=1 -f "{sql_script}" \
-c "\\COPY (SELECT * FROM dataset_3row) TO '{output_file_orange}' WITH DELIMITER E'\\t' CSV HEADER;" \
-c "\\COPY (SELECT * FROM dataset) TO '{output_file}' WITH CSV HEADER;"
'''

print("Running SQL script and exporting both datasets...")
os.system(cmd)

print("Done! Files Created")