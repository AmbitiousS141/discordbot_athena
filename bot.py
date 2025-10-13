# AnnoyBot
# Athena Award
# Stephanie Uzea
# This program is meant to annoy people who send my emoji in one of the servers I'm in :3
# v1 9/29/2025

import random
import discord
from discord.ext import commands
from dotenv import load_dotenv, dotenv_values
import os


STEPHI_LURKING_ID = 1362259950767706193
STEPHANIE_ID = 1310081903579238440
STEPHI_SMIRK_ID = 1356730689705218069
LUCASIO_ID = 1360023421789929542
LILI_FLUTE_ID = 1310363420717223988
LILI_2_ID = 1310405735913361458
GHOST_LILI_ID = 1350626640698282035

STEPHI_LURKING_EMOJI = "<:stephi_lurking:1362259950767706193>"
STEPHANIE_EMOJI = "<:stephanie:1310081903579238440>"
STEPHI_SMIRK_EMOJI = "<:stephismirk:1356730689705218069>"
LUCASIO_EMOJI = "<:lucasio:1360023421789929542>"
LILI_FLUTE_EMOJI = "<:lili_flute:1310363420717223988>"
LILI_2_EMOJI = "<:lili_2:1310405735913361458>"
GHOST_LILI_EMOJI = "<:ghost_lili:1350626640698282035>"

emoji_bag = [LUCASIO_EMOJI, LUCASIO_EMOJI, LUCASIO_EMOJI, LUCASIO_EMOJI, LUCASIO_EMOJI, LILI_FLUTE_EMOJI, LILI_2_EMOJI, GHOST_LILI_EMOJI]

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if (f"<:stephi_lurking:{STEPHI_LURKING_ID}>" in message.content) or (f"<:stephanie:{STEPHANIE_ID}>" in message.content) or (f"<:stephismirk:{STEPHI_SMIRK_ID}>" in message.content):
        num1 = message.content.count("<:stephi_lurking:1362259950767706193>")
        num2 = message.content.count("<:stephanie:1310081903579238440>")
        num3 = message.content.count("<:stephismirk:1356730689705218069>")
        chosen_ones = ''
        for i in range((num1 + num2 + num3)*3):
            next_emoji = random.choice(emoji_bag)
            if len(chosen_ones) + len(next_emoji) > 2000:
                break
            chosen_ones += next_emoji
        await message.channel.send(chosen_ones)


@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if hasattr(reaction.emoji, 'id') and (reaction.emoji.id == STEPHI_LURKING_ID or reaction.emoji.id == STEPHANIE_ID or reaction.emoji.id == STEPHI_SMIRK_ID):
        one_in_a_melon = random.sample(list(set(emoji_bag)), 2)
        for emoji in one_in_a_melon:
            await reaction.message.add_reaction(emoji)

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot.run(BOT_TOKEN) 