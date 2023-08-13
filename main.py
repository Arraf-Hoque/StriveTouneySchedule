# Among Us Sus Deez Nuts


"""
Hi, Its CptnHawkeye with the NAFGC Discord Bot. 

Daily log: so i got filtering working but the problem is i have no idea how to actually get it to work within the embed.
Im at a complete loss and ill need to ask cfresh or someone in the morning.
"""
# Work Log so i can remember what i did(im very forgetful)



import discord
from datetime import datetime
import gspread
from discord.ext import commands
from discord import Colour
import numpy as np 
import random as rand

sa = gspread.service_account(filename="creds.json")

sh = sa.open("NA/EMEA GGST/SF6 Online Tourney Times")

wks = sh.worksheet("Sheet1")

class MyClient(discord.Client):

    now  = datetime.now()
    weekday = 3
    async def on_ready(self):
        print(f'Logged on as {self.user}!') #notif that loggin was successful

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        

    async def on_message(self, message):
        now  = datetime.now()
        weekday = now.strftime('%A')

        if message.author == self.user:
            return # if the previous message was itself: stop
        
        if message.content == "$schedule":
            print("NA Schedule Request") #confirmation of a Schedule Request
            RegionSearchCon  = "NA" #set the search condition for the region
            DaySearchCon = weekday
            NASearchVal = np.array([r for r in wks.get_all_values() if r[7] == DaySearchCon])
            print(DaySearchCon )
            lolembed = discord.Embed(title = weekday + " Tournament Times", colour = None)
            for row in NASearchVal:
                lolembed.add_field(name = row[1], value = "Start time: " + row[6] + "\nGame: " + row[4]+ "\n Region: " + row[5] + "\n [Bracket link](" + row[2] + ")", inline = False)
            lolembed.add_field(name = "Creator", value = "CptnHawkeye")
            await message.channel.send(embed=lolembed)
        '''if message.content == "?EMEAschedule":
            print("EMEA Schedule Request") #confirmation of a schedule request
            RegionSearchCon = "EMEA" #set the search condition for the region
            RegionSearchVal = [r for r in wks.get_all_values() if r[7] == RegionSearchCon]
            embed = discord.Embed(title = "EMEA TOURNAMENT TIMES", colour = None)
            embed.add_field(name= "Work In Progres", value = "I'm working on it") #look for all rows with the RegionSearchCon in that column. Store as list.
            await message.channel.send(embed=embed)''' 
 
        if message.content == "$hawkeyeball":
            print("Hawkeyeball")
            nocommandembed = discord.Embed(title = "Hawkeyeball", colour=None)
            nocommandembed.set_thumbnail(url="https://media.discordapp.net/attachments/993612030483365969/1138660307418497054/New_Project.png?width=662&height=662")
            nocommandembed.set_image(url = "https://media.discordapp.net/attachments/993612030483365969/1138660307418497054/New_Project.png?width=662&height=662")
            nocommandembed.add_field(name = "Hawkeyeball", value = "Hawkeyeball")
            nocommandembed.add_field(name = "Creator", value = "CptnHawkeye")
            await message.channel.send(embed = nocommandembed)
        if message.content == "$pinghawkeye":
            x = rand.randint(0,3)
            if x == 0:
                await message.channel.send("<@" + str(422548728248008716) + "> <- is cringe")
            elif x == 1:
                await message.channel.send("<@" + str(422548728248008716) + "> <- short mf")
            elif x == 2:
                await message.channel.send("<@" + str(422548728248008716) + ">")
            elif x == 3:
                await message.channel.send("<@" + str(422548728248008716) + "> <- dumbass")
        if message.content == "$help":
            teal = Colour.teal()
            helpEmbed = discord.Embed(title = "Bot Commands", colour = teal)
            helpEmbed.add_field(name = "Possible Commands", value = "$help \n $pinghawkeye \n $schedule \n $hawkeyeball",)
            helpEmbed.add_field(name = "Creator", value = "CptnHawkeye")
            await message.channel.send(embed = helpEmbed)
            


    

intents = discord.Intents.default()
intents.message_content = True # funny discord thing DO NOT TOUCH

client = MyClient(intents=intents)
client.run('MTEzNjA5MDk0MDY3NTczOTY3OQ.GKgTsf.u6-XcugDYTQwbI_7ckl1wcmiv0YLiz1H6Gu8-4') # Code to actually have the bot run