<h1 align="center">
    <br>
    <a href="https://github.com/DiegoMagdaleno/cheems-bot"><img src="https://i.imgur.com/gymxVRg.jpg" width=25% height=25%></a>
    <br>
    Cheems Bot!
    <br>
</h1>

<h4 align="center">Reddit, 4chan, Memes, Package managers, Information.</h4>

<p align="center">
<a href="https://github.com/diegomagdaleno/cheems-bot/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/diegomagdaleno/cheems-bot?style=flat-square"></a>
<a href="https://github.com/diegomagdaleno/cheems-bot/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/diegomagdaleno/cheems-bot?style=flat-square"></a>
<a href="https://github.com/diegomagdaleno/cheems-bot/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/diegomagdaleno/cheems-bot?style=flat-square"></a>
</p>


<p align="center">
    <a href="#overview">Overview</a>
    •
    <a href="#installation">Installation</a>
    •
    <a href="">Documentation</a>
    •
    <a href="#contributing">Contributing</a>
    •
    <a href="#credits">Credits</a>
</p>

# Overview

Cheems bot was a project created by me and a couple of friends, the original intention was to be able to get r/Dogelore memes on the Discord chat, however the project quickly scalated to become a multifunctional Discord bot.

The goal of Cheems then became to make a easy to install, self-hosted multifunctional Discord bot. While Cheems is still in early development it can perform a lot of actions and operations!

**Some features:**
- Check Dogelore memes
- Get memes from different subreddits
- Get 4chan posts from a board
- Get NSFW content 
- Get cute images of animals
- Get Homebrew packages information
- Get GitHub repository information
- Get Urban Dictionary information
- Get Google images

Cheems is install in development and the stuff that it can do, is getting bigger and bigger! In the future, Cheems might even be able to fully moderate servers.

# Installation

We support the major platforms, but pretty much any operating system that is UNIX-like or NT should be supported!, still you can see specific for each platform:

- [Windows]()
- [macOS]()
- [Linux]()

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

