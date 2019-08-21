# watson
Sherlock assistant to bulk username research

>Info !

## Get started

**Note** : Python 3.6 or higher is required.

>Make sure that you have installed [sherlock](https://github.com/sherlock-project/sherlock) before starting installation !

```bash
# clone the repository in sherlock's folder
$ git clone https://github.com/boardens/watson.git

# change the working directory to watson
$ cd watson

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```

### Usage

```bash
$ python3 watson.py --help
usage: watson.py [-h] [-q] [--csv] FILE

Watson : Sherlock assistant to bulk username research

positional arguments:
  FILE         File containing usernames

optional arguments:
  -h, --help   show this help message and exit
  -q, --quiet  Quiet Sherlock output from terminal and keep only essential
               informations.
  --csv        Use Comma-Separated Values (CSV) File.

(Version 1.0.0)
```

Run presinstalled examples :

```bash
# basic text file
watson.py examples/example.txt

# csv text file
watson.py --csv examples/example.csv
```
