import discord as dc
from discord.ext import commands

TOKEN = '#'
SERVER_ID = 280049066493083649
from random import randint
import praw
from radio import play_radio
from threading import Thread
import asyncio

FM_STATION = None
stop_t = False


reddit = praw.Reddit(client_id='m5EKLT9vYQIkhg',
                     client_secret='#',
                     user_agent='<DISCORD>:<app 1>:<0.1> (by /u/batuhanyndny)')

subreddits= ['assholedesign', 'blursedimages', 'CrappyDesign', 'cursedcomments', 'gifsthatendtoosoon',
'gifsthatkeepongiving', 'HistoryMemes', 'holdmyfries', 'instant_regret', 'instantkarma', 'memes', 'mildlyinfuriating',
'MurderedByWords', 'perfectlycutscreams', 'PornhubComments', 'ProgrammerHumor', 'PublicFreakout', 'rareinsults',
'softwaregore', 'TurkeyJerky', 'Whatcouldgowrong']
bot = commands.Bot(command_prefix="$")

@bot.command(name="meme")
async def meme(ctx):
    reddit_C = "reddit"
    if str(ctx.channel) == reddit_C :
        sub = subreddits[randint(0,len(subreddits)-1)]
        for submission in reddit.subreddit(sub).top('hour'):
            await ctx.channel.send(f""" **Top post from r/{sub}**\n*{submission.title}*\n{submission.url}""")
            break
    else:
        await ctx.channel.send("memeler sadece 'reddit' kanalindan istenebilir yallah koyune")

@bot.command(name="pal")
async def pal(ctx):
    global stop_t
    global vc
    global thread
    global FM_STATION
    FM_STATION = "PAL_FM"
    stop_t = False
    guild = bot.get_guild(SERVER_ID)
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    await ctx.channel.send("MERHABALAR AQ")
    thread = Thread(target=play_radio, args=(FM_STATION, lambda: stop_t))
    thread.start()
    await asyncio.sleep(1)
    stream = dc.FFmpegPCMAudio('stream.mp3')
    vc.play(stream)


@bot.command(name="lalegul")
async def lalegul(ctx):
    global stop_t
    global vc
    global thread
    global FM_STATION
    FM_STATION = "LALEGUL"
    stop_t = False
    guild = bot.get_guild(SERVER_ID)
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    await ctx.channel.send("MERHABALAR AQ")
    thread = Thread(target=play_radio, args=(FM_STATION, lambda: stop_t))
    thread.start()
    await asyncio.sleep(1)
    stream = dc.FFmpegPCMAudio('stream.mp3')
    vc.play(stream)

@bot.command(name="stop")
async def stop(ctx):
    global stop_t
    global thread
    await ctx.channel.send("CIKIS YAPIYORUM")
    stop_t = True
    await vc.disconnect()
    thread.join()
    
bot.run(TOKEN)
