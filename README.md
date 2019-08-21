# watson
🏌️‍♀️ Sherlock assistant to bulk username research

>This script is based on [Sherlock](https://github.com/sherlock-project/sherlock) originally created by [Siddharth Dushantha](https://github.com/sdushantha)

## Get started

**Note** : Python 3.6 or higher is required.

>Make sure that you have installed [Sherlock](https://github.com/sherlock-project/sherlock) before starting installation !

```bash
# clone the repository in sherlock's directory
$ git clone https://github.com/boardens/watson.git

# change the working directory to watson
$ cd watson

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```

>The best way to use Watson is to clone it in the Sherlock's directory.<br>
Anyway, you can change it path to reach Sherlock.

```py
# Sherlock directory
sh_dir = 'cd .. && '
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
