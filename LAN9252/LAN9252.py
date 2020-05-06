from PyMCP2210 import PyMCP2210
from LAN9252 import LAN9252Reg

import hid
# pip install hidapi
# https://github.com/trezor/cython-hidapi
import time

class LAN9252:
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
        self.mcp2210.GPIO_GP7_Value(1)
    def LAN925X_SPI_READ(self,addr):
        self.mcp2210.ByteLength = 0x07
        self.mcp2210.SPI_Setup()
        wdata = [0x03,0xFF&(addr>>8),0xFF&(addr>>0),0x00,0x00,0x00,0x00]
        self.mcp2210.SPI_WRITE(wdata)
        rdata =self.mcp2210.SPI_READ()[3:7]
        return rdata[3]<<24 |rdata[2]<<16 |rdata[1]<<8 |rdata[0]<<0  
    def LAN925X_SPI_WRITE(self,addr,data):
        self.mcp2210.ByteLength = 0x07
        self.mcp2210.SPI_Setup()
        wdata = [0x02,0xFF&(addr>>8),0xFF&(addr>>0),0xFF&(data>>0),0xFF&(data>>8),0xFF&(data>>16),0xFF&(data>>24)]
        self.mcp2210.SPI_WRITE(wdata)
    #=============================================================================#
    # LAN9252 RESET
    #=============================================================================#
    def LAN9252_RESET(self):
        addr = LAN9252Reg.RESET_CTL
        self.LAN925X_SPI_WRITE(addr,LAN9252Reg.ETHERCAT_RST)
        addr = LAN9252Reg.BYTE_TEST
        rdata = self.LAN925X_SPI_READ(addr)
        while(rdata!=0x87654321):
            addr = LAN9252Reg.BYTE_TEST
            rdata = LAN925X_SPI_READ(addr)

    #=============================================================================#
    # LAN9252 EtherCAT CSR WRITE
    #=============================================================================#
    def LAN9252_EtherCAT_CSR_WRITE(self,csr_size,csr_addr,csr_data):
        addr = LAN9252Reg.ECAT_CSR_DATA
        wdata = csr_data
        self.LAN925X_SPI_WRITE(addr,wdata)
        addr = LAN9252Reg.ECAT_CSR_CMD
        wdata = LAN9252Reg.CSR_BUSY | 0 | csr_size<<16 | csr_addr 
        self.LAN925X_SPI_WRITE(addr,wdata)
        rdata = self.LAN925X_SPI_READ(addr)
        while(LAN9252Reg.CSR_BUSY&rdata):
            addr = LAN9252Reg.ECAT_CSR_CMD
            rdata = self.LAN925X_SPI_READ(addr)
    #=============================================================================#
    # LAN9252 EtherCAT CSR READ
    #=============================================================================#
    def LAN9252_EtherCAT_CSR_READ(self,csr_size,csr_addr):
        addr = LAN9252Reg.ECAT_CSR_CMD
        wdata = LAN9252Reg.CSR_BUSY | 1<<30 | csr_size<<16 | csr_addr
        self.LAN925X_SPI_WRITE(addr,wdata)
        addr = LAN9252Reg.ECAT_CSR_CMD
        rdata = self.LAN925X_SPI_READ(addr)
        while(LAN9252Reg.CSR_BUSY&rdata):
            addr = LAN9252Reg.ECAT_CSR_CMD
            rdata = LAN925X_SPI_READ(addr)
        addr = LAN9252Reg.ECAT_CSR_DATA
        rdata = self.LAN925X_SPI_READ(addr)
        return rdata

    #=============================================================================#
    # LAN9252 EtherCAT Prossec RAM Read
    #=============================================================================#
    def LAN9252_EtherCAT_PRAM_READ(self,pram_read_len,pram_read_addr):
        addr = LAN9252Reg.ECAT_PRAM_RD_ADDR_LEN
        wdata = pram_read_len<<16 | pram_read_addr 
        LAN925X_SPI_WRITE(addr,wdata)

        addr = LAN9252Reg.ECAT_PRAM_RD_CMD
        wdata = LAN9252Reg.PRAM_READ_BUSY  
        LAN925X_SPI_WRITE(addr,wdata)

        addr = LAN9252Reg.ECAT_PRAM_RD_DATA
        rdata = LAN925X_SPI_READ(addr)

        addr = LAN9252Reg.ECAT_PRAM_RD_CMD
        tmp = LAN925X_SPI_READ(addr)
        while(LAN9252Reg.PRAM_READ_BUSY&tmp):
            addr = LAN9252Reg.ECAT_PRAM_RD_CMD
            tmp = LAN925X_SPI_READ(addr)
        return rdata

    #=============================================================================#
    # LAN9252 EtherCAT Prossec RAM WRITE
    #=============================================================================#
    def LAN9252_EtherCAT_PRAM_WRITE(self,pram_read_len,pram_read_addr,pram_wr_data):
        addr = LAN9252Reg.ECAT_PRAM_WR_DATA
        wdata = LAN9252Reg.PRAM_READ_BUSY  
        LAN925X_SPI_WRITE(addr,wdata)

        addr = LAN9252Reg.ECAT_PRAM_WR_ADDR_LEN
        wdata = pram_read_len<<16 | pram_read_addr 
        LAN925X_SPI_WRITE(addr,wdata)

        addr = LAN9252Reg.ECAT_PRAM_RD_CMD
        wdata = LAN9252Reg.PRAM_READ_BUSY  
        LAN925X_SPI_WRITE(addr,wdata)

        addr = LAN9252Reg.ECAT_PRAM_RD_CMD
        tmp = LAN925X_SPI_READ(addr)
        while(LAN9252Reg.PRAM_READ_BUSY&tmp):
            addr = LAN9252Reg.ECAT_PRAM_RD_CMD
            tmp = LAN925X_SPI_READ(addr)

'''
//=============================================================================//
// LAN9252 EtherCAT Prossec RAM Read
//=============================================================================//
void LAN9252_EtherCAT_PRAM_WRITE(uint16_t PRAM_WRITE_LEN,uint16_t PRAM_WRITE_ADDR, uint32_t PRAM_WR_DATA)
{
    uint32_t rdata;
    uint32_t wdata;
    uint32_t tmp;
    uint16_t addr;

    
    addr = ECAT_PRAM_WR_DATA;
    wdata = PRAM_WR_DATA; 
    LAN925X_SPI_WRITE(addr,wdata);
    
    addr = ECAT_PRAM_WR_ADDR_LEN;
    wdata = PRAM_WRITE_LEN<<16 | PRAM_WRITE_ADDR; 
    LAN925X_SPI_WRITE(addr,wdata);

    addr = ECAT_PRAM_WR_CMD;
    wdata = PRAM_WRITE_BUSY ; 
    LAN925X_SPI_WRITE(addr,wdata);

    addr = ECAT_PRAM_WR_CMD;
    tmp = LAN925X_SPI_READ(addr);
    while(PRAM_WRITE_BUSY&tmp)
    {
        addr = ECAT_PRAM_WR_CMD;
        tmp = LAN925X_SPI_READ(addr);
    }
}

'''