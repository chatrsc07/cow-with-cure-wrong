import discord
from discord import app_commands
from discord.ext import commands
from config import token_discord
from datetime import timedelta
import random
import os
async def send_message(message, user_message, is_private):
    try:
        response = "Hello"
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    pass

def run_discord_bot():
    TOKEN = token_discord

    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    intents.messages = True
    intents.message_content = True

    intents.members = True
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')
        try:
            synced = await bot.tree.sync()
            print (f"synced {len(synced)} command(s)")
        except Exception as e:
            print (e)
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"Received message in {channel} from {username}: '{user_message}'")

        # if user_message and user_message[0] == '?':
        #     user_message = user_message[1:]
        #     await send_message(message, user_message, is_private=True)
        # else:
        #     await send_message(message, user_message, is_private=False)


    # @bot.tree.command(name="test")
    # async def hello(interaction: discord.Interaction):
    #     print(f" hello command from {interaction.user}")
    #     await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!")
    #
    # @bot.tree.command(name="yes")
    # @app_commands.describe(thing_to_say = "what should I say")
    # async def say(interaction: discord.Interaction, thing_to_say: str):
    #     print(f" say command from {interaction.user} saying {thing_to_say}")
    #     await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}` ")


    @bot.tree.command(name="cramble")
    async def Cramble(interaction: discord.Interaction):
        number = random.randint(1, 20)
        if number <= 15:
            await interaction.response.send_message(f"Bithcy Mitchy")
            duration = timedelta(days=0, seconds=0, minutes=20)
            await interaction.user.timeout(duration)
            print(f" {interaction.user} gambled and lost")
            update_number_in_file(interaction.user.id)
        else:
            print(f" {interaction.user} gambled")
            await interaction.response.send_message(f"{number}")


    bot.run(TOKEN)




def update_number_in_file(target_number):
    lines = []
    found = False

    # Check if the file exists
    if not os.path.exists('data.txt'):
        with open('data.txt', 'w') as file:
            file.write('')

    with open('data.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) == 2:
                number, value = parts
                if number == target_number:
                    value = str(int(value) + 1)
                    found = True
                lines.append(f'{number}, {value}\n')

    if not found:
        lines.append(f'{target_number}, 1\n')

    with open('data.txt', 'w') as file:
        file.writelines(lines)




run_discord_bot()