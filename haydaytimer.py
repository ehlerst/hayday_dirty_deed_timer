#!/bin/env python
import time
from time import gmtime, strftime

def printit():
  print strftime("%H:%M:%S")
  time.sleep(120)
  print "Dirty Deeds ready"

while True:
    printit()
