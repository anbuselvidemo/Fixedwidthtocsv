import io
import re
import argparse
import json
import csv
import logging
import unittest
import random
import string

def parse_spec(spec):
    column_names = []
    offsets = []
    include_header = False
    input_encoding = None
    output_encoding = None

    try:
        with open(spec) as spec_file:
            specdict = json.load(spec_file)
            column_names = specdict['ColumnNames']
            offsets=specdict['Offsets']
            offsets = list(map(int, offsets))
            input_encoding = specdict['FixedWidthEncoding']
            output_encoding = specdict['DelimitedEncoding']

        return (
            offsets,
            input_encoding,
            output_encoding,
        )

    except Exception as err:
        logging.error('Cannot parse the spec')
        logging.error(err)

#CReate a Random file as fixedwidth based on spec.
def generate_file(spec, data):
     offsets, input_encoding, output_encoding = parse_spec(spec)
     stringlen = sum(offsets)
     f = open('input.txt', 'w')
     lines = 10
     for _ in range(lines):
        randstr = "".join(random.choices(string.ascii_letters + string.digits, k=stringlen ))
        f.write(randstr+'\n')

     f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate flat file')
    parser.add_argument('spec', metavar='F', type=str, help='spec')
    args = parser.parse_args()
    spec = args.spec
    data = parse_spec(spec)
    generate_file(spec, data)
