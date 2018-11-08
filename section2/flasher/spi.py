import struct
import usb1

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
  CMD_GET = 8
  CMD_SET_DELAY = 9
  CMD_GET_DELAY = 10
  CMD_SET_START_END_DELAY = 11
  CMD_GET_START_END_DELAY = 12

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
    return ret

  def send_cmd_get(self, num):
    ret = self.send_cmd_simple(num)
    assert len(ret) == 6
    assert ret[0] == 5
    assert ret[1] == 0
    return struct.unpack("I", ret[2:])[0]

  def enable(self):
    ret = self.send_cmd_simple(self.CMD_ENABLE)

  def get_speed(self):
    return self.send_cmd_get(self.CMD_GET_SPEED)

  def set_speed(self, speed):
    self.handle.bulkWrite(1, struct.pack("BBBBI", 7, 6, self.CMD_SET_SPEED, self.port, speed))
    ret = self.handle.bulkRead(2, 0x10)

  def get_delay(self):
    return self.send_cmd_get(self.CMD_GET_DELAY)

  def get_start_end_delay(self):
    # broken?
    #ret = self.send_cmd_simple(self.CMD_GET_START_END_DELAY)
    pass

  def disable(self):
    ret = self.send_cmd_simple(self.CMD_DISABLE)
    assert ret == b"\x01\x00"

  def put(self, b, fSelStart=0, fSelEnd=1):
    rcv = 1

    # queue send
    self.handle.bulkWrite(1, struct.pack("BBBBBBBI", 10, 6, self.CMD_PUT, 0, fSelStart, fSelEnd, rcv, len(b)))
    ret = self.handle.bulkRead(2, 0x10)
    assert ret == b"\x01\x00"

    self.handle.bulkWrite(3, b)
    ret = self.send_cmd_simple(0x87)  # done sending?

    ret = self.handle.bulkRead(4, 0x40)
    return ret

  def get(self, num, fSelStart=0, fSelEnd=1, bFill=0):
    self.handle.bulkWrite(1, struct.pack("BBBBBBBI", 10, 6, self.CMD_GET, 0, fSelStart, fSelEnd, bFill, num))
    ret = self.handle.bulkRead(2, 0x10)
    dret = self.handle.bulkRead(4, num)
    assert len(dret) == num
    ret = self.send_cmd_simple(0x88)
    return dret

