from PyMCP2210 import PyMCP2210
from FT810 import FT810Reg

import hid
# pip install hidapi
# https://github.com/trezor/cython-hidapi
import time

class FT810:
    def __init__(self,VID = 0x04D8,PID = 0x00DE,devnum = 0):
        self.mcp2210 = PyMCP2210.PyMCP2210(VID,PID,devnum)
        
        self.mcp2210.BitRate = 0xb71b00-1
        self.mcp2210.IdleChipSelect = 0x01
        self.mcp2210.ActivChipSelect = 0x00
        self.mcp2210.CStoDataDelay = 0x00
        self.mcp2210.DatatoCSDelay = 0x00
        self.mcp2210.DelayData = 0x00
        self.mcp2210.ByteLength = 0x07
        self.mcp2210.SPIMode = 0x00
        self.mcp2210.SPI_Setup()

        self.mcp2210.GPIO_GP0_MODE_SET(self.mcp2210.CS_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP1_MODE_SET(self.mcp2210.GPIO_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP2_MODE_SET(self.mcp2210.GPIO_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP3_MODE_SET(self.mcp2210.GPIO_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP4_MODE_SET(self.mcp2210.GPIO_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP5_MODE_SET(self.mcp2210.GPIO_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP6_MODE_SET(self.mcp2210.GPIO_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP7_MODE_SET(self.mcp2210.GPIO_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP8_MODE_SET(self.mcp2210.GPIO_MODE,self.mcp2210.Output)
        self.mcp2210.GPIO_GP7_Value(1);    

    def FT810_SPI_HOST_MEM_READ32(self,addr):
        self.mcp2210.ByteLength = 0x08
        self.mcp2210.SPI_Setup()
        wdata = [0xFF&(addr>>16),0xFF&(addr>>8),0xFF&(addr>>0),0x00,0x00,0x00,0x00,0x00]
        self.mcp2210.SPI_WRITE(wdata)
        rdata = self.mcp2210.SPI_READ()
        return rdata[7]<<24 |rdata[6]<<16 |rdata[5]<<8 |rdata[4]<<0  
    def FT810_SPI_HOST_MEM_READ16(self,addr):
        self.mcp2210.ByteLength = 0x06
        self.mcp2210.SPI_Setup()
        wdata = [0xFF&(addr>>16),0xFF&(addr>>8),0xFF&(addr>>0),0x00,0x00,0x00]
        self.mcp2210.SPI_WRITE(wdata)
        rdata = self.mcp2210.SPI_READ()
        return rdata[5]<<8 |rdata[4]<<0  
    def FT810_SPI_HOST_MEM_READ8(self,addr):
        self.mcp2210.ByteLength = 0x05
        self.mcp2210.SPI_Setup()
        wdata = [0xFF&(addr>>16),0xFF&(addr>>8),0xFF&(addr>>0),0x00,0x00]
        self.mcp2210.SPI_WRITE(wdata)
        rdata = self.mcp2210.SPI_READ()
        return rdata[4]<<0  

    def FT810_SPI_HOST_MEM_WRITE32(self,addr,data):
        self.mcp2210.ByteLength = 0x07
        self.mcp2210.SPI_Setup()
        addr = addr | 0x00800000
        wdata = [0xFF&(addr>>16),0xFF&(addr>>8),0xFF&(addr>>0),0xFF&(data>>0),0xFF&(data>>8),0xFF&(data>>16),0xFF&(data>>24)]
        self.mcp2210.SPI_WRITE(wdata)
        #rdata = self.mcp2210.SPI_READ()
    def FT810_SPI_HOST_MEM_WRITE16(self,addr,data):
        self.mcp2210.ByteLength = 0x05
        self.mcp2210.SPI_Setup()
        addr = addr | 0x00800000
        wdata = [0xFF&(addr>>16),0xFF&(addr>>8),0xFF&(addr>>0),0xFF&(data>>0),0xFF&(data>>8)]
        self.mcp2210.SPI_WRITE(wdata)
        #rdata = self.mcp2210.SPI_READ()
    def FT810_SPI_HOST_MEM_WRITE8(self,addr,data):
        self.mcp2210.ByteLength = 0x04
        self.mcp2210.SPI_Setup()
        addr = addr | 0x00800000
        wdata = [0xFF&(addr>>16),0xFF&(addr>>8),0xFF&(addr>>0),0xFF&(data>>0)]
        self.mcp2210.SPI_WRITE(wdata)
        #rdata = self.mcp2210.SPI_READ()

    def FT810_SPI_HOST_COMMAND(self,d1st,d2nd,d3rd):
        self.mcp2210.ByteLength = 0x03
        self.mcp2210.SPI_Setup()
        wdata = [d1st,d2nd,d3rd]
        self.mcp2210.SPI_WRITE(wdata)
        
    def incCMDOffset(self,currentOffset,commandSize):
        newOffset = currentOffset + commandSize
        if(newOffset > 4095):
            newOffset = (newOffset - 4096)
        return newOffset
    def WaitCmdfifo_empty(self):
        cmdBufferRd = self.FT810_SPI_HOST_MEM_READ16(FT810Reg.REG_CMD_READ)
        cmdBufferWr = self.FT810_SPI_HOST_MEM_READ16(FT810Reg.REG_CMD_WRITE)
        while (cmdBufferWr != cmdBufferRd):       
           cmdBufferRd = self.FT810_SPI_HOST_MEM_READ16(FT810Reg.REG_CMD_READ)
           cmdBufferWr = self.FT810_SPI_HOST_MEM_READ16(FT810Reg.REG_CMD_WRITE)
        return  cmdBufferWr

    def FT810_Frame_Start_CMD(self,color,cmdOffset):
        self.FT810_SPI_HOST_MEM_WRITE32(FT810Reg.RAM_CMD + cmdOffset, (FT810Reg.CMD_DLSTART))
        cmdOffset = self.incCMDOffset(cmdOffset, 4)
        self.FT810_SPI_HOST_MEM_WRITE32(FT810Reg.RAM_CMD + cmdOffset, (FT810Reg.DL_CLEAR_RGB | (0x00FFFFFF&color)))
        cmdOffset = self.incCMDOffset(cmdOffset, 4)
        self.FT810_SPI_HOST_MEM_WRITE32(FT810Reg.RAM_CMD + cmdOffset, (FT810Reg.DL_CLEAR | FT810Reg.CLR_COL | FT810Reg.CLR_STN | FT810Reg.CLR_TAG))
        cmdOffset = self.incCMDOffset(cmdOffset, 4)
        return cmdOffset
        
    def FT810_Frame_End_CMD(self,cmdOffset):
        self.FT810_SPI_HOST_MEM_WRITE32(FT810Reg.RAM_CMD + cmdOffset, (FT810Reg.DL_END))
        cmdOffset = self.incCMDOffset(cmdOffset, 4)
        self.FT810_SPI_HOST_MEM_WRITE32(FT810Reg.RAM_CMD + cmdOffset, (FT810Reg.DL_DISPLAY))
        cmdOffset = self.incCMDOffset(cmdOffset, 4)
        self.FT810_SPI_HOST_MEM_WRITE32(FT810Reg.RAM_CMD + cmdOffset, (FT810Reg.CMD_SWAP))
        cmdOffset = self.incCMDOffset(cmdOffset, 4)
        self.FT810_SPI_HOST_MEM_WRITE16(FT810Reg.REG_CMD_WRITE, (cmdOffset))
        cmdOffset = self.incCMDOffset(cmdOffset, 2)
        return cmdOffset
