from FT810 import FT810 
from FT810 import FT810Reg
import time
ft810 = FT810.FT810()

ft810.FT810_SPI_HOST_COMMAND(FT810Reg.HOST_CORERST,0x000,0x000)
time.sleep(0.1)
ft810.FT810_SPI_HOST_COMMAND(FT810Reg.HOST_PWRDOWN,0x000,0x000)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_CPURESET,0x000003)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_CPURESET,0x000000)
time.sleep(0.1)

ft810.FT810_SPI_HOST_COMMAND(FT810Reg.HOST_CLKINT,0x000,0x000)
ft810.FT810_SPI_HOST_COMMAND(FT810Reg.HOST_ACTIVE,0x000,0x000)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_PWM_DUTY,0x000000)
time.sleep(0.1)

ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_PCLK,7)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_HSIZE,480)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_HCYCLE,531)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_HOFFSET,51)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_HSYNC0,8)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_HSYNC1,43)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_VSIZE,272)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_VCYCLE,288)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_VOFFSET,12)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_VSYNC0,4)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_VSYNC1,14)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_SWIZZLE,0)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_PCLK_POL,1)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_GPIO_DIR,0x80)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_GPIO,0x80)
ft810.FT810_SPI_HOST_MEM_WRITE8(FT810Reg.REG_PWM_DUTY,0x40)
time.sleep(0.1)

cmdOffset = ft810.WaitCmdfifo_empty()
cmdOffset = ft810.FT810_Frame_Start_CMD(0x8188FF,cmdOffset); 

ft810.FT810_SPI_HOST_MEM_WRITE32( FT810Reg.RAM_CMD + cmdOffset, (FT810Reg.CMD_LOGO));
cmdOffset = ft810.incCMDOffset(cmdOffset, 4);

cmdOffset = ft810.FT810_Frame_End_CMD(cmdOffset);
cmdOffset = ft810.WaitCmdfifo_empty();

rdata = ft810.FT810_SPI_HOST_MEM_READ8(FT810Reg.REG_CHIP_ID)
print ("[REG_CHIP_ID]: 0x{:02x}".format(rdata))
rdata = ft810.FT810_SPI_HOST_MEM_READ8(FT810Reg.REG_ID)
print ("[REG_ID]: 0x{:02x}".format(rdata))

