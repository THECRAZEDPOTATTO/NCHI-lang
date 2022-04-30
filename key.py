from ply import lex, yacc
import platform
import subprocess
import json
import re
from flask import Flask, render_template
import psutil
import shutil
import urllib.request
import socket
from discordwebhook import Discord
from requests import get
import time
from getmac import get_mac_address
import requests
#---------package end------------------------#
def kill():
  exit(1)
def hold(x):
  time.sleep(x)
def bark(i):
  print(i)
#-------end of base packages-----------------#
def mac():
  get_mac_address()
def xip():
  public_ip =  requests.get("http://wtfismyip.com/text").text
  print(public_ip)
#------end of network------------------------#
def dmessage(webhook, message):
  discord = Discord(url=webhook)
  discord.post(content=message)
#----------end of message package------------#
def webdown(website):
  url = website
  html_output_name = 'download.html'
  req = requests.get(url, 'html.parser')
  with open(html_output_name, 'w') as f:
    f.write(req.text)
    f.close()
#------end of download page----------------#
def wificon():
  import con
def NCHIhelp():
  bark("NCHI is made with python, C++, C, and HTML/JS you are currently in a python shell so you can still run python scripts in a .NCHI file")
  #-----------end of help------------------#
def pcinfo():
  bark("WAITING ON OS")
#-----------------------------------------#
#-----------------------------------------#
#-----------  END OF TOKEN  --------------#
#-----------------------------------------#
#-----------------------------------------#

