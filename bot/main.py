import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.active, activity=discord.Listening("!test"))
    print(f"Logged in as {client.user.name}")
    print(f"Bot ID: {client.user.id})")

@client.command()
async def test(ctx):
    await ctx.send("Tested! It works!")

if __name__ == "__main__":
    bot.run(TOKEN)
