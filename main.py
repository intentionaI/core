import discord, json, sys, os, random, requests, time
from art import *
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
            embed.add_field(name="URL:", value=f"https://roblox.com/library/{id}", inline=False)
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
async def chspam(ctx, amount: int, *, message):
    guild = ctx.message.guild
    await ctx.message.delete()
    for z in range(amount): 
        time.sleep(0.005)
        await guild.create_text_channel(str(message))

@bot.command()
async def caspam(ctx, amount: int, *, message):
    guild = ctx.message.guild
    await ctx.message.delete()
    for z in range(amount): 
        time.sleep(0.005)
        await guild.create_category(str(message))

@bot.command()
async def vspam(ctx, amount: int, *, message):
    guild = ctx.message.guild
    await ctx.message.delete()
    for z in range(amount): 
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
    await ctx.message.delete()
    r = requests.get(f"https://search.roblox.com/catalog/json?https://www.roblox.com/develop/library?CatalogContext=&IncludeNotForSale=true&PageNumber={page}&CreatorName=&SortType=3&SubCategory=16&Category=1&Keyword={message}")
    if r.ok:
        res = r.json()
        for x in res:
            print(str(x['AssetId']) + "; " + str(x['Name']))

@bot.command()
async def inv(ctx, page: int, person):
    await ctx.message.delete()
    r = requests.get(f"https://search.roblox.com/catalog/json?https://www.roblox.com/develop/library?CatalogContext=&IncludeNotForSale=true&PageNumber={page}&CreatorName={person}&SortType=3&SubCategory=16&Category=1&Keyword=")
    if r.ok:
        res = r.json()
        for x in res:
            print(str(x['AssetId']) + "; " + str(x['Name']))

@bot.command()
async def createrole(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.guild.create_role(name=message, color=0x808080)

@bot.command()
async def delallroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@bot.command()
async def manul(ctx):
    await ctx.message.delete()
    r = requests.get("https://infected-rigging.000webhostapp.com/random_manul.php")
    if r.ok:
        embed = discord.Embed(title="Manul!", color=0x666666)
        embed.set_image(url=r.text)
        await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("http://aws.random.cat/meow")
    if r.ok:
        embed = discord.Embed(title="Cat!", color=0x666666)
        embed.set_image(url=r.json()['file'])
        await ctx.send(embed=embed)

@bot.command()
async def boobs(ctx): 
    await ctx.message.delete()
    if str(ctx.channel.type) != "private":
        if ctx.channel.is_nsfw():
            r = requests.get("https://nekos.life/api/v2/img/boobs")
            res = r.json()
            embed = discord.Embed(title="Boobs!", color=0x666666)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            print('u degen use in nsfw channel')
    else:
        print('u degen use in nsfw channel')

@bot.command()
async def nsfwneko(ctx): 
    await ctx.message.delete()
    if str(ctx.channel.type) != "private":
        if ctx.channel.is_nsfw():
            r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
            res = r.json()
            embed = discord.Embed(title="NSFW Neko!", color=0x666666)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            print('u degen use in nsfw channel')
    else:
        print('u degen use in nsfw channel')

@bot.command()
async def lesbian(ctx): 
    await ctx.message.delete()
    if str(ctx.channel.type) != "private":
        if ctx.channel.is_nsfw():
            r = requests.get("https://nekos.life/api/v2/img/les")
            res = r.json()
            embed = discord.Embed(title="Lesbian!", color=0x666666)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            print('u degen use in nsfw channel')
    else:
        print('u degen use in nsfw channel')

@bot.command()
async def yuri(ctx): 
    await ctx.message.delete()
    if str(ctx.channel.type) != "private":
        if ctx.channel.is_nsfw():
            r = requests.get("https://nekos.life/api/v2/img/yuri")
            res = r.json()
            embed = discord.Embed(title="Yuri!", color=0x666666)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            print('u degen use in nsfw channel')
    else:
        print('u degen use in nsfw channel')

@bot.command()
async def trap(ctx): 
    await ctx.message.delete()
    if str(ctx.channel.type) != "private":
        if ctx.channel.is_nsfw():
            r = requests.get("https://nekos.life/api/v2/img/trap")
            res = r.json()
            embed = discord.Embed(title="Trap!", color=0x666666)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            print('u degen use in nsfw channel')
    else:
        print('u degen use in nsfw channel')

@bot.command()
async def tits(ctx): 
    await ctx.message.delete()
    if str(ctx.channel.type) != "private":
        if ctx.channel.is_nsfw():
            r = requests.get("https://nekos.life/api/v2/img/tits")
            res = r.json()
            embed = discord.Embed(title="Titties!", color=0x666666)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            print('u degen use in nsfw channel')
    else:
            print('u degen use in nsfw channel')

@bot.event
async def on_ready():
    r = requests.get('https://raw.githubusercontent.com/pashaaaaaaa/core/main/version.json').json()
    print("started, logged in as " + str(bot.user))
    print("core version: " + str(r['version']))
    print("discord version: " + str(discord.__version__))
    print("prefix is " + str(config.get("prefix")))
tprint("Core", font="bulbhead")
bot.run(config.get("token"), bot = False)
