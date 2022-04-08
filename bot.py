import discord
import os
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!ping'):
            msg = await message.channel.send('pong!')
            await asyncio.sleep(10)
            await msg.delete()

        if message.content.startswith('!ross'):
            msg = await message.channel.send('RACHEL!')
            await asyncio.sleep(10)
            await msg.delete()


intents = discord.Intents.default()
client = MyClient(intents=intents)
client.run(os.environ["SIDHULABS_DISCORD_TOKEN"])

