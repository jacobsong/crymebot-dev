import discord
from discord.ext import commands
import asyncio
import config

client = commands.Bot(command_prefix = config.PREFIX)


@client.event
async def on_ready():
    print("Logged in as " + client.user.name + "#" + client.user.discriminator)


@client.command()
async def role(ctx, *, role: discord.Role):
    roles = discord.utils.get(ctx.guild.roles, name = f'{role}')
    author = ctx.message.author 
    await author.add_roles(roles)
    await author.send(f'{role} has been added.')


@client.command()
async def createarena(ctx, arenaID, Pass: int):
    author = ctx.message.author
    guild = ctx.message.guild
    if Pass >  100000000:
        msg = await ctx.channel.send("Arena password is invalid")
        await asyncio.sleep(10)
        await msg.delete()
    else:
        channel = await guild.create_text_channel(f'{author}s arena')
        await channel.send(f'__**{author} arena**__\nID = {arenaID} \nPassword = {Pass}')


@client.command()
async def hitbox(ctx, name: str, move: str):
    labels = ["Base Knockback", "Angle", "Damage", "Knockback Growth", "Frame", "FAF", "Self Damage"]
    try:
        data = config.hitboxData[name][move]
    except KeyError:
        await ctx.send("Invalid character or move name")
        return

    embed = discord.Embed(color=0x7289da)
    for i in range(7):
        embed.add_field(name=labels[i], value=data[i])
    embed.set_footer(text="Hitbox made by " + data[7])
    embed.set_image(url=data[8])
    await ctx.send(embed=embed)


@client.command()
async def unrole(ctx, *, role: discord.Role):
    roles = discord.utils.get(ctx.guild.roles, name = f'{role}')
    author = ctx.message.author
    await author.remove_roles(roles)
    await author.send(f'{role} has been successfully removed')


client.run(config.TOKEN)
