# -*- coding: UTF-8 -*-
import string
import sys

price = eval('1.017')  # eval(sys.argv[1])

buyNumber = 5000 / price / 100

buyNumber = (str(buyNumber).split(".")[0]) + "00"

message = "买入价格: " + str(price) + "\r\n" + "买入数量: " + buyNumber + "\r\n" + "卖出点: " + str(
    round((price + .008), 3)) + "\r\n" + "买入点: " + str(round((price - .008), 3))

print(message)
