"""
this is the basic layout for the main file. 
This will be outside of any folder, besides the main directory
where all the other folders for you bot will be

cogs will be kept in a seperate file named "cogs"
cogs are used to organize code with seperate files and classes
"""
import discord #obviously
from discord.ext import commands
""" this allows you to create more advanced functions.
you will do async def command_name() and the command_name will be what you call after 
command_prefix """

import os 
# this allows python to interact with your operating system
# this sounds incredibly intimadating, however it is only used here to find the cogs folder
import asyncio # 

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) 
# intents gives your bot permissions
# the command prefix is what you start out non-slash commands with

@bot.event
async def on_ready(): # this is NOT a command, it just prints when your bot is working
    print(f'We have logged in as {bot.user}')
    # this syncs all the slash commands you have made in the cogs folder
    # it will print the number of commands that have synced, or if an error occurs it will print the error
    try: 
        syncCommands = await bot.tree.sync()
        print(f"{len(syncCommands)} commands have been synced")
    except Exception as e:
        print("An error with syncing commands has occured:", e)

""" create a file with your token called "token.txt"
NEVER share your token with anyone, as it is how the program connects with 
your bot """
with open('token.txt') as file:
    token = file.read() # this reads the file and assigns it to a value called 'token'

async def load():
    for file in os.listdir("./cogs"): #searches through cogs folder
        if file.endswith(".py"): #finds python files
            await bot.load_extension(f"cogs.{file[:-3]}") # loads all the .py files as extensions


async def main():
    async with bot:
        await load() # runs the load() function, so loads your cogs
        await bot.start(token) # starts the bot that has your token (your bot)
        
# this starts running your project
asyncio.run(main()) 