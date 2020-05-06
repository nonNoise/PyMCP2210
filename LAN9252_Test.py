from LAN9252 import LAN9252 
from LAN9252 import LAN9252Reg
import time

print("="*50)
lan9252 = LAN9252.LAN9252()
print("="*50)
rdata = lan9252.LAN925X_SPI_READ(LAN9252Reg.ID_REV)
print("ID_REV:0x%04X" % (rdata))
rdata = lan9252.LAN925X_SPI_READ(LAN9252Reg.BYTE_TEST)
print("BYTE_TEST:0x%04X" % (rdata))
rdata = lan9252.LAN925X_SPI_READ(LAN9252Reg.FREE_RUN)
print("FREE_RUN:0x%04X" % (rdata))
rdata = lan9252.LAN9252_EtherCAT_CSR_READ(LAN9252Reg.CSR_SIZE_16bit,LAN9252Reg.Product_ID)
print("Product_ID:0x%04X" % (rdata))
rdata = lan9252.LAN9252_EtherCAT_CSR_READ(LAN9252Reg.CSR_SIZE_16bit,LAN9252Reg.Vendor_ID)
print("Vendor_ID:0x%04X" % (rdata))


rdata = lan9252.LAN9252_EtherCAT_CSR_READ(4,LAN9252Reg.RUN_LED_Override)
print("RUN_LED_Override:0x%04X" % (rdata))
lan9252.LAN9252_EtherCAT_CSR_WRITE(4,LAN9252Reg.RUN_LED_Override,1<<4 | 0x0D)
rdata = lan9252.LAN9252_EtherCAT_CSR_READ(4,LAN9252Reg.RUN_LED_Override)
print("RUN_LED_Override:0x%04X" % (rdata))




