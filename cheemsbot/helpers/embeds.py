# type: ignore
from cheemsbot.helpers.brew import HomebrewPackage
from cheemsbot.helpers.fourchan import FourChanPost
from cheemsbot.helpers.github import GitHubRepository
from cheemsbot.helpers.wikipedia import WikipediaArticle
from cheemsbot.helpers.reddit import RedditPostContents
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
        footer_string=None,
        footer_author_url=None,
    ) -> None:
        self.colour = colour
        self.title = title
        self.image = image
        self.source = source
        self.author = author
        self.author_icon = author_icon
        self.link = link
        self.footer_string = footer_string
        self.footer_author_url = footer_author_url

        # !? Discord embed object intialization.
        self.object_embed_session = discord.Embed()
        self.object_embed_session.color = self.colour
        self.object_embed_session.title = self.title
        if self.image is not None:
            self.object_embed_session.set_image(url=self.image)
        if self.footer_string is not None or self.footer_author_url is not None:
            self.object_embed_session.set_footer(text=self.footer_string,icon_url=self.footer_author_url)

    def get_embed_message(self):
        return self.object_embed_session


class RedditEmbedMessage(EmbedMessage):
    def __init__(self, post: RedditPostContents, post_type: str) -> None:
        self.type = post_type
        with Switch(self.type) as case:
            if case("post"):
                self.credit_string = "Post by:"
            if case("meme"):
                self.credit_string = "Meme by:"
        super().__init__(
            colour=discord.Color.orange(),
            title=post.title,
            image=post.image,
            source=post.subreddit,
            author=post.author,
            author_icon=post.author_avatar,
            link=post.link,
            footer_author_url=post.author_avatar,
            footer_string=f"Posted on: {post.subreddit}\n{self.credit_string} {post.author}"
        )

        self.object_embed_session.insert_field_at(
            20, name="Link to post", value=f"[Go to post]({self.link})", inline=True,
        )

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
            value=f"[Go to thread]({self.link})",
            inline=True,
        )
        return self.embed_object_session


class NekoEmbed(EmbedMessage):
    def __init__(self, image: str, user_a: str, user_b: str, action: str) -> None:
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
        self.embed_object_session.title = f"**{self.article.name}**"
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

class HomebrewEmbed(EmbedMessage):
    def __init__(self, formuale: HomebrewPackage) -> None:
        super().__init__(colour=0x2F2A25)
