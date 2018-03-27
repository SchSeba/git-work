#!/usr/bin/python
import sys

import pydevd

pydevd.settrace('localhost', port=7000, stdoutToServer=True, stderrToServer=True)
print(sys.argv)

