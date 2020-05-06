#############################################################
#    MIT License                                            #
#    Copyright (c) 2017 Yuta KItagami                       #
#############################################################


#######################################################################
# NVRAM is not supported.
# 0x60 – Set Chip NVRAM Parameters
# 0x61 – Get NVRAM Settings – command code
# 0x70 – SEND ACCESS Password – command code
# External Interrupt Pin (GP6) Event Status is not supported.
# 0x12 – Get (VM) the Current Number of Events From the Interrupt Pin
#######################################################################


import hid
# pip install hidapi
# https://github.com/trezor/cython-hidapi
import time

class PyMCP2210_reg:
    def __init__(self,VID = 0x04D8,PID = 0x00DE,devnum = 0):
        self.mcp2210 = hid.device()
        self.mcp2210.open_path(hid.enumerate(VID, PID)[devnum]["path"])
    #######################################################################
    # HID DeviceDriver Info
    #######################################################################
    def DeviceDriverInfo(self):
        print("Manufacturer: %s" % self.mcp2210.get_manufacturer_string())
        print("Product: %s" % self.mcp2210.get_product_string())
        print("Serial No: %s" % self.mcp2210.get_serial_number_string())        
        
    #######################################################################
    # GET_SPI_TRANSFER_SETTINGS
    #######################################################################
    def GET_SPI_TRANSFER_SETTINGS(self):
        buf = [0x00, 0x41, 0x00, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        #for i in range(len(buf)):
        #    print ("[%d]: 0x{:02x}".format(buf[i]) % (i))
        self.BitRate = buf[7]<<24 | buf[6]<<16 | buf[5]<<8 | buf[4]<<0
        self.IdleChipSelect = buf[9]<<8 | buf[8]
        self.ActivChipSelect = buf[11]<<8 | buf[10]
        self.CStoDataDelay = buf[13]<<8 | buf[12]
        self.DatatoCSDelay = buf[15]<<8 | buf[14]
        self.DelayData = buf[17]<<8 | buf[16]
        self.ByteLength = buf[19]<<8 | buf[18]
        self.SPIMode = buf[20]
    #######################################################################
    # SET_SPI_TRANSFER_SETTINGS
    #######################################################################
    def SET_SPI_TRANSFER_SETTINGS(self):
        buf = [0x00, 0x40, 0x00, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        buf[4+1] = 0xFF&(self.BitRate>>0)
        buf[5+1] = 0xFF&(self.BitRate>>8)
        buf[6+1] = 0xFF&(self.BitRate>>16)
        buf[7+1] = 0xFF&(self.BitRate>>24)        
        buf[8+1] = 0xFF&(self.IdleChipSelect>>0)
        buf[9+1] = 0xFF&(self.IdleChipSelect>>8)
        buf[10+1] = 0xFF&(self.ActivChipSelect>>0)
        buf[11+1] = 0xFF&(self.ActivChipSelect>>8)
        buf[12+1] = 0xFF&(self.CStoDataDelay>>0)
        buf[13+1] = 0xFF&(self.CStoDataDelay>>8)
        buf[14+1] = 0xFF&(self.DatatoCSDelay>>0)
        buf[15+1] = 0xFF&(self.DatatoCSDelay>>8)
        buf[16+1] = 0xFF&(self.DelayData>>0)
        buf[17+1] = 0xFF&(self.DelayData>>8)
        buf[18+1] = 0xFF&(self.ByteLength>>0)
        buf[19+1] = 0xFF&(self.ByteLength>>8)
        buf[20+1] = 0xFF&(self.SPIMode)
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        if(buf[1]==0xF8):
            print ("[SET_SPI_TRANSFER_SETTINGS ERROR]: USB transfer in progress – Settings not written")        
    #######################################################################
    # GET_CURRENT_CHIP_SETTING
    #######################################################################
    def GET_CURRENT_CHIP_SETTING(self):
        buf = [0x00, 0x20, 0x00, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        self.GP0_PIN_MODE = buf[4]
        self.GP1_PIN_MODE = buf[5]
        self.GP2_PIN_MODE = buf[6]
        self.GP3_PIN_MODE = buf[7]
        self.GP4_PIN_MODE = buf[8]
        self.GP5_PIN_MODE = buf[9]
        self.GP6_PIN_MODE = buf[10]
        self.GP7_PIN_MODE = buf[11]
        self.GP8_PIN_MODE = buf[12]
        self.DefaultGPIO_Output = buf[14]<<8 | buf[13]
        self.DefaultGPIO_DIR = buf[16]<<8 | buf[15]
        self.OtherChipSettings = buf[17]
        self.NVRAM_ChipAccess = buf[18]
    #######################################################################
    # SET_CURRENT_CHIP_SETTING
    #######################################################################
    def SET_CURRENT_CHIP_SETTING(self):
        buf = [0x00, 0x21, 0x00, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        buf[4+1] = self.GP0_PIN_MODE;
        buf[5+1] = self.GP1_PIN_MODE;
        buf[6+1] = self.GP2_PIN_MODE;
        buf[7+1] = self.GP3_PIN_MODE;
        buf[8+1] = self.GP4_PIN_MODE;
        buf[9+1] = self.GP5_PIN_MODE;
        buf[10+1] = self.GP6_PIN_MODE;
        buf[11+1] = self.GP7_PIN_MODE;
        buf[12+1] = self.GP8_PIN_MODE;
        buf[13+1] = 0xFF&(self.DefaultGPIO_Output>>0);
        buf[14+1] = 0xFF&(self.DefaultGPIO_Output>>8);
        buf[15+1] = 0xFF&(self.DefaultGPIO_DIR>>0);
        buf[16+1] = 0xFF&(self.DefaultGPIO_DIR>>8);
        buf[17+1] = 0xFF&(self.OtherChipSettings>>0);
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
    #######################################################################
    # GET_GPIO_PIN_DIR
    #######################################################################
    def GET_GPIO_PIN_DIR(self):
        buf = [0x00, 0x33, 0x00, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        self.GPIO_DIR = buf[5]<<8 | buf[4]
    #######################################################################
    # SET_GPIO_PIN_DIR
    #######################################################################
    def SET_GPIO_PIN_DIR(self):
        buf = [0x00, 0x32, 0x00, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        buf[4+1] = 0xFF & (self.GPIO_DIR>>0)
        buf[5+1] = 0xFF & (self.GPIO_DIR>>8)
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
    #######################################################################
    # GET_GPIO_PIN_VALUE
    #######################################################################
    def GET_GPIO_PIN_VALUE(self):
        buf = [0x00, 0x31, 0x00, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        self.GPIO_Value = buf[5]<<8 | buf[4]
    #######################################################################
    # GET_GPIO_SET_GPIO_PIN_VALUEPIN_VALUE
    #######################################################################
    def SET_GPIO_PIN_VALUE(self):
        buf = [0x00, 0x30, 0x00, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        buf[4+1] = 0xFF & (self.GPIO_Value>>0)
        buf[5+1] = 0xFF & (self.GPIO_Value>>8)
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
    #######################################################################
    # READ_EEPROM_MEMORY
    #######################################################################
    def READ_EEPROM_MEMORY(self,addr):
        buf = [0x00, 0x50, addr, 0x00, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        return buf[3]
    #######################################################################
    # WRITE_EEPROM_MEMORY
    #######################################################################
    def WRITE_EEPROM_MEMORY(self,addr,value):
        buf = [0x00, 0x51, addr, value, 0x00]
        buf = buf + [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        if(buf[1]==0xFA):
            print ("[WRITE_EEPROM_MEMORY ERROR]: EEPROM Write Failure")
        if(buf[1]==0xFB):
            print ("[WRITE_EEPROM_MEMORY ERROR]: EEPROM is password protected or permanently locked")        
    #######################################################################
    # TRANSFER_SPI_DATA
    #######################################################################
    def TRANSFER_SPI_DATA(self,data):
        buf = [0x00, 0x42, len(data), 0x00, 0x00]
        buf = buf + data + [0 for i in range(65 - len(buf)-len(data))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        """
        if(buf[1]==0xF7):
            print ("[TRANSFER_SPI_DATA ERROR]: SPI Data Not Accepted – SPI bus not available (the external owner has control over it)")
        if(buf[1]==0xF8):
            print ("[TRANSFER_SPI_DATA ERROR]: SPI Data Not Accepted – SPI transfer in progress – cannot accept any data for the moment")
        if(buf[1]==0x00):
            if(buf[3]==0x20):
                print ("[TRANSFER_SPI_DATA Status]: SPI transfer started – no data to receive")
            if(buf[3]==0x30):
                print ("[TRANSFER_SPI_DATA Status]: SPI transfer not finished; received data available")
            if(buf[3]==0x10):
                print ("[TRANSFER_SPI_DATA Status]: SPI transfer finished – no more data to send")
        #print("0x%02X" % buf[2])
        """

        return buf[4:4+buf[2]] 
        #return []
    #######################################################################
    # CANCEL_SPI_TREANSFER
    #######################################################################
    def CANCEL_SPI_TREANSFER(self):
        buf = [0x00, 0x11, 0x00, 0x00, 0x00]
        buf = buf +  [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        """
        if(buf[2]==0x01):
            print ("[CANCEL_SPI_TREANSFER Status]: No External Request for SPI Bus Release")
        if(buf[2]==0x00):
            print ("[CANCEL_SPI_TREANSFER Status]: Pending External Request for SPI Bus Release")
        if(buf[3]==0x00):
            print ("[CANCEL_SPI_TREANSFER Status]: SPI Bus Current = No Owner")
        if(buf[3]==0x01):
            print ("[CANCEL_SPI_TREANSFER Status]: SPI Bus Current = USB Bridge")
        if(buf[3]==0x02):
            print ("[CANCEL_SPI_TREANSFER Status]: SPI Bus Current = External Master")
        print ("[Attempted Password Accesses]:0x{:02x}".format(buf[4]))
        if(buf[5]==0x00):
            print ("[CANCEL_SPI_TREANSFER Status]: Password Guessed = Password Not Guessed")
        if(buf[5]==0x01):
            print ("[CANCEL_SPI_TREANSFER Status]: Password Guessed = Password Guessed")
        """
    #######################################################################
    # REQUEST_SPI_BUS_RELEASE
    #######################################################################
    def REQUEST_SPI_BUS_RELEASE(self):
        buf = [0x00, 0x80, 0x00, 0x00, 0x00]
        buf = buf +  [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        #if(buf[1]==0x00):
        #    print ("[REQUEST_SPI_BUS_RELEASE Status]: Command Completed Successfully – SPI bus released")
        #if(buf[1]==0xF8):
        #    print ("[REQUEST_SPI_BUS_RELEASE Status]: SPI Bus Not Released – SPI transfer in process")
    #######################################################################
    # GET_MCP2210_STATUS
    #######################################################################
    def GET_MCP2210_STATUS(self):
        buf = [0x00, 0x10, 0x00, 0x00, 0x00]
        buf = buf +  [0 for i in range(65 - len(buf))]
        self.mcp2210.write(buf)
        buf = self.mcp2210.read(65)
        if(buf[2]==0x00):
            print ("[SPI Bus Release External Request Status]: Pending External Request for SPI Bus Release")
        if(buf[2]==0x01):
            print ("[SPI Bus Release External Request Status]: No External Request for SPI Bus Release")
        if(buf[3]==0x00):
            print ("[SPI Bus Current Owner]: No Owner")
        if(buf[3]==0x01):
            print ("[SPI Bus Current Owner]: USB Bridge")
        if(buf[3]==0x02):
            print ("[SPI Bus Current Owner]: External Master")
        if(buf[5]==0x00):
            print ("[CANCEL_SPI_TREANSFER Status]: Password Guessed = Password Not Guessed")
        if(buf[5]==0x01):
            print ("[CANCEL_SPI_TREANSFER Status]: Password Guessed = Password Guessed")
