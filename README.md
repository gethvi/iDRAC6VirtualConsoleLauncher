# iDRAC 6 Virtual Console Launcher
Python 3 launcher for iDRAC 6 Virtual Console (including Virtual Media).

Tested on Debian Buster, Windows 10 and MacOS Catalina.

## Installation
To run the Virtual Console, you need to download old Java Runtime Environment 7u80 from Oracle:

https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html

Below are direct links that only work when you log in and accept Oracle license agreement.

**Windows:**
[jre-7u80-windows-x64.tar.gz](https://download.oracle.com/otn/java/jdk/7u80-b15/jre-7u80-windows-x64.tar.gz)

**Linux:**
[jre-7u80-linux-x64.tar.gz](https://download.oracle.com/otn/java/jdk/7u80-b15/jre-7u80-linux-x64.tar.gz)

**MacOS:**
[jre-7u80-macosx-x64.tar.gz](https://download.oracle.com/otn/java/jdk/7u80-b15/jre-7u80-macosx-x64.tar.gz)


Extract the files and place them where the script expects it:

```
iDRAC6VirtualConsoleLauncher
├── iDRAC6VirtualConsoleLauncher.py
├── jre
│   ├── bin
│   │   └── java.exe
│   └── ...
|
├── requirements.txt
└── README.md
```

Install dependencies:

`pip3 install -r requirements.txt`

or use (Linux) distribution packages:

`apt install python3-requests`

## Usage
```
usage: iDRAC6VirtualConsoleLauncher.py [-h] [-u USER] [-p PASSWD] HOST[:PORT]

iDRAC 6 Virtual Console Launcher

positional arguments:
  HOST[:PORT]           host running iDRAC 6 [port:5900]

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  iDRAC username [root]
  -p PASSWD, --passwd PASSWD
                        iDRAC password [calvin]
```