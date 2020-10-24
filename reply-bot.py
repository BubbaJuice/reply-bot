import discord
from discord.ext import commands
import os

token = os.environ.get('DISCORD_APP_TOKEN')

description = """ 
                  !help                   -- display this message
                  !add <key> <response>   -- when a user says "key" as a word, it'll response with the given response
                  !remove <key>           -- removes the key
                  !show                   -- shows the list of keys, and response
              """
bot = commands.Bot(command_prefix='!', description=description)

# In memory database of responses.
replies = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    # don't respond to ourselves
    sender = str(message.author)
    if sender.split('#')[0] == bot.user.name:
        return

    await process_substring(message)
    await bot.process_commands(message)

async def process_substring(message):
    words = message.content.split() # list of words from the message
    print(words)
    responses = [replies[word] for word in words if word in replies]
    if len(responses) > 0:
        response = "\n".join(responses)
        print('---' + response)
        await message.channel.send(response)
    else: 
        print("no response found...")
    return
     
@bot.command()
async def show(ctx):
    result = ""
    if len(replies.items()) == 0: 
        result = "No replies yet..."
    else:
        result = "\n".join(list(map(" ".join, replies.items())))
    await ctx.send(result)

@bot.command()
async def add(ctx, reply: str, response: str):
    """Add a reply"""
    replies[reply] = response
    result = "OK - '" + reply +":" + response + "' added"
    await ctx.send(result)

@bot.command()
async def remove(ctx, reply: str):
    response = replies[reply]
    del replies[reply]
    result = "OK - '" + reply +":" + response + "' removed"
    await ctx.send(result)


bot.run(token)
