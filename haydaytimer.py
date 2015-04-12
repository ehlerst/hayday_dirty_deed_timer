#!/bin/env python
import time
from time import gmtime, strftime

def deedstimer():
  for t in range(120,-1,-1):
      minutes = t / 60
      seconds = t % 60
      print "%d:%2d" % (minutes,seconds)
      time.sleep(1.0)

def printit():
  print strftime("%H:%M:%S")
  deedstimer()
  print "Dirty Deeds ready"

while True:
    printit()
