import csv
import sys


def main():

    # Check for command-line usage

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    csvfile = sys.argv[1]
    textfile = sys.argv[2]
    datacsv = []
    subsequences = []
    datatxt = None

    # Read database file into a variable
    with open(csvfile, "r") as dbase:
        dbase_reader = csv.DictReader(dbase)

        # Read str filenames into a list of subsequences
        fieldnames = dbase_reader.fieldnames[1:]
        for x in fieldnames:
            subsequences.append(x)

        # Read rows into a dict list in the code
        for row in dbase_reader:
            datacsv.append(row)

    # Read DNA sequence file into a variable
    with open(textfile, "r") as sequence:
        sequence_reader = sequence.read()
        datatxt = sequence_reader

    # Find longest match of each STR in DNA sequence
    str_s = []
    # Use the function for each str in subsequences
    for str in subsequences:
        found = longest_match(datatxt, str)
        str_s.append(found)

    # Check database for matching profiles
    y = 0
    x = 0
    found = False

    # Check each column from each role to check if the numbers are equal
    # If they are equal print the value of the name in the row and change found status to true
    for row in datacsv:

        for column in range(len(subsequences)):
            col = subsequences[x]
            if int(datacsv[y][col]) == int(str_s[x]):
                x = x + 1
                if x == len(subsequences):
                    found = True
                    print(datacsv[y]['name'])
        x = 0
        y = y + 1

    if found != True:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
