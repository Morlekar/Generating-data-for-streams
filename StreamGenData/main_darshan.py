import random
import time
from rndstr import random_string
file = open("output.txt","w")

while True:
  file = open("output.txt","a")
  ts=time.time()
  timestamp=time.ctime(ts)
  file.write(timestamp)
  file.write("\t")
  file.write(random_string(9)) #Value in random_string specifies the lenght of EventId
  file.write("\t")
  file.write(str(random.uniform(1.0,50.0))) #Lower limit is 1 and upper limit is 50 for sensor value
  file.write("\n")
  time.sleep(1) #value in time.sleep tells us the delay after every reading in seconds
  file.close()

