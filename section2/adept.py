#!/usr/bin/env python3
import struct
import usb1

context = usb1.USBContext()
handle = context.openByVendorIDAndProductID(0x1443, 0x0007)
#handle.setConfiguration(0)
handle.claimInterface(0)
dev = handle.getDevice()
print(dev)
#print(dir(dev))

# DspiEnableEx:   3 6 0 <1: port request>
# DspiDisable:    3 6 1 <1: port request>
# DspiSetSpeed:   7 6 3 <1: active port> <4: speed>
# DspiGetSpeed:   3 6 4 <1: active port>
# DspiSetSpiMode: 4 6 5 <1: active port> <1: mode?>
# DspiSetSelect:  4 6 6 <1: active port> <1: select state>

# DspiPut:       10 6 7 <1: active port> <1: fSelStart> <1: fSelEnd>
#                       <1: should receive?> <4: number of bytes>
# (fSelStart, fSelEnd, rgbSnd, rgbRcv, cbSend, fOverlap)

def spi_get_speed():
  handle.bulkWrite(1, struct.pack("BBBB", 3, 6, 4, 0))
  ret = handle.bulkRead(2, 0x10)
  assert len(ret) == 6
  assert ret[0] == 5
  assert ret[1] == 0
  return struct.unpack("I", ret[2:])[0]

def spi_put(b):
  fSelStart = 1
  fSelEnd = 0
  rcv = 0
  handle.bulkWrite(1, struct.pack("BBBBBBBI", 10, 6, 7, 0, fSelStart, fSelEnd, rcv, len(b)))
  handle.bulkWrite(3, b)
  ret = handle.bulkRead(2, 0x10)
  print(ret)

def spi_enable(port):
  handle.bulkWrite(1, struct.pack("BBBB", 3, 6, 0, port))
  print(handle.bulkRead(2, 0x10))

def spi_disable(port):
  handle.bulkWrite(1, struct.pack("BBBB", 3, 6, 1, port))
  print(handle.bulkRead(2, 0x10))

spi_enable(0)
print(spi_get_speed())

spi_disable(0)


exit(0)


for i in range(8):
  try:
    mps = dev.getMaxPacketSize(i)
    print(i, mps)
  except Exception:
    pass

# enable
#handle.bulkWrite(1, struct.pack("BBBB", 3, 6, 4, 0))
#print(handle.bulkRead(2, 0x10))

print(spi_get_speed())

handle.bulkWrite(1, struct.pack("BBBB", 3, 6, 1, 0))
print(handle.bulkRead(2, 0x10))


handle.close()

#print(handle.bulkRead(1, 0x10))


