import discord
import json
import time
import requests
import asyncio

from discord.ext import commands
from asyncio import sleep
from config import settings

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.command()
async def хелптест(ctx):
    author = ctx.message.author
    embed = discord.Embed(color = 0xff0000, title="Список команд", description="Поможет с командами!")
    embed.add_field(name="Картинки", value="you can make as much as fields you like to")
    embed.add_field(name="Текст", value="you can make as much as fields you like to")
    embed.set_footer(name="footer") 
    await ctx.send(embed=embed)

@bot.command() 
async def привет(ctx):
    author = ctx.message.author 
    await ctx.send(f'Привет, {author.mention}!')

@bot.command() 
async def нитро(ctx): 
    author = ctx.message.author 
    await ctx.send(f'У меня пока нет нитро кодов, {author.mention}😔') 

@bot.command()
async def кошак(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff0000, title = 'Кошак')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def птиц(ctx):
    response = requests.get('https://some-random-api.ml/img/birb') 
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff0000, title = 'Птиц')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def панда(ctx):
    response = requests.get('https://some-random-api.ml/img/panda') 
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff0000, title = 'Панда')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def краснаяпанда(ctx):
    response = requests.get('https://some-random-api.ml/img/red_panda')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff0000, title = 'Фаерфокс')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def собак(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff0000, title = 'Собак')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff0000, title = 'ЛИС')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def коала(ctx):
    response = requests.get('https://some-random-api.ml/img/koala')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff0000, title = 'Коала)')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def хелп(ctx): 
    author = ctx.message.author
    await ctx.send(f'Я ещё не доделан но, у меня уже есть весёлости!')
    await ctx.send(f'Картинки:')
    await ctx.send(f'!кошак, !собак, !лиса, !птиц, !панда !краснаяпанда, !коала.')
    await ctx.send(f'Текст: ')
    await ctx.send(f'!привет, !нитро.')

bot.run(settings['token']) 