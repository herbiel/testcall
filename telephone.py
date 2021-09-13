#!/usr/bin/env python

'''
single_command.py - execute a single command over ESL
'''
import sys
import configparser
import ESL

config = configparser.ConfigParser()
config.read('config.ini')
server = config['DEFAULT']['server']
port = config['DEFAULT']['port']
auth = config['DEFAULT']['auth']


def cmd(number):
    con = ESL.ESLconnection(server, port, auth)

    if not con.connected():
        print
        'Not Connected'
        sys.exit(2)

    # Run command
    call_str = 'originate user/%s &echo()'%number
    e = con.api(call_str)
    if e:
        print(e.getBody())
    return e.getBody()

