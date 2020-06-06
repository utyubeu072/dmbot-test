
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('Test')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 718821623083433984:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="제목")
                        embed.add_field(name=".", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/DxvmbN4")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzE4ODIwMjkxOTc1MDUzMzYy.Xtueqg.ue9Gw1xVw6Qc2fO8MRnPCdFkAsk')
