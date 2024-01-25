import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)

@client.command()
async def hello(ctx, *args):
    for arg in args:
        await ctx.send(arg)

client.run('MTE5ODQ5NDMzNDY0ODA3MDIzNg.GJ7eLP.BsnDlGE2jV4zoUm5lA9H6copq9GXcKUI6bUQ7A')