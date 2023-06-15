import sqlite3
import re

# Connect to the SQLite database
conn = sqlite3.connect('co.sqlite')
cur = conn.cursor()

# Drop the table if it already exists and create a new table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Specify the file name to read from
fname = 'mbox.txt'

# Open the file
fh = open(fname)

# Iterate through each line in the file
for line in fh:
    if not line.startswith('From: '):
        continue

    # Extract the organization domain from the email address
    org = re.findall('@\S+', line)
    org = str(org)
    org = org[3:-2]

    # Check if the organization already exists in the database
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()

    if row is None:
        # If the organization does not exist, insert it into the database with a count of 1
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        # If the organization exists, update its count by incrementing it by 1
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

    # Commit the changes to the database
    conn.commit()

# Retrieve the top 10 organizations with the highest counts
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# Execute the SQL query and print the results
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and the database connection
cur.close()
conn.close()
