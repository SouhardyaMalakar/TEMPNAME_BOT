import discord
from discord.ext import commands

class custom_bot(commands.Bot):
    async def on_ready(self):
        print('Ready')

a_bot = custom_bot(command_prefix = '!')

@a_bot.command()
async def example(ctx, arg):
    await ctx.send(arg)

a_bot.run('TOKEN GOES HERE')