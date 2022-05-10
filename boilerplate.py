#!/usr/bin/python3 
# https://github.com/k4miyo/Bashed-Autopwn/blob/k4miyo/Bashed_autopwn.py (bashed example)

import sys, time, threading, signal, requests, string, argparse, warnings
from pwn import *

warnings.filterwarnings("ignore")

# execute here
if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description='autopwn script'
  )

  parser.add_argument(
  '--rhost',
  action='store',
  dest='rhost',
  help='remote ip of the HTB machine (victim)'
  )  

  parser.add_argument(
  '--lhost',
  action='store',
  dest='lhost',
  help='Local host ip address (attacker)'
  )  

  parser.add_argument(
  '--lport',
  action='store',
  dest='lport',
  help='Local port of the ip address (attacker)'
  )  

  # create args to be passed
  args = parser.parse_args()

  # attack variables 
  rhost = args.rhost
  lhost = args.lhost 
  lport = args.lport

  # test variables 
  print('rhost : %s' % (rhost))
  print('lhost : %s' % (lhost))
  print('lport : %s' % (lport))

     
