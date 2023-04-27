import pings
import datetime
import subprocess

hosts = ["192.168.11.52"]

p = pings.Ping(quiet=False)
res = p.ping("192.168.11.52", times=10)

# datetime_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

for h in hosts:
    res = p.ping(h)
    if not res.is_reached():
        print('-')
        
def is_connectable(host):
    ping = subprocess.run(["ping", "-w", "1", "-c", "1", host], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return ping.returncode == 0



# 力不足でした。全く分からずこれだけです。