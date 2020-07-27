import discord

class MyClient(discord.Client):
	async def on_ready(self):
		print("Logged on")
	async def on_message(self, msg):
		if msg.content[0:1] == "!":
			await msg.channel.send("Biden +9999")
client = MyClient()
client.run('NzI5NDY4MTEyMDY3MzYyODE2.XwJZAw.yAFR1RBddphGfJ_-sA12tDAzrMg')
