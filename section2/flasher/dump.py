#!/usr/bin/env python3
import struct
from spi import SPI
from tqdm import tqdm

spi = SPI(0)
print("speed:",spi.get_speed())
spi.set_speed(8000000)
print("speed:",spi.get_speed())
print("delay:",spi.get_delay())
spi.put(b"\x9e" + b"\x00"*20)

allret = []
for addr in tqdm(range(0, 0x1000000, 0x1000)):
  ret = spi.put(b"\x03" + struct.pack(">I", addr)[1:], fSelEnd=0)
  ret = spi.get(0x1000, fSelEnd=1)
  allret.append(ret)

out = b''.join(allret)
with open("dump", "wb") as f:
  f.write(out)

del spi

