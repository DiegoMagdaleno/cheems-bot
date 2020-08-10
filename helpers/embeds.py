import discord
from discord import embeds

ourEmbed = discord.Embed()


class EmbedMessage():
    def __init__(self, colour, title, image, source, author, author_icon, link) -> None:
        self.colour = colour
        self.title = title
        self.image = image
        self.source = source
        self.author = author
        self.author_icon = author_icon
        self.link = link

class RedditEmbedMessage(EmbedMessage):
    def __init__(self, colour, title, image, source, author, author_icon, link) -> None:
        super().__init__(colour, title, image, source, author, author_icon, link)
    
    def getEmbedMessage(self):
        ourEmbed.clear_fields()
        ourEmbed.title = self.title
        ourEmbed.set_image(url=self.image)
        ourEmbed.set_footer(text="Posted on: " + self.source +
                            "\nMeme by: " + self.author, icon_url=self.author_icon)
        ourEmbed.color = self.colour
        ourEmbed.insert_field_at(20, name="Link to post", value='[Go to post]({})'.format(self.link), inline=True)
        return ourEmbed

class FourChanEmbed(EmbedMessage):
    def __init__(self, colour, title, image, source, link) -> None:
        super().__init__(colour, title, image, source, None, None, link)
    
    def getEmbedMessage(self):
        ourEmbed.clear_fields()
        ourEmbed.title = self.title
        ourEmbed.set_image(url=self.image)
        ourEmbed.set_footer(text="Posted on: 4chan\nOn board: " + self.source)
        ourEmbed.color = self.colour
        ourEmbed.insert_field_at(20, name="Link to thread", value="[Go to thread]({})".format(self.link), inline=True)
        return ourEmbed