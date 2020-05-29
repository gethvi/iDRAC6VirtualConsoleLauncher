#!/usr/bin/env python3


import argparse
import zipfile
import requests
import io
import pathlib
import sys
import urllib3
import subprocess


def get_libraries(url, path):
    response = requests.get(url)
    with zipfile.ZipFile(file=io.BytesIO(response.content)) as zip:
        for member in zip.infolist():
            if member.filename.endswith(DYNLIBEX):
                print('Extracting: ' + member.filename)
                zip.extract(member, path=path)


def main():
    parser = argparse.ArgumentParser(description='iDRAC 6 Virtual Console Launcher')
    parser.add_argument('-u', '--user', type=str, default='root', action='store', help='iDRAC username [root]')
    parser.add_argument('-p', '--passwd', type=str, default='calvin', action='store', help='iDRAC password [calvin]')
    parser.add_argument('host', metavar='HOST[:PORT]', action='store', help='host running iDRAC 6 [port:5900]')
    args = parser.parse_args()

    url = urllib3.util.parse_url(args.host)
    args.host = url.host
    if url.port:
        args.port = url.port
    else:
        args.port = 5900

    avctvm_url = 'http://{0}/software/avctVM{1}.jar'.format(args.host, PLATFORM)
    avctkvmio_url = 'http://{0}/software/avctKVMIO{1}.jar'.format(args.host, PLATFORM)
    avctkvm_url = 'http://{0}/software/avctKVM.jar'.format(args.host)

    pwd = pathlib.Path(sys.path[0])
    hostdir = pwd.joinpath(args.host)
    java = pwd.joinpath('jre').joinpath('bin').joinpath('java' + BINARYEX)

    libdir = hostdir.joinpath('lib')
    libdir.mkdir(parents=True, exist_ok=True)

    get_libraries(url=avctvm_url, path=libdir)
    get_libraries(url=avctkvmio_url, path=libdir)

    print('Downloading: avctKVM.jar')
    response = requests.get(avctkvm_url)
    with open('avctKVM.jar', 'w+b') as file:
        file.write(response.content)

    if java.exists():
        subprocess.run([
            str(java.absolute()),
            '-cp',
            'avctKVM.jar',
            '-Djava.library.path={}'.format(libdir),
            'com.avocent.idrac.kvm.Main',
            'ip={}'.format(args.host),
            'kmport={}'.format(args.port),
            'vport={}'.format(args.port),
            'user={}'.format(args.user),
            'passwd={}'.format(args.passwd),
            'apcp=1',
            'version=2',
            'vmprivilege=true',
            '"helpurl=https://{}/help/contents.html"'.format(args.host)
        ])


if __name__ == '__main__':
    if sys.platform.startswith('linux'):
        PLATFORM = 'Linux64'
        DYNLIBEX = '.so'
        BINARYEX = ''
    elif sys.platform.startswith('win'):
        PLATFORM = 'Win64'
        DYNLIBEX = '.dll'
        BINARYEX = '.exe'
    elif sys.platform.startswith('darwin'):
        PLATFORM = 'Mac64'
        DYNLIBEX = '.jnilib'
        BINARYEX = ''
    else:
        print('Unsupported platform.')
        sys.exit(0)

    main()
