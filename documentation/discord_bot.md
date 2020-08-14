# Setting up a bot Discord account.
Cheems bot guide, special thanks to [DiscordPy](https://discordpy.readthedocs.io/en/latest/discord.html) for providing a lot of this images.

1. Make sure you are logged into the [Discord website](https://discord.com).
2. Next navigate to the [Application page](https://discord.com/developers/applications)
3. Once you are there, click on the "New Application button" it looks like this:
### Setting up a bot Discord account.

1. Make sure you are logged into the [Discord website](https://discord.com).
2. Next navigate to the [Application page](https://discord.com/developers/applications)
3. Once you are there, click on the "New Application button" it looks like this:

![New app button](https://discordpy.readthedocs.io/en/latest/_images/discord_create_app_button.png)

4. Give the application a name, and click on create (The application name doesn't matter)

![Application name](https://discordpy.readthedocs.io/en/latest/_images/discord_create_app_form.png)

5. Create a Bot User by navigating to the “Bot” tab and clicking “Add Bot”, You will need to click "Yes, do it!" to continue.

![Creating a bot user](https://discordpy.readthedocs.io/en/latest/_images/discord_create_bot_user.png)

6. Make sure that **Public Bot** is ticked if you want others to invite your bot. (_Fair warning: If your computer is not that powerful you only want one instance of 
Cheems running_)
    - You should also make sure that Require OAuth2 Code Grant is unchecked unless you are developing a service that needs it. If you’re unsure, then leave it unchecked.

![Creating the bot itself](https://discordpy.readthedocs.io/en/latest/_images/discord_bot_user_options.png)

7. Copy the token using the “Copy” button. (**IMPORTANT WARNING HERE: NEVER SHARE THIS TOKEN, IT IS LIKE YOUR BOTS PASSWORD**)

### Inviting the bot account.

**Note:** Cheems isn't running yet, think of this as if you bought a lamp, the code in this server is the power outlet, you can place the lamp, but it is useless until
you connect it to a power outlet

1. Make sure you are again in the [Application page](https://discord.com/developers/applications).
2. Click on your bot's page (The one you just created)
3. Go to the “OAuth2” tab, it looks like this:

![OAuth2 tab](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2.png)

4. Tick the “bot” checkbox under “scopes”, this looks like this:

![Bot Checkbox](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2_scope.png)

6. Tick the permissions required for Cheems to function under “Bot Permissions”, as of now the perms Cheems required as not a lot, since it is unable to moderate.
Howerver, it is planned that Cheems is able to moderate in future versions. Here is a quick example (You can check others):

![Cheems perms config](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2_perms.png)

7. Now the resulting URL can be used to add Cheems to a server. Copy and paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.
