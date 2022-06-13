import json
import requests
import discord
import asyncio
from decouple import config

token = config("TOKEN")

client = discord.Client()


def get_score():
    leaderboard = "LEADERBOARD\n\n"
    id = 1
    response = requests.get(
        "http://intense-forest-59687.herokuapp.com/api/score/leaderboard"
    )
    data = json.loads(response.text)
    for item in data:
        leaderboard += str(id) + ". " + item["name"] + ": " + str(item["points"]) + "\n"
        id += 1
    return leaderboard


def update_score(user, points):
    new_points = {"name": user, "points": points}
    response = requests.post(
        "http://intense-forest-59687.herokuapp.com/api/score/update", data=new_points
    )
    return


def get_question():
    qs = ""
    id = 1
    answer = 0
    response = requests.get("http://intense-forest-59687.herokuapp.com/api/random/")
    data = json.loads(response.text)
    qs += "Question: \n"
    qs += data["title"] + "\n"
    for item in data["answer"]:
        qs += str(id) + ". " + item["answer"] + "\n"
        if item["is_correct"]:
            answer = id
        id += 1
    points = data["points"]
    return (qs, answer, points)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!score"):
        leaderboard = get_score()
        await message.channel.send(leaderboard)

    if message.content.lower().startswith("hello"):
        await message.channel.send("hello, I am a bot")

    if message.content.lower().startswith("!question"):
        qs, answer, points = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for("message", check=check, timeout=5.0)
            if int(guess.content) == answer:
                msg = (
                    str(guess.author.name)
                    + " got it right! +"
                    + str(points)
                    + " points."
                )
                await message.channel.send(msg)
                update_score(message.author, points)
            else:
                await message.channel.send("Wrong!")
            # await message.channel.send("Would you like to play again?")
            # confirmation = await client.wait_for("message", check=check, timeout=10.0)

        except asyncio.TimeoutError:
            await message.channel.send("You took too long to answer!")
            return


client.run(token)
