import os  
import traceback  
import discord  
from discord.ext import commands  

from grouping import MakeTeam  
import urllib.request
import json
import re

client = discord.Client()

@client.event
async def on_ready():
   print('login succeed!')
   print(client.user.name)
   print(client.user.id)
   print('------')

citycodes = {
    "青森": '020010',
    "静岡": '220010',
    "札幌": '016010',
    "仙台": '040010',
    "東京": '130010',
    "横浜": '140010',
    "名古屋": '230010',
    "大阪": '270000',
    "広島": '340010',
    "福岡": '400010',
    "鹿児島": '460010',
    "那覇": '471010'
}


##特定の言葉へメンションで返事
@client.event
async def on_message(message):
   if message.author != client.user:
       if message.content == "@ロボばたこ":
           msg1 = message.author.mention + "失せろ"
           print(msg1)
           await message.channel.send(msg1)
       if message.content == "失せた":
           msg2 = message.author.mention + "失せないで"
           print(msg2)
           await message.channel.send(msg2)
       if message.content == "らしい":
           msg3 = message.author.mention + " 興味ないね"
           print(msg3)
           await message.channel.send(msg3)
       reg_res = re.compile(u"ロボばたこ、(.+)の天気は？").search(message.content)
       if reg_res:

        if reg_res.group(1) in citycodes.keys():

          citycode = citycodes[reg_res.group(1)]
          resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
          resp = json.loads(resp.decode('utf-8'))
          msg9 = resp['location']['city']
          msg9 += "の天気は、\n"
          for f in resp['forecasts']:
            msg9 += f['dateLabel'] + "が" + f['telop'] + "\n"
          msg9 += "です。"

          await message.channel.send(message.author.mention + msg9)

        else:
          await message.channel.send("そこの天気はわかりません...")  

client.run("Mzk3MjczNTU0NTM5NzczOTUy.XqfIXQ.0KI7GZee27XY6gGcIl2WGrKudSc")
