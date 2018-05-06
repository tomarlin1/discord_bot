import asyncio

from discord.ext.commands import Bot
import discord

from commands import fortnite_tracker
from utils import constants

client = Bot(command_prefix=constants.BOT_PREFIX)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="The Noobs Club"))


def format_msg(msg):
    return "```" + msg + "```"


async def say(msg):
    await client.say(format_msg(msg))


def speak(msg):
    return "/tts " + msg


@client.command(name="repeat")
async def repeat(*message):
    await client.say(format_msg(" ".join(message)), tts=True)


@client.command(name='loboged')
async def elad_boged():
    say("Elad Ya Boged")


@client.command(name='fortnite')
async def fortnite_stats(nickname):
    try:
        values = fortnite_tracker.get_stats(nickname)
        response_body = ""
        for key in values.keys():
            response_body += key + ": " + values[key] + '\n'
        response = response_body
    except fortnite_tracker.InputException:
        response = "No such Player " + nickname
    except fortnite_tracker.BadConnection:
        response = "Cannot Access Fortnite Tracker"
    await say(response)


async def idle():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current Servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(6)


client.loop.create_task(idle())

client.run(constants.TOKEN)
