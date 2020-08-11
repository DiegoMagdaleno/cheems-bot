import discord
from discord import embeds
from switch import Switch


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

class NekoEmbed(EmbedMessage):
    def __init__(self, colour, image, user_a, user_b, action) -> None:
        super().__init__(colour, None, image, None, None, None, None)
        self.user_a = user_a
        self.user_b = user_b
        self.action = action
    
    def getEmbedMessage(self):
        ourEmbed.clear_fields()
        with Switch(self.action) as case:
            if case("kiss"):
                ourEmbed.title = self.user_a + " is kissing " + self.user_b
            if case("hug"):
                ourEmbed.title = self.user_a + " is hugging " + self.user_b
            if case("headpat"):
                ourEmbed.title = self.user_a + " is patting " + self.user_b
            if case("slap"):
                ourEmbed.title = self.user_a + " is slapping " + self.user_b
            if case("cuddle"):
                ourEmbed.title = self.user_a + " is cludding with " + self.user_b
        ourEmbed.set_image(url=self.image)
        ourEmbed.color = self.colour
        return ourEmbed