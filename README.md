# ahuportallogin

Anhui University campus network login and logout script  

## Features

Supports login and logout via ethernet or ahu.portal.  

## Usage
    ahuportallogin [-h] [-v] [-u [USER]] [-p [PASSWORD]] [--logout]

    optional arguments:  
      -h, --help            show this help message and exit  
      -v, --version         show program's version number and exit  
      -u [USER], --user [USER]  
                            login username  
      -p [PASSWORD], --password [PASSWORD]  
                            login password  
      --logout              logout of the campus network  

## Requisites

python >= 3.7  
Check the requirements for the python packages from requirements.txt  

## Examples

### Login

Username is A12345678@cmccyx, password is xyz  

    python3 main.py -u="A12345678@cmccyx" -p="xyz"

Username is B12345678, password is xyz  

    python3 main.py --user="B12345678" --password="xyz"

### Logout

    python3 main.py --logout

### Get version

    python3 main.py -v

or  

    python3 main.py --version

### Print help message

    python3 main.py -h

or  

    python3 main.py --help
