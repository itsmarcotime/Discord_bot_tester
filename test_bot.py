import discord 

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    message.content.lower()

    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hello! I am Marco's test bot.")


client.run('')

