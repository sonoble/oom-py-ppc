# /////////////////////////////////////////////////////////////////////
#
#  oomtest.py :
#  For each port,
#      for read keys, functions, write keys
#          Read each key, read each function, write each write key
#
#  Not checking values, just making sure every key is coded in a
#  way that doesn't throw an exception.
#
#  Copyright 2015  Finisar Inc.
#
#  Author: Don Bollinger don@thebollingers.or/
#
# ////////////////////////////////////////////////////////////////////

#
from oom import *                   # the published OOM Northbound API
from oom.decode import hexstr           # helper function from the decode pack


portlist = oom_get_portlist()
for port in portlist:
    for key in port.mmap:
        test = oom_get_keyvalue(port, key)
    for key in port.fmap:
        test = oom_get_memory(port, key)
    for key in port.wmap:  # read current value, write it back
        val = oom_get_keyvalue(port, key)
        test = oom_set_keyvalue(port, key, val)
    print '%d raw memory reads for port %s' % (port.readcount, port.port_name)
