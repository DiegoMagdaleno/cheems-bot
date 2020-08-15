# type: ignore
import discord
from switch import Switch


class EmbedMessage:
    def __init__(
        self,
        colour,
        title=None,
        image=None,
        source=None,
        author=None,
        author_icon=None,
        link=None,
    ) -> None:
        self.colour = colour
        self.title = title
        self.image = image
        self.source = source
        self.author = author
        self.author_icon = author_icon
        self.link = link


class RedditEmbedMessage(EmbedMessage):
    def __init__(
        self,
        colour: str,
        title: str,
        image: str,
        source: str,
        author: str,
        author_icon: str,
        link: str,
    ) -> None:
        super().__init__(colour, title, image, source, author, author_icon, link)

    def get_embed_message(self):
        self.embed_object_session = discord.Embed()
        self.embed_object_session.clear_fields()
        self.embed_object_session.title = self.title
        self.embed_object_session.set_image(url=self.image)
        self.embed_object_session.set_footer(
            text="Posted on: " + self.source + "\nMeme by: " + self.author,
            icon_url=self.author_icon,
        )
        self.embed_object_session.color = self.colour
        self.embed_object_session.insert_field_at(
            20,
            name="Link to post",
            value="[Go to post]({})".format(self.link),
            inline=True,
        )
        return self.embed_object_session


class FourChanEmbed(EmbedMessage):
    def __init__(
        self, colour: str, title: str, image: str, src: str, link: str
    ) -> None:
        super().__init__(colour=colour, title=title, image=image, source=src, link=link)

    def get_embed_message(self):
        self.embed_object_session = discord.Embed()
        self.embed_object_session.title = self.title
        self.embed_object_session.set_image(url=self.image)
        self.embed_object_session.set_footer(
            text="Posted on: 4chan\nOn board: " + self.source
        )
        self.embed_object_session.color = self.colour
        self.embed_object_session.insert_field_at(
            20,
            name="Link to thread",
            value="[Go to thread]({})".format(self.link),
            inline=True,
        )
        return self.embed_object_session


class NekoEmbed(EmbedMessage):
    def __init__(
        self, colour: str, image: str, user_a: str, user_b: str, action: str
    ) -> None:
        super().__init__(colour=colour, image=image)
        self.user_a = user_a
        self.user_b = user_b
        self.action = action

    def get_embed_message(self):
        self.embed_object_session = discord.Embed()
        self.embed_object_session.clear_fields()
        with Switch(self.action) as case:
            if case("kiss"):
                self.embed_object_session.title = (
                    self.user_a + " is kissing " + self.user_b
                )
            if case("hug"):
                self.embed_object_session.title = (
                    self.user_a + " is hugging " + self.user_b
                )
            if case("pat"):
                self.embed_object_session.title = (
                    self.user_a + " is patting " + self.user_b
                )
            if case("slap"):
                self.embed_object_session.title = (
                    self.user_a + " is slapping " + self.user_b
                )
            if case("cuddle"):
                self.embed_object_session.title = (
                    self.user_a + " is cludding with " + self.user_b
                )
            if case("tickle"):
                self.embed_object_session.title = (
                    self.user_a + " is tickling " + self.user_b
                )
        self.embed_object_session.set_image(url=self.image)
        self.embed_object_session.color = self.colour
        return self.embed_object_session
