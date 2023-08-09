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
        weekday = 3

        if message.author == self.user:
            return # if the previous message was itself: stop
        
        if message.content == "?NAschedule":
            print("NA Schedule Request") #confirmation of a Schedule Request
            RegionSearchCon  = "NA" #set the search condition for the region
            RegionSearchVal = [r for r in wks.get_all_values() if r[5]== RegionSearchCon] #look for all rows with the RegionSearchCon in that column. Store as list.
            print(RegionSearchVal)
            '''for r in RegionSearchVal():
                lolembed = discord.Embed(title = "{weekday} NA TOURNAMENT TIMES", colour = None)
                lolembed.add_field(name= "Work In Progres", value = r)
                await message.channel.send(embed=lolembed)'''
            if weekday == 0:
                print()
                

            elif weekday == 1:
                print()
            elif weekday == 2:
                print() 

            elif weekday == 3: # if it is Thursday (im adding the other days later)
                scheduleEmbed = discord.Embed (title = "Thursday Tournament Times", colour = None) # create embed
                scheduleEmbed.add_field(name = wks.acell('B29').value, value = wks.acell('C29').value)
                scheduleEmbed.add_field(name = wks.acell('B32').value, value = wks.acell("C32").value, inline=False)
                await message.channel.send(embed=scheduleEmbed) # send embed to discords
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
        if message.content == "?EMEAschedule":
            print("EMEA Schedule Request") #confirmation of a schedule request
            RegionSearchCon = "EMEA" #set the search condition for the region
            RegionSearchVal = [r for r in wks.get_all_values() if r[7] == RegionSearchCon]
            embed = discord.Embed(title = "EMEA TOURNAMENT TIMES", colour = None)
            embed.add_field(name= "Work In Progres", value = "I'm working on it") #look for all rows with the RegionSearchCon in that column. Store as list.
            await message.channel.send(embed=embed) 

        if message.content == "?hawkeyeball":
            print("Hawkeyeball")
            nocommandembed = discord.Embed(title = "Hawkeyeball", colour=None)
            nocommandembed.set_thumbnail(url="https://media.discordapp.net/attachments/993612030483365969/1138660307418497054/New_Project.png?width=662&height=662")
            nocommandembed.set_image(url = "https://media.discordapp.net/attachments/993612030483365969/1138660307418497054/New_Project.png?width=662&height=662")
            nocommandembed.add_field(name = "Hawkeyeball", value = "Hawkeyeball")
            await message.channel.send(embed = nocommandembed)
            


    

intents = discord.Intents.default()
intents.message_content = True # funny discord thing DO NOT TOUCH

client = MyClient(intents=intents)
client.run('MTEzNjA5MDk0MDY3NTczOTY3OQ.GKgTsf.u6-XcugDYTQwbI_7ckl1wcmiv0YLiz1H6Gu8-4') # Code to actually have the bot run
