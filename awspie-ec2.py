#!/usr/bin/env python3

# A Boto3 enabled wrapper script for monitoring and managing ec2 instances
# 
# Author: Prashant Pokhriyal
#

import argparse

if __name__ == '__main__':
    
    # Define command line arguments
    
    parser = argparse.ArgumentParser(description='Monitoring and Managing Ec2 instances')
    parser.add_argument('--list',help='List all the available ec2 instances')
    parser.add_argument('--stop',nargs='+',help='Stop running ec2 instance by passing instance-ids')
    args=parser.parse_args()

    print(args._get_kwargs())
