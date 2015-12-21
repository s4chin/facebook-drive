import argparse
import os
import shutil
import zipfile

def zip(iDir, oZip):
    shutil.make_archive(oZip, 'zip', iDir)

def unzip(iZip, oDir):
    with zipfile.ZipFile(iZip, "r") as z:
        z.extractall(oDir)

def parse():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-Z", "--zip", help="Zip the input folder", action="store_true")
    group.add_argument("-U", "--unzip", help="Unzip the input file", action="store_true")
    parser.add_argument("-I", "--input", required=True, help="Path to the input file")
    parser.add_argument("-O", "--output", required=True, help="Path to the output file")
    args = parser.parse_args()
    if args.zip:
        zip(iDir=args.input, oZip=args.output)
    else:
        unzip(iZip=args.input, oDir=args.output)

if __name__ == '__main__':
    parse()
