from discord.ext import commands
import json
import discord

def load_data(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

    
def find_user_info(search_string, file_path='members.json'):
    # Load the data from the JSON file
    users_data = load_data(file_path)

    # Convert search string to lowercase
    search_string = search_string.lower()

    # List to store matching users
    matching_users = []

    # Loop over each user data
    for user in users_data:
        # Convert the user's name to lowercase and check if the search string is in it
        if search_string in user['name'].lower():
            # If user is a mentee, create a mentee message
            mentee_msg = f"{user['name']} is a mentee under {user['mentor']}" if user['mentee'] else f"{user['name']} is not a mentee"
            
            # Create a message
            message = (f"We found a user matching your search!\n\n"
                       f"User ID: {user['id']}\n"
                       f"Full name: {user['name']}\n"
                       f"Occupation: {user['position']}\n"
                       f"Roles in the team: {user['role']}\n"
                       f"{mentee_msg}\n"
                       f"Keep up the great work, {user['name']}!")

            # Add message to the list
            matching_users.append(message)

    # If the function hasn't returned by now, no user was found
    if not matching_users:
        return ["Sorry, we couldn't find a user with that name. Please try again."]

    return matching_users


import json

def categorize_users_by_team(users_file='members.json'):
    # Load the json data
    with open(users_file, 'r') as f:
        users_data = json.load(f)

    # Define the teams we are interested in
    interested_teams = ["team_one", "team_two", "leaders", "administrators", "seo", "designers", "marketing"]

    # Initialize a dictionary to hold the team data
    teams = {}

    # Loop over each user data
    for user in users_data:
        # Get the list of teams for the user, and normalize them to lowercase and strip leading and trailing white spaces
        teams_user = [team.lower().strip() for team in user['team'].split(',')]

        # Loop over each team
        for team in teams_user:
            # Add the user to the team in the dictionary if the team is one we are interested in
            if team in interested_teams:
                if team not in teams:
                    teams[team] = []
                teams[team].append(user['name'])

    # Generate a string that lists the users in each team
    message = "**🚀 Here's the breakdown of our amazing teams: 🚀**\n\n"
    for team, users in teams.items():
        message += f"**{team.capitalize()} Team ({len(users)} members):**\n"
        for user in users:
            message += f"👤 {user}\n"
        message += "\n"

    message += "Keep up the awesome work, everyone! 🎉"

    return message



COMMANDS_CHANNEL_ID = 1133198780322283540  # Replace with your channel's ID

def is_commands_channel():
    def predicate(ctx):
        if ctx.message.channel.id == COMMANDS_CHANNEL_ID:
            return True
        else:
            ctx.send("Please use commands in the correct channel!")
            return False
    return commands.check(predicate)


@commands.command()
@is_commands_channel()
async def ping(ctx):
    await ctx.send("pong")




@commands.command()
@is_commands_channel()
async def teams(ctx):
    await ctx.send("ok , here is the team")
    teams = categorize_users_by_team()
    print(teams)
    await ctx.send(teams)

@commands.command()
@is_commands_channel()
async def callme(ctx, *, nickname: str = None):
    """Change your nickname"""
    try:
        await ctx.author.edit(nick=nickname)
        if nickname:
            await ctx.send(f"Your nickname has been changed to {nickname}!")
        else:
            await ctx.send("Your nickname has been reset!")
    except commands.BotMissingPermissions:
        await ctx.send("I don't have permission to do that!")
    except commands.CommandInvokeError:
        await ctx.send("I'm unable to change your nickname. Make sure I have the correct permissions and that your role is not higher than mine.")
    except Exception as e:
        await ctx.send(f"An error occurred: we have higher privileges than me !!!")

    

@commands.command()
@is_commands_channel()
async def info(ctx,arg):

    datas = find_user_info(arg)

    if not len(datas):

        await ctx.send(f"There is no user with that name")

    else:

        for data in datas:
            await ctx.send(data)




@commands.command()
@is_commands_channel()
@commands.has_permissions(manage_nicknames=True)
async def call(ctx, member: discord.Member, *, nickname: str = None):
    """Change nickname of a user"""
    try:
        await member.edit(nick=nickname)
        if nickname:
            await ctx.send(f"{member.mention}'s nickname has been changed to {nickname}!")
        else:
            await ctx.send(f"{member.mention}'s nickname has been reset!")
    except commands.BotMissingPermissions:
        await ctx.send("I don't have permission to do that!")
    except commands.CommandInvokeError:
        await ctx.send("I'm unable to change the nickname. Make sure I have the correct permissions and that the user's role is not higher than mine.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
