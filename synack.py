#! /usr/bin/env python

import sys, argparse, socket

class Listener:
    def __init__(self,
                 interfaceName,
                 protocolNumber_HBO=0x0800):
        """Make the raw socket specified. Arrange that it responds SYN/ACK to anything
        arriving that looks like SYN, and builds a collection. Arrange that the entire
        collection can be sent RST."""
        self.interfaceName = interfaceName
        self.protocolNumber_NBO = socket.htons(protocolNumber_HBO)
        self.address = (interfaceName, self.protocolNumber_NBO)
        self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

    def __repr__(self):
        return f'<Listener paddr:{self.sock.getsockname()!r}>'

def main():
    p = argparse.ArgumentParser()
    p.add_argument('interface')
    a = p.parse_args()
    print(f'{Listener(a.interface)!r}')

if __name__ == '__main__':
    sys.exit(main())
