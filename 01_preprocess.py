import pandas as pd
import argparse
import os
import tqdm

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
if not os.path.exists(legitmatepath):
    os.mkdir(legitmatepath)
if not os.path.exists(malicouspath):
    os.mkdir(malicouspath)

def main():
    data = pd.read_csv(args.csv, names=['hash', 'y'])

    for _name in tqdm.tqdm(os.listdir(args.datadir)):
        path = os.path.join(args.datadir, _name)
        y = data[data.hash==_name].values[0][1]

        if y is 1:
            dstpath = os.path.join(malicouspath, _name)
        else:
            dstpath = os.path.join(legitmatepath, _name)

        os.rename(path, dstpath)

if __name__=='__main__':
    main()
    print('Done')
