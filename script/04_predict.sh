#!/bin/sh
PATH='../sam'

for file in $PATH/*
do
  filename=${file}
  python  ../04_checkpe.py ${filename} > result.txt
done

