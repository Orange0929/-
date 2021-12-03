import discord
import asyncio

client = discord.Client()

token = "OTE2MzEyOTMxODMzMTEwNTQ4.YaoU6w._JQrRlbY2h8o295Oek_WRkaoNo0"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇이 성공적으로 작동됬습니다.')
    game = discord.Game('채팅이 열심히 일')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "ㄹㅇ":
        await message.channel.send (f"ㅋㅋ")

@client.event
async def on_message(message):
    if message.content == "시":
        await message.channel.send (f"발")
    


client.run(token)