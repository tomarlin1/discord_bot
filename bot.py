from discord.ext.commands import Bot
import fortnite_tracker

BOT_PREFIX = ("!")
TOKEN = 'NDQwNTc1NDEzMzA4MDk2NTM3.DcjuoA.ywUUxF6oR5OrpLKmibuKotZXgqU'

client = Bot(command_prefix=BOT_PREFIX)


def format_msg(msg):
    return "```" + msg + "```"


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


client.run(TOKEN)
