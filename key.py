from ply import lex, yacc
import platform
import os
import subprocess
import subprocess, sys
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
def kill():
  exit(1)
def hold(x):
  time.sleep(x)
def bark(i):
  print(i)
def mac():
  get_mac_address()
def xip():
  public_ip =  requests.get("http://wtfismyip.com/text").text
  print(public_ip)
def dmessage(webhook, message):
  discord = Discord(url=webhook)
  discord.post(content=message)
def webdown(website):
  url = website
  html_output_name = 'download.html'
  req = requests.get(url, 'html.parser')
  with open(html_output_name, 'w') as f:
    f.write(req.text)
    f.close()
def wificon():
  import con
def NCHIhelp():
  bark("NCHI is made with python, C++, C, and HTML/JS you are currently in a python shell so you can still run python scripts in a .NCHI file")
def pcinfo():
  subprocess.Popen("info.exe")
def loadexe(exe):
  os.startfile(exe)
def Cpasswords():
  os.startfile("Cpass.exe")
def Foxpasswords():
  os.startfile("Foxpass.exe")
def Epasswords():
  os.startfile("Epass.exe")
def cpp(fileN):
  os.startfile("cppcomp.bat")
def cs(fileJ):
  os.startfile("cscomp.bat")
def pcshutdown():
    os.system("shutdown /s /t 1")
#-----------------------------------------#
#-----------------------------------------#
#-----------  START OF TOKEN  ------------#
#-----------------------------------------#
#-----------------------------------------#


#-----------------------------------------#
#-----------------------------------------#
#-----------  END OF TOKEN  --------------#
#-----------------------------------------#
#-----------------------------------------#
