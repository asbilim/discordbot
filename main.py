import discord
import os
from discord.ext import commands
from functions import ping,info,teams,callme,call

intents = discord.Intents.all()
token = os.getenv('DISCORD_BOT_TOKEN')
bot =  commands.Bot(command_prefix="newgenbot ", intents=intents)

@bot.event
async def on_message(message):


    if message.content.startswith('newgenbot ') and message.channel.id != 1133198780322283540:
        await message.channel.send(f"hello @{message.author.name} this is not the appropriate channel for commands, go to #commands")

    await bot.process_commands(message)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Please use commands in the correct channel!")


class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.send_welcome_message(member)
        channel = bot.get_channel(1132993981932912725)
        await channel.send(f"🎉 Welcome to NewGen Africa, {member.mention}! We're thrilled to have you here. 🎉\nMake sure to check out the rules and feel free to introduce yourself. Enjoy your stay!")

    async def send_welcome_message(self, member):
        message = (f"Welcome to our server, {member.name}!\n\n"
                   f"Here's how things work around here:\n\n"
                   f"1️⃣ **GENERAL Category:** This is where the general conversation happens. It includes the general and staff channels.\n"
                   f"2️⃣ **TEAMS Category:** This is where team-specific discussions take place. Depending on your team, you will have access to team-one, team-two, or designers channels.\n"
                   f"3️⃣ **PROJECTS Category:** This is where project ideas, submissions, and selected projects are discussed.\n"
                   f"4️⃣ **QUALITY EXPERIENCE Category:** This category is for enhancing the quality of conversation and interaction in our server.\n"
                   f"5️⃣ **INFORMATIONS Category:** This is where you will find important information. It includes welcome and rules, announcements, resources, and commands channels.\n\n"
                   f"Remember to always be respectful and considerate to others. Enjoy your stay! 😊")
        try:
            await member.send(message)
        except discord.Forbidden:
            print(f"Failed to send DM to {member.name}")


    
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    await bot.add_cog(WelcomeCog(bot))

bot.add_command(ping)  # Add the ping command to the bot
bot.add_command(info)
bot.add_command(teams)
bot.add_command(callme)
bot.add_command(call)


if __name__ == '__main__':
    bot.run(token)
