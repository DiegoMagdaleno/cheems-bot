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
        description=None,
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
        self.description = description

        # !? Discord embed object intialization.
        self.object_embed_session = discord.Embed()
        self.object_embed_session.color = self.colour
        self.object_embed_session.title = self.title
        if self.image is not None:
            self.object_embed_session.set_image(url=self.image)
        if self.footer_string is not None:
            self.object_embed_session.set_footer(text=self.footer_string)
            if self.footer_author_url is not None:
                self.object_embed_session.set_footer(
                    text=self.footer_string, icon_url=self.footer_author_url
                )
        if self.description is not None:
            self.object_embed_session.description = self.description

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
            footer_string=f"Posted on: {post.subreddit}\n{self.credit_string} {post.author}",
        )

        self.object_embed_session.insert_field_at(
            20, name="Link to post", value=f"[Go to post]({self.link})", inline=True,
        )


class FourChanEmbed(EmbedMessage):
    def __init__(self, post: FourChanPost) -> None:
        super().__init__(
            colour=discord.Color.green(),
            title=post.submission_topic,
            image=post.submission_image_url,
            source=post.board_title,
            link=post.submission_url,
            footer_string=f"Posted on board: {post.board_title} at 4chan!",
        )

        self.object_embed_session.insert_field_at(
            20,
            name="Link to thread",
            value=f"[Go to thread]({self.link})",
            inline=True,
        )


class NekoEmbed(EmbedMessage):
    def __init__(self, image: str, user_a: str, user_b: str, action: str) -> None:
        self.user_a = user_a
        self.user_b = user_b
        self.action = action
        with Switch(self.action) as case:
            if case("kiss"):
                self.title_neko_string = f"{self.user_a} is kissing {self.user_b}"
            if case("hug"):
                self.title_neko_string = f"{self.user_a} is hugging {self.user_b}"
            if case("pat"):
                self.title_neko_string = f"{self.user_a} is patting {self.user_b}"
            if case("slap"):
                self.title_neko_string = f"{self.user_a} is slapping {self.user_b}"
            if case("cuddle"):
                self.title_neko_string = f"{self.user_a} is cuddling with {self.user_b}"
            if case("tickle"):
                self.title_neko_string = f"{self.user_a} is tickling {self.user_b}"
        super().__init__(
            colour=discord.Color.blurple(), image=image, title=self.title_neko_string
        )


class WikipediaEmbed(EmbedMessage):
    def __init__(self, colour: str, article: WikipediaArticle) -> None:
        self.article = article
        super().__init__(
            colour=colour,
            author=article.author,
            footer_author_url=article.icon_url,
            title=f"**{self.article.name}**",
            link=self.article.url,
            description=self.article.description,
            footer_string="Article last modified:",
        )

        self.object_embed_session.set_author(
            name="Wikipedia", url="https://wikipedia.org", icon_url=article.icon_url
        )
        self.object_embed_session.timestamp = self.article.last_modified


class GitHubEmbed(EmbedMessage):
    def __init__(self, colour: str, repository: GitHubRepository) -> None:
        self.repository = repository
        super().__init__(
            colour=colour, title=self.repository.full_name, link=self.repository.url
        )

        self.object_embed_session.add_field(
            name="Stars", value=self.repository.stars, inline=True
        )
        self.object_embed_session.add_field(
            name="Forks", value=self.repository.forks, inline=True
        )
        self.object_embed_session.add_field(
            name="Issues", value=self.repository.open_issues, inline=True
        )
        self.object_embed_session.add_field(
            name="Private", value=str(self.repository.is_private), inline=True
        )
        self.object_embed_session.set_author(
            name="GitHub Repository info",
            icon_url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
        )
        self.object_embed_session.set_thumbnail(url=self.repository.avatar_url)
        if self.repository.license_id == "NOASSERTION":
            self.object_embed_session.add_field(
                name="License", value="Other Non-standard license.", inline=True
            )
        elif self.repository.license_id is None:
            self.object_embed_session.add_field(
                name="License", value="All rights reserved.", inline=True
            )
        else:
            self.object_embed_session.add_field(
                name="License", value=self.repository.license_id, inline=True
            )


class HomebrewEmbed(EmbedMessage):
    def __init__(self, formuale: HomebrewPackage) -> None:
        super().__init__(
            colour=0x2F2A25, title=formuale.name, description=formuale.desc
        )
        self.object_embed_session.set_author(
            name="Homebrew",
            url="https://brew.sh",
            icon_url="https://brew.sh/assets/img/homebrew-256x256.png",
        )
        self.object_embed_session.add_field(
            name="Homepage", value=formuale.homepage, inline=True
        )
        self.object_embed_session.add_field(
            name="Version", value=formuale.version, inline=True
        )
        self.deps = "\n".join("⊛ {}".format(each) for each in formuale.dependencies)
        self.object_embed_session.add_field(
            name="Dependecies", value=self.deps, inline=False
        )
