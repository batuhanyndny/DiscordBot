import discord as dc
from discord.ext import commands

TOKEN = 'NjYyOTcxODk4OTMzODA1MDc2.XhBuwA.GXUhDdH1p1Lwa1VdtOpQ95hiThA'
SERVER_ID = 280049066493083649
from random import randint
import praw
from radio import play_radio, get_cuma_saati
from threading import Thread
import asyncio
import os
import datetime

stop_t = False
thread_list = []

reddit = praw.Reddit(client_id='m5EKLT9vYQIkhg',
                     client_secret='njjAvOhN2gw3sXDY1JZSsyFAOZk',
                     user_agent='<DISCORD>:<app 1>:<0.1> (by /u/batuhanyndny)')

subreddits= ['assholedesign', 'blursedimages', 'CrappyDesign', 'cursedcomments', 'gifsthatendtoosoon',
'gifsthatkeepongiving', 'HistoryMemes', 'holdmyfries', 'instant_regret', 'instantkarma', 'memes', 'mildlyinfuriating',
'MurderedByWords', 'perfectlycutscreams', 'PornhubComments', 'ProgrammerHumor', 'PublicFreakout', 'rareinsults',
'softwaregore', 'TurkeyJerky', 'Whatcouldgowrong']

bot = commands.Bot(command_prefix="$")

def clear():
    try:
        os.remove("stream.mp3")
    except:
        pass

@bot.event
async def on_ready():
    game = dc.Game("fancy patches are being done")
    await bot.change_presence(status=dc.Status.online, activity=game)


@bot.command(name="meme")
async def meme(ctx):
    reddit_C = "reddit"
    if str(ctx.channel) == reddit_C :
        sub = subreddits[randint(0,len(subreddits)-1)]
        for submission in reddit.subreddit(sub).top('hour'):
            await ctx.channel.send(f""" **Top post from r/{sub}**\n*{submission.title}*\n{submission.url}""")
            break
    else:
        await ctx.channel.send("Xd")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if str(member) == "ilostinlife#4940": #ilostinlife#4940
            vc = await after.channel.connect()
            pu = bot.get_channel(280049066493083649)
            await pu.send("Okay hosgeldin kardesim") #280049066493083649
            stream = dc.FFmpegPCMAudio('okay.mp3')
            vc.play(stream)
    if before.channel is not None and after.channel is None:
        if str(member) == "ilostinlife#4940": #ilostinlife#4940
            guild = bot.get_guild(SERVER_ID)
            pu = bot.get_channel(280049066493083649)
            await pu.send("Okay gorusuruz kardesim")
            await guild.voice_client.disconnect()

async def check_cuma():
    now = datetime.datetime.now()
    day = str(now.strftime("%A"))
    if day == "Friday":
        await asyncio.sleep(13000)
        pu = bot.get_channel(280049066493083649)
        current_time = now.strftime("%H:%M:%S").split(':')
        cuma = get_cuma_saati()
        saat_farki =  int(cuma[0]) - int(current_time[0])
        dakika_farki = int(cuma[1]) - int(current_time[1])
        if saat_farki < 0 and dakika_farki < 0:
            await pu.send("Batuhan tüm Discorda hayırlı cumalar diler. Cuma saati geçti.")

        else:
            await pu.send("Batuhan tüm Discorda hayırlı cumalar diler.\n```Cuma namazına kalan süre {} saat {} dakika```".format(saat_farki,dakika_farki))
    else:
        await asyncio.sleep(43000)


#############################
#
#     RADIO
#
#############################
@bot.command(name="pal")
async def pal(ctx):
    clear()
    global stop_t
    stop_t = False
    guild = bot.get_guild(SERVER_ID)
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    print("GIRDI" , flush=True)
    await ctx.channel.send("MERHABALAR AQ")
    print("sa" , flush=True)
    thread = Thread(target=play_radio, args=("PAL_FM", lambda: stop_t))
    print("THREAD OLUSTU", flush=True)
    thread_list.append(thread)
    print("EKLENDI", flush=True)
    thread.start()
    print("BASLADI", flush=True)
    await asyncio.sleep(1)
    print("UYUDU", flush=True)
    stream = dc.FFmpegPCMAudio('stream.mp3')
    vc.play(stream)

@bot.command(name="lalegul")
async def lalegul(ctx):
    clear()
    global stop_t
    stop_t = False
    guild = bot.get_guild(SERVER_ID)
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    print("GIRDI" , flush=True)
    await ctx.channel.send("MERHABALAR AQ")
    print("sa" , flush=True)
    thread = Thread(target=play_radio, args=("LALEGUL", lambda: stop_t))
    print("THREAD OLUSTU", flush=True)
    thread_list.append(thread)
    print("EKLENDI", flush=True)
    thread.start()
    print("BASLADI", flush=True)
    await asyncio.sleep(1)
    print("UYUDU", flush=True)
    stream = dc.FFmpegPCMAudio('stream.mp3')
    vc.play(stream)

@bot.command(name="rock")
async def rock(ctx):
    clear()
    global stop_t
    stop_t = False
    guild = bot.get_guild(SERVER_ID)
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    print("GIRDI" , flush=True)
    await ctx.channel.send("MERHABALAR AQ")
    print("sa" , flush=True)
    thread = Thread(target=play_radio, args=("ROCK", lambda: stop_t))
    print("THREAD OLUSTU", flush=True)
    thread_list.append(thread)
    print("EKLENDI", flush=True)
    thread.start()
    print("BASLADI", flush=True)
    await asyncio.sleep(1)
    print("UYUDU", flush=True)
    stream = dc.FFmpegPCMAudio('stream.mp3')
    vc.play(stream)


#############################
#
#     CIKIS
#
#############################
@bot.command(name="terket")
async def terket(ctx):
    global stop_t
    await ctx.channel.send("CIKIS YAPIYORUM")
    stop_t = True
    guild = bot.get_guild(SERVER_ID)
    await guild.voice_client.disconnect()
    for th in thread_list:
        th.join()
    thread_list.clear()

@bot.command(name="siktirgit")
async def siktirgit(ctx):
    global stop_t
    await ctx.channel.send("CIKIS YAPIYORUM")
    stop_t = True
    guild = bot.get_guild(SERVER_ID)
    await guild.voice_client.disconnect()
    for th in thread_list:
        th.join()
    thread_list.clear()

@bot.command(name="defol")
async def defol(ctx):
    global stop_t
    await ctx.channel.send("CIKIS YAPIYORUM")
    stop_t = True
    guild = bot.get_guild(SERVER_ID)
    await guild.voice_client.disconnect()
    for th in thread_list:
        th.join()
    thread_list.clear()

@bot.command(name="git")
async def git(ctx):
    global stop_t
    await ctx.channel.send("CIKIS YAPIYORUM")
    stop_t = True
    guild = bot.get_guild(SERVER_ID)
    await guild.voice_client.disconnect()
    for th in thread_list:
        th.join()
    thread_list.clear()

@bot.command(name="stop")
async def stop(ctx):
    global stop_t
    await ctx.channel.send("CIKIS YAPIYORUM")
    stop_t = True
    guild = bot.get_guild(SERVER_ID)
    await guild.voice_client.disconnect()
    for th in thread_list:
        th.join()
    thread_list.clear()

bot.loop.create_task(check_cuma())

bot.run(TOKEN)
