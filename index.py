import discord
import os 
token = "ODM5NjQxMjQyNzAyOTcwODgw.YJMm2A.Bghz8ZgtzE07T533touSgTwhNdE"
Client = discord.Client()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@Client.event
async def on_ready(): #봇이 준비되었을떄
    print("봇 준비 완료!")
    print(Client.user)
    print("===============================")

@Client.event
async def on_message(message):
    if message.content == "야":
        await message.channel.send("왜")
    if message.content == "ㅎㅇ":
        await message.channel.send("ㅂㅇ")

    if message.content == "임베드내놔":
        embed = discord.Embed(Colour=discord.Colour.random(), title="서버소개", description="이 서버는 Fantboss가 운영하는 서버입니다!")
        await message.channel.send(embed=embed)

    if message.content.startswith(f"!채널메시지"):
        ch = Client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지 삭제 완료!")

    if message.content.startswith("!추방"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.kick(member, reason=''.join(message.content.split(" ")[2:]))

    if message.content.startswith("!차단"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.ban(member, reason=''.join(message.content.split(" ")[2:]))

Client.run(token)
