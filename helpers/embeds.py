import discord
from discord.colour import Color

ourEmbed = discord.Embed()


class EmbedMessage():
    def __init__(self, colour, title, image, subreddit, author, author_icon) -> None:
        self.colour = colour
        self.title = title
        self.image = image
        self.subreddit = subreddit
        self.author = author
        self.author_icon = author_icon

    def getEmbedMessage(self):
        ourEmbed.title = self.title
        print(self.image)
        ourEmbed.set_image(url=self.image)
        ourEmbed.set_footer(text="Posted on: " + self.subreddit +
                            "\nMeme by: " + self.author, icon_url=self.author_icon)
        ourEmbed.color = self.colour
        return ourEmbed
