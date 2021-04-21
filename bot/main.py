import discord
import aiohttp
import random
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
    await ctx.send("List of commands: `!test`, `!source`, `!say <value>`, `!ping`, `!meme`, `!guessthenumber`")
    
@client.command()
async def source(ctx):
    await ctx.send("This Bot is made by TheYoBots. Checkout the source code here: https://github.com/TheYoBots/discord-bot")
    
@client.command()
async def test(ctx):
    await ctx.send("Tested! It works!") 
   
@client.command()
async def say(ctx, message):
	await ctx.send(f"{ctx.author.name} said {message}")
    
@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms 🏓")

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="Memes", description="🤣")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
	
@client.event
async def on_message(message):
    if message.content.startswith('!q'):
        randomlist = ["yes","no",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    else:
        await client.process_commands(message)

@client.command()
async def guessthenumber(ctx):
    computer = random.randint(1, 10)
    await ctx.send("Guess my number. It could be any from 1 to 10.")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    msg = await client.wait_for("message", check=check)

    if int(msg.content) == computer:
        await ctx.send("Correct")
    else:
        await ctx.send(f"Nope it was {computer}")
            
if __name__ == "__main__":
    client.run(TOKEN)
