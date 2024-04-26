import discord
from discord import app_commands
from discord.ext import commands
from ..Cow import config
import random
async def send_message(message, user_message, is_private):
    # try:
    #     response = "Hello"
    #     await message.author.send(response) if is_private else await message.channel.send(response)
    # except Exception as e:
    #     print(e)
    pass

def run_discord_bot():
    TOKEN = config.token_discord

    # Define the intents and enable them
    intents = discord.Intents.default()
    intents.typing = False  # Disable typing events if desired
    intents.presences = False  # Disable presence events if desired
    intents.messages = True  # Enable message events
    intents.message_content = True

    # Explicitly enable privileged intents (for members and message content)
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

        if user_message and user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


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
            await interaction.response.send_message(f"you lost")
            print(f" {interaction.user} gambled and lost")
        else:
            print(f" {interaction.user} gambled")
            await interaction.response.send_message(f"{number}")


    # Run the bot
    bot.run(TOKEN)






run_discord_bot()