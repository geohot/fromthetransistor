#!/usr/bin/env python3
import usb1

context = usb1.USBContext()
handle = context.openByVendorIDAndProductID(0x1443, 0x0007)
dev = handle.getDevice()
print(dev)





