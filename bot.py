import json
import requests
import discord
import asyncio

client = discord.Client()


def get_question():
    qs = ""
    id = 1
    answer = 0
    response = requests.get("http://127.0.0.1:8000/api/random/")
    data = json.loads(response.text)
    qs += "Question: \n"
    qs += data["title"] + "\n"
    for item in data["answer"]:
        qs += str(id) + ". " + item["answer"] + "\n"
        if item["is_correct"]:
            answer = id
        id += 1

    return (qs, answer)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("hello"):
        await message.channel.send("hello, I am a bot")

    if message.content.lower().startswith("!question"):
        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for("message", check=check, timeout=5.0)
            if int(guess.content) == answer:
                await message.channel.send("Correct!")
            else:
                await message.channel.send("Wrong!")
            # await message.channel.send("Would you like to play again?")
            # confirmation = await client.wait_for("message", check=check, timeout=10.0)

        except asyncio.TimeoutError:
            await message.channel.send("You took too long to answer!")
            return


client.run("OTg1NzgwODIzNTA2NzAyMzk2.G6i7mW.H7lBkf5Kf3t2kEj2BEdt1OUZIi1OBAkFjVxPNk")
