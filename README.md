# WARNING: CHEEMS IS IN ACTIVE, VERY ACTIVE DEVELOPMENT, (ALPHA) AND IT DOESN'T HAVE A STABLE INTERFACE. IT ISN'T RECOMMENDED TO SELF HOST CHEEMS YET, AS IT ISNT MOVES VERY VERY VERY, A FEATURE THAT WAS ADDED AN HOUR AGO COULD BE REMOVED IN A MINUTE. WAIT FOR A STABLE RELEASE.

<p align="center">
<img src="https://i.imgur.com/gymxVRg.jpg" width=25% height=25%/>
</p>

# Cheems bot
mmmmm Dismcord, Cheems is a Discord bot created by me and some friends to have fun, it is still on early development, however it is able to do a lot of stuff and provide 
fun to your Discord server!

## Table of notes

- [Requirements](#requirements)
- [Installation](#installation)
- [Contributing](#contributing)

## Requirements

In order to install and get an instance of Cheems running, you will need:

1. A computer that has good uptime (Running Windows, macOS or Linux)
2. Python 3 installed on your computer. If you don't have Python you can install it [here](https://www.python.org/downloads/).
3. A text editor (Can be notepad, but I recommend [Visual Studio Code](https://code.visualstudio.com/))

## Installation

Before you install and get Cheems running, Cheems requires some stuff to be able to provide all features:

1. A bot Discord account.
2. A Reddit account, with a "developer" application.

You can skip this sections, if you already have this requirements.

Tutorials on how to setup these can be found here:
- [Discord](https://github.com/DiegoMagdaleno/cheems-bot/blob/master/documentation/discord_bot.md)
- [Reddit](https://github.com/DiegoMagdaleno/cheems-bot/blob/master/documentation/reddit_dev.md)

After you have setup your account to perform any operations that Cheems might need, it is now time to run our setup script.

Now this changes depending on your operating system.

A "UNIX" based operating system, needs to run `setup.sh` while an NT based operating system needs to run `setup.bat`. 

To determine if your operating system is UNIX or NT based you can just find your operating system here:

- **UNIX BASED**:
    - macOS / OS X
    - Linux
    - *BSD (FreeBSD, OpenBSD)
    - Android
    - ChromeOS
- **NT BASED**:
    - Windows

Once you determine what kind of operating system you have, it is now time to run the script, you need access to terminal in the case of UNIX based operating systems, and to Powershell/Terminal Windows app in the case of NT Operating systems.

If you don't know how to open the terminal in your operating system, a quick Google search should be enough.

Now run the script that is needed in your operating system, by dragging and dropping into the terminal, or changing directory `cd` into the location and executing `setup.sh` or `setup.bat`.

Follow the configuration process, here is an example:

```
❯ ./setup.sh
What's your Reddit client ID?:
rerdasf
What's your Reddit client secret?:
afdsafadsfads
What's your Reddit user agent?:
fadsfadsfasd
What's your Reddit username?
fadsfadsfds
What's your Reddit password?
fdasfdasfdasfdasf
What's your Discord bot token?
fadsafadsfadsf
```

Once you are done, active the Python environment by using the following command `source ./venv/bin/activate`.

Now execute main.py inside cheemsbot using your python installation.

You are done and ready to have fun with cheems.

