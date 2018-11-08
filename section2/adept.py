#!/usr/bin/env python3
import struct
import usb1
import time
from hexdump import hexdump

# DspiEnableEx:   3 6 0 <1: port request>
# DspiDisable:    3 6 1 <1: port request>
# DspiSetSpeed:   7 6 3 <1: active port> <4: speed>
# DspiGetSpeed:   3 6 4 <1: active port>
# DspiSetSpiMode: 4 6 5 <1: active port> <1: mode?>
# DspiSetSelect:  4 6 6 <1: active port> <1: select state>

# DspiPut:       10 6 7 <1: active port> <1: fSelStart> <1: fSelEnd>
#                       <1: should receive?> <4: number of bytes>
# (fSelStart, fSelEnd, rgbSnd, rgbRcv, cbSend, fOverlap)

class SPI(object):
  CMD_ENABLE = 0
  CMD_DISABLE = 1
  CMD_SET_SPEED = 3
  CMD_GET_SPEED = 4
  CMD_SET_SPI_MODE = 5
  CMD_SET_SELECT = 6
  CMD_PUT = 7

  def __init__(self, port):
    self.context = usb1.USBContext()
    self.handle = self.context.openByVendorIDAndProductID(0x1443, 0x0007)
    self.handle.claimInterface(0)

    self.port = port
    self.enable()

  def __del__(self):
    self.disable()
    self.handle.close()

  def send_cmd_simple(self, num):
    self.handle.bulkWrite(1, struct.pack("BBBB", 3, 6, num, self.port))
    ret = self.handle.bulkRead(2, 0x10)
    hexdump(ret)
    return ret

  def enable(self):
    ret = self.send_cmd_simple(self.CMD_ENABLE)

  def get_speed(self):
    ret = self.send_cmd_simple(self.CMD_GET_SPEED)
    assert len(ret) == 6
    assert ret[0] == 5
    assert ret[1] == 0
    return struct.unpack("I", ret[2:])[0]

  def disable(self):
    ret = self.send_cmd_simple(self.CMD_DISABLE)
    assert ret == b"\x01\x00"

  def put(self, b, fSelStart=0, fSelEnd=1):
    rcv = 1
    self.handle.bulkWrite(1, struct.pack("BBBBBBBI", 10, 6, 7, 0, fSelStart, fSelEnd, rcv, len(b)))
    self.handle.bulkWrite(3, b)
    hexdump(self.handle.bulkRead(2, 0x10))
    hexdump(self.handle.bulkRead(2, 0x10))
    hexdump(self.handle.bulkRead(4, 0x40))

spi = SPI(0)
print(spi.get_speed())
spi.put(b"\x9e" + b"\x00"*20)
del spi

