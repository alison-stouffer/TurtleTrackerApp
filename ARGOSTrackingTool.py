#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Alison Stouffer (alison.stouffer@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Create a variable pointing to the data file.
file_name = 'Data/Raw/sara.txt'

#Create a file object from the file.
file_object = open(file=file_name, mode='r')

#Read contents of file one line at a time.
lineString = file_object.readline()

#Extract one data line into a variable.
while lineString:

    #Check to see if the lineString is a data line.]
    if lineString[0] == "#" or lineString[0] == "u":
        lineString = file_object.readline()
        continue

    #Split the string into a list of data items.
    lineData = lineString.split()
    
    #Extract items in list into variables.
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print the location of sara.
    print(f"Record {record_id} indicates Sara was seen at {obs_lat}N, {obs_lon}W on {obs_date}")

    #Move to the next line in the file.
    lineString = file_object.readline()

#Close the file.
file_object.close()