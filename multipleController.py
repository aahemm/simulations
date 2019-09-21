#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import run

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')
    
    Y = run.run()
    print(Y)
    M = 20
    N = 10
    IP = '192.168.56.103'
    info( '*** Adding controllers\n' )
    controllers = []
    ports = range(6633,6643)
    for i in range(N):
    	c = net.addController(name='c%s' % i,
                     	     controller=RemoteController,
                             protocol='tcp',
                             ip=IP,
                             port=ports[i])
        controllers.append(c)

    info( '*** Adding switches\n')
    switches = []
    for i in range(20):
   	sw = net.addSwitch('s%s' % i, cls=OVSKernelSwitch)
        switches.append(sw)

    info( '*** Adding hosts\n')
    hosts = []
    for i in range(M):
         ind = 2*i
   	 h1 = net.addHost('h%s' % ind, cls=Host, ip='10.0.0.%s' % (ind+1), defaultRoute=None)
   	 hosts.append(h1)
         ind += 1 
         h2 = net.addHost('h%s' % ind, cls=Host, ip='10.0.0.%s' % (ind+1), defaultRoute=None)
         hosts.append(h2)
 
    info('*** Adding links\n')
    for i in range(M):
   	 net.addLink(hosts[2*i], switches[i])
         net.addLink(hosts[2*i+1], switches[i])
       

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in controllers:
        controller.start()

    info( '*** Starting switches\n')
    for n in range(N):
        for m in range(M):
            if Y[n][m]:
               switches[m].start([controllers[n]])          
               print(n,m)
    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

