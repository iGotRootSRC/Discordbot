import os
from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv
from itertools import cycle

# Load discord token from .env file
# remember pip3 install python-dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot prefix for commands
client = commands.Bot(command_prefix = '!') # Not using this yet
# Status cycles
status = cycle(['Byggemand bob', 'Bygger byen'])

# On bot ready start task change_status and print in console
@client.event
async def on_ready():
    change_status.start()
    print('Bot\'s runnin motherfucker')

# define task change_status
@tasks.loop(seconds=5)
async def change_status():
        await client.change_presence(activity=discord.Game(next(status)))

# Event handler that reacts on specific messages in specific channels
@client.event
async def on_message(message):
        # Define strings
        # Channels the bot listens in for '!whitelist' and '!support'
        channels =["whitelist-skriv", "💬support-skriv💬"]
        # Canned speeches for the bot to reference 
        whitelist = 'Hvem afventer whitelist: {0.author.mention} \n\n Du har orienteret en <@&698964223543214140> om du afventer whitelist. \n \n Du bedes have tålmodighed, da der kan forkomme ventetid til tider.'.format(message)
        support = '<@&698964221982933012> <@&698964221114843177> <@&698964220540092467> \n\n Sidder i afventer support: {0.author.mention} \n\n Du bedes vente på at en staff er ledig.'.format(message)
        # Get group id's by doing \@Admin in discord chat for example
        
        # Make sure we are not writing to ourself LOL - kinda dumb
        if message.author == client.user:
                return
        
        if str(message.channel) in channels:
            if message.content.startswith('!whitelist'):
                await message.channel.send(whitelist)
            elif message.content.startswith('!support'):
                await message.channel.send(support)
client.run(TOKEN)
