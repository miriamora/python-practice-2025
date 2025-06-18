import csv

with open('ec2.csv', 'w', newline='') as f:

    pen = csv.writer(f)
    pen.writerow(["INSTANCE_ID", "INSTANCE_TYPE", "AZ"])
    pen.writerow(["id-254513df56", "t2.xlarge", "us-east-1"])