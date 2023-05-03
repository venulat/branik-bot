import discord
import re
import math

cena = 34

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("běží ti braník?")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("b!ping"):
    await message.channel.send("ok")

  numb = [int(i) for i in re.findall(r'\d+', message.content)]

  pos = 0
  dlouh = len(numb)

  for i in range(dlouh):
    kc = numb[pos]
    pos = pos + 1
    kcstr = str(kc)
    if kc <= 1.7976931348623156e+308:
      rdown = math.floor(kc / 34)
      rdownstr = str(rdown)
    if kc < cena:
      await message.channel.send("Za " + kcstr + " Kč si braník nekoupíš nikde")
    if kc >= cena and kc < 2 * cena:
      await message.channel.send(kcstr + " Kč ti vyjde na jeden braník ve slevě")
    if kc >= 2 * cena and kc < 5 * cena:
      await message.channel.send("Za tuhle částku (" + kcstr + " Kč) by sis mohl koupit " + rdownstr + " braníky ve slevě")
    if kc >= 5 * cena and kc < 1.7976931348623156e+308:
      await message.channel.send("Za tuhle částku (" + kcstr + " Kč) by sis mohl koupit " + rdownstr + " braníků ve slevě")
    if kc >= 1.7976931348623156e+308:
      await message.channel.send("hodně braníků")

client.run("SVŮJ TOKEN ZDE")
