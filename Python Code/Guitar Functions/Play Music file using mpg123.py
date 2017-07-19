import sys
import mpg123

filename = "badswap.wav"
player = subprocess.Popen(["mpg123", filename, '-q'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr.subprocess.PIPE)

while player.get_busy() == True:
    print ("playing file now")
    continue
