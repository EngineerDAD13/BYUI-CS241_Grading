import csv

assign_data = {}
class_data = {}

def open_grades():
    file_no_good = True
    tries = 0
    while file_no_good:
        try:
            grade_file = input("Please Enter Grade CSV filename: ")
            reader = csv.reader(open(grade_file))
            for row in reader:
                key = row[0]
                assign_data[key] = row[1]
            #print(assign_data['#tphollis'])
            file_no_good = False
            ret_val = True
        except IOError:
            print ("Invalid Filename")
            tries +=1
            if tries > 3:
                print ("Restart to try again")
                file_no_good = False
                ret_val = False
    return ret_val
            
def parse_files():

    reader = csv.reader(open('Class_Header.csv'))
    row = next(reader)
    index = 0
    for cell in row:
        print(index, ": ", cell)
        index += 1
    assignment = int(input("Please Enter Assignment Header Index: "))
    csv_header = ["Student", "ID", "SIS User ID", "SIS Login ID", "Root Account", "Section", row[assignment]]

    #print(assign_data['#tphollis'])

    reader = csv.reader(open('Class.csv'))
    out = open('output.csv', 'w', newline='')

    with out:
        writer = csv.writer(out, delimiter=',')
        writer.writerow(csv_header)

        
        for row in reader:
            key = row[3]
            class_data[key] = row[0:]
            new_key = ("#{}".format(key))
            if new_key in assign_data:
                class_data[key].append(assign_data[new_key])
                #print(class_data[key])
                writer.writerow(class_data[key])



success = open_grades()
if success:
    parse_files()
    