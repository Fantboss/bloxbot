import discord
import openpyxl
token = "ODM5NjQxMjQyNzAyOTcwODgw.YJMm2A.vCErUGDxqozpm492a10XwRW1ZSs"
intents = discord.Intents.all()
Client = discord.Client(intents=intents)

@Client.event
async def on_ready():
    print("봇 준비 완료")
    print(Client.user)
    print("===============================")
    
@Client.event
async def on_message(message):
    if message.content == "야":
        await message.channel.send("왜")
    if message.content == "ㅎㅇ":
        await message.channel.send("ㅂㅇ")

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지 삭제 완료!")

    if message.content.startswith("!추방"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))

    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)
    if message.content.startswith("!경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.txt")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author.id):
                sheet ["B" + str(i)].value = int(sheet ["B" + str(i)].value) + 1
                file.save("경고.tsxt")
                if sheet ["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send("경고 2회 받으면, 서버에서 추방됩니다")
            else:
                await message.channel.send("경고를 1회 받았습니다.")
            break
        if sheet ["A" + str(i)].value == None:
            sheet ["A" + str(i)].value = str(author.id)
            sheet ["B" + str(i)].value = 1
            file.save("경고.txt")
            await message.channel.send("경고를 1회 받았습니다.")
        i += 1


Client.run(token)
    