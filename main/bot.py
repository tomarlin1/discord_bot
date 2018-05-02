from discord.ext.commands import Bot
from commands import fortnite_tracker
from main import constants

client = Bot(command_prefix=constants.BOT_PREFIX)


def format_msg(msg):
    return "```" + msg + "test```"


@client.command(name='test')
async def test():
    await client.say(format_msg("test"))


@client.command(name='Loboged')
async def elad_boged():
    await client.say("ELAD YA BOGED")


@client.command(name='fortnite')
async def fortnite_stats(nickname):
    try:
        values = fortnite_tracker.get_stats(nickname)
        response_body = ""
        for key in values.keys():
            response_body += key + ": " + values[key] + '\n'
        response = format_msg(response_body)
    except fortnite_tracker.InputException:
        response = format_msg("No such Player " + nickname)
    except fortnite_tracker.BadConnection:
        response = format_msg("Cannot Access Fortnite Tracker")
    await client.say(response)


client.run(constants.TOKEN)
