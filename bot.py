# AnnoyBot x TreeHuggr
# Athena Award
# Stephanie Uzea
# This program is meant to annoy people who send my emoji in one of the servers I'm in :3 . To repurpose it for most servers, it also sends positive messages related to the environment to raise awareness.
# v1 9/29/2025, v2 10/14/2025

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

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# TreeHuggr
quotes_ball = [
    '"*For many people around the world, the climate crisis is already a question of life and death.*"\n—**Camille Etienne** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*It is time to prioritize people and our planet over short-term profits.*"\n—**Elizabeth Wathuti** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*But there is still hope! Hope that can be found in the resilience of our vulnerable communities.*"\n—**Brianna Fruea** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*A win for us, is a win for our planet.*"\n—**Helena Gualinga** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*The best time to plant a tree is 20 years ago; the next best time is now.*"\n—**Dean Bhebhe** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*Now is the time for change and now is the time for real action.*"\n—**Jerome Foster II** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*We are the first generation to feel the effect of climate change and the last generation who can do something about it.*"\n—**Barack Obama** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*Believe in the power of your own voice. The more noise you make, the more accountability you demand from your leaders, the more our world will change for the better.*"\n—**Al Gore** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*Twenty-five years ago people could be excused for not knowing much, or doing much, about climate change. Today we have no excuse.*"\n—**Desmond Tutu** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*What you do makes a difference, and you have to decide what kind of difference you want to make.*"\n—**Jane Goodall** . ݁₊ ⊹ . ݁˖ . ݁💚',
    '"*Harmony with land is like harmony with a friend; you cannot cherish his right hand and chop off his left.*"\n—**Aldo Leopold** . ݁₊ ⊹ . ݁˖ . ݁💚'
]

tips_speech = ["🌟 From bags to waterbottles, go reusable! This prevents pollution. 🌟", 
               "🌟 Turn off lights, electronics, and chargers when they're not being used. This helps conserve energy. 🌟", 
               "🌟 Walk, bike, carpool, or use public transit for shorter trips. This lowers your carbon footprint. 🌟", 
               "🌟 Plant flowers or herbs in pots or on a balcony to support pollinators. 🌟", 
               "🌟 Check out organizations in your neighborhood to volunteer in conservation efforts! 🌟", 
               "🌟 You'd be impressed how useful a single piece of paper could be. Use all sides of a sheet before recycling it! 🌟", 
               "🌟 Reduce, reuse, and THEN recycle. 🌟",
               "🌟 Any artists in here? Turn your waste into art! 🌟",
               "🌟 Your voice matters. Spread the word, and take a stand. 🌟"
]

plant_emojis = {
    "🌵", "🌲", "🌳", "🌴", "🌱", "🌿", "☘️", "🍀", "🎍", "🪴",
    "🍃", "🍂", "🍁", "🍄", "🐚", "🪸", "🌷", "🌹", "💠",
    "🌸", "🌺", "🌻"
}

@bot.command()
async def quote(ctx):
    await ctx.send(random.choice(quotes_ball))

@bot.command()
async def tip(ctx):
    await ctx.send(random.choice(tips_speech))





# AnnoyBot
emoji_bag = {
    LUCASIO_EMOJI, LUCASIO_EMOJI, LUCASIO_EMOJI, LUCASIO_EMOJI, LUCASIO_EMOJI, 
    LILI_FLUTE_EMOJI, 
    LILI_2_EMOJI, 
    GHOST_LILI_EMOJI
}

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
    await bot.process_commands(message)



@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    
    # AnnoyBot
    if hasattr(reaction.emoji, 'id') and (reaction.emoji.id == STEPHI_LURKING_ID or reaction.emoji.id == STEPHANIE_ID or reaction.emoji.id == STEPHI_SMIRK_ID):
        one_in_a_melon = random.sample(list(set(emoji_bag)), 2)
        for emoji in one_in_a_melon:
            await reaction.message.add_reaction(emoji)
    
    # TreeHuggr
    elif str(reaction.emoji) in plant_emojis:
        await reaction.message.add_reaction("✨")
        await reaction.message.add_reaction("💚")

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot.run(BOT_TOKEN)