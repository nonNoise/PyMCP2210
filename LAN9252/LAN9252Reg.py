

ECAT_PRAM_RD_DATA                      = 0x000
ECAT_PRAM_WR_DATA                      = 0x020
ID_REV                                 = 0x050
IRQ_CFG                                = 0x054
INT_STS                                = 0x058
INT_EN                                 = 0x05C
BYTE_TEST                              = 0x064
HW_CFG                                 = 0x074
PMT_CTRL                               = 0x084
GPT_CFG                                = 0x08C
GPT_CNT                                = 0x090
FREE_RUN                               = 0x09C
RESET_CTL                              = 0x1F8
ETHERCAT_RST                           = 0x40
PHY_B_RST                              = 0x04
PHY_A_RST                              = 0x02
DIGITAL_RST                            = 0x01
ECAT_CSR_DATA                          = 0x300
ECAT_CSR_CMD                           = 0x304
CSR_BUSY                               = 1<<31
CSR_SIZE_8bit                          = 1
CSR_SIZE_16bit                         = 2
CSR_SIZE_32bit                         = 4
ECAT_PRAM_RD_ADDR_LEN                  = 0x308
ECAT_PRAM_RD_CMD                       = 0x30C
ECAT_PRAM_WR_ADDR_LEN                  = 0x310
ECAT_PRAM_WR_CMD                       = 0x314
PRAM_READ_BUSY                         = 1<<31
PRAM_READ_ABORT                        = 1<<30
PRAM_WRITE_BUSY                        =  1<<31
PRAM_WRITE_ABORT                       = 1<<30
#-----------------------------------------------------------------------#
# ESC Information
#-----------------------------------------------------------------------#
Type_Register                          = 0x0000
Revision_Register                      = 0x0001
Build_Register                         = 0x0002
FMMUs_Supported                        = 0x0004
SyncManagers_Supported                 = 0x0005
RAM_Size                               = 0x0006
Port_Descriptor                        = 0x0007
ESC_Features_Supported                 = 0x0008
#-----------------------------------------------------------------------#
# Station Address
#-----------------------------------------------------------------------#
Configured_Station                     = 0x0010
Configured_Station_Alias               = 0x0012
#-----------------------------------------------------------------------#
# Write Protection
#-----------------------------------------------------------------------#
Write_Enable                           = 0x0020
Write_Protection                       = 0x0021
ESC_Write_Enable                       = 0x0030
ESC_Write_Protection                   = 0x0031
#-----------------------------------------------------------------------#
# Data Link Layer
#-----------------------------------------------------------------------#
ESC_Reset_ECAT                         = 0x0040
ESC_Reset_PDI                          = 0x0041
ESC_DL_Control                         = 0x0100
Physical_Read_Write_Offset             = 0x0108
ESC_DL_Status                          = 0x0110
#-----------------------------------------------------------------------#
# Application Layer
#-----------------------------------------------------------------------#
AL_Control                             = 0x0120
AL_Status                              = 0x0130
AL_Status_Code                         = 0x0134
RUN_LED_Override                       = 0x0138
#-----------------------------------------------------------------------#
# PDI (Process Data Interface)
#-----------------------------------------------------------------------#
PDI_Control                            = 0x0140
ESC_Configuration                      = 0x0141
ASIC_Configuration                     = 0x0142
PDI_Configuration                      = 0x0150
Sync_Latch_PDI_Configuration           = 0x0151
Extended_PDI_Configuration             = 0x0152
#-----------------------------------------------------------------------#
#Interrupts
#-----------------------------------------------------------------------#
ECAT_Event_Mask                        = 0x0200
AL_Event_Mask                          = 0x0204
ECAT_Event_Request                     = 0x0210
AL_Event_Request                       = 0x0220
#-----------------------------------------------------------------------#
# Error Counters
#-----------------------------------------------------------------------#
RX_Error_Counters                      = 0x0300
Forwarded_RX_Error_Counters            = 0x0308
ECAT_Processing_Unit_Error_Counter     = 0x030C
PDI_Error_Counter                      = 0x030D
PDI_Error_Code                         = 0x030E
Lost_Link_Counters                     = 0x0310
#-----------------------------------------------------------------------#
# Watchdogs
#-----------------------------------------------------------------------#
Watchdog_Time_PDI                      = 0x0410
Watchdog_Time_Process_Data             = 0x0420
Watchdog_Status_Process_Data           = 0x0440
Watchdog_Counter_Process_Data          = 0x0442
Watchdog_Counter_PDI                   = 0x0443
#-----------------------------------------------------------------------#
# EEPROM Interface
#-----------------------------------------------------------------------#
EEPROM_Configuration                   = 0x0500
EEPROM_PDI_Access_State                = 0x0501
EEPROM_Control_Status                  = 0x0502
EEPROM_Address                         = 0x0504
EEPROM_Data                            = 0x0508
#-----------------------------------------------------------------------#
# MII Management Interface
#-----------------------------------------------------------------------#
MII_Management_Control_Status          = 0x0510
PHY_Address                            = 0x0512
PHY_Register_Address                   = 0x0513
PHY_DATA                               = 0x0514
MII_Management_ECAT_Access_State       = 0x0516
MII_Management_PDI_Access_State        = 0x0517
PHY_Port_Statuss                       = 0x0518

"""
0600h FMMU[2:0]s (3x16 bytes)
+0h-3h FMMUx Logical Start Address
+4h-5h FMMUx Length
+6h FMMUx Logical Start Bit
+7h FMMUx Logical Stop Bit
+8h-9h FMMUx Physical Start Address
+Ah FMMUx Physical Start Bit
+Bh FMMUx Type
+Ch FMMUx Activate
+Dh-Fh FMMUx Reserved
0800h-081Fh SyncManager[3:0]s (4x8 bytes)
+0h-1h SyncManager x Physical Start Address
+2h-3h SyncManager x Length
+4h SyncManager x Control
+5h SyncManager x Status
+6h SyncManager x Activate
+7h SyncManager x PDI Control
"""
#-----------------------------------------------------------------------#
# Distributed Clocks - Receive Times
#-----------------------------------------------------------------------#
Receive_Time_Port_0                     = 0x0900
Receive_Time_Port_1                     = 0x0904
Receive_Time_Port_2                     = 0x0908
#-----------------------------------------------------------------------#
#Distributed Clocks - Time Loop Control Unit
#-----------------------------------------------------------------------#
System_Time                             = 0x0910
Receive_Time_ECAT_Processing_Unit       = 0x0918
System_Time_Offset                      = 0x0920
System_Time_Delay                       = 0x0928
System_Time_Difference                  = 0x092C
Speed_Counter_Start                     = 0x0930
Speed_Counter_Diff                      = 0x0932
System_Time_Difference_Filter_Depth     = 0x0934
Speed_Counter_Filter_Depth              = 0x0935
#-----------------------------------------------------------------------#
# Distributed Clocks - Cyclic Unit Control
#-----------------------------------------------------------------------#
Cyclic_Unit_Control                     = 0x0980
#-----------------------------------------------------------------------#
# Distributed Clocks - SYNC Out Unit
#-----------------------------------------------------------------------#
Activation                              = 0x0981
Pulse_Length_of_SyncSignals             = 0x0982
Activation_Status                       = 0x0984
SYNC0_Status                            = 0x098E
SYNC1_Status                            = 0x098F
Start_Time_Cyclic_Operation             = 0x0990
Next_SYNC1_Pulse                        = 0x0998
SYNC0_Cycle_Time                        = 0x09A0
SYNC1_Cycle_Time                        = 0x09A4
#-----------------------------------------------------------------------#
# Distributed Clocks - Latch In Unit
#-----------------------------------------------------------------------#
LATCH0_Control                          = 0x09A8
LATCH1_Control                          = 0x09A9
LATCH0_Status                           = 0x09AE
LATCH1_Status                           = 0x09AF
LATCH0_Time_Positive_Edge               = 0x09B0
LATCH0_Time_Negative_Edge               = 0x09B8
LATCH1_Time_Positive_Edge               = 0x09C0
LATCH1_Time_Negative_Edge               = 0x09C8
#-----------------------------------------------------------------------#
# Distributed Clocks - SyncManager Event Times
#-----------------------------------------------------------------------#
EtherCAT_Buffer_Change_Event_Time       = 0x09F0
PDI_Buffer_Start_Time_Event             = 0x09F8
PDI_Buffer_Change_Event_Time            = 0x09FC
#-----------------------------------------------------------------------#
# ESC Specific
#-----------------------------------------------------------------------#
Product_ID                              = 0x0E00
Vendor_ID                               = 0x0E08
#-----------------------------------------------------------------------#
# Digital Input/Output
#-----------------------------------------------------------------------#
Digital_IO_Output_Data                  = 0x0F00
General_Purpose_Output                  = 0x0F10
General_Purpose_Input                   = 0x0F18
#-----------------------------------------------------------------------#
# User RAM
#-----------------------------------------------------------------------#
User_RAM                                = 0x0F80
#-----------------------------------------------------------------------#
# Process Data RAM
#-----------------------------------------------------------------------#
Process_Data_RAM                        = 0x1000    

