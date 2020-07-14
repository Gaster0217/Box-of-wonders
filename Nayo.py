import discord
from discord.ext import commands
import time
import os
import random

acrs = [""] * 1000
resps = [""] * 1000
a = commands.Bot(command_prefix = "n.")
zt = 0


@a.event
async def on_ready():
    await a.change_presence(status=discord.Status.idle, activity=discord.Game("with the new sacrifices"))
    print("Bot has started")

@a.command()
async def reminder(ctx, msg=None, t=0):
    await ctx.send(f"Okay I will send {msg} after {t} seconds")
    time.sleep(t)
    await ctx.send(f"{msg}")

@a.command()
async def punch(ctx, member : discord.Member):
    urls = ["https://vignette.wikia.nocookie.net/powerlisting/images/1/17/Saitama_Megaton_Punch.gif/revision/latest?cb=20151113185826",
    "https://psychopowah.files.wordpress.com/2017/01/luffy-punch.gif?w=473&h=271",
    "http://pa1.narvii.com/5898/ce7d8e20b04acdb770c89b42e24c67a9aeae1302_hq.gif",
    "https://gifimage.net/wp-content/uploads/2017/09/anime-punching-gif-6.gif",
    "https://78.media.tumblr.com/6968c2ec1cdb5e10c8e5e39021b6fd3c/tumblr_oqzfqfIGia1qbq5g5o1_500.gif",
    "http://pa1.narvii.com/6084/7233693717bc4536a8403a06b194e9c2e32172eb_hq.gif"]
    punchy = discord.Embed(
        title = "SUMAAAAAASHHHHHH",
        description = f"{member.mention} just received a whack by {ctx.message.author.mention}.... However shall they respond..",
        color = discord.Color.red()
        )
    punchy.set_image(url=urls[random.randint(0, 5)])
    await ctx.send(embed=punchy)
    if member == ctx.message.author:
        await ctx.send("*Someone's a massochist*")

@a.command()
async def kiss(ctx, member : discord.Member):
    urls = ["https://68.media.tumblr.com/e14ed420800e7756934aa9058f0e1c7f/tumblr_mvckmnkug91sw3d45o1_500.gif",
    "https://static.tumblr.com/479e517cd2e75727b6bc1f77fe01422d/f2bl8jz/wninyl6ki/tumblr_static_a8jjk15rm3kkokwwcs0ck04gc.gif",
    "https://66.media.tumblr.com/b3d77735e349aefec4039e60eae51fd2/tumblr_mqc7j92TYp1rvkw6no1_500.gif",
    "http://media.giphy.com/media/JYpVJEcNrDAWc/giphy.gif", "https://pa1.narvii.com/5823/f10cce909b5bfa6f05f0af496558a16ed4840c06_hq.gif"]
    responses = ["Someone's bold", "Haha gayyyy", "*Adorable*", "Ew"]
    kissy = discord.Embed(
        title = "OoooOoOoooo",
        description = f"{member.mention} received a kiss by {ctx.message.author.mention}",
        color = discord.Color.red()
        )
    kissy.set_image(url=urls[random.randint(0, 4)])
    await ctx.send(embed=kissy)
    await ctx.send(responses[random.randint(0, 3)])

@a.command()
async def upset(ctx):
    urls = ["https://gifimage.net/wp-content/uploads/2017/06/sad-anime-gif-16.gif",
    "https://giphy.com/gifs/black-and-white-girl-6LFpgSJKJOaFG",
    "https://media.tenor.co/images/f478ddf5e80f54ce3e386b9f230de68c/raw",
    "https://i.pinimg.com/originals/c5/ac/f5/c5acf5b2b691adf17247ce3144372bcd.gif"]
    acdc = ["In the words of a not-so-great twitch streamer, the key to not being upset is to not be upset... Maybe I made it worse..",
    f"Hang in there, {ctx.message.author.mention}", "Too bad I can't hug you right now..."]
    mad = discord.Embed(
        title = "Augh, life is so tough",
        description = f"{ctx.message.author.mention} is upset...",
        color = discord.Color.red()
        )
    mad.set_image(url=urls[random.randint(0, 3)])
    await ctx.send(embed=mad)
    time.sleep(2)
    await ctx.send(acdc[random.randint(0, 2)])

@a.command()
async def highfive(ctx, member : discord.Member):
    urls = ["http://pa1.narvii.com/5696/a162f33dff8185278c495a7eb541e7aac3d7e91a_hq.gif",
    "https://pa1.narvii.com/6569/e6f98a639dca7ea813d53db4360ce317c411da8b_hq.gif",
    "https://gifimage.net/wp-content/uploads/2017/09/anime-high-five-gif-13.gif",
    "https://media.giphy.com/media/oiCBLYU2TH3JS/giphy.gif"]
    uwa = discord.Embed(
        title = "Woohoo",
        description = f"{ctx.message.author.mention} high fived {member.mention}",
        color = discord.Color.red()
        )
    uwa.set_image(url=urls[random.randint(0, 3)])
    await ctx.send(embed=uwa)
    if member == ctx.message.author:
        await ctx.send("*how sad, no one to highfive to*")

os.chdir(r"C:\D drive\Official")

@a.event
async def on_user_join(member):
    print(f"{member} has joined")
    a.load_extension('cogs.music')

@a.event
async def on_user_leave(member):
    print(f"{member} just left")

@a.event
async def command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Do it right.")

@a.command()
async def hello(ctx, num=1):
    if num > 4:
        await ctx.send("Don't wanna spam")
    else:
        for i in range(0, num):
            await ctx.send("Hello")

@a.command()
@commands.has_role("Kami_sama")
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(amount, "msgs deleted")

@a.command()
@commands.has_role("Kami_sama")
async def kick(ctx, member : discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked")
    except:
        await ctx.send("okay, no.")

@a.command()
@commands.has_role("Kami_sama")
async def ban(ctx, member : discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned")
    except:
        await ctx.send("I won't do it because I can't or I don't want to.")

@a.command()
@commands.has_role("Kami_sama")
async def unban(ctx, *, member):
    try:
        bu = await ctx.guild.bans()
        a, b = member.split("#")
        for j in bu:
            u = j
            if (u.x, u.y) == (a, b):
                await ctx.guild.unban(u)
                await ctx.send(f"Unbanned {u.x}#{u.y}")
    except:
        await ctx.send("I won't do it because I can't or I don't want to.")

@a.command()
async def roll(ctx):
    b = random.randint(1, 36)
    rolls = discord.Embed(
    title = "Roll",
    description = f"Your number is... {b}",
    color = discord.Color.red()
    )
    if b == 6 or b == 36:
        jackpot = discord.Embed(
        title = "Jackpot!",
        description = "You have won the jackpot!",
        color = discord.Color.red()
        )
        jackpot.set_image(url="https://cdn.discordapp.com/attachments/535829367264247828/698142466859073606/download_7.gif")
        await ctx.send(embed=rolls)
        await ctx.send(embed=jackpot)
    else:
        await ctx.send(embed=rolls)
        await ctx.send("Better luck next time..")


@a.command()
async def cook(ctx, food):
    try:
        urls = ["https://i.ytimg.com/vi/5t8USrM9Hck/maxresdefault.jpg", "https://appzzang.me/data/file/animation/1982796218_v9FUoqmx_pds_584744_1456410157_55735.gif",
                "https://th.bing.com/th/id/OIP.8fAe1v_E3D-g5PGJ0CTMGAHaEK?pid=Api&rs=1", "https://th.bing.com/th/id/OIP.i5zWsSRVGTeVkuN0lp5bJQHaER?pid=Api&rs=1"]
        cooky = discord.Embed(
        title = "Ready to be served!!",
        description = f"Your {food} is ready to be served... Did I get it right?",
        color = discord.Color.red()
        )
        cooky.set_image(url=urls[random.randint(0, 3)])
        await ctx.send(embed=cooky)
    except:
        mistaken = discord.Embed(
        title = "Something went wrong",
        description = "It seems something went wrong, make sure you type the food you want. :?",
        color = discord.Color.red()
        )
        mistaken.set_image(url="https://gifimage.net/wp-content/uploads/2017/09/anime-confused-gif-9.gif")

@a.command()
async def bwish(ctx, member):
    try:
        wishes = discord.Embed(
        title = "Happy Birthday!!",
        description = f"Lalaaaaaalaaa, happy birthday to you! May you have a prosperous life, {member}!",
        color = discord.Color.red()
        )
        wishes.set_image(url="https://cdn.discordapp.com/attachments/693356943255011368/698424665944883241/cake_animation.gif")
        await ctx.send(embed=wishes)
    except:
        await ctx.send("Something's not right... Sorry!!")


a.run("hahyoufellforitfoolitwasIDIO")
