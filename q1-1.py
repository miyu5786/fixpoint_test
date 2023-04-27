import subprocess
import time

hosts = ["192.168.11.52"]

for host in hosts:
    res = subprocess.run(["ping",host,"-c","2", "-W", "300"],stdout=subprocess.PIPE)

    print(res.stdout.decode("cp932"))
    
    if res.returncode == 0 :
        print("成功\n\n")
    else:
        print("失敗\n\n")
    print("-----------------------------")