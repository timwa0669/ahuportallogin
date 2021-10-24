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

### Login examples

Username is A12345678@cmccyx, password is xyz  

    ahuportallogin -u="A12345678@cmccyx" -p="xyz"

Username is B12345678, password is xyz  

    ahuportallogin --user="B12345678" --password="xyz"

### Logout examples

    ahuportallogin --logout

### Print version

    ahuportallogin -v

or  

    ahuportallogin --version

### Print help messages

    ahuportallogin -h

or  

    ahuportallogin --help

## Build

### Requisites

python >= 3.7  
All running dependencies from requirements.txt  
pyinstaller >= 4

### One-file build scripts

    pyinstaller -F -n="ahuportallogin" main.py