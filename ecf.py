#!/usr/bin/env python
import sys

if len(sys.argv) == 1:
    ecf = float(raw_input("ECF grade: "))
    print "FIDE grade: " + str(int((ecf*7.5) + 700))
else:
    ecf = float(sys.argv[1])
    print  "ECF grade: " + str(int(ecf))
    print "FIDE grade: " + str(int((ecf*7.5) + 700))

