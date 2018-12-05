from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--csv', type=str, required=True, help='csv file for getting accuracy')
parser.add_argument('-o', '--output', default=None, help="save [option]")
parser.add_argument('-a', '--answer', help='answer file', required=True)
args = parser.parse_args()

def main():
    data = pd.read_csv(args.csv, names=['hash', 'pred_y'])
    answer = pd.read_csv(args.answer, names=['hash', 'y'])
    
    pred_y = data.pred_y
    y = answer.y

    #get and print accuracy
    accuracy = accuracy_score(y, pred_y)
    print("accuracy : %.0000f%%" % (np.round(accuracy, decimals=4)*100))

if __name__=='__main__':
    main()
