#!/usr/bin/python
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.log import setLogLevel
'''
Single switch connected to n hosts.
'''
class SingleSwitchTopo(Topo):
	def build(enable_all = True):
		#add switch
		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')
		switch3 = self.addSwitch('s3')
		switch4 = self.addSwitch('s4')
		switch5 = self.addSwitch('s5')
		switch6 = self.addSwitch('s6')
		switch7 = self.addSwitch('s7')
		#add host
		host1 = self.addHost('h1')
		host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
		host6 = self.addHost('h6')
		host7 = self.addHost('h7')
		host8 = self.addHost('h8')
		#add link
		self.addLink(host1, switch1)
		self.addLink(host2, switch1)
		self.addLink(host2, switch4)
		self.addLink(host5, switch4)
		self.addLink(host2, switch2)
		self.addLink(host2, switch6)
		self.addLink(host7, switch6)
		self.addLink(host3, switch2)
		self.addLink(host3, switch5)
		self.addLink(host3, switch3)
		self.addLink(host3, switch7)
		self.addLink(host6, switch5)
		self.addLink(host8, switch7)
		self.addLink(host4, switch3)
'''
Create and test a simple network
'''
def test():
	#create topo with 8 host ,7 switch
	topo = SingleSwitchTopo(enable_all = True)
	
	net = Mininet(topo = topo, controller = OVSConroller, link = TCLink)
	#start
	net.start()
	dumpNodeConnections(net.hosts)
	dumpNodeConnections(net.switches)
	CLI(net)

'''
Main (entry point)
'''
if __name__ == '__main__':
	setLogLevel('info')
	#test
	test()
