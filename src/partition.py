import argparse, os
kB = 1024
mB = 1024 * kB
chunkSize = 1 * mB
readSize = 1 * kB

def split(iFile, oDir, chunkSize=chunkSize):
    if not os.path.exists(oDir):
        os.mkdir(oDir)
    else:
        for fname in os.listdir(oDir):
            os.remove(os.path.join(oDir, fname))
    input = open(iFile, 'rb')
    pnum = 0
    while True:
        chunk = input.read(chunkSize)
        if not chunk:
            break
        pnum = pnum + 1
        filename = os.path.join(oDir, 'part{:05d}'.format(pnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()
    input.close()

def join(iDir, oFile):
    output = open(oFile, 'wb')
    parts = os.listdir(iDir)
    parts.sort()
    for fname in parts:
        filepath = os.path.join(iDir, fname)
        fileobj = open(filepath, 'rb')
        while True:
            filebytes = fileobj.read(readSize)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()

def parse():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-S", "--split", help="Split input file into chunks", action="store_true")
    group.add_argument("-J", "--join", help="Join input folder to a single file", action="store_true")
    parser.add_argument("-I", "--input", required=True, help="Path to the input file")
    parser.add_argument("-O", "--output", required=True, help="Path to the output file")
    args = parser.parse_args()
    if args.split:
        split(args.input, args.output)
    else:
        join(args.input, args.output)

if __name__ == '__main__':
    parse()
