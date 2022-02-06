# Small example from this website

https://pytorch.org/tutorials/beginner/text_sentiment_ngrams_tutorial.html

# FAQ

## First Error
Collecting torchtext
  Downloading torchtext-0.11.2-cp36-cp36m-manylinux1_x86_64.whl (8.0 MB)
     |████████████████████████████████| 8.0 MB 31.7 MB/s eta 0:00:01
Collecting torch==1.10.2
  Using cached torch-1.10.2-cp36-cp36m-manylinux1_x86_64.whl (881.9 MB)
Requirement already satisfied: numpy in /home/lucasnn/miniconda3/envs/py36/lib/python3.6/site-packages (from torchtext) (1.19.5)
Collecting tqdm
  Using cached tqdm-4.62.3-py2.py3-none-any.whl (76 kB)
Requirement already satisfied: requests in /home/lucasnn/miniconda3/envs/py36/lib/python3.6/site-packages (from torchtext) (2.27.1)
Requirement already satisfied: dataclasses in /home/lucasnn/miniconda3/envs/py36/lib/python3.6/site-packages (from torch==1.10.2->torchtext) (0.8)
Requirement already satisfied: typing-extensions in /home/lucasnn/miniconda3/envs/py36/lib/python3.6/site-packages (from torch==1.10.2->torchtext) (3.10.0.2)
Requirement already satisfied: charset-normalizer~=2.0.0 in /home/lucasnn/miniconda3/envs/py36/lib/python3.6/site-packages (from requests->torchtext) (2.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /home/lucasnn/miniconda3/envs/py36/lib/python3.6/site-packages (from requests->torchtext) (2020.6.20)
Requirement already satisfied: idna<4,>=2.5 in /home/lucasnn/miniconda3/envs/py36/lib/python3.6/site-packages (from requests->torchtext) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/lucasnn/miniconda3/envs/py36/lib/python3.6/site-packages (from requests->torchtext) (1.26.8)
Installing collected packages: tqdm, torch, torchtext
  Attempting uninstall: torch
    Found existing installation: torch 1.10.1
    Uninstalling torch-1.10.1:
      Successfully uninstalled torch-1.10.1
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
torchvision 0.11.2 requires torch==1.10.1, but you have torch 1.10.2 which is incompatible.
Successfully installed torch-1.10.2 torchtext-0.11.2 tqdm-4.62.3
Note: you may need to restart the kernel to use updated packages.


