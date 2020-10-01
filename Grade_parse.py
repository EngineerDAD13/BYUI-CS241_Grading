import csv

assign_data = {}
class_data = {}
"""
Function that opens the grade file from the Linux lab
"""
def open_grades():
    file_no_good = True
    tries = 0
    while file_no_good:
        try: 
            # try to open the file name provided by the user
            grade_file = input("Please Enter Grade CSV filename: ")
            reader = csv.reader(open(grade_file))
            for row in reader:
                #copy the data from the csv file to the global assign_data array
                key = row[0]
                assign_data[key] = row[1]
            file_no_good = False
            ret_val = True
        except IOError: 
            # You get 3 trys to provide a valid file name
            print ("Invalid Filename")
            tries +=1
            if tries > 3:
                # quit after 3 tries
                print ("Restart to try again")
                file_no_good = False
                ret_val = False
    return ret_val

"""
Function to populate the class_data using the Class data and the assign_data
Once populated the class_data is written to the outpu.csv file
"""
def parse_files():

    # Open the header file
    reader = csv.reader(open('Class_Header.csv'))
    row = next(reader)
    index = 0
    for cell in row:
        # assign an index to the assignment names
        print(index, ": ", cell)
        index += 1
    # request the assignment index and populate the output CSV header
    assignment = int(input("Please Enter Assignment Header Index: "))
    csv_header = ["Student", "ID", "SIS User ID", "SIS Login ID", "Root Account", "Section", row[assignment]]

    # Open the class list
    reader = csv.reader(open('Class.csv'))
    out = open('output.csv', 'w', newline='')

    with out:
        # write the header row to the output CSV
        writer = csv.writer(out, delimiter=',')
        writer.writerow(csv_header)

        
        for row in reader:
            # the key is the student username
            key = row[3]
            # the class_data array uses the key as its hash index and copies the 
            #   gradebook information for the current username into the row
            class_data[key] = row[0:]
            new_key = ("#{}".format(key))
            if new_key in assign_data:
                # Now we connect the username between the gradebook and the Linux grades
                class_data[key].append(assign_data[new_key])
                writer.writerow(class_data[key])


# Open the Linux grade file
success = open_grades()
if success:
    # If the Linux grade file was read successfully then parse it
    parse_files()
    
