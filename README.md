fork URL: https://github.com/CircleZ3791117/PEMalDetection.git

Overview
============
This project helps train a classifier to be able to detect [PE files](https://en.wikipedia.org/wiki/Portable_Executable) as either malicious or legitimate. It tries out 6 different classification algorithms before deciding which one to use for prediction by comparing their results.

Dependencies
============
```
$ source [virtualenv]
$ pip install -r requirements.txt
```

Basic Usage
===========
script/01_preprocess.sh -> script/02_generatedata.sh -> script/03_learning.sh -> script/04_predict.sh