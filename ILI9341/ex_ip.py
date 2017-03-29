
import time
import ILI9341
import commands



sysIP = commands.getoutput("hostname -I")

ILI9341.INIT()
ILI9341.CLS3()
ILI9341.Text_16(0,0,"IP:",ILI9341.GREEN,ILI9341.BLACK)
ILI9341.Text_16(16*3 + 2 ,0,str(sysIP),ILI9341.WHITE,ILI9341.BLACK)

