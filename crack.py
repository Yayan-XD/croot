#!/usr/bin/python2
# coding=utf-8

try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, bababindsix
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bababindsix')
    os.system('bash install.sh')
    time.sleep(1)
    os.system('python2 croot.py')

reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


logo = '''
 \x1b[1;90m ██████╗██████╗  ██████╗  ██████╗ ████████╗ 
 \x1b[1;90m██╔════╝██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝
 \x1b[1;90m██║     ██████╔╝██║   ██║██║   ██║   ██║   
 \x1b[1;94m██║     ██╔══██╗██║   ██║██║   ██║   ██║   
 \x1b[1;94m╚██████╗██║  ██║╚██████╔╝╚██████╔╝   ██║   
 \x1b[1;94m ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   
\x1b[1;91m              𝙍𝘼𝙏𝙐 𝙀𝙍𝙍𝙊𝙍 \x1b[1;97m𝙋𝙍𝙊𝙅𝙀𝘾𝙏𝙎
\x1b[1;94m────────────────────────────────────────────────────
\x1b[1;97m {\x1b[1;94m•\x1b[1;97m} Author   : YayanXD
\x1b[1;97m {\x1b[1;94m•\x1b[1;97m} Github   : https://github.com/Yayan-XD
\x1b[1;97m {\x1b[1;94m•\x1b[1;97m} Facebook : https://www.facebook.com/KM39453
\x1b[1;94m────────────────────────────────────────────────────'''

cusr = 'YayanXD'
keyyy = '1qC3c8i'

def moch_yayan():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97m  LOGIN PASSWORD'
    print '\x1b[1;94m ─────────────────'
    print '\x1b[1;97m '
    usr = raw_input('          \x1b[1;92mPASSWORD \x1b[1;91m: \x1b[1;96m')
    if usr == cusr:
        tik()
        memek()
    else:
        os.system('clear')
        print logo
        print
        print
        print '\x1b[1;97m  LOGIN PASSWORD'
        print '\x1b[1;94m ─────────────────'
        print '\x1b[1;97m '
        print '          \x1b[1;92mPASSWORD \x1b[1;91m: \x1b[1;96m' + usr + ' (X)'
        time.sleep(1)
        os.system('xdg-open https://youtu.be/bEUPM_BNMBw')
        u()


def memek():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97m  LOGIN PASSWORD'
    print '\x1b[1;94m ─────────────────'
    print '\x1b[1;97m '
    psb('          \x1b[1;97mYOUR PASSWORD \x1b[1;91m: \x1b[1;96mYayanXD \x1b[1;97m(\x1b[1;92m•\x1b[1;97m)')
    print
    print
    psb(' \x1b[1;92mPASSWORD APPROVED BY \x1b[1;96mYayan XD.\x1b[0m')
    yayan()


def yayan():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97m  LICENSE KEY'
    print '\x1b[1;94m ───────────────'
    print '\x1b[1;97m '
    usr = raw_input('          \x1b[1;92mYOUR KEY \x1b[1;91m: \x1b[1;90m')
    if usr == keyyy:
        tik()
        xd()
    else:
        os.system('clear')
        print logo
        print
        print
        print '\x1b[1;97m  LICENSE KEY'
        print '\x1b[1;94m ───────────────'
        print '\x1b[1;97m '
        print '          \x1b[1;97mYOUR KEY \x1b[1;91m: \x1b[1;90mJQSADSE3267 \x1b[1;96m' + usr + ' (X)'
        time.sleep(1)
        os.system('xdg-open https://youtu.be/bEUPM_BNMBw')
        yayan()


def xd():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97m  LICENSE KEY'
    print '\x1b[1;94m ───────────────'
    print '\x1b[1;97m '
    print '          \x1b[1;97mYOUR KEY \x1b[1;91m: \x1b[1;90m1qC3c8i \x1b[1;97m(\x1b[1;92m•\x1b[1;97m)'
    print '\n\n \x1b[1;97mLICENSE KEY APPROVED BY \x1b[1;96mYayan XD.\x1b[0m'
    print
    jalan('\x1b[1;93mPLEASE WAIT 2MINUTES, ALL PACKAGES ARE CHECKING...')
    time.sleep(1)
    os.system('python2 lib/ngentod.py')


if __name__ == '__main__':
    moch_yayan()
