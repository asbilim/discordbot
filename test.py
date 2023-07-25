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

print(categorize_users_by_team())  # Reads from the file 'members.json'
