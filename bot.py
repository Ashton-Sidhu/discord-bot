import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!ping'):
            await message.channel.send('pong!')

intents = discord.Intents.default()
client = MyClient(intents=intents)
client.run(os.getenv["SIDHULABS_DISCORD_TOKEN"])
