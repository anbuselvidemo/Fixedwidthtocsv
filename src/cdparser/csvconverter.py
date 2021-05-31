# parser.py
#!/usr/bin/python3
"""
## Judgment Criteria
- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Parse fixed width file
- Generate a fixed width file using the provided spec.
- Implement a parser that can parse the fixed width file and generate a csv file.
- DO NOT use pre built python libraries like pandas for parsing. You can use a library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

## Sample spec file (json file)
{
    "ColumnNames":"f1, f2, f3, f4, f5, f6, f7, f8, f9, f10",
    "Offsets":"3,12,3,2,13,1,10,13,3,13",
    "InputEncoding":"windows-1252",
    "IncludeHeader":"True",
    "OutputEncoding":"utf-8"
}
"""

import re
import argparse
import json
import csv
import logging


#split line  based on spec
def split_line_by_fixed_widths(textline = '', offsets = []):
    line = textline
    delimiter = ','

    for idx, n in enumerate(offsets):

        if idx == len(offsets) - 1:
            continue

        line = re.sub(r"^(.{%d})()" % (n + idx), r"\1%s" % delimiter, line)
        logging.debug(line)
    line = [n.strip() if len(n.strip()) > 0 else '_' for n in line.split(delimiter)]

    return line


#input file parser and converter to csv
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
            include_header = specdict['IncludeHeader']
            output_encoding = specdict['DelimitedEncoding']
            return (
                column_names,
                offsets,
                include_header,
                input_encoding,
                output_encoding,
            )

    except Exception as err:
        logging.error('Cannot parse the spec')
        logging.error(err)


def run(spec):
    column_names, offsets, include_header, input_encoding, output_encoding = parse_spec(spec)
    # We calculate the offsets to the line-beginning
    reduced_offsets = []
    for idx, width in enumerate(offsets):
        distance = width if idx == 0 else width + reduced_offsets[idx - 1]
        reduced_offsets.append(distance)

    try:
        with open('result.csv', 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')

            with open('input.txt', 'r') as f:

                if include_header:
                    writer.writerow(column_names)

                for line_index, line in enumerate(f.readlines()):

                    if line_index == 1 or len(line) == 0:
                        continue

                    splitted_line = split_line_by_fixed_widths(line, reduced_offsets)
                    writer.writerow(splitted_line)

                f.close()
            csv_file.close()
    except Exception as err:
        logging.error('File IO error')
        logging.error(err)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text to csv')
    parser.add_argument('spec', metavar='F', type=str, help='spec')
    args = parser.parse_args()
    spec = args.spec
    run(spec)



