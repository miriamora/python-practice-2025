import boto3

ec2_client = boto3.client('ec2', region_name= "us-east-2")

def listEc2():

    r = ec2_client.describe_instances()
    ec2_list = []

    for item in r['Reservations']:
        for i in item['Instances']:
            ec2_list.append(i['InstanceId'])

    return ec2_list

def stopInstances(instancelist):
    ec2_client.stop_instances(InstanceIds = instancelist)

l = listEc2()
#stopInstances(l)

def startInstances(instancelist):
    ec2_client.start_instances(InstanceIds = instancelist)

startInstances(l)


