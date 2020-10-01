from os import listdir
import csv
import sys
path = ""

if len(sys.argv) > 1:
    path = sys.argv[1]
    print(sys.argv[1])
    

line_to_find = ("Passed all tests with no errors.")
pass_score = 100
fail_score = 0
csv_header = ["Username", "Grade"]
out_data = {}
class_data = {}

ls = listdir(path)
for file in ls:
    parts = file.split('.')
    if parts[1] == "log":
        with open("{}\\{}".format(path,file)) as f:
            key = parts[0]
            if line_to_find in f.read():
                #print(file, "- true")
                out_data[key] = pass_score               
            else:
                print(file, "- false")
                #out_data[key] = fail_score


reader = csv.reader(open('ClassList.csv'))
out = open('grade.csv', 'w', newline='')
with out:
    writer = csv.writer(out, delimiter=',')
    writer.writerow(csv_header)
    for row in reader:
        key = row[0]
        class_data[key] = row[1]
        if key in out_data:
            class_data[key] = ["#{}".format(class_data[key]), out_data[key]]
            print(class_data[key])
            writer.writerow(class_data[key])
        else:
            print("Couldn't file ", key)


