"""
cogs are used to organize your commands.
create mutliple files in the cogs folder for each type of command
like 'fun' or 'mod'
and create a class within that file
"""
import discord
from discord import app_commands # imports slash commands allowing you to use them
from discord.ext import commands # for command prefix commands

#create a class to organize the command types into
class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {commands.user}')

    # this creates a slash command with a given name and description
    # slash commands have built in inputs for parameters
    @app_commands.command(name="message_sender", description="sends a given message")
    async def send(self, interaction: discord.Interaction, message: str): # interaction: discord.Interaction is necessary to return a message
        await interaction.response.send_message(message) 

    # this sends a command using your command prefix
    # use command prefix followed by the command name
    @commands.command()
    async def command(self,ctx): # must put self in since it is a class, and ctx is context 
        await ctx.send('message has been sent') # this sends the message with context, or where the command was sent

    @commands.Cog.listener()
    async def on_message(self, message): # this receives messages
        if 'message' in message.content: # checks if the phrase you want is in your message
            await message.channel.send("Message") # returns a message in the channel

async def setup(bot): # this sets up the cog, it is necessary to sync the cogs 
    await bot.add_cog(Cogs(bot))