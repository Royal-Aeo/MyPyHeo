import discord

clint = discord.Client()
print("starts!")

@clint.event
async def on_message(message):
    #if msg.author == msg.user:
        #return
    if message.content.startswith("&Testbot"):
      await message.channel.send("Yeah! I am lisining my baby!")


clint.run("OTc1MzcyOTYzMjU3OTE3NDQw.G3S7s2.P97pGnQBCVVNxnHQqLseiLgi1MnSjnXbn6suMc")
