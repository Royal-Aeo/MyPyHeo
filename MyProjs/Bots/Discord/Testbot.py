import discord
import re
I = re.compile(r"channel:#[a-z0-9]")
Text = re.compile(r'text:"[a-z0-9]")
clint = discord.Client()
print("starts!")

@clint.event
async def on_message(message):
    Msg = message.content
    if Msg.startswith("/testbot-sendit"):
      Msg.remove("/testbot-sendit ")
      Ch = re.search(I,Msg)
      await message.Ch.send(re.search(Text,Msg))


clint.run("OTc1MzcyOTYzMjU3OTE3NDQw.G3S7s2.P97pGnQBCVVNxnHQqLseiLgi1MnSjnXbn6suMc")
