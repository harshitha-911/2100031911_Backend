import sqlite3


conn = sqlite3.connect("sarftektest.db")
cur = conn.cursor()

# Create tables and insert data
cur.execute('''
CREATE TABLE locations (
    location_id INTEGER,
    street_address TEXT,
    postal_code TEXT,
    city TEXT,
    state_province TEXT,
    country_id TEXT
);
''')

cur.execute('''
CREATE TABLE countries (
    country_id TEXT,
    country_name TEXT,
    region_id INTEGER
);
''')

locations_data = [
    (1000, '1297 Via Cola di Rie', '989', 'Roma', 'IT'),
    (1297, '93091 Calle della Te', '10934', 'Venice','','IΤ'),
    (1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefectu','JP'),
    (1300, '9450 Kamiya-cho', '6623', 'Hiroshima', '','JP'),
    (1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas','US'),
    (1500, '2011 Interiors Blvd', '99236', 'South San', 'California','US'),
    (1600, '2007 Zagora St', '50090', 'South Brun', 'New Jersey','US'),
    (1700, '2004 Charade Ad', '98199', 'Seattle', 'Washington','US'),
    (1500, '147 Spadina Ave', 'MSV 267', 'Toronto', 'Ontario','CA')
]

countries_data = [
    ('AR', 'Argentina', 2),
    ('AU', 'Australia', 3),
    ('BE', 'Belgium', 1),
    ('BR','Brazil', 2),
    ('CA', 'Canada', 2),
    ('CH', 'Switzerland', 1),
    ('CN', 'China', 3),
    ('DE', 'Germany', 1)
]

cur.executemany('INSERT INTO locations VALUES (1000,1200,14000,1500,1600,1100)', locations_data)
cur.executemany('INSERT INTO countries VALUES (AR,AU,BE)', countries_data)

# Query using JOIN
cur.execute('''
SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
FROM locations l
JOIN countries c ON l.country_id = c.country_id
WHERE c.country_name = 'Canada'
''')

# Fetch and print results
rows = cur.fetchall()
print("Query using JOIN:")
for row in rows:
    print(row)

