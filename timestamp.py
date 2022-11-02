import sys
import time


def toDateString(timeStamp):
    timeArray: object = time.localtime(timeStamp)
    otherStyleTime: str = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


length: int = 13

try:
    timeStamp = int(sys.argv[1])
    #timeStamp: str = int("1667291607827")
    length: int = len(str(timeStamp))
    if length != 13 and length != 10:
        print("时间戳只能是10位或者13位整数,当前长度：" + str(length))
    elif length == 13:
        timeStamp = timeStamp / 1000
    print(toDateString(timeStamp))
except Exception as e:
    print("只能输入数字", e)
