#!/usr/bin/env python3
import qrcode

img = qrcode.make("https://aranjan21cloudtech.com")
img.save("mywebsite.png")
