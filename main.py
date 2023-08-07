# Among Us Sus Deez Nuts


"""
Hi, Its CptnHawkeye with the NAFGC Discord Bot. 
as of rn im a little stuck with gathering data from the sheet cuz i am unable to filter the 6th column (Region)
between EMEA and NA and seperating the 2 values. Since im unable to do that i am currently unable to group the Tournaments 
via day of the week. 
"""
# Work Log so i can remember what i did(im very forgetful)



import discord
from datetime import datetime
import gspread
from discord.ext import commands 


sa = gspread.service_account(filename="creds.json")

sh = sa.open("NA/EMEA GGST/SF6 Online Tourney Times")

wks = sh.worksheet("Sheet1")

class MyClient(discord.Client):
    now  = datetime.now()
    weekday = now.weekday()
    print("The Day of the week is: ", weekday) #shows what day it is today

    async def on_ready(self):
        print(f'Logged on as {self.user}!') #notif that loggin was successful

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
            
    async def on_message(self, message):
        now  = datetime.now()
        weekday = now.weekday() # finds out what day it is today (Monday = 0, Tuesday = 1 ...)
        
         # reads the exported CSV(google sheets) file

        if message.author == self.user:
            return # if the previous message was itself: stop
        
        if message.content == "?NAschedule": #if someone types "NASchedule"
            print("NA Command Sent!") #confirmation that the command worked (meant for troubleshooting)
            search  = "NA"
            values = [r for r in wks.get_all_values() if r[5]== search]
            if weekday == 0: #Monday
                searchday = "Monday"
                dayvalues = [r for r in wks.get_all_values() if r[4] == searchday]
                print(dayvalues)
            elif weekday == 1:
                print()
            elif weekday == 2:
                print()
            elif weekday == 3: # if it is Thursday (im adding the other days later)
                scheduleEmbed = discord.Embed (title = "Thursday Tournament Times", colour = None) # create embed
                scheduleEmbed.add_field(name = wks.acell('B29').value, value = wks.acell('C29').value)
                scheduleEmbed.add_field(name = wks.acell('B32').value, value = wks.acell("C32").value, inline=False)
                await message.channel.send(embed=scheduleEmbed) # send embed to discord
            elif weekday == 4: # if it is Friday
                scheduleEmbed = discord.Embed (title = "Friday Tournament Times", colour = None) # create embed
                scheduleEmbed.add_field(name = "9Moons strive", value = "holy shit it works")
                scheduleEmbed.add_field(name = "CptnHawkeyes Beginner Beatdown", value = "Start Time: <t:1690930800:t> \n [start.gg link](https://start.gg/beginner_beatdown)", inline=False)
                await message.channel.send(embed=scheduleEmbed) # send embed on discord

            elif weekday == 5: # if it is Saturday
                scheduleEmbed = discord.Embed (title = "Saturday Tournament Times", colour = None) # create embed
                scheduleEmbed.add_field(name = "9Moons strive", value = "[start.gg link](https://start.gg/9moonsGGST)")
                scheduleEmbed.add_field(name = "CptnHawkeyes Beginner Beatdown", value = "Start Time: <t:1690930800:t> \n [start.gg link](https://start.gg/beginner_beatdown)", inline=False)
                await message.channel.send(embed=scheduleEmbed) # Send the above embed to discord
            elif weekday == 6:
                print()
        else:
            return



intents = discord.Intents.default()
intents.message_content = True # funny discord thing DO NOT TOUCH

client = MyClient(intents=intents)
client.run('MTEzNjA5MDk0MDY3NTczOTY3OQ.GoEGRo.2e6ciWBEiFQvG_zCNsouzup_LZHQgga2ON1jjE') # Code to actually have the bot run
