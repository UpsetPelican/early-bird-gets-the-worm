from random import randint
import datetime
import time
#import secrets # Secret local shit
import requests

testURL="https://www.posttestserver.com/post.php"

now = datetime.datetime.now()
idGen = int(round(time.time() * 1000));
randmin = randint(10, 30)
payload = {}

payload["entryId"] = idGen
payload["clockEmployeeId"] = 666
payload["entryTime"] = "{}T07:{}:{}.000Z".format(now.strftime("%Y-%m-%d"),randmin,randint(1,59))

print "Sending request..."
req = requests.post(testURL,data=payload)
print req.text