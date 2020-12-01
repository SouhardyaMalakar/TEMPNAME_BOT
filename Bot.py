import discord
from discord.ext import commands
from discord.ext.commands import Bot
import wikipedia

class custom_bot(commands.Bot):
    async def on_ready(self):
        print('Ready')

a_bot = commands.Bot(command_prefix = '!')
@a_bot.command()
async def example(ctx, arg):
    await ctx.send(arg)

@a_bot.command()
async def search(ctx, *args):
    x = " ".join(args[:])
    try:
        article=wikipedia.summary(x,chars =2000, auto_suggest=True, redirect=True)
        ser = discord.Embed(title="Thanks for asking!!",description=article, colour=discord.Colour.blue())
        await ctx.send(content= None,embed=ser)
    except wikipedia.DisambiguationError as e:
        ser = discord.Embed(title="Be more specific",description="Wikipedia does not like disambiguation", colour=discord.Colour.blue())
        await ctx.send(content=None, embed=ser)
    
a_bot.run('NzgyMTY0NDkyMjc2NTk2NzU3.X8INcg.wocLDrGkpnc_aZUqLtMnHi2jIPs')

