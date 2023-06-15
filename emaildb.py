import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the table if it already exists and create a new table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# Prompt the user to enter a file name, defaulting to 'mbox-short.txt' if no input is provided
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

# Open the file
fh = open(fname)

# Iterate through each line in the file
for line in fh:
    if not line.startswith('From: '):
        continue

    # Extract the email address from the line
    pieces = line.split()
    email = pieces[1]

    # Check if the email already exists in the database
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()

    if row is None:
        # If the email does not exist, insert it into the database with a count of 1
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        # If the email exists, update its count by incrementing it by 1
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    # Commit the changes to the database
    conn.commit()

# Retrieve the top 10 email addresses with the highest counts
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# Execute the SQL query and print the results
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and the database connection
cur.close()
conn.close()
