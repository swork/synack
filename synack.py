#! /usr/bin/env python

import sys, argparse, socket

class Listener:
    def __init__(self, interface = None):
        """Make a promiscuous raw socket. Arrange that it responds SYN/ACK to
        anything arriving that looks like SYN, and builds a
        collection. Arrange that the entire collection can be sent
        RST.
        """

        if interface:
            gai = list(
                filter(
                    lambda x: x[1] == socket.SOCK_RAW,
                    socket.getaddrinfo(interface, 0, family=socket.AF_INET)))[0]
        else:
            gai = (socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW, '', ('', 0))

        try:
            s = socket.socket(family=gai[0], type=gai[1], proto=gai[2])
        except OSError as e:
            print(f'{e!r}')
            s = socket.socket(family=gai[0], type=gai[1], proto=socket.IPPROTO_RAW)

        s.bind(gai[4])
        print(f'{s!r}')

        #### This sequence leads to a socket that looks right, but .readone()
        #### gets nothing in my testing (Linux 4.15). Left it here for now.
        
        self.sock = s

    def __repr__(self):
        return f'<Listener paddr:{self.sock.getsockname()!r}>'

    def readone(self):
        packet = self.sock.recvmsg(1500, 1500)
        (data, ancdata, msg_flags, address) = packet
        print(f'from:{address} - {bytearray(data)}')

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--interface')
    a = p.parse_args()
    if a.interface:
        s = Listener(a.interface.encode('utf-8'))
    else:
        s = Listener()
    print(f'{s!r}')
    s.readone()

if __name__ == '__main__':
    sys.exit(main())
