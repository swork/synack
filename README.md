# synack
TCP investigation tool

First pass: raw socket makes SYN/ACK response to every SYN until quit, then RST to all.

Current state: Not working in tests (Linux 4.15) though socket setup looks right.
