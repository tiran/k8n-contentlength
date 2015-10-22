#!/usr/bin/env python
from __future__ import print_function

import socket
import sys

def err(msg):
    print(msg, file=sys.stderr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8080))
s.listen(1)

err('LISTENING')

while 1:
    conn, addr = s.accept()
    err(addr)
    err(conn.recv(65565))
    err('---')
    conn.sendall("HTTP/1.1 418 I'm a teapot\r\n\r\n")
    conn.close()

