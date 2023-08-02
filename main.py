# This example requires the 'message_content' intent.

import discord
from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == "?schedule":
            await message.channel.send("I'm working on it!")
     
    


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTEzNjA5MDk0MDY3NTczOTY3OQ.GoEGRo.2e6ciWBEiFQvG_zCNsouzup_LZHQgga2ON1jjE')
