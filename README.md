# Fixedwidthtocsv
Generate a fixed width based on offset length from spec file and convert to csv with delimiter as comma.



# Steps to run Fixedwidthtocsv

1. git clone the project
2. cd Fixedwidthtocsv\src\cdparser
3. RUN python Inputfile.py spec.json    #to generate a fixed width file
4. RUN python csvconverter.py spec.json
5. A Sample fixedwidth file input.txt will be generated based on the provided spec.
6. The Fixedwidth file will be converted to csv and saved as result.csv.


# Steps for testing
1. cd Fixedwidthtocsv\src
2. RUN python -m pytest tst/test_with_pytest.py
     



## Problem 1

### Parse fixed width file

- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding


## Choices

- Any language, any platform
- One of the above problems or both, if you feel like it.
