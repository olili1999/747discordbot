import discord
from discord.ext import commands, tasks
from twilio.rest import Client
import datetime
from datetime import timedelta
from dominos import orderDominos

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


@tasks.loop(seconds=30)
async def minute_check():
    print(data)
    curr_hour = str(datetime.datetime.now().hour)
    curr_day = str(datetime.datetime.now().day)
    curr_min = str(datetime.datetime.now().minute)
    try:
        for d in data:
            compare_hour = str(d[3].hour)
            compare_day = str(d[3].day)
            compare_min = str(d[3].minute)
            print("current time: " + "\n")
            print("\t" + curr_day + curr_hour + curr_min + "\n")
            print("comparison: ")
            print("\t" + compare_day + compare_hour + compare_min)
            if curr_hour == compare_hour and curr_day == compare_day and curr_min == compare_min:
                channel = client.get_channel(int(d[4]))
                await channel.send(d[5])
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
        # check there is a number for duration
        try:
            int(message.content.split()[1])
        except:
            await message.channel.send(
                "Correct format is as follows: !addreminder <#> <min/hr> <# repeats> <insert message>"
            )
            return
        for s in message.content.split()[3:]:
            msg += s + " "
        print(msg)
        templist = message.content.split()[0:3]
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
        if "menu" in message.content:
            await message.channel.send("""
            ```
                ==================================
                MEATS\n
                ==================================\n
                1 - Ham\n
                2 - Beef\n 
                3 - Salami\n 
                4 - Pepperoni\n
                5 - Italian Sausage\n
                6 - Premium Chicken\n 
                7 - Bacon\n
                8 - Philly Steak\n 
                ==================================\n
                CHOOSE NON-MEATS\n
                ==================================\n
                10 - Hot Buffalo Sauce\n
                11 - Garlic\n
                12 - Jalapeno Peppers\n
                13 - Onions\n
                14 - Banana Peppers\n
                15 - Diced Tomatoes\n
                16 - Black Olives\n
                17 - Mushrooms\n
                18 - Pineapple\n
                19 - Shredded Provolone Cheese\n
                20 - Cheddar Cheese\n
                21 - Green Peppers\n
                22 - Spinach\n
                23 - Roasted Red Peppers\n
                24 - Feta Cheese\n
                25 - Shredded Parmesan Asiago\n 
            ```
                """)
        try:
            messagelist = message.content.split()
            # toppings info
            toppingslist = messagelist[2].split(',')
            # customer info
            infolist = messagelist[3:]
            # reformat the infolist
            for i in range(len(infolist)):
                infolist[i] = infolist[i].strip()
                infolist[i] = infolist[i].strip(',')
            # check single or double is successfully selected
            if (messagelist[1] != 'single' and messagelist[1] != 'double'):
                await message.channel.send(
                    "Correct format is as follows: !dominos <single/double> <#,#,#> <First Name, Last Name, E-mail, Phone #>"
                )
                return
            # if 1 pizza, # toppings must = 3
            if (messagelist[1] == 'single' and len(toppingslist) != 3):
                await message.channel.send(
                    "Note: For a single pizza, # of toppings must = 3")
                return
            # if 2 pizzas, # toppings must = 2 or 4
            elif (messagelist[1] == 'double'
                  and (len(toppingslist) != 2 and len(toppingslist) != 4)):
                await message.channel.send(
                    "Note: For double, # toppings must = 2 or 4")
                return

            if (len(infolist) != 4):
                await message.channel.send(
                    "Correct format is as follows: !dominos <single/double> <#,#,#> <First Name, Last Name, E-mail, Phone #>"
                )
                return
            try:
                print("broken here 1")
                pizzaobj = orderDominos(messagelist[1], toppingslist, infolist)
                print("broken here 2")
                pizzaobj.find_nearest_store()
                if (pizzaobj.pizzatype == 'single'):
                    print("broken here 3")
                    pizzaobj.get_single()
                elif (pizzaobj.pizzatype == 'double'):
                    print("broken here 4")
                    pizzaobj.get_double()
                print("broken here 5")
                d = pizzaobj.checkout()
                await message.channel.send("Total cost for pizza(s): " +
                                           d['total'])
                await message.channel.send("Toppings for pizza: " +
                                           d['toppings'])

                await message.channel.send(
                    "Should I proceed? Type !confirmorder to confirm your order"
                )

                author = message.author

                def check_same_author(m):
                    return m.author == author

                check = await client.wait_for('message',
                                              check=check_same_author,
                                              timeout=60.0)
                await message.channel.send(check.content)
                if ("!confirmorder" in check.content):
                    await message.channel.send("Ordered completed.")
                else:
                    await message.channel.send(
                        "Pizza was NOT ordered successfully :sob:")
                return

            except:
                await message.channel.send(
                    "Pizza was NOT ordered successfully :sob:")
                return
        except:
            await message.channel.send(
                "Correct format is as follows: !dominos <single/double> <#,#,#> <First Name, Last Name, E-mail, Phone #>"
            )
            return

    elif "!diquacommands" in message.content:
        await message.channel.send("""
            ```NOTICE THE SPACES IN BETWEEN INPUTS. IMPORTANT!\n1. Order a dominos pizza: !dominos <single/double> <#,#,#> <First Name, Last Name, E-mail, Phone #>\n2. Set a reminder: !addreminder <#> <min/hr> <# repeats> <insert message>
               \nNote: For a single pizza, # of toppings must = 3. For double, # toppings must = 2 or 4  
            ```
            """)


minute_check.start()
client.run('NzkwMDE5MTQyNjkzODE0Mjg5.X96gqQ.Ny_k9Arqe7eylXY4LRCuiZaW5DM')
