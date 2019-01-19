#import subprocess
from subprocess import call
import os
import sys
_command1 = 'sudo python /home/pi/SiriControl-System/Siri_Web_Control_Simple.py'
_arg1 = 'Foxtel'
_arg2 = 'Foxtel1\n'
test_string = "test string"

#cmd = ['/home/pi/SiriControl-System/Siri_Web_Control_Simple.py', 'Foxtel', 'null']
#subprocess.Popen(cmd).wait()

call (["bash","/home/pi/SiriControl-System/Siri_Web_Control_Simple.py",_arg1])

#exec("_command1","_arg1")
#exec("_command1","_arg1","_arg2")

#os.system('sh python /home/pi/SiriControl-System/Siri_Web_Control_Simple.py',_arg1,_arg2)
#subprocess.call(['/home/pi/SiriControl-System/Siri_Web_Control_Simple.py'])

#subprocess.call(_command1, "Foxtel")
#subprocess.call(["command1", "arg1", "arg2"])
#execfile('/home/pi/SiriControl-System/Siri_Web_Control_Simple.py','Foxtel\n')
print("-test sending to sending to Node Red-",_arg1)
print("\n")
#/home/pi/SiriControl-System
