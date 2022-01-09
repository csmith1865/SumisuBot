import discord,random,asyncio,os
from discord.ext import commands, tasks
from discord.ext.commands.bot import Bot
import discord_slash
from discord_slash.context import SlashContext
from discord_slash.utils.manage_commands import create_option
import mcstatus
import requests
from mcstatus import MinecraftServer
import json
import random
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from typing import Optional
from discord import Embed, Member
from discord.ext.commands import cooldown, BucketType
import time
import os
import platform
import sys
from datetime import datetime
from itertools import cycle
import calendar

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

############################################################Auth Bot####################################################################

botId = config["botId"]

BotActiver = requests.get('https://sumisuapi.herokuapp.com/sumisu/' + str(botId))
BotActiverurl = BotActiver.url
BotActiverequest = requests.get(BotActiverurl)
BotActivetext_json = json.loads(BotActiverequest.text)
BotActiveparse_json = BotActivetext_json
BotActiveChecker = BotActiveparse_json['data']

if BotActiveChecker == "yes":
    print("Bot Authenticated!")
    print("-------------------")
else:
    print("Bot Not Valid!")
    time.sleep(10)
    exit()

#######################################################################################################################################

client = commands.Bot(command_prefix=config["prefix"], help_command=None)
cmdprfx = config["prefix"]
#guild = config["guild"]
randomgreetings = config["greetings"]

dailyweatherlocation = config["dailyweatherlocation"]

dailycolorchannel = config["dailycolorchannel"]
memeofthehourchannel = config["memeofthehourchannel"]
quoteofthedaychannel = config["quoteofthedaychannel"]
dailyweatherchannel = config["dailyweatherchannel"]

boticon = config["boticon"]
discordusername = config["discordusername"]
discordusernameurl = config["discordusernameurl"]

embedhex = config["hex"]
embedhexfix = int(embedhex, 16)

dscactivitystatus = config["activity"]
dscstatus = config["status"]

dsclisteningstatus = config["listeningstatuses"]
dscwatchingstatus = config["watchingingstatuses"]
dscplayingstatuses = config["playingstatuses"]

if dscactivitystatus == "listening":
    dscactivity = discord.ActivityType.listening
    discordactivitystatus = cycle(dsclisteningstatus)
elif dscactivitystatus == "watching":
    dscactivity = discord.ActivityType.watching
    discordactivitystatus = cycle(dscwatchingstatus)
else:
    dscactivity = discord.ActivityType.playing
    discordactivitystatus = cycle(dscplayingstatuses)

if dscstatus == "online":
    dcstatus = discord.Status.online
elif dscstatus == "idle":
    dcstatus = discord.Status.idle
else:
    dcstatus = discord.Status.dnd


@client.event
async def on_ready():
    change_status.start()
    daily_color.start()
    quote_of_the_day.start()
    meme_of_the_hour.start()
    daily_weather_forecast.start()
    print(f"Logged in as {client.user.name}")
    print(f"Discord PY version: {discord.__version__}")
    print(f"Discord Slash version: {discord_slash.__version__}")
    print(f"MCStatus version: 7.0.0")
    print(f"PHUE version: 1.1")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    print("Bot is online.")
    print()

@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(status=dscstatus, activity=discord.Activity(type=dscactivity, name=next(discordactivitystatus)))


@client.command()
async def help(ctx):
        embed = discord.Embed(
                title="Error:",
                description="Use " + cmdprfx + "help`pagenumber` (with no spaces) for help!",
                color=embedhexfix,
            )
        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.author.send(embed=embed)
        print("Help Command Used By: {}".format(ctx.author))

@client.command()
async def help1(ctx):
        embed = discord.Embed(
                title="Commands Page 1:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )

        embed.add_field(name=cmdprfx + "mc `server`", value="Allows you to look up information about a minecraft server!", inline=True)
        embed.add_field(name=cmdprfx + "catfact", value="Tells you a random fact about cats!", inline=True)
        embed.add_field(name=cmdprfx + "cat", value="Displays a random cat image!", inline=True)
        embed.add_field(name=cmdprfx + "meme", value="Shows you a random meme!", inline=True)
        embed.add_field(name=cmdprfx + "food", value="Shows a random image of food!", inline=True)
        embed.add_field(name=cmdprfx + "age", value="Tells you when your account was created!", inline=True)
        embed.add_field(name=cmdprfx + "baka", value="Sends a baka anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "bite", value="Sends a biting anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "blush", value="Sends a blushing anime gif in chat!", inline=True)

        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.author.send(embed=embed)
        print("Help Page 1 Command Used By: {}".format(ctx.author))

@client.command()
async def help2(ctx):
        embed = discord.Embed(
                title="Commands Page 2:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )

        embed.add_field(name=cmdprfx + "bored", value="Sends a bored anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "cry", value="Sends a crying anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "cuddle", value="Sends a cuddling anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "dance", value="Sends a dancing anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "facepalm", value="For when someone does something **REALLY** stupid!", inline=True)
        embed.add_field(name=cmdprfx + "feed", value="Sends a feeding anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "happy", value="Sends a happy gif on anime!", inline=True)
        embed.add_field(name=cmdprfx + "highfive", value="Sends a highfiving anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "hug", value="Sends a huging anime gif in chat!", inline=True)
        
        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.author.send(embed=embed)
        print("Help Page 2 Command Used By: {}".format(ctx.author))

@client.command()
async def help3(ctx):
        embed = discord.Embed(
                title="Commands Page 3:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )

        embed.add_field(name=cmdprfx + "kiss", value="Sends a kissing anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "laugh", value="Sends a laughing anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "nekos", value="Cat Girls!", inline=True)
        embed.add_field(name=cmdprfx + "newlife", value="Use this for when you need to start a new life, and go on the run!", inline=True)
        embed.add_field(name=cmdprfx + "pat", value="Sends a patting anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "poke", value="Sends a poking anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "pout", value="Sends a pouting anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "shrug", value="Sends a shrugging anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "slap", value="When you really want to slap the $4IT out of someone!", inline=True)
        
        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.author.send(embed=embed)
        print("Help Page 3 Command Used By: {}".format(ctx.author))

@client.command()
async def help4(ctx):
        embed = discord.Embed(
                title="Commands Page 4:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )

        embed.add_field(name=cmdprfx + "sleep", value="Use this when you get sleepy!", inline=True)
        embed.add_field(name=cmdprfx + "smile", value="Say Cheese!", inline=True)
        embed.add_field(name=cmdprfx + "smug", value="Shady shady shady...", inline=True)
        embed.add_field(name=cmdprfx + "stare", value="O.O", inline=True)
        embed.add_field(name=cmdprfx + "think", value="Brain blast!", inline=True)
        embed.add_field(name=cmdprfx + "thumbsup", value="You did good! You deserve it!", inline=True)
        embed.add_field(name=cmdprfx + "tickle", value="Sends a tickling anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "wave", value="Sends a waving anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "wink", value="Sends a winking anime gif in chat!", inline=True)
        
        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.author.send(embed=embed)
        print("Help Page 4 Command Used By: {}".format(ctx.author))

@client.command()
async def help5(ctx):
        embed = discord.Embed(
                title="Commands Page 5:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )
        embed.add_field(name=cmdprfx + "yesorno", value="When you can't decide, let someone else!", inline=True)
        embed.add_field(name=cmdprfx + "insult", value="Fuck 'em!", inline=True)
        embed.add_field(name=cmdprfx + "ipconfig `ipaddress`", value="Get information about an IP Address.", inline=True)
        embed.add_field(name=cmdprfx + "randomcolor", value="Sends a random HEX color with example!", inline=True)
        embed.add_field(name=cmdprfx + "boredactivity", value="Gives you an activity to do when you are bored!", inline=True)
        embed.add_field(name=cmdprfx + "time", value="Tells you the current time!", inline=True)
        embed.add_field(name=cmdprfx + "qrurl `url`", value="Turns the URL into a QR Code!", inline=True)
        embed.add_field(name=cmdprfx + "lookup `word`", value="Defines a word!", inline=True)

        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.author.send(embed=embed)
        print("Help Page 5 Command Used By: {}".format(ctx.author))

@client.command()
async def help6(ctx):
        embed = discord.Embed(
                title="Commands Page 6:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )
        embed.add_field(name=cmdprfx + "yomomma", value="Sends a Yo Momma Joke!", inline=True)
        embed.add_field(name=cmdprfx + "uselessfact", value="Sends a useless fact!", inline=True)
        embed.add_field(name=cmdprfx + "coffee", value="Sends a picture of coffee!", inline=True)
        embed.add_field(name=cmdprfx + "mcskin `username`", value="Show someones Minecraft Skin!", inline=True)
        embed.add_field(name=cmdprfx + "mcskindownload `username`", value="Download someones Minecraft Skin!", inline=True)
        embed.add_field(name=cmdprfx + "drawcard", value="Draws a random playing card!", inline=True)
        embed.add_field(name=cmdprfx + "D6", value="Rolls a D6 dice!", inline=True)
        embed.add_field(name=cmdprfx + "D20", value="Rolls a D20 dice!", inline=True)

        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.author.send(embed=embed)
        print("Help Page 5 Command Used By: {}".format(ctx.author))

@client.command()
async def help7(ctx):
        embed = discord.Embed(
                title="Commands Page 7:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )
        embed.add_field(name=cmdprfx + "covid", value="Show's current COVID info!", inline=True)
        embed.add_field(name=cmdprfx + "hex `hexcolor`", value="Show's the HEX color!", inline=True)

        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.author.send(embed=embed)
        print("Help Page 5 Command Used By: {}".format(ctx.author))

@client.command()
async def mc(ctx, arg):
    r = requests.get('https://api.mcsrvstat.us/2/', arg)
    mcurl = r.url.replace("%0A", "").replace("?", "")
    mcrequest = requests.get(mcurl)
    text_json = json.loads(mcrequest.text)
    parse_json = text_json
    server = MinecraftServer.lookup(arg)
    status = server.status()

    online = text_json['online']

    # This is where you want to store the parsed IP Addresses IF they are online  
    try:
        if online:
            mcip = text_json['ip']
            mcport = text_json['port']
            #This is for the Version
            mcversion = text_json['version']
            decodedversion = mcversion.replace("\u279c", "->").replace("\u2503", "|").replace("\u2718", "x").replace("\u25aa", "").replace("\u3010", "[").replace("\u3011", "]").replace("\u25cf", "*").replace("\u27a2", ">")

            #This is for the MOTD
            mcmotd = parse_json['motd']
            data = []
            for cleanmotd in mcmotd['clean']:
                
                ecleanmotd = cleanmotd.replace(",", " -").replace("    ", " ")
                encodedmotd = ecleanmotd.encode("ascii", "ignore")
                decodedmotd = encodedmotd.decode()
                data.append(decodedmotd)

            mcplayers = parse_json['players']
            playerdata = []
            for cleanplayers in mcplayers['list']:
                
                ecleanmotd = cleanplayers.replace(",", " -").replace("    ", " ")
                encodedplayers = cleanplayers.encode("ascii", "ignore")
                decodedplayers = encodedplayers.decode()
                playerdata.append(decodedplayers)
            
            embed = discord.Embed(
                title="Server: " + arg,
                description='**IP:** ' + str(mcip) + '\n**Port:** ' + str(mcport) + '\n**Players:** ' + str(status.players.online) + '/' + str(status.players.max) + '\n**Version:** ' + str(decodedversion) + '\n\n**Description:** ' + str(data).replace("[", "").replace("]", "").replace("'", "") + '\n\n**Online:** ' + str(playerdata).replace("[", "").replace("]", "").replace("'", ""),
                color=embedhexfix,
            )
            embed.set_thumbnail(url="https://eu.mc-api.net/v3/server/favicon/" + arg)
            embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
            embed.set_footer(text="Made by: Sumisu®")

            await ctx.send(embed=embed)
            print("Server IP: " + mcip)
        else:
            print("Online: False")
    except:
        print("Minecraft Server Command Used By: {}".format(ctx.author) + " | Server: " + arg)

        embed = discord.Embed(
            title="Server: " + arg,
            description='**IP:** ' + str(mcip) + '\n**Port:** ' + str(mcport) + '\n**Players:** ' + str(status.players.online) + '/' + str(status.players.max) + '\n**Version:** ' + str(decodedversion) + '\n\n**Description:** ' + str(data).replace("[", "").replace("]", "").replace("'", "") + '\n\n**Online:** N/A',
            color=embedhexfix,
        )
        embed.set_thumbnail(url="https://eu.mc-api.net/v3/server/favicon/" + arg)
        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")

        await ctx.send(embed=embed)
        

@client.command()
async def catfact(ctx):
    r = requests.get('https://meowfacts.herokuapp.com/')
    catfacturl = r.url
    catrequest = requests.get(catfacturl)
    text_json = json.loads(catrequest.text)
    parse_json = text_json
    catfact = parse_json['data']
    cleancatfact = str(catfact).replace("['", "").replace("']", "")

    catimager = requests.get('https://aws.random.cat/meow')
    catimageurl = catimager.url
    catimagerequest = requests.get(catimageurl)
    catimagetext_json = json.loads(catimagerequest.text)
    catimageparse_json = catimagetext_json
    catimage = catimageparse_json['file']
    embed = discord.Embed(
            title="CatFact!",
            description='\n\n**Fact:** ' + cleancatfact,
            color=embedhexfix,
        )

    embed.set_thumbnail(url=catimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")

    await ctx.send(embed=embed)
    print("Cat Fact Command Used By: {}".format(ctx.author) + " | Cat Fact: " + cleancatfact)

@client.command()
async def cat(ctx):
    catimager = requests.get('https://aws.random.cat/meow')
    catimageurl = catimager.url
    catimagerequest = requests.get(catimageurl)
    catimagetext_json = json.loads(catimagerequest.text)
    catimageparse_json = catimagetext_json
    catimage = catimageparse_json['file']
    embed = discord.Embed(
            color=embedhexfix,
        )
    embed.set_image(url=catimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Cat Image Command Used By: {}".format(ctx.author) + " | Image URL: " + catimage)

@client.command()
async def meme(ctx):
    memeimager = requests.get('https://meme-api.herokuapp.com/gimme')
    memeimageurl = memeimager.url
    memeimagerequest = requests.get(memeimageurl)
    memeimagetext_json = json.loads(memeimagerequest.text)
    memeimageparse_json = memeimagetext_json
    memeimage = memeimageparse_json['url']
    memeauthorurl = memeimager.url
    memeauthorrequest = requests.get(memeauthorurl)
    memeauthortext_json = json.loads(memeauthorrequest.text)
    memeauthorparse_json = memeauthortext_json
    memeauthor = memeauthorparse_json['author']

    
    embed = discord.Embed(
            description="Made by: " + str(memeauthor),
            color=embedhexfix,
        )
    embed.set_image(url=memeimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Meme Image Command Used By: {}".format(ctx.author) + " | Image URL: " + str(memeimage))

#@client.command()
#async def yt(ctx):
#    embed = discord.Embed(
#            title="Sumisu's Youtube!",
#            url="https://www.youtube.com/channel/UCZ_lWTHNwPIAecB8nHLje9w",
#            description="https://www.youtube.com/channel/UCZ_lWTHNwPIAecB8nHLje9w",
#            color=embedhexfix,
#        )

#    embed.add_field(name="Sumisu's Youtube:", value="https://www.youtube.com/embed/ur3-A7ovGUk", inline=True)
#    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
#    embed.set_footer(text="Made by: Sumisu®")
#    await ctx.send(embed=embed)
#    await ctx.send("https://www.youtube.com/embed/ur3-A7ovGUk")
#    print("Youtube Command Used By: {}".format(ctx.author))

@client.command(name="hello",
            description="Sends a DM to someone as the bot.",
            brief="Sends DM.",
            aliases=['hiya', 'hey', 'hi', 'howdy'],
            pass_context=True)
async def hello(ctx):
    greetings = random.choice(randomgreetings)
    embed = discord.Embed(
            title=greetings,
            description=ctx.author.mention,
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Hello Command Used By: {}".format(ctx.author) + " | Greeting used: " + greetings)

@client.command()
async def food(ctx):
    foodimager = requests.get('https://foodish-api.herokuapp.com/api')
    foodimageurl = foodimager.url
    foodimagerequest = requests.get(foodimageurl)
    foodimagetext_json = json.loads(foodimagerequest.text)
    foodimageparse_json = foodimagetext_json
    foodimage = foodimageparse_json['image']
    embed = discord.Embed(
           description="Food Image: ",
            color=embedhexfix,
        )
    embed.set_image(url=foodimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Food Image Command Used By: {}".format(ctx.author) + " | Image URL: " + foodimage)

@client.command()
async def anime(ctx, *, content:str):
    animer = requests.get('https://api.jikan.moe/v3/search/anime?q={}&limit=1'.format(content))
    import time
    time.sleep(3)
    animeurl = animer.url
    animerequest = requests.get(animeurl)
    animetext_json = json.loads(animerequest.text)
    animeparse_json = animetext_json
    animedata = animeparse_json['results']
    animeone = animedata[0]
    animedataurl = animeone['url']
    animetitle = animeone['title']
    animesynopsis = animeone['synopsis']
    animescore = animeone['score']
    animeairing = animeone['airing']
    animeepisodes = animeone['episodes']
    animeimageurl = animeone['image_url']

    embed = discord.Embed(
            title=animetitle,
            url=animedataurl,
            description=animesynopsis,
            color=embedhexfix,
        )
    embed.add_field(name="Episodes:", value=animeepisodes, inline=False)
    embed.add_field(name="Airing:", value=animeairing, inline=False)
    embed.add_field(name="Score:", value=animescore, inline=False)
    embed.set_image(url=animeimageurl)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Anime Command Used By: {}".format(ctx.author) + " | Anime Searched: {}".format(content))

@client.command()
async def age(ctx):
    accountage = ctx.author.created_at
    date = accountage
    utc_time = calendar.timegm(date.utctimetuple())
    embed = discord.Embed(
           title="Account Age: <t:{}:R>".format(utc_time),
           description=ctx.author.mention + "\n\nYour account was created on: **" + accountage.strftime('%B %d %Y') + " at " + accountage.strftime('%I:%M:%S %p') + "**",
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Age Command Used By: {}".format(ctx.author) + " | Account Age: " + accountage.strftime('%B %d %Y') + " at " + accountage.strftime('%I:%M:%S %p'))

@client.command()
async def baka(ctx):
    bakaimager = requests.get('https://nekos.best/api/v1/baka')
    bakaimageurl = bakaimager.url
    bakaimagerequest = requests.get(bakaimageurl)
    bakaimagetext_json = json.loads(bakaimagerequest.text)
    bakaimageparse_json = bakaimagetext_json
    bakaimage = bakaimageparse_json['url']
    bakaname = bakaimageparse_json['anime_name']
    embed = discord.Embed(

           description=bakaname,
            color=embedhexfix,
        )
    embed.set_image(url=bakaimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Baka Image Command Used By: {}".format(ctx.author) + " | Image URL: " + bakaimage)

@client.command()
async def bite(ctx):
    biteimager = requests.get('https://nekos.best/api/v1/bite')
    biteimageurl = biteimager.url
    biteimagerequest = requests.get(biteimageurl)
    biteimagetext_json = json.loads(biteimagerequest.text)
    biteimageparse_json = biteimagetext_json
    biteimage = biteimageparse_json['url']
    bitename = biteimageparse_json['anime_name']
    embed = discord.Embed(

           description=bitename,
            color=embedhexfix,
        )
    embed.set_image(url=biteimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Bite Image Command Used By: {}".format(ctx.author) + " | Image URL: " + biteimage)

@client.command()
async def blush(ctx):
    blushimager = requests.get('https://nekos.best/api/v1/blush')
    blushimageurl = blushimager.url
    blushimagerequest = requests.get(blushimageurl)
    blushimagetext_json = json.loads(blushimagerequest.text)
    blushimageparse_json = blushimagetext_json
    blushimage = blushimageparse_json['url']
    blushname = blushimageparse_json['anime_name']
    embed = discord.Embed(

           description=blushname,
            color=embedhexfix,
        )
    embed.set_image(url=blushimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Blush Image Command Used By: {}".format(ctx.author) + " | Image URL: " + blushimage)

@client.command()
async def bored(ctx):
    boredimager = requests.get('https://nekos.best/api/v1/bored')
    boredimageurl = boredimager.url
    boredimagerequest = requests.get(boredimageurl)
    boredimagetext_json = json.loads(boredimagerequest.text)
    boredimageparse_json = boredimagetext_json
    boredimage = boredimageparse_json['url']
    boredname = boredimageparse_json['anime_name']
    embed = discord.Embed(

           description=boredname,
            color=embedhexfix,
        )
    embed.set_image(url=boredimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Bored Image Command Used By: {}".format(ctx.author) + " | Image URL: " + boredimage)

@client.command()
async def cry(ctx):
    cryimager = requests.get('https://nekos.best/api/v1/cry')
    cryimageurl = cryimager.url
    cryimagerequest = requests.get(cryimageurl)
    cryimagetext_json = json.loads(cryimagerequest.text)
    cryimageparse_json = cryimagetext_json
    cryimage = cryimageparse_json['url']
    cryname = cryimageparse_json['anime_name']
    embed = discord.Embed(

           description=cryname,
            color=embedhexfix,
        )
    embed.set_image(url=cryimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Cry Image Command Used By: {}".format(ctx.author) + " | Image URL: " + cryimage)

@client.command()
async def cuddle(ctx):
    cuddleimager = requests.get('https://nekos.best/api/v1/cuddle')
    cuddleimageurl = cuddleimager.url
    cuddleimagerequest = requests.get(cuddleimageurl)
    cuddleimagetext_json = json.loads(cuddleimagerequest.text)
    cuddleimageparse_json = cuddleimagetext_json
    cuddleimage = cuddleimageparse_json['url']
    cuddlename = cuddleimageparse_json['anime_name']
    embed = discord.Embed(

           description=cuddlename,
            color=embedhexfix,
        )
    embed.set_image(url=cuddleimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Cuddle Image Command Used By: {}".format(ctx.author) + " | Image URL: " + cuddleimage)

@client.command()
async def dance(ctx):
    danceimager = requests.get('https://nekos.best/api/v1/dance')
    danceimageurl = danceimager.url
    danceimagerequest = requests.get(danceimageurl)
    danceimagetext_json = json.loads(danceimagerequest.text)
    danceimageparse_json = danceimagetext_json
    danceimage = danceimageparse_json['url']
    dancename = danceimageparse_json['anime_name']
    embed = discord.Embed(

           description=dancename,
            color=embedhexfix,
        )
    embed.set_image(url=danceimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Dance Image Command Used By: {}".format(ctx.author) + " | Image URL: " + danceimage)

@client.command()
async def facepalm(ctx):
    facepalmimager = requests.get('https://nekos.best/api/v1/facepalm')
    facepalmimageurl = facepalmimager.url
    facepalmimagerequest = requests.get(facepalmimageurl)
    facepalmimagetext_json = json.loads(facepalmimagerequest.text)
    facepalmimageparse_json = facepalmimagetext_json
    facepalmimage = facepalmimageparse_json['url']
    facepalmname = facepalmimageparse_json['anime_name']
    embed = discord.Embed(

           description=facepalmname,
            color=embedhexfix,
        )
    embed.set_image(url=facepalmimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Facepalm Image Command Used By: {}".format(ctx.author) + " | Image URL: " + facepalmimage)

@client.command()
async def feed(ctx):
    feedimager = requests.get('https://nekos.best/api/v1/feed')
    feedimageurl = feedimager.url
    feedimagerequest = requests.get(feedimageurl)
    feedimagetext_json = json.loads(feedimagerequest.text)
    feedimageparse_json = feedimagetext_json
    feedimage = feedimageparse_json['url']
    feedname = feedimageparse_json['anime_name']
    embed = discord.Embed(

           description=feedname,
            color=embedhexfix,
        )
    embed.set_image(url=feedimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Feed Image Command Used By: {}".format(ctx.author) + " | Image URL: " + feedimage)

@client.command()
async def happy(ctx):
    happyimager = requests.get('https://nekos.best/api/v1/happy')
    happyimageurl = happyimager.url
    happyimagerequest = requests.get(happyimageurl)
    happyimagetext_json = json.loads(happyimagerequest.text)
    happyimageparse_json = happyimagetext_json
    happyimage = happyimageparse_json['url']
    happyname = happyimageparse_json['anime_name']
    embed = discord.Embed(

           description=happyname,
            color=embedhexfix,
        )
    embed.set_image(url=happyimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Happy Image Command Used By: {}".format(ctx.author) + " | Image URL: " + happyimage)

@client.command()
async def highfive(ctx):
    highfiveimager = requests.get('https://nekos.best/api/v1/highfive')
    highfiveimageurl = highfiveimager.url
    highfiveimagerequest = requests.get(highfiveimageurl)
    highfiveimagetext_json = json.loads(highfiveimagerequest.text)
    highfiveimageparse_json = highfiveimagetext_json
    highfiveimage = highfiveimageparse_json['url']
    highfivename = highfiveimageparse_json['anime_name']
    embed = discord.Embed(

           description=highfivename,
            color=embedhexfix,
        )
    embed.set_image(url=highfiveimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Highfive Image Command Used By: {}".format(ctx.author) + " | Image URL: " + highfiveimage)

@client.command()
async def hug(ctx):
    hugimager = requests.get('https://nekos.best/api/v1/hug')
    hugimageurl = hugimager.url
    hugimagerequest = requests.get(hugimageurl)
    hugimagetext_json = json.loads(hugimagerequest.text)
    hugimageparse_json = hugimagetext_json
    hugimage = hugimageparse_json['url']
    hugname = hugimageparse_json['anime_name']
    embed = discord.Embed(

           description=hugname,
            color=embedhexfix,
        )
    embed.set_image(url=hugimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Hug Image Command Used By: {}".format(ctx.author) + " | Image URL: " + hugimage)

@client.command()
async def kiss(ctx):
    kissimager = requests.get('https://nekos.best/api/v1/kiss')
    kissimageurl = kissimager.url
    kissimagerequest = requests.get(kissimageurl)
    kissimagetext_json = json.loads(kissimagerequest.text)
    kissimageparse_json = kissimagetext_json
    kissimage = kissimageparse_json['url']
    kissname = kissimageparse_json['anime_name']
    embed = discord.Embed(

           description=kissname,
            color=embedhexfix,
        )
    embed.set_image(url=kissimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Kiss Image Command Used By: {}".format(ctx.author) + " | Image URL: " + kissimage)

@client.command()
async def laugh(ctx):
    laughimager = requests.get('https://nekos.best/api/v1/laugh')
    laughimageurl = laughimager.url
    laughimagerequest = requests.get(laughimageurl)
    laughimagetext_json = json.loads(laughimagerequest.text)
    laughimageparse_json = laughimagetext_json
    laughimage = laughimageparse_json['url']
    laughname = laughimageparse_json['anime_name']
    embed = discord.Embed(

           description=laughname,
            color=embedhexfix,
        )
    embed.set_image(url=laughimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Laugh Image Command Used By: {}".format(ctx.author) + " | Image URL: " + laughimage)

@client.command()
async def pat(ctx):
    patimager = requests.get('https://nekos.best/api/v1/pat')
    patimageurl = patimager.url
    patimagerequest = requests.get(patimageurl)
    patimagetext_json = json.loads(patimagerequest.text)
    patimageparse_json = patimagetext_json
    patimage = patimageparse_json['url']
    patname = patimageparse_json['anime_name']
    embed = discord.Embed(

           description=patname,
            color=embedhexfix,
        )
    embed.set_image(url=patimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Pat Image Command Used By: {}".format(ctx.author) + " | Image URL: " + patimage)

@client.command()
async def poke(ctx):
    pokeimager = requests.get('https://nekos.best/api/v1/poke')
    pokeimageurl = pokeimager.url
    pokeimagerequest = requests.get(pokeimageurl)
    pokeimagetext_json = json.loads(pokeimagerequest.text)
    pokeimageparse_json = pokeimagetext_json
    pokeimage = pokeimageparse_json['url']
    pokename = pokeimageparse_json['anime_name']
    embed = discord.Embed(

           description=pokename,
            color=embedhexfix,
        )
    embed.set_image(url=pokeimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Poke Image Command Used By: {}".format(ctx.author) + " | Image URL: " + pokeimage)

@client.command()
async def pout(ctx):
    poutimager = requests.get('https://nekos.best/api/v1/pout')
    poutimageurl = poutimager.url
    poutimagerequest = requests.get(poutimageurl)
    poutimagetext_json = json.loads(poutimagerequest.text)
    poutimageparse_json = poutimagetext_json
    poutimage = poutimageparse_json['url']
    poutname = poutimageparse_json['anime_name']
    embed = discord.Embed(

           description=poutname,
            color=embedhexfix,
        )
    embed.set_image(url=poutimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Pout Image Command Used By: {}".format(ctx.author) + " | Image URL: " + poutimage)

@client.command()
async def shrug(ctx):
    shrugimager = requests.get('https://nekos.best/api/v1/shrug')
    shrugimageurl = shrugimager.url
    shrugimagerequest = requests.get(shrugimageurl)
    shrugimagetext_json = json.loads(shrugimagerequest.text)
    shrugimageparse_json = shrugimagetext_json
    shrugimage = shrugimageparse_json['url']
    shrugname = shrugimageparse_json['anime_name']
    embed = discord.Embed(

           description=shrugname,
            color=embedhexfix,
        )
    embed.set_image(url=shrugimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Shrug Image Command Used By: {}".format(ctx.author) + " | Image URL: " + shrugimage)

@client.command()
async def slap(ctx):
    slapimager = requests.get('https://nekos.best/api/v1/slap')
    slapimageurl = slapimager.url
    slapimagerequest = requests.get(slapimageurl)
    slapimagetext_json = json.loads(slapimagerequest.text)
    slapimageparse_json = slapimagetext_json
    slapimage = slapimageparse_json['url']
    slapname = slapimageparse_json['anime_name']
    embed = discord.Embed(

           description=slapname,
            color=embedhexfix,
        )
    embed.set_image(url=slapimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Slap Image Command Used By: {}".format(ctx.author) + " | Image URL: " + slapimage)

@client.command()
async def sleep(ctx):
    sleepimager = requests.get('https://nekos.best/api/v1/sleep')
    sleepimageurl = sleepimager.url
    sleepimagerequest = requests.get(sleepimageurl)
    sleepimagetext_json = json.loads(sleepimagerequest.text)
    sleepimageparse_json = sleepimagetext_json
    sleepimage = sleepimageparse_json['url']
    sleepname = sleepimageparse_json['anime_name']
    embed = discord.Embed(

           description=sleepname,
            color=embedhexfix,
        )
    embed.set_image(url=sleepimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Sleep Image Command Used By: {}".format(ctx.author) + " | Image URL: " + sleepimage)

@client.command()
async def smile(ctx):
    smileimager = requests.get('https://nekos.best/api/v1/smile')
    smileimageurl = smileimager.url
    smileimagerequest = requests.get(smileimageurl)
    smileimagetext_json = json.loads(smileimagerequest.text)
    smileimageparse_json = smileimagetext_json
    smileimage = smileimageparse_json['url']
    smilename = smileimageparse_json['anime_name']
    embed = discord.Embed(

           description=smilename,
            color=embedhexfix,
        )
    embed.set_image(url=smileimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Smile Image Command Used By: {}".format(ctx.author) + " | Image URL: " + smileimage)

@client.command()
async def smug(ctx):
    smugimager = requests.get('https://nekos.best/api/v1/smug')
    smugimageurl = smugimager.url
    smugimagerequest = requests.get(smugimageurl)
    smugimagetext_json = json.loads(smugimagerequest.text)
    smugimageparse_json = smugimagetext_json
    smugimage = smugimageparse_json['url']
    smugname = smugimageparse_json['anime_name']
    embed = discord.Embed(

           description=smugname,
            color=embedhexfix,
        )
    embed.set_image(url=smugimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Smug Image Command Used By: {}".format(ctx.author) + " | Image URL: " + smugimage)

@client.command()
async def stare(ctx):
    stareimager = requests.get('https://nekos.best/api/v1/stare')
    stareimageurl = stareimager.url
    stareimagerequest = requests.get(stareimageurl)
    stareimagetext_json = json.loads(stareimagerequest.text)
    stareimageparse_json = stareimagetext_json
    stareimage = stareimageparse_json['url']
    starename = stareimageparse_json['anime_name']
    embed = discord.Embed(

           description=starename,
            color=embedhexfix,
        )
    embed.set_image(url=stareimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Stare Image Command Used By: {}".format(ctx.author) + " | Image URL: " + stareimage)

@client.command()
async def think(ctx):
    thinkimager = requests.get('https://nekos.best/api/v1/think')
    thinkimageurl = thinkimager.url
    thinkimagerequest = requests.get(thinkimageurl)
    thinkimagetext_json = json.loads(thinkimagerequest.text)
    thinkimageparse_json = thinkimagetext_json
    thinkimage = thinkimageparse_json['url']
    thinkname = thinkimageparse_json['anime_name']
    embed = discord.Embed(

           description=thinkname,
            color=embedhexfix,
        )
    embed.set_image(url=thinkimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Think Image Command Used By: {}".format(ctx.author) + " | Image URL: " + thinkimage)

@client.command()
async def thumbsup(ctx):
    thumbsupimager = requests.get('https://nekos.best/api/v1/thumbsup')
    thumbsupimageurl = thumbsupimager.url
    thumbsupimagerequest = requests.get(thumbsupimageurl)
    thumbsupimagetext_json = json.loads(thumbsupimagerequest.text)
    thumbsupimageparse_json = thumbsupimagetext_json
    thumbsupimage = thumbsupimageparse_json['url']
    thumbsupname = thumbsupimageparse_json['anime_name']
    embed = discord.Embed(

           description=thumbsupname,
            color=embedhexfix,
        )
    embed.set_image(url=thumbsupimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Thumbsup Image Command Used By: {}".format(ctx.author) + " | Image URL: " + thumbsupimage)

@client.command()
async def tickle(ctx):
    tickleimager = requests.get('https://nekos.best/api/v1/tickle')
    tickleimageurl = tickleimager.url
    tickleimagerequest = requests.get(tickleimageurl)
    tickleimagetext_json = json.loads(tickleimagerequest.text)
    tickleimageparse_json = tickleimagetext_json
    tickleimage = tickleimageparse_json['url']
    ticklename = tickleimageparse_json['anime_name']
    embed = discord.Embed(

           description=ticklename,
            color=embedhexfix,
        )
    embed.set_image(url=tickleimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Tickle Image Command Used By: {}".format(ctx.author) + " | Image URL: " + tickleimage)

@client.command()
async def wave(ctx):
    waveimager = requests.get('https://nekos.best/api/v1/wave')
    waveimageurl = waveimager.url
    waveimagerequest = requests.get(waveimageurl)
    waveimagetext_json = json.loads(waveimagerequest.text)
    waveimageparse_json = waveimagetext_json
    waveimage = waveimageparse_json['url']
    wavename = waveimageparse_json['anime_name']
    embed = discord.Embed(

           description=wavename,
            color=embedhexfix,
        )
    embed.set_image(url=waveimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Wave Image Command Used By: {}".format(ctx.author) + " | Image URL: " + waveimage)

@client.command()
async def wink(ctx):
    winkimager = requests.get('https://nekos.best/api/v1/wink')
    winkimageurl = winkimager.url
    winkimagerequest = requests.get(winkimageurl)
    winkimagetext_json = json.loads(winkimagerequest.text)
    winkimageparse_json = winkimagetext_json
    winkimage = winkimageparse_json['url']
    winkname = winkimageparse_json['anime_name']
    embed = discord.Embed(

           description=winkname,
            color=embedhexfix,
        )
    embed.set_image(url=winkimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Wink Image Command Used By: {}".format(ctx.author) + " | Image URL: " + winkimage)

@client.command()
async def nekos(ctx):
    nekosimager = requests.get('https://nekos.best/api/v1/nekos')
    nekosimageurl = nekosimager.url
    nekosimagerequest = requests.get(nekosimageurl)
    nekosimagetext_json = json.loads(nekosimagerequest.text)
    nekosimageparse_json = nekosimagetext_json
    nekosimage = nekosimageparse_json['url']
    nekosname = nekosimageparse_json['artist_name']
    nekosurl= nekosimageparse_json['artist_href']
    embed = discord.Embed(
           title="Artist: " + nekosname,
            url=nekosurl,

            color=embedhexfix,
        )
    embed.set_image(url=nekosimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Nekos Image Command Used By: {}".format(ctx.author) + " | Image URL: " + nekosimage)

@client.command()
async def newlife(ctx):
    newlifer = requests.get('https://randomuser.me/api/')
    newlifeurl = newlifer.url
    newliferequest = requests.get(newlifeurl)
    newlifetext_json = json.loads(newliferequest.text)
    newlifeparse_json = newlifetext_json
    newlifedata = newlifeparse_json['results']
    newlifeone = newlifedata[0]

    newlifegender = newlifeone['gender']

    newlifename = newlifeone['name']
    newlifetitle = newlifename['title']
    newlifefirstname = newlifename['first']
    newlifelastname = newlifename['last']

    newlifelocation = newlifeone['location']
    newlifestreet = newlifelocation['street']
    newlifestreetnumber = newlifestreet['number']
    newlifestreetname = newlifestreet['name']

    newlifecity = newlifelocation['city']
    newlifestate = newlifelocation['state']
    newlifecountry = newlifelocation['country']
    newlifepostalcode = newlifelocation['postcode']

    newlifeemail = newlifeone['email']
    newlifelogininfo = newlifeone['login']
    newlifeloginusername = newlifelogininfo['username']
    newlifeloginpassword = newlifelogininfo['password']

    newlifedob = newlifeone['dob']
    newlifedobdate = newlifedob['date']
    newlifeage = newlifedob['age']

    newlifehomephone = newlifeone['phone']
    newlifecellphone = newlifeone['cell']

    newlifepicture = newlifeone['picture']
    newlifelargepicture = newlifepicture['large']

    newlifecardr = requests.get('https://random-data-api.com/api/stripe/random_stripe')
    newlifecardurl = newlifecardr.url
    newlifecardrequest = requests.get(newlifecardurl)
    newlifecardtext_json = json.loads(newlifecardrequest.text)
    newlifecardparse_json = newlifecardtext_json
    newlifecarddata = newlifecardparse_json
    newlifcardnumber = newlifecarddata['valid_card']
    newlifcardmonth = newlifecarddata['month']
    newlifcardyear = newlifecarddata['year']
    newlifcardccv = newlifecarddata['ccv']
    newlifcardtoken = newlifecarddata['token']
    newlifecardtokenfix = newlifcardtoken.replace("tok_", "").title()
    newlifecardbrand = newlifecardtokenfix.replace("_", " ")


    embed = discord.Embed(
            title=newlifetitle + ". " + newlifefirstname + " " + newlifelastname,
            description='',
            color=embedhexfix,
        )
    embed.add_field(name="Gender:", value=newlifegender.title(), inline=False)
    embed.add_field(name="Address:", value=str(newlifestreetnumber) + " " + str(newlifestreetname) + ", " + str(newlifecity) + ", " + str(newlifestate) + ", " + str(newlifecountry) + ", " + str(newlifepostalcode), inline=False)
    embed.add_field(name="Email: ", value="Email: " + str(newlifeemail) + "\nUsername: " + str(newlifeloginusername) + "\nPassword: " + str(newlifeloginpassword), inline=False)
    embed.add_field(name="DOB: ", value="Date: " + str(newlifedobdate) + "\nAge: " + str(newlifeage), inline=False)
    embed.add_field(name="Phone: ", value="Home: " + str(newlifehomephone) + "\nCell: " + str(newlifecellphone), inline=False)
    embed.add_field(name="Card: ", value="Card Number: " + str(newlifcardnumber) + "\nCCV: " + str(newlifcardccv) + "\nCard Brand: " + str(newlifecardbrand) + "\nExpires: " + str(newlifcardmonth) + "/" + str(newlifcardyear), inline=False)
    embed.set_image(url=newlifelargepicture)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("NewLife Command Used By: {}".format(ctx.author))

@client.command()
async def yesorno(ctx):
    yesornor = requests.get('https://yesno.wtf/api')
    yesornourl = yesornor.url
    yesornorequest = requests.get(yesornourl)
    yesornotext_json = json.loads(yesornorequest.text)
    yesornoparse_json = yesornotext_json
    yesorno = yesornoparse_json['answer']
    yesornoimage = yesornoparse_json['image']
    embed = discord.Embed(
           title=yesorno.title(),

            color=embedhexfix,
        )
    embed.set_image(url=yesornoimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("YesORNo Command Used By: {}".format(ctx.author) + " | Yes or no?: " + yesorno)

@client.command()
async def insult(ctx):
    insultr = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    insulturl = insultr.url
    insultrequest = requests.get(insulturl)
    insulttext_json = json.loads(insultrequest.text)
    insultparse_json = insulttext_json
    insult = insultparse_json['insult']

    embed = discord.Embed(
           title=insult,

            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Insult Command Used By: {}".format(ctx.author) + " | Insult: " + insult)

@client.command()
async def ipconfig(ctx, arg):
    ipr = requests.get('https://api.techniknews.net/ipgeo/' + arg)
    ipurl = ipr.url
    iprequest = requests.get(ipurl)
    iptext_json = json.loads(iprequest.text)
    ipparse_json = iptext_json
    status = ipparse_json['status']
    continent = ipparse_json['continent']
    country = ipparse_json['country']
    countryCode = ipparse_json['countryCode']
    regionName = ipparse_json['regionName']
    city = ipparse_json['city']
    zip = ipparse_json['zip']
    timezone = ipparse_json['timezone']
    currency = ipparse_json['currency']
    isp = ipparse_json['isp']
    ip = ipparse_json['ip']

    embed = discord.Embed(
           title="Status: " + status.title(),

            color=embedhexfix,
        )

    embed.add_field(name="Continent: ", value=continent, inline=False)
    embed.add_field(name="Country: ", value=country, inline=False)
    embed.add_field(name="Country Code: ", value=countryCode, inline=False)
    embed.add_field(name="Region Name: ", value=regionName, inline=False)
    embed.add_field(name="City: ", value=city, inline=False)
    embed.add_field(name="Zip: ", value=zip, inline=False)
    embed.add_field(name="Timezone: ", value=timezone, inline=False)
    embed.add_field(name="Currency: ", value=currency, inline=False)
    embed.add_field(name="ISP: ", value=isp, inline=False)
    embed.add_field(name="IP: ", value=ip, inline=False)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("IP Command Used By: {}".format(ctx.author) + " | IP: " + arg)

@client.command(name="randomcolor",
            description="Shows a random color!",
            aliases=['randomcolour', 'rcolor', 'rcolour'],
            pass_context=True)
async def randomcolor(ctx):
    randomcolorr = requests.get('https://x-colors.herokuapp.com/api/random')
    randomcolorurl = randomcolorr.url
    randomcolorrequest = requests.get(randomcolorurl)
    randomcolortext_json = json.loads(randomcolorrequest.text)
    randomcolorparse_json = randomcolortext_json
    randomcolor = randomcolorparse_json['hex']
    randomcolorfixed = randomcolor.replace("#","")
    randomcolorembed = int(randomcolorfixed, 16)

    embed = discord.Embed(
           title=randomcolor,
           url='https://www.color-hex.com/color/' + randomcolorfixed,

            color=randomcolorembed
        )
    embed.set_image(url="https://plchldr.co/i/250x215?&bg=" + randomcolorfixed + "&text=")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Random Color Command Used By: {}".format(ctx.author) + " | Random Color: " + randomcolor)

@client.command()
async def boredactivity(ctx):
    boredr = requests.get('https://www.boredapi.com/api/activity')
    boredurl = boredr.url
    boredrequest = requests.get(boredurl)
    boredtext_json = json.loads(boredrequest.text)
    boredparse_json = boredtext_json
    boredactivity = boredparse_json['activity']
    boredactivitytype = boredparse_json['type']
    boredactivityparticipants = boredparse_json['participants']
    
    embed = discord.Embed(
           title='Bored Activity:',

           description=boredactivity + ".",
            color=embedhexfix,
        )

    embed.add_field(name="Type: ", value=boredactivitytype.title(), inline=True)
    embed.add_field(name="Participants: ", value=boredactivityparticipants, inline=True)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Bored Activity Command Used By: {}".format(ctx.author) + " | Activity: " + boredactivity)

@client.command()
async def time(ctx):
    timer = requests.get('https://icanhazepoch.com/')
    timeurl = timer.url
    timerequest = requests.get(timeurl)
    timetext_json = json.loads(timerequest.text)
    timeparse_json = timetext_json
    timeepoch = timeparse_json
    time = "<t:" + str(timeepoch) + ":F>"
    
    embed = discord.Embed(
           title='Time:',

           description=time,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Time Command Used By: {}".format(ctx.author) + " | Time: " + time)

@client.command()
async def qrurl(ctx, args):
    embed = discord.Embed(
           title='URL:',
           url=str(args),
           description="Link: " + str(args),
            color=embedhexfix,
        )
    embed.set_image(url='https://www.qrtag.net/api/qr_12.png?url=' + args)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("URL QR Command Used By: {}".format(ctx.author) + " | URL: " + str(args))

@client.command(name="lookup",
            description="Lookup a word.",
            brief="Define a word.",
            aliases=['search', 'define'],
            pass_context=True)
async def lookup(ctx, arg):
    lookupr = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + arg)
    lookupurl = lookupr.url
    lookuprequest = requests.get(lookupurl)
    lookuptext_json = json.loads(lookuprequest.text)
    lookupparse_json = lookuptext_json
    lookupnull = lookupparse_json[0]
    lookupword = lookupnull['word']

    lookupmeanings = lookupnull['meanings']
    lookupchoice = lookupmeanings[0]
    lookupdefinitions = lookupchoice['definitions']
    lookupdefinitionschoice = lookupdefinitions[0]

    lookupdefinition = lookupdefinitionschoice['definition']
    
    lookupexample = lookupdefinitionschoice['example']
    
    lookupsynonyms = lookupdefinitionschoice['synonyms']
    lookupsynonymslist = str(lookupsynonyms).replace("['", "").replace("']", "").replace("'", "")

    partofspeech = lookupchoice['partOfSpeech']


    embed = discord.Embed(
           title="__Define: " + lookupword.capitalize() + "__",

            color=embedhexfix,
        )
    embed.add_field(name="Type: ", value=partofspeech.capitalize(), inline=False)
    embed.add_field(name="Definition: ", value=lookupdefinition.capitalize(), inline=False)
    embed.add_field(name="Example: ", value=lookupexample.capitalize().replace(lookupword, "**" + lookupword + "**"), inline=False)
    embed.add_field(name="Synonyms: ", value=lookupsynonymslist.title(), inline=False)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Define Command Used By: {}".format(ctx.author) + " | Word: " + str(arg))

@client.command(name="yomomma",
            description="Sends a Yo Momma joke!",

            pass_context=True)
async def yomomma(ctx):
    yomommar = requests.get('https://sumisuyomomma-api.herokuapp.com/jokes')
    yomommaurl = yomommar.url
    yomommarequest = requests.get(yomommaurl)
    yomommatext_json = json.loads(yomommarequest.text)
    yomommaparse_json = yomommatext_json
    yomommajoke = yomommaparse_json['joke']
    
    embed = discord.Embed(


           description=yomommajoke,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Yo Momma Command Used By: {}".format(ctx.author) + " | Joke: " + yomommajoke)

@client.command(name="uselessfact",
            description="Sends a useless fact!",

            pass_context=True)
async def uselessfact(ctx):
    uselessfactr = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    uselessfacturl = uselessfactr.url
    uselessfactrequest = requests.get(uselessfacturl)
    uselessfacttext_json = json.loads(uselessfactrequest.text)
    uselessfactparse_json = uselessfacttext_json
    uselessfact = uselessfactparse_json['text']
    
    embed = discord.Embed(


           description=uselessfact,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Useless Fact Command Used By: {}".format(ctx.author) + " | Fact: " + uselessfact)

@client.command()
async def coffee(ctx):
    coffeeimager = requests.get('https://coffee.alexflipnote.dev/random.json')
    coffeeimageurl = coffeeimager.url
    coffeeimagerequest = requests.get(coffeeimageurl)
    coffeeimagetext_json = json.loads(coffeeimagerequest.text)
    coffeeimageparse_json = coffeeimagetext_json
    coffeeimage = coffeeimageparse_json['file']
    embed = discord.Embed(


            color=embedhexfix,
        )
    embed.set_image(url=coffeeimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Coffee Image Command Used By: {}".format(ctx.author) + " | Image URL: " + coffeeimage)


@client.command(name="mcskin",
            description="Show someones Minecraft Skin!",
            aliases=['mcs'],
            pass_context=True)
async def mcskin(ctx, arg):
    mcskinuuidr = requests.get('https://api.mojang.com/users/profiles/minecraft/' + arg)
    mcskinuuidurl = mcskinuuidr.url
    mcskinuuidrequest = requests.get(mcskinuuidurl)
    mcskinuuidtext_json = json.loads(mcskinuuidrequest.text)
    mcskinuuidparse_json = mcskinuuidtext_json
    mcskinselect = mcskinuuidparse_json
    mcskinuuid = mcskinselect['id']
    mcskinname = mcskinselect['name']

    embed = discord.Embed(
           title=mcskinname,

            color=embedhexfix,
        )
    embed.set_image(url="https://crafatar.com/renders/body/" + mcskinuuid + "?overlay")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("MC Skin Command Used By: {}".format(ctx.author) + " | UUID: " + str(mcskinname))

@client.command(name="mcskindownload",
            description="Download someones Minecraft Skin!",
            aliases=['mcsdownload'],
            pass_context=True)
async def mcskindownload(ctx, arg):
    mcskinuuidr = requests.get('https://api.mojang.com/users/profiles/minecraft/' + arg)
    mcskinuuidurl = mcskinuuidr.url
    mcskinuuidrequest = requests.get(mcskinuuidurl)
    mcskinuuidtext_json = json.loads(mcskinuuidrequest.text)
    mcskinuuidparse_json = mcskinuuidtext_json
    mcskinselect = mcskinuuidparse_json
    mcskinuuid = mcskinselect['id']
    mcskinname = mcskinselect['name']

    embed = discord.Embed(
           title="Download: " + mcskinname + "'s Skin!",
           url="https://crafatar.com/skins/" + mcskinuuid,

            color=embedhexfix,
        )
    embed.set_image(url="https://crafatar.com/skins/" + mcskinuuid)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("MC Skin Download Command Used By: {}".format(ctx.author) + " | UUID: " + str(mcskinname))

@client.command()
async def drawcard(ctx):
    drawcardimager = requests.get('http://deckofcardsapi.com/api/deck/new/draw/?count=1')
    drawcardimageurl = drawcardimager.url
    drawcardimagerequest = requests.get(drawcardimageurl)
    drawcardimagetext_json = json.loads(drawcardimagerequest.text)
    drawcardimageparse_json = drawcardimagetext_json
    drawcardimage = drawcardimageparse_json['cards']
    drawcarddata = drawcardimage[0]
    drawcardsuit = drawcarddata['suit']
    drawcardvalue = drawcarddata['value']
    drawcard = drawcarddata['image']
    drawcardcode = str(drawcardvalue).capitalize() + " of " + str(drawcardsuit).capitalize()
    embed = discord.Embed(
           title=drawcardcode,

            color=embedhexfix,
        )
    embed.set_image(url=drawcard)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Draw Card Command Used By: {}".format(ctx.author) + " | Card: " + str(drawcardcode))

@client.command(name="randomd6",
            description="See someones Minecraft Skin!",
            aliases=['d6', 'randomdie', 'randomdice'],
            pass_context=True)
async def randomd6(ctx):
    random6dimager = requests.get('http://roll.diceapi.com/json/d6')
    random6dimageurl = random6dimager.url
    random6dimagerequest = requests.get(random6dimageurl)
    random6dimagetext_json = json.loads(random6dimagerequest.text)
    random6dimageparse_json = random6dimagetext_json
    random6dimagedata = random6dimageparse_json['dice']
    random6dimageselect = random6dimagedata[0]
    random6dimagevalue = random6dimageselect['value']
    random6dimagevaluefixed = str(random6dimagevalue).replace("6", "Six").replace("5", "Five").replace("4", "Four").replace("3", "Three").replace("2", "Two").replace("1", "One")
 

    embed = discord.Embed(
           title=random6dimagevaluefixed,

            color=embedhexfix,
        )
    embed.set_image(url="http://roll.diceapi.com/images/poorly-drawn/d6/" + str(random6dimagevalue) + ".png")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Random D6 Command Used By: {}".format(ctx.author) + " | Die: " + str(random6dimagevaluefixed))

@client.command(name="randomd20",
            description="See someones Minecraft Skin!",
            aliases=['d20'],
            pass_context=True)
async def randomd20(ctx):
    randomd20imager = requests.get('http://roll.diceapi.com/json/d20')
    randomd20imageurl = randomd20imager.url
    randomd20imagerequest = requests.get(randomd20imageurl)
    randomd20imagetext_json = json.loads(randomd20imagerequest.text)
    randomd20imageparse_json = randomd20imagetext_json
    randomd20imagedata = randomd20imageparse_json['dice']
    randomd20imageselect = randomd20imagedata[0]
    randomd20imagevalue = randomd20imageselect['value']
    randomd20imagevaluefixed = str(randomd20imagevalue).replace("20", "Twenty").replace("19", "Nineteen").replace("18", "Eightteen").replace("17", "Seventeen").replace("16", "Sixteen").replace("15", "Fifteen").replace("14", "Fourteen").replace("13", "Thirteen").replace("12", "Twelve").replace("11", "Eleven").replace("10", "Ten").replace("9", "Nine").replace("8", "Eight").replace("7", "Seven").replace("6", "Six").replace("5", "Five").replace("4", "Four").replace("3", "Three").replace("2", "Two").replace("1", "One")
 

    embed = discord.Embed(
           title=randomd20imagevaluefixed,

            color=embedhexfix,
        )
    embed.set_image(url="http://roll.diceapi.com/images/poorly-drawn/d20/" + str(randomd20imagevalue) + ".png")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Random D20 Command Used By: {}".format(ctx.author) + " | Die: " + str(randomd20imagevaluefixed))

@client.command(name="covid",
            description="See someones Minecraft Skin!",
            aliases=['covidinfo', 'covidfacts'],
            pass_context=True)
async def covid(ctx):
    covidr = requests.get('https://api.quarantine.country/api/v1/summary/region?region=usa')
    covidurl = covidr.url
    covidrequest = requests.get(covidurl)
    covidtext_json = json.loads(covidrequest.text)
    covidparse_json = covidtext_json
    coviddata = covidparse_json['data']
    coviddatasummary = coviddata['summary']
    covidtotalcases = coviddatasummary['total_cases']
    covidactivecases = coviddatasummary['active_cases']
    covidrecovered = coviddatasummary['recovered']
    covidcritical = coviddatasummary['critical']

    embed = discord.Embed(
           title="Covid Information:",

            color=embedhexfix,
        )
    embed.add_field(name="Total Cases: ", value=covidtotalcases, inline=True)
    embed.add_field(name="Active Cases: ", value=covidactivecases, inline=True)
    
    embed.add_field(name="Recovered: ", value=covidrecovered, inline=True)
    embed.add_field(name="Critical: ", value=covidcritical, inline=True)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("COVID Information Command Used By: {}".format(ctx.author))

@client.command(name="hex",
            description="Shows the HEX color!",
            aliases=['hexcolor', 'hexcolour', 'hcolor', 'hcolour'],
            pass_context=True)
async def hex(ctx, args):
    hexr = requests.get('https://x-colors.herokuapp.com/api/hex2rgb?value=' + args)
    hexurl = hexr.url
    hexrequest = requests.get(hexurl)
    hextext_json = json.loads(hexrequest.text)
    hexparse_json = hextext_json
    hexcolor = hexparse_json['hex']
    hexcolorfixed = hexcolor.replace("#","")
    hexcolorembed = int(hexcolorfixed, 16)

    embed = discord.Embed(
           title=hexcolor,
           url='https://www.color-hex.com/color/' + args,

            color=hexcolorembed
        )
    embed.set_image(url="https://plchldr.co/i/250x215?&bg=" + hexcolorfixed + "&text=")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Hex Color Command Used By: {}".format(ctx.author) + " | Hex Color: " + hexcolor)

@client.command()
async def poll(ctx, *, content:str):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
            title="Poll asked by {}:".format(ctx.author),
            description="```{}``` \n✅ = Yes\n❌ = No\n".format(content),
            color=embedhexfix
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    message = await ctx.send(embed=embed)
    await message.add_reaction('❌')
    await message.add_reaction('✅')
    print("Poll Command Used By: {}".format(ctx.author) + " | Question: {}".format(content))

@client.command(name="latestyt",
            description="Shows the latest Youtube video from Channel_ID!",
            aliases=['lyt', 'lateyt', 'latestyoutubevideofrom', 'lytv'],
            pass_context=True)
async def latestyt(ctx, *, content:str):
    ytr = requests.get('https://rss-to-json-serverless-api.vercel.app/api?feedURL=https://www.youtube.com/feeds/videos.xml?channel_id={}'.format(content))
    yturl = ytr.url
    ytrequest = requests.get(yturl)
    yttext_json = json.loads(ytrequest.text)
    ytparse_json = yttext_json
    ytitems = ytparse_json['items'][0]
    yttitle = ytitems['title']
    ytvideourl = ytitems['url']
    ytthumbnail = ytitems['enclosures'][0]
    ytauthor = ytitems['author']

    embed = discord.Embed(
           title=yttitle,
           url=ytvideourl,
           description="Video made by: **{}**".format(ytauthor),
           color=embedhexfix
        )
    embed.set_image(url=ytthumbnail)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Latest Youtube Video Command Used By: {}".format(ctx.author) + " | Youtube Video: {}".format(ytvideourl))

@client.command(name="funfact",
            description="Shows a FunFact!",
            aliases=['ff'],
            pass_context=True)
async def funfact(ctx):
    ffr = requests.get('https://asli-fun-fact-api.herokuapp.com')
    ffurl = ffr.url
    ffrequest = requests.get(ffurl)
    fftext_json = json.loads(ffrequest.text)
    ffparse_json = fftext_json
    funfact = ffparse_json['data']['fact']

    embed = discord.Embed(
           title="Fun Fact:",
           description=funfact,
           color=embedhexfix
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Fun Fact Command Used By: {}".format(ctx.author) + " | Fun Fact: {}".format(funfact))

@client.command(name="trumpquote",
            description="Shows a random Trump Quote!",
            aliases=['tq'],
            pass_context=True)
async def trumpquote(ctx):
    trumpquoter = requests.get('https://www.tronalddump.io/random/quote')
    trumpquoteurl = trumpquoter.url
    trumpquoterequest = requests.get(trumpquoteurl)
    trumpquotetext_json = json.loads(trumpquoterequest.text)
    trumpquoteparse_json = trumpquotetext_json
    trumpquote = trumpquoteparse_json['value']

    embed = discord.Embed(
           title="Trump Quote:",
           description=trumpquote,
           color=embedhexfix
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Trump Quote Command Used By: {}".format(ctx.author) + " | Trump Quote: {}".format(trumpquote))

@client.command(name="steam",
            description="Shows Steam profile information!",
            aliases=['steamlookup', 'steaminfo'],
            pass_context=True)
async def steam(ctx, *, content:str):
    steamr = requests.get('https://playerdb.co/api/player/steam/{}'.format(content))
    steamurl = steamr.url
    steamrequest = requests.get(steamurl)
    steamtext_json = json.loads(steamrequest.text)
    steamparse_json = steamtext_json
    steamusername = steamparse_json['data']['player']['username']
    steamurl = steamparse_json['data']['player']['meta']['profileurl']
    steampfp = steamparse_json['data']['player']['meta']['avatarfull']
    steamrealname = steamparse_json['data']['player']['meta']['realname']
    steamloccountrycode = steamparse_json['data']['player']['meta']['loccountrycode']
    steamid = steamparse_json['data']['player']['id']

    embed = discord.Embed(
           title=steamusername,
           url=steamurl,
           color=embedhexfix
        )
    embed.add_field(name="Real Name: ", value=steamrealname, inline=True)
    embed.add_field(name="From: ", value=steamloccountrycode, inline=True)
    embed.add_field(name="ID: ", value=steamid, inline=False)
    embed.set_image(url=steampfp)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Steam Command Used By: {}".format(ctx.author) + " | User: {}".format(content))

@client.command(name="deal",
            description="Shows a FunFact!",
            aliases=['deals'],
            pass_context=True)
async def deal(ctx, *, content:str):
    r = requests.get('https://www.cheapshark.com/api/1.0/games?title={}&limit=1&exact=0'.format(content))
    url = r.url
    request = requests.get(url)
    text_json = json.loads(request.text)
    parse_json = text_json
    gameid = parse_json[0]['gameID']
    gamename = parse_json[0]['external']
    gamethumbnail = parse_json[0]['thumb']
    gamesteamid = parse_json[0]['steamAppID']

    dealr = requests.get('https://www.cheapshark.com/api/1.0/games?ids={}'.format(gameid))
    dealurl = dealr.url
    dealrequest = requests.get(dealurl)
    dealtext_json = json.loads(dealrequest.text)
    dealparse_json = dealtext_json
    cheapestdeal = dealparse_json[gameid]['cheapestPriceEver']['price']
    cheapestdealdate = dealparse_json[gameid]['cheapestPriceEver']['date']
    cheapestdealnow = dealparse_json[gameid]['deals'][0]['price']
    cheapestdealnowstore = dealparse_json[gameid]['deals'][0]['storeID']
    cheapestdealnowstorefixed = cheapestdealnowstore.replace("1", "Steam").replace("2", "GamersGate").replace("3", "GreenManGaming").replace("4", "Amazon").replace("5", "GameStop").replace("6", "Direct2Drive").replace("7", "GoG").replace("8", "Origin").replace("9", "Get Games").replace("10", "Shiny Loot").replace("11", "Humble Store").replace("12", "Desura").replace("13", "Uplay").replace("14", "IndieGameStand").replace("15", "Fanatical").replace("16", "Gamesrocket").replace("17", "Games Republic").replace("18", "SilaGames").replace("19", "Playfield").replace("20", "ImperialGames").replace("21", "WinGameStore").replace("22", "FunStockDigital").replace("23", "GameBillet").replace("24", "Voidu")


    embed = discord.Embed(
            title=gamename,
            url="https://store.steampowered.com/app/{}".format(gamesteamid),
            color=embedhexfix
        )
    embed.add_field(name="Cheapest Price Ever: ", value=cheapestdeal, inline=False)
    embed.add_field(name="On: ", value="<t:{}:F>".format(cheapestdealdate), inline=False)
    embed.add_field(name="Cheapest Price Currently: ", value=cheapestdealnow, inline=False)
    embed.add_field(name="From: ", value=cheapestdealnowstorefixed, inline=False)
    embed.set_image(url=gamethumbnail)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Deal Command Used By: {}".format(ctx.author) + " | Game: {}".format(content))


@client.command(name="randomquote",
            description="Shows a Random Quote!",
            aliases=['rq'],
            pass_context=True)
async def randomquote(ctx):
    randomquoter = requests.get('https://zenquotes.io/api/random')
    randomquoteurl = randomquoter.url
    randomquoterequest = requests.get(randomquoteurl)
    randomquotetext_json = json.loads(randomquoterequest.text)
    randomquoteparse_json = randomquotetext_json
    randomquote = randomquoteparse_json[0]['q']
    randomquoteauthor = randomquoteparse_json[0]['a']

    embed = discord.Embed(
           title="Random Quote:",
           description=randomquote,
           color=embedhexfix
        )
    embed.add_field(name="Author: ", value=randomquoteauthor, inline=False)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Random Quote Command Used By: {}".format(ctx.author) + " | Quote: {}".format(randomquote) + " | Quote Author: {}".format(randomquoteauthor))

@client.command(name="randommeal",
            description="Shows a Random Quote!",
            aliases=['meal', 'meals'],
            pass_context=True)
async def randommeal(ctx):
    randommealr = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    randommealurl = randommealr.url
    randommealrequest = requests.get(randommealurl)
    randommealtext_json = json.loads(randommealrequest.text)
    randommealparse_json = randommealtext_json
    randommeal = randommealparse_json['meals'][0]['strMeal']
    randommealsource = randommealparse_json['meals'][0]['strSource']
    randommealimage = randommealparse_json['meals'][0]['strMealThumb']
    randommealinstructions = randommealparse_json['meals'][0]['strInstructions']

    embed = discord.Embed(
           title=randommeal,
           url=randommealsource,
           description=randommealinstructions,
           color=embedhexfix
        )
    embed.set_image(url=randommealimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Random Meal Command Used By: {}".format(ctx.author) + " | Meal: {}".format(randommeal))

@client.command(name="randomdrink",
            description="Shows a Random Quote!",
            aliases=['cocktail', 'drinks', 'drink'],
            pass_context=True)
async def randomdrink(ctx):
    randomdrinkr = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
    randomdrinkurl = randomdrinkr.url
    randomdrinkrequest = requests.get(randomdrinkurl)
    randomdrinktext_json = json.loads(randomdrinkrequest.text)
    randomdrinkparse_json = randomdrinktext_json
    randomdrink = randomdrinkparse_json['drinks'][0]['strDrink']
    randomdrinkimage = randomdrinkparse_json['drinks'][0]['strDrinkThumb']
    randomdrinkinstructions = randomdrinkparse_json['drinks'][0]['strInstructions']

    embed = discord.Embed(
           title=randomdrink,
           description=randomdrinkinstructions,
           color=embedhexfix
        )
    embed.set_image(url=randomdrinkimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Random Drink Command Used By: {}".format(ctx.author) + " | Drink: {}".format(randommeal))

'''
@client.command()
async def purge(ctx, *, content:int):
    embed = discord.Embed(
            title="Purge:",
            description="{} Messages Purged!".format(content),
            color=embedhexfix
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.channel.purge(limit=content)
    await ctx.send(embed=embed)
    print("Purge Command Used By: {}".format(ctx.author) + " | Messages purged: {}".format(content))

@client.command()
async def purgeself(ctx, *, content:int):
    embed = discord.Embed(
            title="Purge:",
            description="{} Messages Purged!".format(content),
            color=embedhexfix
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.channel.purge(limit=content)
    print("Purge Self Command Used By: {}".format(ctx.author) + " | Messages purged: {}".format(content))
'''

@client.command(name="weather5",
            description="Shows weather forcast information!",
            aliases=['fivedayforcast', '5df', 'fdf'],
            pass_context=True)
async def weather5(ctx, *, content:str):
    import requests
    import time
    searchlocation = "{}".format(content)
    location = searchlocation.replace(",", "+")
    zipurl = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + location +"&format=json&limit=1"
    zipresponse = requests.get(zipurl).json()
    longitude = zipresponse[0]["lon"]
    latitude = zipresponse[0]["lat"]
    zipclass = zipresponse[0]["class"]
    try:
        if zipclass == "natural":
            city = zipresponse[0]["address"]["natural"]
            county = zipresponse[0]["address"]["county"]
            state = zipresponse[0]["address"]["state"]
            country = zipresponse[0]["address"]["country"]
        else:
            city = zipresponse[0]["address"]["city"]
            county = zipresponse[0]["address"]["county"]
            state = zipresponse[0]["address"]["state"]
            country = zipresponse[0]["address"]["country"]
    except:
        print("Weather Error!")


    r = requests.get('https://api.weather.gov/points/' + latitude + ',' + longitude)
    url = r.url
    request = requests.get(url)
    text_json = json.loads(request.text)
    parse_json = text_json
    forcasturl = parse_json['properties']['forecast']

    forecastresponse = requests.get(forcasturl).json()
    #################################################Forecast 1####################################################################
    forecast1name = forecastresponse["properties"]["periods"][0]["name"]
    forecast1temperatureunit = forecastresponse["properties"]["periods"][0]["temperatureUnit"]
    forecast1temperature = forecastresponse["properties"]["periods"][0]["temperature"]
    forecast1temperatureTrend = forecastresponse["properties"]["periods"][0]["temperatureTrend"]
    forecast1windspeed = forecastresponse["properties"]["periods"][0]["windSpeed"]
    forecast1winddirection = forecastresponse["properties"]["periods"][0]["windDirection"]
    forecast1icon = forecastresponse["properties"]["periods"][0]["icon"]
    forecast1shortforecast = forecastresponse["properties"]["periods"][0]["shortForecast"]
    forecast1detailedforecast = forecastresponse["properties"]["periods"][0]["detailedForecast"]
    embed1 = discord.Embed(
           title='Forcast For: ' + city,
           description=forecast1name + " it's " + forecast1shortforecast,
           color=embedhexfix
        )
    embed1.add_field(name="Temperature: ", value=str(forecast1temperature) + " °" + forecast1temperatureunit, inline=True)
    embed1.add_field(name="The tempature is: ", value=str(forecast1temperatureTrend).title().replace("None", "Stable"), inline=True)
    embed1.add_field(name="Wind: ", value=str(forecast1windspeed) + " " + forecast1winddirection, inline=True)
    embed1.add_field(name="Forecast: ", value=forecast1detailedforecast, inline=True)
    embed1.set_image(url=forecast1icon)
    embed1.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed1.set_footer(text="Made by: Sumisu®")



    #################################################Forecast 2####################################################################
    forecast2name = forecastresponse["properties"]["periods"][1]["name"]
    forecast2temperatureunit = forecastresponse["properties"]["periods"][1]["temperatureUnit"]
    forecast2temperature = forecastresponse["properties"]["periods"][1]["temperature"]
    forecast2temperatureTrend = forecastresponse["properties"]["periods"][1]["temperatureTrend"]
    forecast2windspeed = forecastresponse["properties"]["periods"][1]["windSpeed"]
    forecast2winddirection = forecastresponse["properties"]["periods"][1]["windDirection"]
    forecast2icon = forecastresponse["properties"]["periods"][1]["icon"]
    forecast2shortforecast = forecastresponse["properties"]["periods"][1]["shortForecast"]
    forecast2detailedforecast = forecastresponse["properties"]["periods"][1]["detailedForecast"]
    embed2 = discord.Embed(
           title='Forcast For: ' + city,
           description=forecast2name + " it's " + forecast2shortforecast,
           color=embedhexfix
        )
    embed2.add_field(name="Temperature: ", value=str(forecast2temperature) + " °" + forecast2temperatureunit, inline=True)
    embed2.add_field(name="The tempature is: ", value=str(forecast2temperatureTrend).title().replace("None", "Stable"), inline=True)
    embed2.add_field(name="Wind: ", value=str(forecast2windspeed) + " " + forecast2winddirection, inline=True)
    embed2.add_field(name="Forecast: ", value=forecast2detailedforecast, inline=True)
    embed2.set_image(url=forecast2icon)
    embed2.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed2.set_footer(text="Made by: Sumisu®")

    #################################################Forecast 3####################################################################
    forecast3name = forecastresponse["properties"]["periods"][2]["name"]
    forecast3temperatureunit = forecastresponse["properties"]["periods"][2]["temperatureUnit"]
    forecast3temperature = forecastresponse["properties"]["periods"][2]["temperature"]
    forecast3temperatureTrend = forecastresponse["properties"]["periods"][2]["temperatureTrend"]
    forecast3windspeed = forecastresponse["properties"]["periods"][2]["windSpeed"]
    forecast3winddirection = forecastresponse["properties"]["periods"][2]["windDirection"]
    forecast3icon = forecastresponse["properties"]["periods"][2]["icon"]
    forecast3shortforecast = forecastresponse["properties"]["periods"][2]["shortForecast"]
    forecast3detailedforecast = forecastresponse["properties"]["periods"][2]["detailedForecast"]
    embed3 = discord.Embed(
           title='Forcast For: ' + city,
           description=forecast3name + " it's " + forecast3shortforecast,
           color=embedhexfix
        )
    embed3.add_field(name="Temperature: ", value=str(forecast3temperature) + " °" + forecast3temperatureunit, inline=True)
    embed3.add_field(name="The tempature is: ", value=str(forecast3temperatureTrend).title().replace("None", "Stable"), inline=True)
    embed3.add_field(name="Wind: ", value=str(forecast3windspeed) + " " + forecast3winddirection, inline=True)
    embed3.add_field(name="Forecast: ", value=forecast3detailedforecast, inline=True)
    embed3.set_image(url=forecast3icon)
    embed3.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed3.set_footer(text="Made by: Sumisu®")

    #################################################Forecast 4####################################################################
    forecast4name = forecastresponse["properties"]["periods"][3]["name"]
    forecast4temperatureunit = forecastresponse["properties"]["periods"][3]["temperatureUnit"]
    forecast4temperature = forecastresponse["properties"]["periods"][3]["temperature"]
    forecast4temperatureTrend = forecastresponse["properties"]["periods"][3]["temperatureTrend"]
    forecast4windspeed = forecastresponse["properties"]["periods"][3]["windSpeed"]
    forecast4winddirection = forecastresponse["properties"]["periods"][3]["windDirection"]
    forecast4icon = forecastresponse["properties"]["periods"][3]["icon"]
    forecast4shortforecast = forecastresponse["properties"]["periods"][3]["shortForecast"]
    forecast4detailedforecast = forecastresponse["properties"]["periods"][3]["detailedForecast"]
    embed4 = discord.Embed(
           title='Forcast For: ' + city,
           description=forecast4name + " it's " + forecast4shortforecast,
           color=embedhexfix
        )
    embed4.add_field(name="Temperature: ", value=str(forecast4temperature) + " °" + forecast4temperatureunit, inline=True)
    embed4.add_field(name="The tempature is: ", value=str(forecast4temperatureTrend).title().replace("None", "Stable"), inline=True)
    embed4.add_field(name="Wind: ", value=str(forecast4windspeed) + " " + forecast4winddirection, inline=True)
    embed4.add_field(name="Forecast: ", value=forecast4detailedforecast, inline=True)
    embed4.set_image(url=forecast4icon)
    embed4.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed4.set_footer(text="Made by: Sumisu®")

    #################################################Forecast 5####################################################################
    forecast5name = forecastresponse["properties"]["periods"][4]["name"]
    forecast5temperatureunit = forecastresponse["properties"]["periods"][4]["temperatureUnit"]
    forecast5temperature = forecastresponse["properties"]["periods"][4]["temperature"]
    forecast5temperatureTrend = forecastresponse["properties"]["periods"][4]["temperatureTrend"]
    forecast5windspeed = forecastresponse["properties"]["periods"][4]["windSpeed"]
    forecast5winddirection = forecastresponse["properties"]["periods"][4]["windDirection"]
    forecast5icon = forecastresponse["properties"]["periods"][4]["icon"]
    forecast5shortforecast = forecastresponse["properties"]["periods"][4]["shortForecast"]
    forecast5detailedforecast = forecastresponse["properties"]["periods"][4]["detailedForecast"]
    embed5 = discord.Embed(
           title='Forcast For: ' + city,
           description=forecast5name + " it's " + forecast5shortforecast,
           color=embedhexfix
        )
    embed5.add_field(name="Temperature: ", value=str(forecast5temperature) + " °" + forecast5temperatureunit, inline=True)
    embed5.add_field(name="The tempature is: ", value=str(forecast5temperatureTrend).title().replace("None", "Stable"), inline=True)
    embed5.add_field(name="Wind: ", value=str(forecast5windspeed) + " " + forecast5winddirection, inline=True)
    embed5.add_field(name="Forecast: ", value=forecast5detailedforecast, inline=True)
    embed5.set_image(url=forecast5icon)
    embed5.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed5.set_footer(text="Made by: Sumisu®")

    await ctx.send(embed=embed1)
    time.sleep(5)
    await ctx.send(embed=embed2)
    time.sleep(5)
    await ctx.send(embed=embed3)
    time.sleep(5)
    await ctx.send(embed=embed4)
    time.sleep(5)
    await ctx.send(embed=embed5)
    print("Five Day Forecast Command Used By: {}".format(ctx.author) + " | Location: {}".format(content))

@client.command(name="dailyweather",
            description="Shows weather forcast information!",
            aliases=['dailyforecast', 'df', 'dw', 'weather'],
            pass_context=True)
async def dailyweather(ctx, *, content:str):
    import requests
    import time
    searchlocation = "{}".format(content)
    location = searchlocation.replace(",", "+")
    zipurl = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + location +"&format=json&limit=1"
    zipresponse = requests.get(zipurl).json()
    longitude = zipresponse[0]["lon"]
    latitude = zipresponse[0]["lat"]
    zipclass = zipresponse[0]["class"]
    try:
        if zipclass == "natural":
            city = zipresponse[0]["address"]["natural"]
            county = zipresponse[0]["address"]["county"]
            state = zipresponse[0]["address"]["state"]
            country = zipresponse[0]["address"]["country"]
        else:
            city = zipresponse[0]["address"]["city"]
            county = zipresponse[0]["address"]["county"]
            state = zipresponse[0]["address"]["state"]
            country = zipresponse[0]["address"]["country"]
    except:
        print("Daily Forecast Error!")


    r = requests.get('https://api.weather.gov/points/' + latitude + ',' + longitude)
    url = r.url
    request = requests.get(url)
    text_json = json.loads(request.text)
    parse_json = text_json
    forcasturl = parse_json['properties']['forecast']

    forecastresponse = requests.get(forcasturl).json()

    #################################################Forecast 1####################################################################
    forecast1name = forecastresponse["properties"]["periods"][0]["name"]
    forecast1temperatureunit = forecastresponse["properties"]["periods"][0]["temperatureUnit"]
    forecast1temperature = forecastresponse["properties"]["periods"][0]["temperature"]
    forecast1temperatureTrend = forecastresponse["properties"]["periods"][0]["temperatureTrend"]
    forecast1windspeed = forecastresponse["properties"]["periods"][0]["windSpeed"]
    forecast1winddirection = forecastresponse["properties"]["periods"][0]["windDirection"]
    forecast1icon = forecastresponse["properties"]["periods"][0]["icon"]
    forecast1shortforecast = forecastresponse["properties"]["periods"][0]["shortForecast"]
    forecast1detailedforecast = forecastresponse["properties"]["periods"][0]["detailedForecast"]
    embed = discord.Embed(
           title='Forcast For: ' + city,
           description=forecast1name + " it's " + forecast1shortforecast,
           color=embedhexfix
        )
    embed.add_field(name="Temperature: ", value=str(forecast1temperature) + " °" + forecast1temperatureunit, inline=True)
    embed.add_field(name="The tempature is: ", value=str(forecast1temperatureTrend).title().replace("None", "Stable"), inline=True)
    embed.add_field(name="Wind: ", value=str(forecast1windspeed) + " " + forecast1winddirection, inline=True)
    embed.add_field(name="Forecast: ", value=forecast1detailedforecast, inline=True)
    embed.set_image(url=forecast1icon)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")

    await ctx.send(embed=embed)
    print("Daily Forecast Command Used By: {}".format(ctx.author) + " | Location: {}".format(content))






























##################################################################################################################
#####################LOOPS##################LOOPS####################LOOPS########################################
##################################################################################################################

@tasks.loop(hours=24)
async def daily_color():
    target_channel_id = dailycolorchannel
    randomcolorr = requests.get('https://x-colors.herokuapp.com/api/random')
    randomcolorurl = randomcolorr.url
    randomcolorrequest = requests.get(randomcolorurl)
    randomcolortext_json = json.loads(randomcolorrequest.text)
    randomcolorparse_json = randomcolortext_json
    randomcolor = randomcolorparse_json['hex']
    randomcolorfixed = randomcolor.replace("#","")
    randomcolorembed = int(randomcolorfixed, 16)
    embed = discord.Embed(
        title="Color of the day: " + randomcolor,
        url='https://www.color-hex.com/color/' + randomcolorfixed,

        color=randomcolorembed
    )
    embed.set_image(url="https://plchldr.co/i/250x215?&bg=" + randomcolorfixed + "&text=")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    message_channel = client.get_channel(target_channel_id)
    await message_channel.send(embed=embed)

@tasks.loop(hours=1)
async def meme_of_the_hour():
    target_channel_id = memeofthehourchannel
    memeimager = requests.get('https://meme-api.herokuapp.com/gimme')
    memeimageurl = memeimager.url
    memeimagerequest = requests.get(memeimageurl)
    memeimagetext_json = json.loads(memeimagerequest.text)
    memeimageparse_json = memeimagetext_json
    memeimage = memeimageparse_json['url']
    memeauthorurl = memeimager.url
    memeauthorrequest = requests.get(memeauthorurl)
    memeauthortext_json = json.loads(memeauthorrequest.text)
    memeauthorparse_json = memeauthortext_json
    memeauthor = memeauthorparse_json['author']
    embed = discord.Embed(
        title="Meme of the hour:",
        url="https://www.reddit.com/user/{}".format(memeauthor),
        description="Made by: " + str(memeauthor),
        color=embedhexfix,
    )
    embed.set_image(url=memeimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    message_channel = client.get_channel(target_channel_id)
    await message_channel.send(embed=embed)

@tasks.loop(hours=24)
async def quote_of_the_day():
    target_channel_id = quoteofthedaychannel
    randomquoter = requests.get('https://zenquotes.io/api/random')
    randomquoteurl = randomquoter.url
    randomquoterequest = requests.get(randomquoteurl)
    randomquotetext_json = json.loads(randomquoterequest.text)
    randomquoteparse_json = randomquotetext_json
    randomquote = randomquoteparse_json[0]['q']
    randomquoteauthor = randomquoteparse_json[0]['a']
    embed = discord.Embed(
        title="Random Quote:",
        description=randomquote,
        color=embedhexfix
    )
    embed.add_field(name="Author: ", value=randomquoteauthor, inline=False)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    message_channel = client.get_channel(target_channel_id)
    await message_channel.send(embed=embed)

#################################################Daily Forecast####################################################################

@tasks.loop(hours=24)
async def daily_weather_forecast():
    target_channel_id = dailyweatherchannel
    import requests
    searchlocation = dailyweatherlocation
    location = searchlocation.replace(",", "+")
    zipurl = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + location +"&format=json&limit=1"
    zipresponse = requests.get(zipurl).json()
    longitude = zipresponse[0]["lon"]
    latitude = zipresponse[0]["lat"]
    zipclass = zipresponse[0]["class"]
    try:
        if zipclass == "natural":
            city = zipresponse[0]["address"]["natural"]
            county = zipresponse[0]["address"]["county"]
            state = zipresponse[0]["address"]["state"]
            country = zipresponse[0]["address"]["country"]
        else:
            city = zipresponse[0]["address"]["city"]
            county = zipresponse[0]["address"]["county"]
            state = zipresponse[0]["address"]["state"]
            country = zipresponse[0]["address"]["country"]
    except:
        print("Daily Forecast Error!")


    r = requests.get('https://api.weather.gov/points/' + latitude + ',' + longitude)
    url = r.url
    request = requests.get(url)
    text_json = json.loads(request.text)
    parse_json = text_json
    forcasturl = parse_json['properties']['forecast']

    forecastresponse = requests.get(forcasturl).json()

    forecast1name = forecastresponse["properties"]["periods"][0]["name"]
    forecast1temperatureunit = forecastresponse["properties"]["periods"][0]["temperatureUnit"]
    forecast1temperature = forecastresponse["properties"]["periods"][0]["temperature"]
    forecast1temperatureTrend = forecastresponse["properties"]["periods"][0]["temperatureTrend"]
    forecast1windspeed = forecastresponse["properties"]["periods"][0]["windSpeed"]
    forecast1winddirection = forecastresponse["properties"]["periods"][0]["windDirection"]
    forecast1icon = forecastresponse["properties"]["periods"][0]["icon"]
    forecast1shortforecast = forecastresponse["properties"]["periods"][0]["shortForecast"]
    forecast1detailedforecast = forecastresponse["properties"]["periods"][0]["detailedForecast"]
    embed = discord.Embed(
           title='Forcast For: ' + city,
           description=forecast1name + " it's " + forecast1shortforecast,
           color=embedhexfix
        )
    embed.add_field(name="Temperature: ", value=str(forecast1temperature) + " °" + forecast1temperatureunit, inline=True)
    embed.add_field(name="The tempature is: ", value=str(forecast1temperatureTrend).title().replace("None", "Stable"), inline=True)
    embed.add_field(name="Wind: ", value=str(forecast1windspeed) + " " + forecast1winddirection, inline=True)
    embed.add_field(name="Forecast: ", value=forecast1detailedforecast, inline=True)
    embed.set_image(url=forecast1icon)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")

    message_channel = client.get_channel(target_channel_id)
    await message_channel.send(embed=embed)
















































##################################################################################################################
#####################LIGHTS##################LIGHTS####################LIGHTS################LIGHTS###############
##################################################################################################################
'''
@client.command(name="lightson",
            description="Turn my lights on!",
            aliases=['lighton', 'on'],
            pass_context=True)
async def lightson(ctx):
    import requests
    api_url = "http://10.0.0.4/api/jlxCFrG2Nt64uPaCuIo8YA7Yc0uAqe12IkE2lMh1/lights/4/state"
    todo = {"on": True}
    response = requests.put(api_url, json=todo)
    response.json()
    {'on': True}

    embed = discord.Embed(
           title="Lights On",
           description="Turned on bedroom lights!",
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Light On Command Used By: {}".format(ctx.author))

@client.command(name="lightsoff",
            description="Turn my lights on!",
            aliases=['lightoff', 'off'],
            pass_context=True)
async def lightsoff(ctx):
    import requests
    api_url = "http://10.0.0.4/api/jlxCFrG2Nt64uPaCuIo8YA7Yc0uAqe12IkE2lMh1/lights/4/state"
    todo = {"on": False}
    response = requests.put(api_url, json=todo)
    response.json()
    {'on': False}

    embed = discord.Embed(
           title="Lights Off",
           description="Turned off bedroom lights!",
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Light Off Command Used By: {}".format(ctx.author))

@client.command(name="lightbri",
            description="Set light brightness!",
            aliases=['lbri', 'bri'],
            pass_context=True)
async def lightbri(ctx, arg):
    from phue import Bridge
    b = Bridge('10.0.0.4')
    lights = b.lights
    b.set_light(4, 'bri', int(arg))
    embed = discord.Embed(
           title="Light Brightness:",
           description="Set lights to: " + arg,
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Light Brightness Command Used By: {}".format(ctx.author) + " | Brightness: " + str(arg))
'''
##################################################################################################################


















































































































##########################################################################################
################################Slash Command Zone########################################
##########################################################################################
slash = SlashCommand(client, sync_commands=True)

@slash.slash(
    name="help",
    description="Error: Use " + cmdprfx + "help `pagenumber` (with no spaces) for help!"
)
async def _help(ctx:SlashContext):
    embed = discord.Embed(
            title="Error:",
            description="Use " + cmdprfx + "help`pagenumber` (with no spaces) for help!",
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.author.send(embed=embed)
    print("/Help Command Used By: {}".format(ctx.author))

@slash.slash(
    name="help1",
    description="Commands Page 1: A list of all the commands that you can use with SumisuBot!"
)
async def _help1(ctx):
        embed = discord.Embed(
                title="Commands Page 1:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )

        embed.add_field(name=cmdprfx + "mc `server`", value="Allows you to look up information about a minecraft server!", inline=True)
        embed.add_field(name=cmdprfx + "catfact", value="Tells you a random fact about cats!", inline=True)
        embed.add_field(name=cmdprfx + "cat", value="Displays a random cat image!", inline=True)
        embed.add_field(name=cmdprfx + "meme", value="Shows you a random meme!", inline=True)
        embed.add_field(name=cmdprfx + "food", value="Shows a random image of food!", inline=True)
        embed.add_field(name=cmdprfx + "age", value="Tells you when your account was created!", inline=True)
        embed.add_field(name=cmdprfx + "baka", value="Sends a baka anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "bite", value="Sends a biting anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "blush", value="Sends a blushing anime gif in chat!", inline=True)

        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.send(embed=embed)
        print("/Help Page 1 Command Used By: {}".format(ctx.author))

@slash.slash(
    name="help2",
    description="Commands Page 2: A list of all the commands that you can use with SumisuBot!"
)
async def _help2(ctx):
        embed = discord.Embed(
                title="Commands Page 2:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )

        embed.add_field(name=cmdprfx + "bored", value="Sends a bored anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "cry", value="Sends a crying anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "cuddle", value="Sends a cuddling anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "dance", value="Sends a dancing anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "facepalm", value="For when someone does something **REALLY** stupid!", inline=True)
        embed.add_field(name=cmdprfx + "feed", value="Sends a feeding anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "happy", value="Sends a happy gif on anime!", inline=True)
        embed.add_field(name=cmdprfx + "highfive", value="Sends a highfiving anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "hug", value="Sends a huging anime gif in chat!", inline=True)
        
        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.send(embed=embed)
        print("/Help Page 2 Command Used By: {}".format(ctx.author))

@slash.slash(
    name="help3",
    description="Commands Page 3: A list of all the commands that you can use with SumisuBot!"
)
async def _help3(ctx):
        embed = discord.Embed(
                title="Commands Page 3:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )

        embed.add_field(name=cmdprfx + "kiss", value="Sends a kissing anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "laugh", value="Sends a laughing anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "nekos", value="Cat Girls!", inline=True)
        embed.add_field(name=cmdprfx + "newlife", value="Use this for when you need to start a new life, and go on the run!", inline=True)
        embed.add_field(name=cmdprfx + "pat", value="Sends a patting anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "poke", value="Sends a poking anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "pout", value="Sends a pouting anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "shrug", value="Sends a shrugging anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "slap", value="When you really want to slap the $4IT out of someone!", inline=True)
        
        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.send(embed=embed)
        print("/Help Page 3 Command Used By: {}".format(ctx.author))

@slash.slash(
    name="help4",
    description="Commands Page 4: A list of all the commands that you can use with SumisuBot!"
)
async def _help4(ctx):
        embed = discord.Embed(
                title="Commands Page 4:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )

        embed.add_field(name=cmdprfx + "sleep", value="Use this when you get sleepy!", inline=True)
        embed.add_field(name=cmdprfx + "smile", value="Say Cheese!", inline=True)
        embed.add_field(name=cmdprfx + "smug", value="Shady shady shady...", inline=True)
        embed.add_field(name=cmdprfx + "stare", value="O.O", inline=True)
        embed.add_field(name=cmdprfx + "think", value="Brain blast!", inline=True)
        embed.add_field(name=cmdprfx + "thumbsup", value="You did good! You deserve it!", inline=True)
        embed.add_field(name=cmdprfx + "tickle", value="Sends a tickling anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "wave", value="Sends a waving anime gif in chat!", inline=True)
        embed.add_field(name=cmdprfx + "wink", value="Sends a winking anime gif in chat!", inline=True)
        
        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.send(embed=embed)
        print("/Help Page 4 Command Used By: {}".format(ctx.author))

@slash.slash(
    name="help5",
    description="Commands Page 5: A list of all the commands that you can use with SumisuBot!"
)
async def _help5(ctx):
        embed = discord.Embed(
                title="Commands Page 5:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )
        embed.add_field(name=cmdprfx + "yesorno", value="When you can't decide, let someone else!", inline=True)
        embed.add_field(name=cmdprfx + "insult", value="Fuck 'em!", inline=True)
        embed.add_field(name=cmdprfx + "ipconfig `ipaddress`", value="Get information about an IP Address.", inline=True)
        embed.add_field(name=cmdprfx + "randomcolor", value="Sends a random HEX color with example!", inline=True)
        embed.add_field(name=cmdprfx + "boredactivity", value="Gives you an activity to do when you are bored!", inline=True)
        embed.add_field(name=cmdprfx + "time", value="Tells you the current time!", inline=True)
        embed.add_field(name=cmdprfx + "qrurl `url`", value="Turns the URL into a QR Code!", inline=True)
        embed.add_field(name=cmdprfx + "lookup `word`", value="Defines a word!", inline=True)

        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.send(embed=embed)
        print("Help Page 5 Command Used By: {}".format(ctx.author))

@slash.slash(
    name="help6",
    description="Commands Page 6: A list of all the commands that you can use with SumisuBot!"
)
async def _help6(ctx):
        embed = discord.Embed(
                title="Commands Page 6:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )
        embed.add_field(name=cmdprfx + "yomomma", value="Sends a Yo Momma Joke!", inline=True)
        embed.add_field(name=cmdprfx + "uselessfact", value="Sends a useless fact!", inline=True)
        embed.add_field(name=cmdprfx + "coffee", value="Sends a picture of coffee!", inline=True)
        embed.add_field(name=cmdprfx + "mcskin `username`", value="Show someones Minecraft Skin!", inline=True)
        embed.add_field(name=cmdprfx + "mcskindownload `username`", value="Download someones Minecraft Skin!", inline=True)
        embed.add_field(name=cmdprfx + "drawcard", value="Draws a random playing card!", inline=True)
        embed.add_field(name=cmdprfx + "D6", value="Rolls a D6 dice!", inline=True)
        embed.add_field(name=cmdprfx + "D20", value="Rolls a D20 dice!", inline=True)

        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.send(embed=embed)
        print("Help Page 6 Command Used By: {}".format(ctx.author))

@slash.slash(
    name="help7",
    description="Commands Page 7: A list of all the commands that you can use with SumisuBot!"
)
async def _help7(ctx):
        embed = discord.Embed(
                title="Commands Page 7:",
                description="A list of all the commands that you can use with SumisuBot!",
                color=embedhexfix,
            )
        embed.add_field(name=cmdprfx + "covid", value="Show's current COVID info!", inline=True)

        embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
        embed.set_footer(text="Made by: Sumisu®")
        await ctx.send(embed=embed)
        print("Help Page 7 Command Used By: {}".format(ctx.author))

@slash.slash(
    name="catfact",
    description="Tells you a random fact about cats!"
)
async def _catfact(ctx):
    r = requests.get('https://meowfacts.herokuapp.com/')
    catfacturl = r.url
    catrequest = requests.get(catfacturl)
    text_json = json.loads(catrequest.text)
    parse_json = text_json
    catfact = parse_json['data']
    cleancatfact = str(catfact).replace("['", "").replace("']", "").replace('"]', '').replace('["', '')

    catimager = requests.get('https://aws.random.cat/meow')
    catimageurl = catimager.url
    catimagerequest = requests.get(catimageurl)
    catimagetext_json = json.loads(catimagerequest.text)
    catimageparse_json = catimagetext_json
    catimage = catimageparse_json['file']
    embed = discord.Embed(
            title="CatFact!",
            description='\n\n**Fact:** ' + cleancatfact,
            color=embedhexfix,
        )

    embed.set_thumbnail(url=catimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")

    await ctx.send(embed=embed)
    print("/Cat Fact Command Used By: {}".format(ctx.author) + " | Cat Fact: " + cleancatfact)

@slash.slash(
    name="cat",
    description="Displays a random cat image!"
)
async def _cat(ctx):
    catimager = requests.get('https://aws.random.cat/meow')
    catimageurl = catimager.url
    catimagerequest = requests.get(catimageurl)
    catimagetext_json = json.loads(catimagerequest.text)
    catimageparse_json = catimagetext_json
    catimage = catimageparse_json['file']
    embed = discord.Embed(


            color=embedhexfix,
        )
    embed.set_image(url=catimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Cat Image Command Used By: {}".format(ctx.author) + " | Image URL: " + catimage)

@slash.slash(
    name="meme",
    description="Shows you a random meme!"
)
async def _meme(ctx):
    memeimager = requests.get('https://meme-api.herokuapp.com/gimme')
    memeimageurl = memeimager.url
    memeimagerequest = requests.get(memeimageurl)
    memeimagetext_json = json.loads(memeimagerequest.text)
    memeimageparse_json = memeimagetext_json
    memeimage = memeimageparse_json['url']
    memeauthorurl = memeimager.url
    memeauthorrequest = requests.get(memeauthorurl)
    memeauthortext_json = json.loads(memeauthorrequest.text)
    memeauthorparse_json = memeauthortext_json
    memeauthor = memeauthorparse_json['author']

    
    embed = discord.Embed(

            description="Made by: " + str(memeauthor),
            color=embedhexfix,
        )
    embed.set_image(url=memeimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Meme Image Command Used By: {}".format(ctx.author) + " | Image URL: " + str(memeimage))

@slash.slash(
    name="hello",
    description="Greets you!"
)
async def _hello(ctx):
    greetings = random.choice(randomgreetings)
    embed = discord.Embed(
            title=greetings,
            description=ctx.author.mention,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Hello Command Used By: {}".format(ctx.author) + " | Greeting used: " + greetings)

@slash.slash(
    name="hi",
    description="Greets you!"
)
async def _hi(ctx):
    greetings = random.choice(randomgreetings)
    embed = discord.Embed(
            title=greetings,
            description=ctx.author.mention,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Hi Command Used By: {}".format(ctx.author) + " | Greeting used: " + greetings)

@slash.slash(
    name="hey",
    description="Greets you!"
)
async def _hey(ctx):
    greetings = random.choice(randomgreetings)
    embed = discord.Embed(
            title=greetings,
            description=ctx.author.mention,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Hey Command Used By: {}".format(ctx.author) + " | Greeting used: " + greetings)

@slash.slash(
    name="food",
    description="Shows you a random meme!"
)
async def _food(ctx):
    foodimager = requests.get('https://foodish-api.herokuapp.com/api')
    foodimageurl = foodimager.url
    foodimagerequest = requests.get(foodimageurl)
    foodimagetext_json = json.loads(foodimagerequest.text)
    foodimageparse_json = foodimagetext_json
    foodimage = foodimageparse_json['image']
    embed = discord.Embed(

           description="Food Image: ",
            color=embedhexfix,
        )
    embed.set_image(url=foodimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Food Image Command Used By: {}".format(ctx.author) + " | Image URL: " + foodimage)

@slash.slash(
    name="age",
    description="Tells you when your account was created!"
)
async def _age(ctx):
    accountage = ctx.author.created_at
    date = accountage
    utc_time = calendar.timegm(date.utctimetuple())
    embed = discord.Embed(
           title="Account Age: <t:{}:R>".format(utc_time),
           description=ctx.author.mention + "\n\nYour account was created on: **" + accountage.strftime('%B %d %Y') + " at " + accountage.strftime('%I:%M:%S %p') + "**",
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Age Command Used By: {}".format(ctx.author) + " | Account Age: " + accountage.strftime('%B %d %Y') + " at " + accountage.strftime('%I:%M:%S %p'))


@slash.slash(
    name="baka",
    description="Sends a baka anime gif in chat!"
)
async def _baka(ctx):
    bakaimager = requests.get('https://nekos.best/api/v1/baka')
    bakaimageurl = bakaimager.url
    bakaimagerequest = requests.get(bakaimageurl)
    bakaimagetext_json = json.loads(bakaimagerequest.text)
    bakaimageparse_json = bakaimagetext_json
    bakaimage = bakaimageparse_json['url']
    bakaname = bakaimageparse_json['anime_name']
    embed = discord.Embed(

           description=bakaname,
            color=embedhexfix,
        )
    embed.set_image(url=bakaimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Baka Image Command Used By: {}".format(ctx.author) + " | Image URL: " + bakaimage)

@slash.slash(
    name="bite",
    description="Sends a biting anime gif in chat!"
)
async def _bite(ctx):
    biteimager = requests.get('https://nekos.best/api/v1/bite')
    biteimageurl = biteimager.url
    biteimagerequest = requests.get(biteimageurl)
    biteimagetext_json = json.loads(biteimagerequest.text)
    biteimageparse_json = biteimagetext_json
    biteimage = biteimageparse_json['url']
    bitename = biteimageparse_json['anime_name']
    embed = discord.Embed(

           description=bitename,
            color=embedhexfix,
        )
    embed.set_image(url=biteimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Bite Image Command Used By: {}".format(ctx.author) + " | Image URL: " + biteimage)

@slash.slash(
    name="blush",
    description="Sends a blushing anime gif in chat!"
)
async def _blush(ctx):
    blushimager = requests.get('https://nekos.best/api/v1/blush')
    blushimageurl = blushimager.url
    blushimagerequest = requests.get(blushimageurl)
    blushimagetext_json = json.loads(blushimagerequest.text)
    blushimageparse_json = blushimagetext_json
    blushimage = blushimageparse_json['url']
    blushname = blushimageparse_json['anime_name']
    embed = discord.Embed(

           description=blushname,
            color=embedhexfix,
        )
    embed.set_image(url=blushimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Blush Image Command Used By: {}".format(ctx.author) + " | Image URL: " + blushimage)

@slash.slash(
    name="bored",
    description="Sends a bored anime gif in chat!"
)
async def _bored(ctx):
    boredimager = requests.get('https://nekos.best/api/v1/bored')
    boredimageurl = boredimager.url
    boredimagerequest = requests.get(boredimageurl)
    boredimagetext_json = json.loads(boredimagerequest.text)
    boredimageparse_json = boredimagetext_json
    boredimage = boredimageparse_json['url']
    boredname = boredimageparse_json['anime_name']
    embed = discord.Embed(

           description=boredname,
            color=embedhexfix,
        )
    embed.set_image(url=boredimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Bored Image Command Used By: {}".format(ctx.author) + " | Image URL: " + boredimage)

@slash.slash(
    name="cry",
    description="Sends a crying anime gif in chat!"
)
async def _cry(ctx):
    cryimager = requests.get('https://nekos.best/api/v1/cry')
    cryimageurl = cryimager.url
    cryimagerequest = requests.get(cryimageurl)
    cryimagetext_json = json.loads(cryimagerequest.text)
    cryimageparse_json = cryimagetext_json
    cryimage = cryimageparse_json['url']
    cryname = cryimageparse_json['anime_name']
    embed = discord.Embed(

           description=cryname,
            color=embedhexfix,
        )
    embed.set_image(url=cryimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Cry Image Command Used By: {}".format(ctx.author) + " | Image URL: " + cryimage)

@slash.slash(
    name="cuddle",
    description="Sends a cuddling anime gif in chat!"
)
async def _cuddle(ctx):
    cuddleimager = requests.get('https://nekos.best/api/v1/cuddle')
    cuddleimageurl = cuddleimager.url
    cuddleimagerequest = requests.get(cuddleimageurl)
    cuddleimagetext_json = json.loads(cuddleimagerequest.text)
    cuddleimageparse_json = cuddleimagetext_json
    cuddleimage = cuddleimageparse_json['url']
    cuddlename = cuddleimageparse_json['anime_name']
    embed = discord.Embed(

           description=cuddlename,
            color=embedhexfix,
        )
    embed.set_image(url=cuddleimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Cuddle Image Command Used By: {}".format(ctx.author) + " | Image URL: " + cuddleimage)

@slash.slash(
    name="dance",
    description="Sends a dancing anime gif in chat!"
)
async def _dance(ctx):
    danceimager = requests.get('https://nekos.best/api/v1/dance')
    danceimageurl = danceimager.url
    danceimagerequest = requests.get(danceimageurl)
    danceimagetext_json = json.loads(danceimagerequest.text)
    danceimageparse_json = danceimagetext_json
    danceimage = danceimageparse_json['url']
    dancename = danceimageparse_json['anime_name']
    embed = discord.Embed(

           description=dancename,
            color=embedhexfix,
        )
    embed.set_image(url=danceimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Dance Image Command Used By: {}".format(ctx.author) + " | Image URL: " + danceimage)

@slash.slash(
    name="facepalm",
    description="For when someone does something REALLY stupid!"
)
async def _facepalm(ctx):
    facepalmimager = requests.get('https://nekos.best/api/v1/facepalm')
    facepalmimageurl = facepalmimager.url
    facepalmimagerequest = requests.get(facepalmimageurl)
    facepalmimagetext_json = json.loads(facepalmimagerequest.text)
    facepalmimageparse_json = facepalmimagetext_json
    facepalmimage = facepalmimageparse_json['url']
    facepalmname = facepalmimageparse_json['anime_name']
    embed = discord.Embed(

           description=facepalmname,
            color=embedhexfix,
        )
    embed.set_image(url=facepalmimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Facepalm Image Command Used By: {}".format(ctx.author) + " | Image URL: " + facepalmimage)

@slash.slash(
    name="feed",
    description="Sends a feeding anime gif in chat!"
)
async def _feed(ctx):
    feedimager = requests.get('https://nekos.best/api/v1/feed')
    feedimageurl = feedimager.url
    feedimagerequest = requests.get(feedimageurl)
    feedimagetext_json = json.loads(feedimagerequest.text)
    feedimageparse_json = feedimagetext_json
    feedimage = feedimageparse_json['url']
    feedname = feedimageparse_json['anime_name']
    embed = discord.Embed(

           description=feedname,
            color=embedhexfix,
        )
    embed.set_image(url=feedimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Feed Image Command Used By: {}".format(ctx.author) + " | Image URL: " + feedimage)

@slash.slash(
    name="happy",
    description="Sends a happy gif on anime!"
)
async def _happy(ctx):
    happyimager = requests.get('https://nekos.best/api/v1/happy')
    happyimageurl = happyimager.url
    happyimagerequest = requests.get(happyimageurl)
    happyimagetext_json = json.loads(happyimagerequest.text)
    happyimageparse_json = happyimagetext_json
    happyimage = happyimageparse_json['url']
    happyname = happyimageparse_json['anime_name']
    embed = discord.Embed(

           description=happyname,
            color=embedhexfix,
        )
    embed.set_image(url=happyimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Happy Image Command Used By: {}".format(ctx.author) + " | Image URL: " + happyimage)

@slash.slash(
    name="highfive",
    description="Sends a highfiving anime gif in chat!"
)
async def _highfive(ctx):
    highfiveimager = requests.get('https://nekos.best/api/v1/highfive')
    highfiveimageurl = highfiveimager.url
    highfiveimagerequest = requests.get(highfiveimageurl)
    highfiveimagetext_json = json.loads(highfiveimagerequest.text)
    highfiveimageparse_json = highfiveimagetext_json
    highfiveimage = highfiveimageparse_json['url']
    highfivename = highfiveimageparse_json['anime_name']
    embed = discord.Embed(

           description=highfivename,
            color=embedhexfix,
        )
    embed.set_image(url=highfiveimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Highfive Image Command Used By: {}".format(ctx.author) + " | Image URL: " + highfiveimage)

@slash.slash(
    name="hug",
    description="Sends a huging anime gif in chat!"
)
async def _hug(ctx):
    hugimager = requests.get('https://nekos.best/api/v1/hug')
    hugimageurl = hugimager.url
    hugimagerequest = requests.get(hugimageurl)
    hugimagetext_json = json.loads(hugimagerequest.text)
    hugimageparse_json = hugimagetext_json
    hugimage = hugimageparse_json['url']
    hugname = hugimageparse_json['anime_name']
    embed = discord.Embed(

           description=hugname,
            color=embedhexfix,
        )
    embed.set_image(url=hugimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Hug Image Command Used By: {}".format(ctx.author) + " | Image URL: " + hugimage)

@slash.slash(
    name="kiss",
    description="Sends a kissing anime gif in chat!"
)
async def _kiss(ctx):
    kissimager = requests.get('https://nekos.best/api/v1/kiss')
    kissimageurl = kissimager.url
    kissimagerequest = requests.get(kissimageurl)
    kissimagetext_json = json.loads(kissimagerequest.text)
    kissimageparse_json = kissimagetext_json
    kissimage = kissimageparse_json['url']
    kissname = kissimageparse_json['anime_name']
    embed = discord.Embed(

           description=kissname,
            color=embedhexfix,
        )
    embed.set_image(url=kissimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Kiss Image Command Used By: {}".format(ctx.author) + " | Image URL: " + kissimage)

@slash.slash(
    name="laugh",
    description="Sends a laughing anime gif in chat!"
)
async def _laugh(ctx):
    laughimager = requests.get('https://nekos.best/api/v1/laugh')
    laughimageurl = laughimager.url
    laughimagerequest = requests.get(laughimageurl)
    laughimagetext_json = json.loads(laughimagerequest.text)
    laughimageparse_json = laughimagetext_json
    laughimage = laughimageparse_json['url']
    laughname = laughimageparse_json['anime_name']
    embed = discord.Embed(

           description=laughname,
            color=embedhexfix,
        )
    embed.set_image(url=laughimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Laugh Image Command Used By: {}".format(ctx.author) + " | Image URL: " + laughimage)

@slash.slash(
    name="pat",
    description="Sends a patting anime gif in chat!"
)
async def _pat(ctx):
    patimager = requests.get('https://nekos.best/api/v1/pat')
    patimageurl = patimager.url
    patimagerequest = requests.get(patimageurl)
    patimagetext_json = json.loads(patimagerequest.text)
    patimageparse_json = patimagetext_json
    patimage = patimageparse_json['url']
    patname = patimageparse_json['anime_name']
    embed = discord.Embed(

           description=patname,
            color=embedhexfix,
        )
    embed.set_image(url=patimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Pat Image Command Used By: {}".format(ctx.author) + " | Image URL: " + patimage)

@slash.slash(
    name="poke",
    description="Sends a poking anime gif in chat!"
)
async def _poke(ctx):
    pokeimager = requests.get('https://nekos.best/api/v1/poke')
    pokeimageurl = pokeimager.url
    pokeimagerequest = requests.get(pokeimageurl)
    pokeimagetext_json = json.loads(pokeimagerequest.text)
    pokeimageparse_json = pokeimagetext_json
    pokeimage = pokeimageparse_json['url']
    pokename = pokeimageparse_json['anime_name']
    embed = discord.Embed(

           description=pokename,
            color=embedhexfix,
        )
    embed.set_image(url=pokeimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Poke Image Command Used By: {}".format(ctx.author) + " | Image URL: " + pokeimage)

@slash.slash(
    name="pout",
    description="Sends a pouting anime gif in chat!"
)
async def _pout(ctx):
    poutimager = requests.get('https://nekos.best/api/v1/pout')
    poutimageurl = poutimager.url
    poutimagerequest = requests.get(poutimageurl)
    poutimagetext_json = json.loads(poutimagerequest.text)
    poutimageparse_json = poutimagetext_json
    poutimage = poutimageparse_json['url']
    poutname = poutimageparse_json['anime_name']
    embed = discord.Embed(

           description=poutname,
            color=embedhexfix,
        )
    embed.set_image(url=poutimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Pout Image Command Used By: {}".format(ctx.author) + " | Image URL: " + poutimage)

@slash.slash(
    name="shrug",
    description="Sends a shrugging anime gif in chat!"
)
async def _shrug(ctx):
    shrugimager = requests.get('https://nekos.best/api/v1/shrug')
    shrugimageurl = shrugimager.url
    shrugimagerequest = requests.get(shrugimageurl)
    shrugimagetext_json = json.loads(shrugimagerequest.text)
    shrugimageparse_json = shrugimagetext_json
    shrugimage = shrugimageparse_json['url']
    shrugname = shrugimageparse_json['anime_name']
    embed = discord.Embed(

           description=shrugname,
            color=embedhexfix,
        )
    embed.set_image(url=shrugimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Shrug Image Command Used By: {}".format(ctx.author) + " | Image URL: " + shrugimage)

@slash.slash(
    name="slap",
    description="When you really want to slap the $4IT out of someone!"
)
async def _slap(ctx):
    slapimager = requests.get('https://nekos.best/api/v1/slap')
    slapimageurl = slapimager.url
    slapimagerequest = requests.get(slapimageurl)
    slapimagetext_json = json.loads(slapimagerequest.text)
    slapimageparse_json = slapimagetext_json
    slapimage = slapimageparse_json['url']
    slapname = slapimageparse_json['anime_name']
    embed = discord.Embed(

           description=slapname,
            color=embedhexfix,
        )
    embed.set_image(url=slapimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Slap Image Command Used By: {}".format(ctx.author) + " | Image URL: " + slapimage)

@slash.slash(
    name="sleep",
    description="Use this when you get sleepy!"
)
async def _sleep(ctx):
    sleepimager = requests.get('https://nekos.best/api/v1/sleep')
    sleepimageurl = sleepimager.url
    sleepimagerequest = requests.get(sleepimageurl)
    sleepimagetext_json = json.loads(sleepimagerequest.text)
    sleepimageparse_json = sleepimagetext_json
    sleepimage = sleepimageparse_json['url']
    sleepname = sleepimageparse_json['anime_name']
    embed = discord.Embed(

           description=sleepname,
            color=embedhexfix,
        )
    embed.set_image(url=sleepimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Sleep Image Command Used By: {}".format(ctx.author) + " | Image URL: " + sleepimage)

@slash.slash(
    name="smile",
    description="Say Cheese!"
)
async def _smile(ctx):
    smileimager = requests.get('https://nekos.best/api/v1/smile')
    smileimageurl = smileimager.url
    smileimagerequest = requests.get(smileimageurl)
    smileimagetext_json = json.loads(smileimagerequest.text)
    smileimageparse_json = smileimagetext_json
    smileimage = smileimageparse_json['url']
    smilename = smileimageparse_json['anime_name']
    embed = discord.Embed(

           description=smilename,
            color=embedhexfix,
        )
    embed.set_image(url=smileimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Smile Image Command Used By: {}".format(ctx.author) + " | Image URL: " + smileimage)

@slash.slash(
    name="smug",
    description="Shady shady shady..."
)
async def _smug(ctx):
    smugimager = requests.get('https://nekos.best/api/v1/smug')
    smugimageurl = smugimager.url
    smugimagerequest = requests.get(smugimageurl)
    smugimagetext_json = json.loads(smugimagerequest.text)
    smugimageparse_json = smugimagetext_json
    smugimage = smugimageparse_json['url']
    smugname = smugimageparse_json['anime_name']
    embed = discord.Embed(

           description=smugname,
            color=embedhexfix,
        )
    embed.set_image(url=smugimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Smug Image Command Used By: {}".format(ctx.author) + " | Image URL: " + smugimage)

@slash.slash(
    name="stare",
    description="O.O"
)
async def _stare(ctx):
    stareimager = requests.get('https://nekos.best/api/v1/stare')
    stareimageurl = stareimager.url
    stareimagerequest = requests.get(stareimageurl)
    stareimagetext_json = json.loads(stareimagerequest.text)
    stareimageparse_json = stareimagetext_json
    stareimage = stareimageparse_json['url']
    starename = stareimageparse_json['anime_name']
    embed = discord.Embed(

           description=starename,
            color=embedhexfix,
        )
    embed.set_image(url=stareimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Stare Image Command Used By: {}".format(ctx.author) + " | Image URL: " + stareimage)

@slash.slash(
    name="think",
    description="Brain blast!"
)
async def _think(ctx):
    thinkimager = requests.get('https://nekos.best/api/v1/think')
    thinkimageurl = thinkimager.url
    thinkimagerequest = requests.get(thinkimageurl)
    thinkimagetext_json = json.loads(thinkimagerequest.text)
    thinkimageparse_json = thinkimagetext_json
    thinkimage = thinkimageparse_json['url']
    thinkname = thinkimageparse_json['anime_name']
    embed = discord.Embed(

           description=thinkname,
            color=embedhexfix,
        )
    embed.set_image(url=thinkimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Think Image Command Used By: {}".format(ctx.author) + " | Image URL: " + thinkimage)

@slash.slash(
    name="thumbsup",
    description="You did good! You deserve it!"
)
async def _thumbsup(ctx):
    thumbsupimager = requests.get('https://nekos.best/api/v1/thumbsup')
    thumbsupimageurl = thumbsupimager.url
    thumbsupimagerequest = requests.get(thumbsupimageurl)
    thumbsupimagetext_json = json.loads(thumbsupimagerequest.text)
    thumbsupimageparse_json = thumbsupimagetext_json
    thumbsupimage = thumbsupimageparse_json['url']
    thumbsupname = thumbsupimageparse_json['anime_name']
    embed = discord.Embed(

           description=thumbsupname,
            color=embedhexfix,
        )
    embed.set_image(url=thumbsupimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Thumbsup Image Command Used By: {}".format(ctx.author) + " | Image URL: " + thumbsupimage)

@slash.slash(
    name="tickle",
    description="Sends a tickling anime gif in chat!"
)
async def _tickle(ctx):
    tickleimager = requests.get('https://nekos.best/api/v1/tickle')
    tickleimageurl = tickleimager.url
    tickleimagerequest = requests.get(tickleimageurl)
    tickleimagetext_json = json.loads(tickleimagerequest.text)
    tickleimageparse_json = tickleimagetext_json
    tickleimage = tickleimageparse_json['url']
    ticklename = tickleimageparse_json['anime_name']
    embed = discord.Embed(

           description=ticklename,
            color=embedhexfix,
        )
    embed.set_image(url=tickleimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Tickle Image Command Used By: {}".format(ctx.author) + " | Image URL: " + tickleimage)

@slash.slash(
    name="wave",
    description="Sends a waving anime gif in chat!"
)
async def _wave(ctx):
    waveimager = requests.get('https://nekos.best/api/v1/wave')
    waveimageurl = waveimager.url
    waveimagerequest = requests.get(waveimageurl)
    waveimagetext_json = json.loads(waveimagerequest.text)
    waveimageparse_json = waveimagetext_json
    waveimage = waveimageparse_json['url']
    wavename = waveimageparse_json['anime_name']
    embed = discord.Embed(

           description=wavename,
            color=embedhexfix,
        )
    embed.set_image(url=waveimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Wave Image Command Used By: {}".format(ctx.author) + " | Image URL: " + waveimage)

@slash.slash(
    name="wink",
    description="Sends a winking anime gif in chat!"
)
async def _wink(ctx):
    winkimager = requests.get('https://nekos.best/api/v1/wink')
    winkimageurl = winkimager.url
    winkimagerequest = requests.get(winkimageurl)
    winkimagetext_json = json.loads(winkimagerequest.text)
    winkimageparse_json = winkimagetext_json
    winkimage = winkimageparse_json['url']
    winkname = winkimageparse_json['anime_name']
    embed = discord.Embed(

           description=winkname,
            color=embedhexfix,
        )
    embed.set_image(url=winkimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Wink Image Command Used By: {}".format(ctx.author) + " | Image URL: " + winkimage)

@slash.slash(
    name="nekos",
    description="Cat Girls!"
)
async def _nekos(ctx):
    nekosimager = requests.get('https://nekos.best/api/v1/nekos')
    nekosimageurl = nekosimager.url
    nekosimagerequest = requests.get(nekosimageurl)
    nekosimagetext_json = json.loads(nekosimagerequest.text)
    nekosimageparse_json = nekosimagetext_json
    nekosimage = nekosimageparse_json['url']
    nekosname = nekosimageparse_json['artist_name']
    nekosurl= nekosimageparse_json['artist_href']
    embed = discord.Embed(
           title="Artist: " + nekosname,
            url=nekosurl,

            color=embedhexfix,
        )
    embed.set_image(url=nekosimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Nekos Image Command Used By: {}".format(ctx.author) + " | Image URL: " + nekosimage)

@slash.slash(
    name="newlife",
    description="Use this for when you need to start a new life, and go on the run!"
)
async def _newlife(ctx):
    newlifer = requests.get('https://randomuser.me/api/')
    newlifeurl = newlifer.url
    newliferequest = requests.get(newlifeurl)
    newlifetext_json = json.loads(newliferequest.text)
    newlifeparse_json = newlifetext_json
    newlifedata = newlifeparse_json['results']
    newlifeone = newlifedata[0]

    newlifegender = newlifeone['gender']

    newlifename = newlifeone['name']
    newlifetitle = newlifename['title']
    newlifefirstname = newlifename['first']
    newlifelastname = newlifename['last']

    newlifelocation = newlifeone['location']
    newlifestreet = newlifelocation['street']
    newlifestreetnumber = newlifestreet['number']
    newlifestreetname = newlifestreet['name']

    newlifecity = newlifelocation['city']
    newlifestate = newlifelocation['state']
    newlifecountry = newlifelocation['country']
    newlifepostalcode = newlifelocation['postcode']

    newlifeemail = newlifeone['email']
    newlifelogininfo = newlifeone['login']
    newlifeloginusername = newlifelogininfo['username']
    newlifeloginpassword = newlifelogininfo['password']

    newlifedob = newlifeone['dob']
    newlifedobdate = newlifedob['date']
    newlifeage = newlifedob['age']

    newlifehomephone = newlifeone['phone']
    newlifecellphone = newlifeone['cell']

    newlifepicture = newlifeone['picture']
    newlifelargepicture = newlifepicture['large']

    newlifecardr = requests.get('https://random-data-api.com/api/stripe/random_stripe')
    newlifecardurl = newlifecardr.url
    newlifecardrequest = requests.get(newlifecardurl)
    newlifecardtext_json = json.loads(newlifecardrequest.text)
    newlifecardparse_json = newlifecardtext_json
    newlifecarddata = newlifecardparse_json
    newlifcardnumber = newlifecarddata['valid_card']
    newlifcardmonth = newlifecarddata['month']
    newlifcardyear = newlifecarddata['year']
    newlifcardccv = newlifecarddata['ccv']
    newlifcardtoken = newlifecarddata['token']
    newlifecardtokenfix = newlifcardtoken.replace("tok_", "").title()
    newlifecardbrand = newlifecardtokenfix.replace("_", " ")


    embed = discord.Embed(
            title=newlifetitle + ". " + newlifefirstname + " " + newlifelastname,
            description='',
            color=embedhexfix,
        )
    embed.add_field(name="Gender:", value=newlifegender.title(), inline=False)
    embed.add_field(name="Address:", value=str(newlifestreetnumber) + " " + str(newlifestreetname) + ", " + str(newlifecity) + ", " + str(newlifestate) + ", " + str(newlifecountry) + ", " + str(newlifepostalcode), inline=False)
    embed.add_field(name="Email: ", value="Email: " + str(newlifeemail) + "\nUsername: " + str(newlifeloginusername) + "\nPassword: " + str(newlifeloginpassword), inline=False)
    embed.add_field(name="DOB: ", value="Date: " + str(newlifedobdate) + "\nAge: " + str(newlifeage), inline=False)
    embed.add_field(name="Phone: ", value="Home: " + str(newlifehomephone) + "\nCell: " + str(newlifecellphone), inline=False)
    embed.add_field(name="Card: ", value="Card Number: " + str(newlifcardnumber) + "\nCCV: " + str(newlifcardccv) + "\nCard Brand: " + str(newlifecardbrand) + "\nExpires: " + str(newlifcardmonth) + "/" + str(newlifcardyear), inline=False)
    embed.set_image(url=newlifelargepicture)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/NewLife Command Used By: {}".format(ctx.author))

@slash.slash(
    name="yesorno",
    description="When you can't decide, let someone else do it for you!"
)
async def _yesorno(ctx):
    yesornor = requests.get('https://yesno.wtf/api')
    yesornourl = yesornor.url
    yesornorequest = requests.get(yesornourl)
    yesornotext_json = json.loads(yesornorequest.text)
    yesornoparse_json = yesornotext_json
    yesorno = yesornoparse_json['answer']
    yesornoimage = yesornoparse_json['image']
    embed = discord.Embed(
           title=yesorno.title(),

            color=embedhexfix,
        )
    embed.set_image(url=yesornoimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/YesORNo Command Used By: {}".format(ctx.author) + " | Yes or no?: " + yesorno)

@slash.slash(
    name="insult",
    description="Fuck 'em!"
)
async def _insult(ctx):
    insultr = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    insulturl = insultr.url
    insultrequest = requests.get(insulturl)
    insulttext_json = json.loads(insultrequest.text)
    insultparse_json = insulttext_json
    insult = insultparse_json['insult']

    embed = discord.Embed(
           title=insult,

            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Insult Command Used By: {}".format(ctx.author) + " | Insult: " + insult)

@slash.slash(
    name="randomcolor",
    description="Sends a random HEX color with example!"
)
async def _randomcolor(ctx):
    randomcolorr = requests.get('https://x-colors.herokuapp.com/api/random')
    randomcolorurl = randomcolorr.url
    randomcolorrequest = requests.get(randomcolorurl)
    randomcolortext_json = json.loads(randomcolorrequest.text)
    randomcolorparse_json = randomcolortext_json
    randomcolor = randomcolorparse_json['hex']
    randomcolorfixed = randomcolor.replace("#","")
    randomcolorembed = int(randomcolorfixed, 16)

    embed = discord.Embed(
           title=randomcolor,
           url='https://www.color-hex.com/color/' + randomcolorfixed,

            color=randomcolorembed
        )
    embed.set_image(url="https://plchldr.co/i/250x215?&bg=" + randomcolorfixed + "&text=")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("/Random Color Command Used By: {}".format(ctx.author) + " | Random Color: " + randomcolor)

@slash.slash(
    name="time",
    description="Tells you the current time!"
)
async def _time(ctx):
    timer = requests.get('https://icanhazepoch.com/')
    timeurl = timer.url
    timerequest = requests.get(timeurl)
    timetext_json = json.loads(timerequest.text)
    timeparse_json = timetext_json
    timeepoch = timeparse_json
    time = "<t:" + str(timeepoch) + ":F>"
    
    embed = discord.Embed(
           title='Time:',

           description=time,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Time Command Used By: {}".format(ctx.author) + " | Time: " + time)

@slash.slash(
    name="yomomma",
    description="Sends a Yo Momma joke!"
)
async def _yomomma(ctx):
    yomommar = requests.get('https://sumisuyomomma-api.herokuapp.com/jokes')
    yomommaurl = yomommar.url
    yomommarequest = requests.get(yomommaurl)
    yomommatext_json = json.loads(yomommarequest.text)
    yomommaparse_json = yomommatext_json
    yomommajoke = yomommaparse_json['joke']
    
    embed = discord.Embed(


           description=yomommajoke,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Yo Momma Command Used By: {}".format(ctx.author) + " | Joke: " + yomommajoke)

@slash.slash(
    name="uselessfact",
    description="Sends a useless fact!"
)
async def _uselessfact(ctx):
    uselessfactr = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    uselessfacturl = uselessfactr.url
    uselessfactrequest = requests.get(uselessfacturl)
    uselessfacttext_json = json.loads(uselessfactrequest.text)
    uselessfactparse_json = uselessfacttext_json
    uselessfact = uselessfactparse_json['text']
    
    embed = discord.Embed(


           description=uselessfact,
            color=embedhexfix,
        )

    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Useless Fact Command Used By: {}".format(ctx.author) + " | Fact: " + uselessfact)

@slash.slash(
    name="coffee",
    description="Sends a picture of coffee!"
)
async def _coffee(ctx):
    coffeeimager = requests.get('https://coffee.alexflipnote.dev/random.json')
    coffeeimageurl = coffeeimager.url
    coffeeimagerequest = requests.get(coffeeimageurl)
    coffeeimagetext_json = json.loads(coffeeimagerequest.text)
    coffeeimageparse_json = coffeeimagetext_json
    coffeeimage = coffeeimageparse_json['file']
    embed = discord.Embed(


            color=embedhexfix,
        )
    embed.set_image(url=coffeeimage)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Coffee Image Command Used By: {}".format(ctx.author) + " | Image URL: " + coffeeimage)

@slash.slash(
    name="drawcard",
    description="Draws a random playing card!"
)
async def _drawcard(ctx):
    drawcardimager = requests.get('http://deckofcardsapi.com/api/deck/new/draw/?count=1')
    drawcardimageurl = drawcardimager.url
    drawcardimagerequest = requests.get(drawcardimageurl)
    drawcardimagetext_json = json.loads(drawcardimagerequest.text)
    drawcardimageparse_json = drawcardimagetext_json
    drawcardimage = drawcardimageparse_json['cards']
    drawcarddata = drawcardimage[0]
    drawcardsuit = drawcarddata['suit']
    drawcardvalue = drawcarddata['value']
    drawcard = drawcarddata['image']
    drawcardcode = str(drawcardvalue).capitalize() + " of " + str(drawcardsuit).capitalize()
    embed = discord.Embed(
           title=drawcardcode,

            color=embedhexfix,
        )
    embed.set_image(url=drawcard)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Draw Card Command Used By: {}".format(ctx.author) + " | Card: " + str(drawcardcode))

@slash.slash(
    name="d6",
    description="Rolls a D6 dice!"
)
async def _d6(ctx):
    random6dimager = requests.get('http://roll.diceapi.com/json/d6')
    random6dimageurl = random6dimager.url
    random6dimagerequest = requests.get(random6dimageurl)
    random6dimagetext_json = json.loads(random6dimagerequest.text)
    random6dimageparse_json = random6dimagetext_json
    random6dimagedata = random6dimageparse_json['dice']
    random6dimageselect = random6dimagedata[0]
    random6dimagevalue = random6dimageselect['value']
    random6dimagevaluefixed = str(random6dimagevalue).replace("6", "Six").replace("5", "Five").replace("4", "Four").replace("3", "Three").replace("2", "Two").replace("1", "One")
 

    embed = discord.Embed(
           title=random6dimagevaluefixed,

            color=embedhexfix,
        )
    embed.set_image(url="http://roll.diceapi.com/images/poorly-drawn/d6/" + str(random6dimagevalue) + ".png")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Random D6 Command Used By: {}".format(ctx.author) + " | Die: " + str(random6dimagevaluefixed))

@slash.slash(
    name="d20",
    description="Rolls a D20 dice!"
)
async def _d20(ctx):
    randomd20imager = requests.get('http://roll.diceapi.com/json/d20')
    randomd20imageurl = randomd20imager.url
    randomd20imagerequest = requests.get(randomd20imageurl)
    randomd20imagetext_json = json.loads(randomd20imagerequest.text)
    randomd20imageparse_json = randomd20imagetext_json
    randomd20imagedata = randomd20imageparse_json['dice']
    randomd20imageselect = randomd20imagedata[0]
    randomd20imagevalue = randomd20imageselect['value']
    randomd20imagevaluefixed = str(randomd20imagevalue).replace("20", "Twenty").replace("19", "Nineteen").replace("18", "Eightteen").replace("17", "Seventeen").replace("16", "Sixteen").replace("15", "Fifteen").replace("14", "Fourteen").replace("13", "Thirteen").replace("12", "Twelve").replace("11", "Eleven").replace("10", "Ten").replace("9", "Nine").replace("8", "Eight").replace("7", "Seven").replace("6", "Six").replace("5", "Five").replace("4", "Four").replace("3", "Three").replace("2", "Two").replace("1", "One")
 

    embed = discord.Embed(
           title=randomd20imagevaluefixed,

            color=embedhexfix,
        )
    embed.set_image(url="http://roll.diceapi.com/images/poorly-drawn/d20/" + str(randomd20imagevalue) + ".png")
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Random D20 Command Used By: {}".format(ctx.author) + " | Die: " + str(randomd20imagevaluefixed))

@slash.slash(
    name="covid",
    description="Show's current COVID info!"
)
async def _covid(ctx):
    covidr = requests.get('https://api.quarantine.country/api/v1/summary/region?region=usa')
    covidurl = covidr.url
    covidrequest = requests.get(covidurl)
    covidtext_json = json.loads(covidrequest.text)
    covidparse_json = covidtext_json
    coviddata = covidparse_json['data']
    coviddatasummary = coviddata['summary']
    covidtotalcases = coviddatasummary['total_cases']
    covidactivecases = coviddatasummary['active_cases']
    covidrecovered = coviddatasummary['recovered']
    covidcritical = coviddatasummary['critical']

    embed = discord.Embed(
           title="Covid Information:",

            color=embedhexfix,
        )
    embed.add_field(name="Total Cases: ", value=covidtotalcases, inline=True)
    embed.add_field(name="Active Cases: ", value=covidactivecases, inline=True)
    
    embed.add_field(name="Recovered: ", value=covidrecovered, inline=True)
    embed.add_field(name="Critical: ", value=covidcritical, inline=True)
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("COVID Information Command Used By: {}".format(ctx.author))

##################################################################################################################
#####################LIGHTS##################LIGHTS####################LIGHTS################LIGHTS###############
##################################################################################################################
'''
@slash.slash(
    name="on",
    description="Turns bedroom lights off!"
)
async def _lightson(ctx):
    import requests
    api_url = "http://10.0.0.4/api/jlxCFrG2Nt64uPaCuIo8YA7Yc0uAqe12IkE2lMh1/lights/4/state"
    todo = {"on": True}
    response = requests.put(api_url, json=todo)
    response.json()
    {'on': True}

    embed = discord.Embed(
           title="Lights On",
           description="Turned on bedroom lights!",
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Light On Command Used By: {}".format(ctx.author))

@slash.slash(
    name="off",
    description="Turns bedroom lights on!"
)
async def _off(ctx):
    import requests
    api_url = "http://10.0.0.4/api/jlxCFrG2Nt64uPaCuIo8YA7Yc0uAqe12IkE2lMh1/lights/4/state"
    todo = {"on": False}
    response = requests.put(api_url, json=todo)
    response.json()
    {'on': False}

    embed = discord.Embed(
           title="Lights Off",
           description="Turned off bedroom lights!",
            color=embedhexfix,
        )
    embed.set_author(name=discordusername, url=discordusernameurl, icon_url=boticon)
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Light Off Command Used By: {}".format(ctx.author))
'''
##################################################################################################################
##################################################################################################################

client.run(config["token"])

# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)
