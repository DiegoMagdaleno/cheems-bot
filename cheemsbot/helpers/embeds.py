# type: ignore
from cheemsbot.helpers.fourchan import FourChanPost
from re import T
from cheemsbot.helpers.github import GitHubRepository
from cheemsbot.helpers.wikipedia import WikipediaArticle
from prawcore import auth
from cheemsbot.helpers.reddit import RedditPostContents, RedditSession
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
    def __init__(self, post: RedditPostContents, post_type: str) -> None:
        super().__init__(
            discord.Color.orange(),
            post.title,
            post.image,
            post.subreddit,
            post.author,
            post.author_avatar,
            post.link,
        )
        self.type = post_type

    def get_embed_message(self):
        self.embed_object_session = discord.Embed()
        self.embed_object_session.clear_fields()
        self.embed_object_session.title = self.title
        self.embed_object_session.set_image(url=self.image)
        with Switch(self.type) as case:
            if case("post"):
                self.credit_string = "Post by:"
            if case("meme"):
                self.credit_string = "Meme by:"
        self.embed_object_session.set_footer(
            text="Posted on: {0}\n{1} {2}".format(
                self.source, self.credit_string, self.author
            ),
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
    def __init__(self, post: FourChanPost) -> None:
        super().__init__(
            discord.Color.green(),
            post.submission_topic,
            post.submission_image_url,
            post.board_title,
            post.submission_url,
        )

    def get_embed_message(self):
        self.embed_object_session = discord.Embed()
        self.embed_object_session.title = self.title
        self.embed_object_session.set_image(url=self.image)
        self.embed_object_session.set_footer(
            text=f"Posted on board: {self.source} at 4chan!"
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
        self, image: str, user_a: str, user_b: str, action: str
    ) -> None:
        super().__init__(colour=discord.Color.blurple(), image=image)
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


class WikipediaEmbed(EmbedMessage):
    def __init__(self, colour: str, article: WikipediaArticle) -> None:
        super().__init__(
            colour=colour, author=article.author, author_icon=article.icon_url
        )

        self.article = article

    def get_embed_message(self):
        self.embed_object_session = discord.Embed()
        self.embed_object_session.clear_fields()
        self.embed_object_session.title = "**{}**".format(self.article.name)
        self.embed_object_session.url = self.article.url
        self.embed_object_session.description = self.article.description

        self.embed_object_session.set_footer(
            text="Article last modified:", icon_url=self.author_icon
        )

        self.embed_object_session.set_author(
            name="Wikipedia", url="https://wikipedia.org", icon_url=self.author_icon
        )
        self.embed_object_session.timestamp = self.article.last_modified
        return self.embed_object_session


class GitHubEmbed(EmbedMessage):
    def __init__(self, colour: str, repository: GitHubRepository) -> None:
        super().__init__(colour=colour)
        self.repository = repository

    def get_embed_message(self):
        self.embed_object_session = discord.Embed()
        self.embed_object_session.title = self.repository.full_name
        self.embed_object_session.url = self.repository.url
        self.embed_object_session.description = self.repository.description
        self.embed_object_session.add_field(
            name="Stars", value=self.repository.stars, inline=True
        )
        self.embed_object_session.add_field(
            name="Forks", value=self.repository.forks, inline=True
        )
        self.embed_object_session.add_field(
            name="Issues", value=self.repository.open_issues, inline=True
        )
        self.embed_object_session.add_field(
            name="Private", value=str(self.repository.is_private), inline=True
        )
        self.embed_object_session.set_author(
            name="GitHub Repository info",
            icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
        )
        self.embed_object_session.set_thumbnail(url=self.repository.avatar_url)
        if self.repository.license_id == "NOASSERTION":
            self.embed_object_session.add_field(
                name="License", value="Other Non-standard license.", inline=True
            )
        elif self.repository.license_id is None:
            self.embed_object_session.add_field(
                name="License", value="All rights reserved.", inline=True
            )
        else:
            self.embed_object_session.add_field(
                name="License", value=self.repository.license_id, inline=True
            )

        return self.embed_object_session
