import discord
import aiohttp
import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")
TOKEN = os.getenv("TOKEN")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='!support | By TheYoBots'))
    print(f"Logged in as {client.user.name}")
    print(f"Bot ID: {client.user.id}")
    
@client.command()
async def support(ctx):
    await ctx.send("List of commands: `!test`, `!source`, `!ping`, `!meme`")
    
@client.command()
async def source(ctx):
    await ctx.send("This Bot is made by TheYoBots. Checkout the source code here: https://github.com/TheYoBots/discord-bot")
    
@client.command()
async def test(ctx):
    await ctx.send("Tested! It works!")
    
@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms 🏓")

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="Memes", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

if __name__ == "__main__":
    client.run(TOKEN)
