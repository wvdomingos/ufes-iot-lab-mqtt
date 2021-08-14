#!/usr/bin/python

# Link: https://gist.github.com/ramonfontes/651c591141a66280f6433bae28217919

'Setting the position of Nodes and providing mobility using mobility models'
import os

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8',
                   min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10)
    net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8',
                   min_x=20, max_x=40, min_y=10, max_y=20, min_v=1, max_v=5)
    net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8',
                   min_x=80, max_x=100, min_y=10, max_y=20, min_v=1, max_v=5)
    net.addStation('sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8',
                   min_x=60, max_x=70, min_y=10, max_y=20, min_v=1, max_v=5)
    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', channel='1',
                             failMode="standalone", position='50,50,0')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.plotGraph(max_x=300, max_y=300)

    net.setMobilityModel(time=0, model='RandomDirection', max_x=100, max_y=100,
                         seed=20)

    info("*** Starting network\n")
    net.build()
    ap1.start([])

    i = 0
    while True:
        i+=1
        if i == 5000000: 
            for sta in net.stations:
                x = sta.pos[0]
                y = sta.pos[1]
                z = sta.pos[2]
                os.system('mosquitto_pub -t \"%s\" -P user -u user -m \"x=%s,y=%s,z=%s\"' % (sta.name,x,y,z))
            i=0

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
