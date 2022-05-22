import discord
clint = discord.Client()
print("starts!")

@clint.event
async def on_message(message):
    Msg = message.content
    if Msg.startswith("/sys-sendit"):
        Msg.remove("/sys-sendit text:")
        await message.channel.send(Msg)



Clint.run("OTc1MzcyOTYzMjU3OTE3NDQw.G8TAMj.kItBHdsUwBv9NcnAuw-NXnsP7Wv2MWUM_VZPRE")
