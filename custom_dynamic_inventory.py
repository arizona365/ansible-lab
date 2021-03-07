#!/bin/python
import sys
import json

try:
   import boto3
except ImportError:
   print("Please install boto3 using pip install boto3 and try again")
   sys.exit(1)
except Exception as e:
   print(e)
   sys.exit(2)

def get_hosts(all_ec2s,f_value):
   custom_filter={"Name":"tag:Environment", "Values":[f_value]}
   hosts=[]
   for instance in all_ec2s.instances.filter(Filters=[custom_filter]):
    hosts.append(instance.private_ip_address)
   return hosts

# main function which will poll all ec2 resources from us-east-1
def main():
   all_ec2s=boto3.resource("ec2","us-east-1")
   db_group=get_hosts(all_ec2s,"db")
   web_group=get_hosts(all_ec2s,"web")
   all_groups= { 'db': db_group,
                  'web': web_group
               }
   print(json.dumps(all_groups))

if __name__=="__main__":
   main()