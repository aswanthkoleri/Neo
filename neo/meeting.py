import zulip

def getAllUsers(sender_email, bot_email):

    # Pass the path to your zuliprc file here.
    client = zulip.Client(config_file="~/.zuliprc")

    # Get all users in the realm
    result = client.get_members()

    emails = []
    for member in result['members']:
        email = member['email']
        if email != sender_email and email != bot_email:
            emails.append(member['email'])
    
    return emails
