#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: test_rpc_client.py
Author: tdoly
Description: test rpc client
'''

import zerorpc

def test():
    c = zerorpc.Client()
    c.connect("tcp://0.0.0.0:4242")
    dbs = c.getDB()
    print dbs
    for db in dbs:
        print c.getDatas(db)


if __name__ == '__main__':
    test()
