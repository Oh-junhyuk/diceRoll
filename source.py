import discord
import random

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!diceroll"):
        channel = client.get_channel(852641956969316403)
        await channel.send(str(random.randrange(1,7)))
        print(str(random.randrange(1,7)))

client.run('ODkzODA0OTA2NDEzMTgyOTk3.YVgyrw.X7Jp1HYHXTIYLMcVVNxiBfGPXU0')