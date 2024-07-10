import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command(name='start')
async def list(ctx):
    await ctx.send('ну привет)')


@bot.command(name='fact') 
async def list(ctx):
    list_facts = ['Хамелеоны могут двигать глазами в разных направлениях одновременно.',
             'Белка – лучший садовник. Миллионы деревьев вырастают потому, что белки забывают, куда спрятали семечки.',
             'У млекопитающих кровь красная, у насекомых жёлтая, у омаров синяя.',
             'Муравьи никогда не спят. Вместо этого, они «отдыхают» по восемь минут “отдохнуть” два раза в день. Отдых королевы муравьев занимает  90 минут в день.'
             ]

    fact = random.choice(list_facts)
    await ctx.send(fact)

bot.run("token")
