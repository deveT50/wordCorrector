#!/usr/bin/env python
# coding: utf-8

# Python 2 compatibility:
from __future__ import unicode_literals

host = '127.0.0.1'
port = 9199
name = 'CubReporter'

import sys
import json
import random

import jubatus
from jubatus.common import Datum

def _output(unicode_value):
    if hasattr(sys.stdout, 'buffer'):
        # for Python 3
        stdout = sys.stdout.buffer
    else:
        # for Python 2
        stdout = sys.stdout
    stdout.write(unicode_value.encode('utf-8'))

def train(client, fname):
    data=[]
    with open(fname, "r") as fd:
        data = fd.readlines()
    fd.close()

    # prepare training data
    train_data = []
    for i in range(10000):
        #add string("key", "value")
        print i
        s = data[i].decode("utf-8").strip("\r").strip("\n")
        train_data.append((s, Datum({"message": s})))

    # training data must be shuffled on online learning!
    random.shuffle(train_data)

    # run train
    client.train(train_data)

def predict(client):
    data = [
        Datum({'message': 'ほんま'}),
        Datum({'message': '今日'}),
        Datum({'message': 'は'}),
        Datum({'message': 'よく'}),
        Datum({'message': '晴れ'}),
        Datum({'message': 'たでー'}),
    ]
    for d in data:
        res = client.classify([d])
        correct_message = max(res[0], key = lambda x: x.score).label
        type_name    = d.string_values[0][1]
        _output('{0}: {1}\n'.format(correct_message, type_name))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: python {0} <fname>".format(sys.argv[0]))
        exit()
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    # run example
    train(client, sys.argv[1])
    predict(client)
