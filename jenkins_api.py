import jenkins
import csv
import os

URL = 'http://54.175.188.135:8000'
USERNAME = os.getenv("USERNAME") #use 'export USERNAME=admin' to add env variable before running script
PASSWORD = os.getenv("PASSWORD")

server = jenkins.Jenkins(URL, username=USERNAME, password=PASSWORD)

user = server.get_whoami()
version = server.get_version()

#print(user['fullName'])
#print(version)
#print (f"Number of jobs: {server.jobs_count()}")
#print(server.get_nodes())

jobs = server.get_all_jobs()
job_list = []
for job in jobs:
    #print(job['name'], job['url'], job['color'])
    job_list.append(job['name'], job['url'], job['color'])

#print(job_list)

with open('jenkins_inv.csv', 'w', newline='') as j:
    pen = csv.writer(j)
    header = ["JOB_NAME", "JOB_URL", "JOB_STATUS"]
    pen.writerow(header)

    for row in job_list:
        pen.writerow(row)
