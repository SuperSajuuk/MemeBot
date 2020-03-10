import memes, asyncio, typing, importlib
from discord.ext import commands
moderator_roles = [231848293322326017,315961378420555777]
allowed_roles = [253573759460442114,508424413746692126,576864397704822784,585711329491288065]
allowed_channels = [351834237818634242,360965133834649602,381200080796909568,417472207082749952]

# Functions
async def mod_log(ctx):
	if ctx.guild is None:
		log_post = f":computer: {str(ctx.author)} ({ctx.author.id}) used command in my DM's: `{ctx.message.clean_content}`"
	else:
		log_post = f":computer: {str(ctx.author)} ({ctx.author.id}) used command in *{ctx.channel.name}*: `{ctx.message.clean_content}`"
	ch = ctx.guild.get_channel(438100727198515201)
	if ch:
		await ch.send(log_post)
	
async def has_perm(ctx):
	if ctx.channel.category_id == 360949225229647872:
		return True
	if ctx.channel.id not in allowed_channels:
		return False
	return any(role.id in (moderator_roles + allowed_roles) for role in ctx.author.roles)

async def is_mod(ctx):
	return any(role.id in moderator_roles for role in ctx.author.roles)

async def is_dm_only(ctx):
	return ctx.guild is None
	
# Public Commands
@commands.command()
@commands.check(has_perm)
@commands.cooldown(2, 10.0, type=commands.BucketType.member)
async def meme(ctx):
	await ctx.send(memes.getRandomMeme())
	await mod_log(ctx)

@commands.command()
@commands.check(has_perm)
@commands.cooldown(2, 10.0, type=commands.BucketType.member)
async def tweet(ctx):
	await ctx.send(memes.getRandomTweet())
	await mod_log(ctx)
	
@commands.command()
@commands.check(has_perm)
@commands.cooldown(2, 10.0, type=commands.BucketType.member)
async def image(ctx):
	await ctx.send(memes.getRandomImage())
	await mod_log(ctx)
	
@commands.command()
@commands.check(has_perm)
@commands.cooldown(2, 10.0, type=commands.BucketType.member)
async def clip(ctx):
	await ctx.send(memes.getRandomClip())
	await mod_log(ctx)

@commands.command()
@commands.check(has_perm)
@commands.cooldown(2, 10.0, type=commands.BucketType.member)
async def other(ctx):
	await ctx.send(memes.getRandomSomething())
	await mod_log(ctx)
	
@commands.command()
@commands.check(has_perm)
@commands.cooldown(2, 10.0, type=commands.BucketType.member)
async def therace(ctx):
	await ctx.send("THE RACE: https://clips.twitch.tv/GeniusEnthusiasticManateeKappaPride")
	await mod_log(ctx)
	
@commands.command()
@commands.check(has_perm)
@commands.cooldown(2, 10.0, type=commands.BucketType.member)
async def oliver(ctx):
	await ctx.send("Josh gets attacked by his cat, Oliver: https://clips.twitch.tv/PrettiestPowerfulCakeKappa")
	await mod_log(ctx)

# Error Handler for
# public commands
@meme.error
@tweet.error
@image.error
@clip.error
@other.error
@therace.error
async def public_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		return
	elif isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f":warning: You're on a cooldown right now! You have to wait {round(error.retry_after, 1)} seconds before trying again.")
	elif isinstance(error, commands.CheckFailure):
		await ctx.send(":lock: You lack permission to be able to use this command!", delete_after=5)
		await asyncio.sleep(3)
		await ctx.message.delete()
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f":question: You're missing a required argument in this command! `{error}`", delete_after=10)
		await asyncio.sleep(5)
		await ctx.message.delete()
	elif isinstance(error, commands.CommandInvokeError):
		await ctx.send(":warning: Sorry, something went wrong invoking this command, try again later.")

# Restricted commands
@commands.command()
@commands.check(is_mod)
async def stop(ctx):
	await ctx.send("Shutting down....")
	await ctx.bot.close()

@commands.command()
@commands.check(is_mod)
async def thanos(ctx):
	total = len(ctx.guild.members)
	half = total / 2
	await ctx.send(f":ok_hand: banhammered {half} random members :hammer: :wave: :wave:")
	await mod_log(ctx)

@commands.command()
@commands.check(is_mod)
async def count(ctx, *, cmd: typing.Optional[str] = None):
	# Get all module stats
	if cmd is None:
		image_ct = len(memes.images)
		tweet_ct = len(memes.tweets)
		other_ct = len(memes.other)
		clip_ct = len(memes.clips)
		totals = image_ct + tweet_ct + other_ct + clip_ct
		out = f"""Here are the stats: 
		
		- {image_ct} images
		- {tweet_ct} tweets
		- {clip_ct} clips
		- {other_ct} other random memes.
		
		There are a total of {totals} links that can be selected from the commands."""
		await ctx.send(out)
		await mod_log(ctx)
	else:
		try:
			ct = len(getattr(memes, cmd))
		except AttributeError:
			await ctx.send(":warning: no such command exists.")
		else:
			await ctx.send("There are currently {} choices that can be selected for that command.".format(ct))
		finally:
			await mod_log(ctx)
		
@stop.error
@count.error
async def mod_cmd_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		return
	elif isinstance(error, commands.CheckFailure):
		await ctx.send(":lock: You lack permission to be able to use this command!", delete_after=5)
		await asyncio.sleep(3)
		await ctx.message.delete()
	elif isinstance(error, commands.CommandInvokeError):
		await ctx.send(":warning: Sorry, something went wrong invoking this command, try again later.")
		print(error.original)
	
@commands.command()
@commands.is_owner()
async def reload(ctx):
	m = {"meme": memes}
	try:
		importlib.reload(m["meme"])
	except Exception as e:
		await ctx.send(":warning: Can't seem to reload memes module. Maybe there's a code error or something.")
	else:
		await ctx.message.add_reaction("👍")
		
def setup(bot):
	bot.add_command(meme)
	bot.add_command(tweet)
	bot.add_command(image)
	bot.add_command(clip)
	bot.add_command(other)
	bot.add_command(therace)
	bot.add_command(oliver)
	bot.add_command(suggest)
	bot.add_command(stop)
	bot.add_command(thanos)
	bot.add_command(count)
	bot.add_command(reload)