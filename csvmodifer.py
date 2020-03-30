############################################
##      CSE 174 - Decision Analysis       ##
############################################
## Python script to clean and modify a    ##
## .csv file to import into pgAdmin4 so   ##
## that it can be used to perform data    ##
## anlysis for our final project          ##
############################################
## csvmodifier.py                         ##
############################################

# Import csv library
import csv

# File to be read
readFile = 'dirtyMetro.csv'

# File to write to
writeFile = 'cleanMetro.csv'

# Declare array of new fields to use
fields = ['itemNum', 'route', 'trip', 'bus', 'rdr_c', 'Key_UC_STDNT', 'Key_UC_STAFF', 'UC_Riders', 'non_UC_Riders', 'Date_And_Time', 'Trip_Date', 'Trip_Timestamp', 'Weekday', 'Trip_Month', 'Trip_Time', 'Holiday', 'Holiday_Factor', 'Strike', 'Quarter_Year', 'Week', 'Finals', 'Enrollment', 'Quarter', 'School_Year', 'Campus_Route', 'Artic']

# Declare disposable array for old fields to be removed
rem = []

# Declare rows[] to store data from csv file
rows = []

# Specify which columns within the csv files are integer data type so it can be cleaned accordingly for ease of import into pgAdmin4
intArray = [0, 1, 3, 4, 5, 6, 7, 8, 14, 19, 21, 23]
boolArray = [17, 20, 24, 25]

# Reading metro.csv
with open(readFile, 'r') as csvfile:

    # Creating new csv reader object
    csvreader = csv.reader(csvfile)

    # Get old fields and store to disposal array
    rem = csvreader.__next__()

    # Extract data row by row from csv file
    for row in csvreader:

        # Clean up data to make it easier to handle

        ## Formatting [NULL] data type #########################################
        for x in range(0, 26):

            if row[x] == '':

                row[x] = ' '

            elif row[x] == 'NA':

                row[x] = ' '

            else:
                pass

        ## Formatting [timestamp] data type ####################################
        if row[9] == ' ':                                                           ## "date_and_time" column

            row[9] = '1111-11-11 11:11:11'

        if row[11] == ' ':                                                          ## "trip_timestamp" column

            row[11] = '1111-11-11 11:11:11'

        ## Formatting [Boolean] data type ######################################
        if row[17] == 'FALSE':                                                      ## "strike" column

            row[17] = 0

        elif row[17] == 'TRUE':                                                     ## "strike" column

            row[17] = 1

        ####

        if row[20] == 'FALSE':                                                      ## "finals" column

            row[20] = 0

        elif row[20] == 'TRUE':                                                     ## "finals" column

            row[20] = 1

        ####

        if row[24] == 'FALSE':                                                      ## "campus_route" column

            row[24] = 0

        elif row[24] == 'TRUE':                                                     ## "campus_route" column

            row[24] = 1

        ####

        if row[25] == 'FALSE':                                                      ## "artic" column

            row[25] = 0

        elif row[25] == 'TRUE':                                                     ## "artic" column

            row[25] = 1

        ## Formatting [integer] data type ######################################
        for i in intArray:                                                               ## Where 'int' is an array containing the integer type columns in pgAdmin4

            if row[i] == ' ':                                                       ## Since we can't allow for basic NULL data types, we are searching for NULL space

                row[i] = -1                                                         ## For each occurance of NULL space, insert value {-1} to indicate NULL

        ## if No Neccessary Changes to Data ####################################
        else:
            pass

        # Append the data to row[]
        rows.append(row)

    # Check to make sure all rows from csv file are copied
    print("Total number of rows: %d" %(csvreader.line_num))

    # Check to make sure old fields are captured
    print(rem)

# Write to newMetro.csv
with open(writeFile, 'w') as csvfile:

    # Create new csv writer object
    csvwriter = csv.writer(csvfile)

    # Write updated fields row to new csv file
    csvwriter.writerow(fields)

    # Write all data from metro.csv to newMetro.csv
    csvwriter.writerows(rows)

    # Check to make sure that the fields for newMetro.csv have been updated
    print(fields)

    print("Total number of rows: %d" %(csvreader.line_num))
