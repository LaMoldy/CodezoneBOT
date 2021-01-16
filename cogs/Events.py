import discord
from discord import member, client
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("\t- Events have loaded")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(777661356836782091)
        message = f':grin:  Welcome {str(member)[:-5]} to the Codezone server  :grin:  '
        await channel.send(message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(777661356836782091)
        message = f':sob: {str(member)[:-5]} has left the server :sob:'
        await channel.send(message)


def setup(client):
    client.add_cog(Events(client))
