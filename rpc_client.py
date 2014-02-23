#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: rpc_client.py
Author: tdoly
Description: rpc client, get data from database
'''

import zerorpc

c = zerorpc.Client()
c.connect("tcp://0.0.0.0:4242")

def dbs():
    '''get dataname'''
    return c.getDB()

def datas(sheet):
    '''get datas'''
    return c.getDatas(sheet)
