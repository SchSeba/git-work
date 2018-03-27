#!/usr/bin/env python
import sys

import pydevd as pydevd

pydevd.settrace('localhost', port=7000, stdoutToServer=True, stderrToServer=True)
print(sys.argv)

