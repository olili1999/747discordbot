import discord
from discord.ext import commands, tasks
from twilio.rest import Client
from pizzapi import *
import datetime
from datetime import timedelta
# instance of the bot created
client = commands.Bot(command_prefix=".")

# # Your Account SID from twilio.com/console
# account_sid = "AC1a17d74e4b470de46a6df56d22026a97"
# # Your Auth Token from twilio.com/console
# auth_token = "5cea8334681ad82bd240738fe0131dc4"

# client = Client(account_sid, auth_token)

# message = client.messages.create(to="+12484953497",
#                                     from_="+12517662846",
#                                     body="<insert reminder message here!!")
# print(message.sid)
data = []


@client.event
async def on_ready():
    print("Bot is ready.")


@tasks.loop(seconds=10)
async def minute_check():
    print(data)
    curr_hour = str(datetime.datetime.now().hour)
    curr_day = str(datetime.datetime.now().day)
    curr_min = str(datetime.datetime.now().minute)
    try:
        for d in data:
            compare_hour = str(d[4].hour)
            compare_day = str(d[4].day)
            compare_min = str(d[4].minute)
            print("current time: " + "\n")
            print("\t" + curr_day + curr_hour + curr_min + "\n")
            print("comparison: ")
            print("\t" + compare_day + compare_hour + compare_min)
            if curr_hour == compare_hour and curr_day == compare_day and curr_min == compare_min:
                channel = client.get_channel(int(d[5]))
                await channel.send(d[6])
                data.remove(d)
    except:
        print('Diqua Error 404')


@client.event
async def on_message(message):

    # ignore bot's own messages
    if message.author.bot == True or "!" not in message.content:
        return
    # !addreminder 5 min/hr 2 message asfdasdfasdfasdf asdfasdf
    msg = ""
    num_count = 0
    if "!addreminder" in message.content:
        # check that the message contains >= 4 items
        if len(message.content.split()) < 4:
            await message.channel.send(
                "Correct format is as follows: !addreminder <#> <min/hr> <# repeats> <insert message>"
            )
            return
        # check there is a number for duration and # of repeats
        try:
            int(message.content.split()[1])
            int(message.content.split()[3])
        except:
            await message.channel.send(
                "Correct format is as follows: !addreminder <#> <min/hr> <# repeats> <insert message>"
            )
            return
        for s in message.content.split():
            if (num_count == 2):
                msg += s
            try:
                int(s)
                num_count += 1
            except:
                continue
        templist = message.content.split()[0:4]
        minorhr = templist[2]
        if minorhr == "min":
            templist.append(datetime.datetime.now() +
                            timedelta(minutes=int(message.content.split()[1])))
        elif minorhr == "hr":
            templist.append(datetime.datetime.now() +
                            timedelta(hours=int(message.content.split()[1])))
        templist.append(message.channel.id)
        templist.append(msg.lstrip())
        data.append(templist)

        await message.channel.send("Added reminder")

    # !pizza single/double 1,2,3,4
    elif "!dominos" in message.content:
        try:
            toppingslist = message.content.split()[2].split(',')
            # check that the # toppings = 2, 3 or 4
            # check that the # list items = 3
            if (len(toppingslist) != 2 and len(toppingslist) != 3
                    and len(toppingslist) != 4
                    or len(message.content.split()) != 3):
                await message.channel.send(
                    "Correct format is as follows: !dominos <single/double> <#,#,#>"
                )
                return

        except:
            await message.channel.send(
                "Correct format is as follows: !dominos <single/double> <#,#,#>"
            )
            return

    elif "!commands" in message.content:
        await message.channel.send("""
            ```NOTICE THE SPACES IN BETWEEN INPUTS. IMPORTANT!\n1. Order a dominos pizza: !dominos <single/double> <#,#,#>\n2. Set a reminder: !addreminder <#> <min/hr> <# repeats> <insert message>
            ```
            """)


minute_check.start()
client.run('NzkwMDE5MTQyNjkzODE0Mjg5.X96gqQ.Ny_k9Arqe7eylXY4LRCuiZaW5DM')
