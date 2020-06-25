# watson
🏌️‍♀️ Sherlock assistant to bulk username research.

>This script is based on [Sherlock](https://github.com/sherlock-project/sherlock), originally created by [Siddharth Dushantha](https://github.com/sdushantha).

## Get started

**Note** : Python 3.6 or higher is required.

```bash
# install sherlock if not already done

# clone the repository in sherlock/sherlock directory
$ git clone https://github.com/boardens/watson.git

# change the working directory to watson
$ cd watson

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```

>The best way to use Watson is to clone it in the `sherlock/sherlock` directory.<br>
Anyway, you can change it path to reach `sherlock.py`.

```py
# sherlock directory
sh_dir = 'cd .. && '
```
```bash
· sherlock
├ data_bad_site.json
├ site_list.py
└ . sherlock
  ├ notify.py
  ├ result.py
  ├ sherlock.py
  ├ sites.py
  · watson
    └ watson.py
```

### Usage

```bash
$ python3 watson.py --help
usage: watson.py [-h] [-q] [--csv] [--json] FILE

Watson : Sherlock assistant to bulk username research

positional arguments:
  FILE         File containing usernames

optional arguments:
  -h, --help   show this help message and exit
  -q, --quiet  Quiet Sherlock output from terminal and keep only essential
               informations.
  --csv        Use Comma-Separated Values (CSV) File.
  --json       Use JavaScript Object Notation (JSON) File.

(Version 1.0.0)
```

Run presinstalled examples :

```bash
# basic text file
$ python3 watson.py examples/example.txt

# csv file
$ python3 watson.py --csv examples/example.csv

# json file
$ python3 watson.py --json examples/example.json
```

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
