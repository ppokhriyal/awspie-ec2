#!/usr/bin/env python3

import os
import sys

import botocore
from ec2.aws_api import AwsBotoApi
from ec2.aws_tabula import CreateTable

#function: error message
def error_msg(msg :str)-> str:
    return f"\033[1;31;40m Error: {msg} \033[0m"

#function: messages
def messages(msg :str)-> str:
    return f"\033[1;36;40m Info: {msg} \033[0m"

#function: validate parent arguments
def validate_parent_args(argslist :list)-> bool:

    #dict: parent -> child arguments length
    parent_args_dict = {
        'list':[3],
        'stop':[4],
        'start':[4],
        'terminate':[4],
        '-help':[1]
    }

    if argslist[0] in parent_args_dict:
        if len(argslist) == parent_args_dict.get(argslist[0])[0]:
            if argslist[0] == 'list':
                if argslist[1] != '-region':
                    return False
                else:
                    return True
            elif argslist[0] in ['stop','start','terminate']:
                if argslist[2] != '-region':
                    return False
                else:
                    return True
        else:
            return False
    else:
        return False

#function: main
def main():
    #create the object of AwsBotoApi
    boto_api_obj = AwsBotoApi()

    #create the object of CreateTable
    create_table_obj = CreateTable()

    #check the length of arguments
    if len(sys.argv[1:]) == 0:
        print(error_msg("Invalid arguments.Try awspie-ec2 -help"))
        quit(1)

    #check the parent arguments
    args = sys.argv[1:]
    if validate_parent_args(args):
        # check for list parent args
        if args[0] == 'list':
            result = boto_api_obj.list_instances(args[2])
            if result == 'Empty Reservations':
                print(messages(result))
                quit(0)
            else:
                create_table_obj.list_table(result)
                quit(0)

        # check for stop parent args
        if args[0] == 'stop':
            result = boto_api_obj.stop_instance(args[1],args[3])
            if result['result'] == 'fail':
                print(error_msg(result['msg']))
                quit(1)
            else:
                print(messages('Status changed to stopping'))
                quit(0)

        # check for start parent args
        if args[0] == 'start':
            result = boto_api_obj.start_instance(args[1],args[3])
            if result['result'] == 'fail':
                print(error_msg(result['msg']))
                quit(1)
            else:
                print(messages('Status changed to starting'))
                quit(0)

        # check for terminate parent args
        if args[0] == 'terminate':
            result = boto_api_obj.terminate_instance(args[1],args[3])
            if result['result'] == 'fail':
                print(error_msg(result['msg']))
                quit(1)
            else:
                print(messages('Status changed to '+result['msg']['TerminatingInstances'][0]['CurrentState']['Name']))
                quit(0)
    else:
        print(error_msg("Invalid arguments.Try awspie-ec2 -help"))
        quit(1)


if __name__ == '__main__':
    main()