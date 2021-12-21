import discord
from discord.ext import commands
import requests
from mcstatus import MinecraftServer
import json
import datetime

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="!mc Minecraft Server IP"))
    print("Bot is online.")

@client.command()
async def commands(ctx):
    embed = discord.Embed(
            title="Commands:",
            description="A list of all the commands that you can use with SumisuBot!",
            color=discord.Color.from_rgb(0, 255, 0),
        )
    embed.add_field(name="!mc server", value="Allows you to look up information about a minecraft server!", inline=True)
    embed.add_field(name="!catfact", value="Tells you a random fact about cats!", inline=True)
    embed.add_field(name="!cat", value="Displays a random cat image!", inline=True)
    embed.add_field(name="!meme", value="Shows you a random meme!", inline=True)
#    embed.add_field(name="!yt", value="Send an embedded Youtube message!", inline=True)
    embed.add_field(name="!food", value="Shows a random image of food!", inline=True)
    embed.add_field(name="!age", value="Tells you when your account was created!", inline=True)
#    embed.set_image(url=catimage)
    embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Commands Command Used By: {}".format(ctx.author.display_name))

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
                color=discord.Color.from_rgb(0, 255, 0),
            )
            embed.set_thumbnail(url="https://eu.mc-api.net/v3/server/favicon/" + arg)
            embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
            embed.set_footer(text="Made by: Sumisu®")

            await ctx.send(embed=embed)
            print("Server IP: " + mcip)
        else:
            print("Online: False")
    except:
        print("Minecraft Server Command Used By: {}".format(ctx.author.display_name) + " | Server: " + arg)

        embed = discord.Embed(
            title="Server: " + arg,
            description='**IP:** ' + str(mcip) + '\n**Port:** ' + str(mcport) + '\n**Players:** ' + str(status.players.online) + '/' + str(status.players.max) + '\n**Version:** ' + str(decodedversion) + '\n\n**Description:** ' + str(data).replace("[", "").replace("]", "").replace("'", "") + '\n\n**Online:** N/A',
            color=discord.Color.from_rgb(0, 255, 0),
        )
        embed.set_thumbnail(url="https://eu.mc-api.net/v3/server/favicon/" + arg)
        embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
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
            color=discord.Color.from_rgb(0, 255, 0),
        )

    embed.set_thumbnail(url=catimage)
    embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
    embed.set_footer(text="Made by: Sumisu®")

    await ctx.send(embed=embed)
    print("Cat Fact Command Used By: {}".format(ctx.author.display_name) + " | Cat Fact: " + cleancatfact)

@client.command()
async def cat(ctx):
    catimager = requests.get('https://aws.random.cat/meow')
    catimageurl = catimager.url
    catimagerequest = requests.get(catimageurl)
    catimagetext_json = json.loads(catimagerequest.text)
    catimageparse_json = catimagetext_json
    catimage = catimageparse_json['file']
    embed = discord.Embed(
#           title=catimage,
#           description=catimage,
            color=discord.Color.from_rgb(0, 255, 0),
        )
    embed.set_image(url=catimage)
    embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Cat Image Command Used By: {}".format(ctx.author.display_name) + " | Image URL: " + catimage)

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
#            title=catimage,
            description="Made by: " + str(memeauthor),
            color=discord.Color.from_rgb(0, 255, 0),
        )
    embed.set_image(url=memeimage)
    embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Meme Image Command Used By: {}".format(ctx.author.display_name) + " | Image URL: " + str(memeimage))

@client.command()
async def yt(ctx):
    embed = discord.Embed(
#            title="Sumisu's Youtube!",
#            description="https://www.youtube.com/channel/UCZ_lWTHNwPIAecB8nHLje9w",
            color=discord.Color.from_rgb(0, 255, 0),
        )
#    embed.set_image(url=memeimage)
    embed.add_field(name="Sumisu's Youtube:", value="https://www.youtube.com/channel/UCZ_lWTHNwPIAecB8nHLje9w", inline=True)
    embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Youtube Command Used By: {}".format(ctx.author.display_name))

@client.command()
async def food(ctx):
    foodimager = requests.get('https://foodish-api.herokuapp.com/api')
    foodimageurl = foodimager.url
    foodimagerequest = requests.get(foodimageurl)
    foodimagetext_json = json.loads(foodimagerequest.text)
    foodimageparse_json = foodimagetext_json
    foodimage = foodimageparse_json['image']
    embed = discord.Embed(
#           title=catimage,
           description="Food Image:",
            color=discord.Color.from_rgb(0, 255, 0),
        )
    embed.set_image(url=foodimage)
    embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Food Image Command Used By: {}".format(ctx.author.display_name) + " | Image URL: " + foodimage)

@client.command()
async def anime(ctx, args):
    animesearch = anime
    animer = requests.get('https://api.jikan.moe/v3/search/anime?q=' + str(anime).join('%20') + '&sort=desc&page=1')
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
            color=discord.Color.from_rgb(0, 255, 0),
        )
    embed.add_field(name="Episodes:", value=animeepisodes, inline=False)
    embed.add_field(name="Airing:", value=animeairing, inline=False)
    embed.add_field(name="Score:", value=animescore, inline=False)
    embed.set_image(url=animeimageurl)
    embed.set_author(name="SumisuMC#0001", url="https://bit.ly/SumisuDC", icon_url="https://cdn.discordapp.com/avatars/391291696098312202/a_6ffa06c159fe4c0453f8d21eac9ee194.webp?size=32")
    embed.set_footer(text="Made by: Sumisu®")
    await ctx.send(embed=embed)
    print("Anime Command Used By: {}".format(ctx.author.display_name) + " | Anime Searched: " + str(animesearch))

@client.command()
async def age(ctx):
    accountage = ctx.author.created_at
    await ctx.send(format(ctx.author.mention) + ", your account was created on:" + accountage.strftime('%B %d %Y') + " at " + accountage.strftime('%I:%M:%S %p'))
    print("Age Command Used By: {}".format(ctx.author.display_name) + " | Account Age: " + accountage.strftime('%B %d %Y') + " at " + accountage.strftime('%I:%M:%S %p'))

client.run('Nzc2NTIxMDY1OTcwNDAxMjkw.X62FmQ.qx0PTJzEJqvWxsSiahmRswyWV7Y')

# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)
