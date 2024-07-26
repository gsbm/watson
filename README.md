# watson
🏌️‍♀️ Sherlock assistant to bulk username research.

>This script is based on [Sherlock](https://github.com/sherlock-project/sherlock), originally created by [Siddharth Dushantha](https://github.com/sdushantha).

## Get started

### Installation

**Note** : Python 3.6 or higher is required.

```bash
# Install sherlock if not already done

# Clone the repository in sherlock/sherlock directory
$ git clone https://github.com/gsbm/watson.git

# Change the working directory to watson
$ cd watson

# Install python and python-pip if they are not installed

# Install the requirements
$ python -m pip install -r requirements.txt
```

>The best way to use Watson is to clone it in the `sherlock/sherlock` directory.<br>
Anyway, you can change it path to reach it in `config.json`

```json
"sherlock_dir": "..\\sherlock.py"
```
```bash
sherlock
├── data_bad_site.json
├── site_list.py
└── sherlock
    ├── notify.py
    ├── result.py
    ├── sherlock.py
    ├── sites.py
    └── watson
        └── watson.py
```

### Usage

```bash
$ python3 watson.py --help
usage: watson.py [-h] [-q] [--csv] [--json] FILE

Watson: Sherlock assistant to bulk username research

positional arguments:
  FILE         File containing usernames

optional arguments:
  -h, --help   show this help message and exit
  -q, --quiet  Quiet Sherlock output from terminal and keep only essential
               informations.
  --csv        Use Comma-Separated Values (CSV) File.
  --json       Use JavaScript Object Notation (JSON) File.

(Version 1.0.2)
```

Run presinstalled examples :

```bash
# Basic text file
$ python3 watson.py examples/example.txt

# CSV file
$ python3 watson.py --csv examples/example.csv

# JSON file
$ python3 watson.py --json examples/example.json
```

## Implementations

Currently working on other implementations like :
- Simultaneous sherlock requests, especially for massive username research
- Sherlock requests over tor, including circuit renew between requests

## License

[GPL-3.0](https://github.com/greenmagenta/watson/LICENSE/) License
