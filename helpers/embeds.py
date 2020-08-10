import discord
from discord import embeds
from discord.colour import Color

ourEmbed = discord.Embed()


class EmbedMessage():
    def __init__(self, colour, title, image, subreddit, author, author_icon, link) -> None:
        self.colour = colour
        self.title = title
        self.image = image
        self.subreddit = subreddit
        self.author = author
        self.author_icon = author_icon
        self.link = link

    def getEmbedMessage(self):
        ourEmbed.clear_fields()
        ourEmbed.title = self.title
        print(self.image)
        ourEmbed.set_image(url=self.image)
        ourEmbed.set_footer(text="Posted on: " + self.subreddit +
                            "\nMeme by: " + self.author, icon_url=self.author_icon)
        ourEmbed.color = self.colour
        ourEmbed.insert_field_at(20, name="Link to post", value='[Go to post]({})'.format(self.link), inline=True)
        return ourEmbed