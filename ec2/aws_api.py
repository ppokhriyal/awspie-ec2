#!/usr/bin/env python3

import boto3
import botocore
import datetime
from dateutil.tz import tzutc

class AwsBotoApi:

    # get list of instances
    def list_instances(self,region :str):
        client = boto3.client('ec2',region_name=region)
        response = client.describe_instances()
        if len(response['Reservations']) == 0:
            return f"Empty Reservations"
        else:
            #dict : create ec2
            list_ec2_dict = {}
            list_ec2_list = []
            list1 = response['Reservations']
            for i in list1:
                #add instance-id
                list_ec2_dict['Instance-Id'] = i['Instances'][0]['InstanceId']
                
                #check for tag
                if 'Tags' in i['Instances'][0]:
                    list_ec2_dict['Tag'] = i['Instances'][0]['Tags'][0]['Value']
                else:
                    list_ec2_dict['Tag'] = '(Unknown)'
                
                #check for private ip address
                if len(i['Instances'][0]['PrivateIpAddress']) == 0:
                    list_ec2_dict['Private-IP'] = '(Unknown)'
                else:
                    list_ec2_dict['Private-IP'] = i['Instances'][0]['PrivateIpAddress']
                
                #check for public ip address
                if len(i['Instances'][0]['PublicIpAddress']) == 0:
                    list_ec2_dict['Public-IP'] = '(Unknown)'
                else:
                    list_ec2_dict['Public-IP'] = i['Instances'][0]['PublicIpAddress']

                #status of ec2
                list_ec2_dict['Status'] = i['Instances'][0]['State']['Name']

                list_ec2_list.append(list_ec2_dict)
                list_ec2_dict = {}

            return list_ec2_list

    # stop ec2 instance
    def stop_instance(self,instanceid :str):
        client = boto3.client('ec2')
        response = client.stop_instances(InstanceIds=[instanceid])
        return response