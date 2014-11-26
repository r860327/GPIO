#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
# 设备URI
apiurl = 'http://api.yeelink.net/v1.0/device/10401/sensor/17373/datapoints/'
# 用户密码
apiheaders = {'U-ApiKey': '45d551044008252bb4e299e4c34294a3'}
while True:
    #发送请求
    r = requests.get(apiurl,headers=apiheaders)
    # 打印响应内容
    print(r.text)
    # 转换为字典类型 请注意 2.7.4版本使用r.json()
    led = r.json()
    # {'value':x} x=1打开状态，x=0关闭状态
    if led['value'] == 1:
        print("led on")
        GPIO.output(11, GPIO.HIGH)
    else:
        print("led off")
        GPIO.output(11, GPIO.LOW)
    # 延时5S
    time.sleep(2)

