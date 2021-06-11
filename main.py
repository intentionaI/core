import discord, json, sys, os
import random
import requests
from art import *
import time
from discord.ext import commands

with open('config.json') as f:
	config = json.load(f)

prefix = config.get("prefix")
bot = commands.Bot(command_prefix = {prefix}, self_bot = True)

@bot.command()
async def info(ctx, id):
	await ctx.message.delete()
	r = requests.get(f"http://api.roblox.com/Marketplace/ProductInfo?assetId={id}")
	if r.ok:
		res = r.json()
		if res['AssetTypeId'] == 3:
			embed = discord.Embed(title=res["Name"], colour=0x666666, inline=False)
			embed.add_field(name="Creator:", value=res['Creator']["Name"], inline=False)
			embed.add_field(name="Asset ID:", value=res["AssetId"], inline=False)
			embed.add_field(name="Is For Sale:", value=res["IsForSale"], inline=False)
			embed.add_field(name="Creation Date:", value=res["Created"], inline=False)
			embed.add_field(name="Sales: ", value=res["Sales"], inline=False)
			embed.set_footer(text=str(bot.user))
			embed.set_thumbnail(url="https://t1.rbxcdn.com/eadc8982548a4aa4c158ba1dad61ff14")
			await ctx.send(embed=embed)
		elif res['AssetTypeId'] != 3:
			embed = discord.Embed(title="ID provided is not a valid audio", colour=0x666666, inline=False)
			embed.add_field(name="Info:", value="Please put a valid audio ID", inline=False)
			embed.set_footer(text=str(bot.user))
			embed.set_thumbnail(url="https://images.rbxcdn.com/9281912c23312bc0d08ab750afa588cc.png")
			await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title="ID provided is not a valid asset", colour=0x666666, inline=False)
		embed.add_field(name="Info:", value="Please put a valid asset ID", inline=False)
		embed.set_footer(text=str(bot.user))
		embed.set_thumbnail(url="https://images.rbxcdn.com/9281912c23312bc0d08ab750afa588cc.png")
		await ctx.send(embed=embed)

@bot.command()
async def lmao(ctx):
    await ctx.message.delete()
    lmaos = [
        "LMFAOOOOOOOOOOOOOOOOO",
        "LMAOOOOOOOOOOOOOOOOOOO",
        "LOOOOOOOOOOOOOOOOOOOOOOOOOOL",
        "LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
        "LLMFAOOOOOMFOASMO"
    ]
    await ctx.send(str(random.choice(lmaos)))

@bot.command()
async def spam(ctx, amount: int, *, message): 
    await ctx.message.delete()    
    for a in range(amount):
        await ctx.send(message)

@bot.command()
async def version(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Discord Version", colour=0x666666, inline=False)
    embed.add_field(name="Version:", value=str(discord.__version__), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def chspam(ctx, *, message):
    guild = ctx.message.guild
    await ctx.message.delete()
    while True:
        time.sleep(0.005)
        await guild.create_text_channel(str(message))

@bot.command()
async def caspam(ctx, *, message):
    guild = ctx.message.guild
    await ctx.message.delete()
    while True:
        time.sleep(0.005)
        await guild.create_category(str(message))

@bot.command()
async def vspam(ctx, *, message):
    guild = ctx.message.guild
    await ctx.message.delete()
    while True:
        time.sleep(0.005)
        await guild.create_voice_channel(str(message))

@bot.command()
async def stunnalaugh(ctx):
    await ctx.message.delete()
    await ctx.send(':joy: :joy: :point_up:')
	
@bot.command()
async def wikstunnalaugh(ctx):
    await ctx.message.delete()
    await ctx.send('<:STUNNALAUGH:840583156285046835> <:STUNNAPOINTUP:840604240803790848> <:STUNNAPOINTUP:840604240803790848>')

@bot.command()
async def delall(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.delete()
    for category in ctx.guild.categories:
        await category.delete()

@bot.command()
async def delch(ctx, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        if channel.name == name:
            await channel.delete()

@bot.command()
async def search(ctx, page: int, *, message):
    r = requests.get(f"https://search.roblox.com/catalog/json?https://www.roblox.com/develop/library?CatalogContext=&IncludeNotForSale=true&PageNumber={page}&CreatorName=&SortType=3&SubCategory=16&Category=1&Keyword={message}")
    if r.ok:
        res = r.json()
        for x in res:
            print(str(x['AssetId']) + "; " + str(x['Name']))

@bot.command()
async def inv(ctx, page: int, person):
    r = requests.get(f"https://search.roblox.com/catalog/json?https://www.roblox.com/develop/library?CatalogContext=&IncludeNotForSale=true&PageNumber={page}&CreatorName={person}&SortType=3&SubCategory=16&Category=1&Keyword=")
    if r.ok:
        res = r.json()
        for x in res:
            print(str(x['AssetId']) + "; " + str(x['Name']))

@bot.event
async def on_ready():
    tprint("Core", font="bulbhead")
    print("started, logged in as " + str(bot.user))
    print("discord version: " + str(discord.__version__))

## NSFW
@bot.command()
async def boobs(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    embed = discord.Embed(title="Boobs!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def pussy(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    embed = discord.Embed(title="Pussy!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def nsfwneko(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    embed = discord.Embed(title="NSFW Neko!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def neko(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/lewd")
    res = r.json()
    embed = discord.Embed(title="Neko!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def lesbian(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    embed = discord.Embed(title="Lesbian!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def cumslut(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    embed = discord.Embed(title="Cumsluts!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def sex(ctx, user: discord.User = None): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/classic")
    res = r.json()
    embed = discord.Embed(title=f"{ctx.author.name} fucking {user.name}", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def bj(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/bj")
    res = r.json()
    embed = discord.Embed(title="BJ!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def anal(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    embed = discord.Embed(title="Anal!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def yuri(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/yuri")
    res = r.json()
    embed = discord.Embed(title="Yuri!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def trap(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/trap")
    res = r.json()
    embed = discord.Embed(title="Trap!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def tits(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    embed = discord.Embed(title="Titties!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def hentai(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hentai")
    res = r.json()
    embed = discord.Embed(title="Hentai!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def blowjob(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    embed = discord.Embed(title="Blowjob!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def cum(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum_jpg")
    res = r.json()
    embed = discord.Embed(title="Cum!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def spank(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/spank")
    res = r.json()
    embed = discord.Embed(title="Spank!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)  



@bot.command()
async def gasm(ctx): 
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/gasm")
    res = r.json()
    embed = discord.Embed(title="Gasm!", color=0xff0000)
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed) 

bot.run(config.get("token"), bot = False)
