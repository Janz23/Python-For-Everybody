'''
This code prompts the user to enter the name of a file.
It then opens the specified file and reads its contents line by line.
For each line, it checks if the line starts with "X-DSPAM-Confidence:".
If it does, it extracts the numerical value after the ':' character,
converts it to a float, and adds it to the sum of all spam confidence values.
It also keeps track of the count of spam confidence lines encountered.
After iterating through all the lines in the file,
it calculates the average spam confidence by dividing the sum by the count.
Finally, it displays the average spam confidence to the user.
'''

# Prompt the user to enter a file name
fname = input("Enter file name: ")

# Open the file
fh = open(fname)

# Initialize variables
all = 0
count = 0

# Iterate through each line in the file
for line in fh:
    # Check if the line does not start with "X-DSPAM-Confidence:", then skip to the next line
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # Find the index of the ':' character in the line
    num = line.find(':')

    # Extract the numerical value after the ':' character
    nume = line[num+1:]

    # Convert the extracted value to a floating-point number
    numer = float(nume)

    # Increment the count of spam confidence lines
    count = count + 1

    # Sum up all the spam confidence values
    all = all + numer

# Calculate the average spam confidence by dividing the sum by the count
ave = all/count

# Print the average spam confidence
print("Average spam confidence:", ave)
