import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('\t- General is loaded')


    @commands.command()
    async def ver(self, ctx):
        await ctx.send("CodezoneBOT VERSION: 1.01")

    @commands.command()
    async def patch(self, ctx):
        await ctx.send("CodezoneBOT VERSION: 1.01\n\n"
                       "COMMANDS:\n"
                       "1. Changed command \"hello\"\n\t\t"
                       "- prints the users name after\n"
                       "2. Changed Error message of command \"tconvert\"\n"
                       "\t\t- Added users name in the message\n"
                       "3. Added a welcome user event\n"
                       "4. Added a user leaving/kicked/removed event\n"
                       "5. Added a command \"tlive\"\n\t\t"
                       "- mentions everyone that you are live on twitch and links it\n\n"
                       "MISC:\n"
                       "1. Added categories in command \"help\"\n"
                       "2. Removed non commands in the help command")


    @commands.command(name="hello")
    async def hello(self, ctx):
        user = str(ctx.message.author)

        await ctx.send(f"Hi {user[:-5]}")

    @commands.command(name="tlive")
    async def live(self, ctx, username):
        user = str(ctx.message.author)
        message = f"@everyone  @{user[:-5]} is now live on twitch. Come check them out here:\n"
        twitch = f"https://www.twitch.tv/{username}"
        result = message + twitch
        await ctx.send(result)


def setup(client):
    client.add_cog(General(client))
