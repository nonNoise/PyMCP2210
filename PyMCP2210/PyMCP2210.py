#############################################################
#    MIT License                                            #
#    Copyright (c) 2017 Yuta KItagami                       #
#############################################################


from PyMCP2210 import PyMCP2210_reg

# pip install hidapi
# https://github.com/trezor/cython-hidapi
import time

class PyMCP2210:
    def __init__(self,VID = 0x04D8,PID = 0x00DE,devnum = 0):
        self.mcp2210 = PyMCP2210_reg.PyMCP2210_reg(VID,PID,devnum)
        self.mcp2210.DeviceDriverInfo()
        self.mcp2210.GET_SPI_TRANSFER_SETTINGS()
        self.mcp2210.GET_CURRENT_CHIP_SETTING()
        self.mcp2210.GET_GPIO_PIN_DIR()
        self.mcp2210.GET_GPIO_PIN_VALUE()
        #self.mcp2210.GET_MCP2210_STATUS()
        self.GPIO_MODE = 0x00
        self.CS_MODE = 0x01
        self.Function_MODE = 0x02
        self.Output = 0x00
        self.Input = 0x01
        
    def GPIO_GP0_MODE_SET(self,mode,dir):
        self.mcp2210.GP0_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<0))  | dir<<0 
        self.mcp2210.SET_GPIO_PIN_DIR()
    def GPIO_GP1_MODE_SET(self,mode,dir):
        self.mcp2210.GP1_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<1))  | dir<<1 
        self.mcp2210.SET_GPIO_PIN_DIR()
    def GPIO_GP2_MODE_SET(self,mode,dir):
        self.mcp2210.GP2_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<2))  | dir<<2 
        self.mcp2210.SET_GPIO_PIN_DIR()
    def GPIO_GP3_MODE_SET(self,mode,dir):
        self.mcp2210.GP3_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<3))  | dir<<3
        self.mcp2210.SET_GPIO_PIN_DIR()
    def GPIO_GP4_MODE_SET(self,mode,dir):
        self.mcp2210.GP4_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<4))  | dir<<4 
        self.mcp2210.SET_GPIO_PIN_DIR()
    def GPIO_GP5_MODE_SET(self,mode,dir):
        self.mcp2210.GP5_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<5))  | dir<<5 
        self.mcp2210.SET_GPIO_PIN_DIR()
    def GPIO_GP6_MODE_SET(self,mode,dir):
        self.mcp2210.GP6_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<6))  | dir<<6 
        self.mcp2210.SET_GPIO_PIN_DIR()
    def GPIO_GP7_MODE_SET(self,mode,dir):
        self.mcp2210.GP7_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<7))  | dir<<7 
        self.mcp2210.SET_GPIO_PIN_DIR()
    def GPIO_GP8_MODE_SET(self,mode,dir):
        self.mcp2210.GP8_PIN_MODE = mode
        self.mcp2210.SET_CURRENT_CHIP_SETTING()
        self.mcp2210.GPIO_DIR = (self.mcp2210.GPIO_DIR & (0x1FF ^ 1<<8))  | dir<<8 
        self.mcp2210.SET_GPIO_PIN_DIR()


        
    def GPIO_GP0_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<0))  | Output<<0
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 0) &0x01
    def GPIO_GP1_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<1))  | Output<<1
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 1) &0x01
    def GPIO_GP2_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<2))  | Output<<2
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 2) &0x01
    def GPIO_GP3_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<3))  | Output<<3
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 3) &0x01
    def GPIO_GP4_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<4))  | Output<<4
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 4) &0x01
    def GPIO_GP5_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<5))  | Output<<5
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 5) &0x01
    def GPIO_GP6_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<6))  | Output<<6
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 6) &0x01
    def GPIO_GP7_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<7))  | Output<<7
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 7) &0x01
    def GPIO_GP8_Value(self,Output=0):
        self.mcp2210.GPIO_Value = (self.mcp2210.GPIO_Value & (0x1FF ^ 1<<8))  | Output<<8
        self.mcp2210.SET_GPIO_PIN_VALUE()
        return (self.mcp2210.GPIO_Value >> 8) &0x01

        
    def SPI_Setup(self):
        self.mcp2210.BitRate = self.BitRate
        self.mcp2210.IdleChipSelect = self.IdleChipSelect
        self.mcp2210.ActivChipSelect = self.ActivChipSelect
        self.mcp2210.CStoDataDelay = self.CStoDataDelay
        self.mcp2210.DatatoCSDelay = self.DatatoCSDelay
        self.mcp2210.DelayData = self.DelayData
        self.mcp2210.ByteLength = self.ByteLength
        self.mcp2210.SPIMode = self.SPIMode
        self.mcp2210.CANCEL_SPI_TREANSFER()
        self.mcp2210.REQUEST_SPI_BUS_RELEASE()
        self.mcp2210.SET_SPI_TRANSFER_SETTINGS()

    def SPI_WRITE(self,data):
        return self.mcp2210.TRANSFER_SPI_DATA(data)
    def SPI_READ(self):
        return self.mcp2210.TRANSFER_SPI_DATA([])