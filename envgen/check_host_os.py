import subprocess
import sys

for i, arg in enumerate(sys.argv):
    if '-host' in arg:
        host = arg.split("-host=")[-1]
    if '-user' in arg:
        user = arg.split("-user=")[-1]

proc = subprocess.Popen("ssh {0}@{1} 'cat /etc/lsb-release'".format(user, host), stdout=subprocess.PIPE, shell=True)
proc.wait()

for info in proc.stdout:
    if "Ubuntu" in str(info): 
        print('ubuntu')
        break
    elif "Manjaro" in str(info): 
        print('manjaro')
        break
