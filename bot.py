# MemeBot
import asyncio, config
from discord.ext import commands
bot = commands.Bot(command_prefix="!")
bot.load_extension("cmds")
bot.load_extension("jishaku")
bot.remove_command('help')

@bot.event
async def on_command_error(ctx, error):
	pass

bot.run(config.bot_token)