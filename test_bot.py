import discord

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        
        if message.author == 'itsmarcotime':
            await message.content.send("Greetings my creator! Hope all is well.")
        else:
            await message.channel.send("Hello! I am Marco's test bot.")


client.run('MTE5ODQ5NDMzNDY0ODA3MDIzNg.GJ7eLP.BsnDlGE2jV4zoUm5lA9H6copq9GXcKUI6bUQ7A')

