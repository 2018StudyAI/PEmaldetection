import pandas as pd
import argparse
import os

legitmatepath = 'legitimate'
malicouspath = 'malicious'

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--csv', help='trainset csv file', required=True)
parser.add_argument('-d', '--datadir', help='trainset path', required=True)
args = parser.parse_args()

if not os.path.exists(args.csv):
    parser.error('{} does not exist'.format(args.csv))
if not os.path.exists(args.datadir):
    parser.error('{} does not exist'.format(args.datadir))
if not os.path.exists(args.output):
    os.mkdir(args.output)

def main():
    data = pd.read_csv(args.csv, names=['hash', 'y'])

    for index, row in data.iterrows():
        name = row['hash']
        y = row['y']
        srcpath = os.path.join(args.datadir, name)
        dstpath = ''

        if y == 0:
            dstpath = os.path.join('../', legitmatepath, name)
        else:
            dstpath = os.path.join('../', malicouspath, name)
        os.rename(srcpath, dstpath)

if __name__=='__main__':
    main()
    print('Done')