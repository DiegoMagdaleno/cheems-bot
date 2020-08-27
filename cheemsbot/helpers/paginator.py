# Paginator.py is hugely based on this contributions:
# pagination.py by runerw0lf https://gist.github.com/runew0lf/fce60414d7a4ee9dfac8f442eca39687
# The Discord bot https://github.com/python-discord/bot community
# And more! Check them out they did all the work here.
# This acts as a collection of Master classes, this are overriden in "embeds.py", but
# many of the methods are kept

from typing import Iterable, List, Optional, Tuple
from discord.ext.commands import Context, Paginator
from discord import Embed, Member, Reaction
from discord.abc import User
from loguru import logger as log
import asyncio


# Constants
FIRST_EMOJI = "\u23EE"
LEFT_EMOJI = "\u2B05"
RIGHT_EMOJI = "\u27A1"
LAST_EMOJI = "\u23ED"
DELETE_EMOJI = "\u274c"


PAGINATION_EMOJI: List[str] = [
    FIRST_EMOJI,
    LEFT_EMOJI,
    RIGHT_EMOJI,
    LAST_EMOJI,
    DELETE_EMOJI,
]


class LinePaginator(Paginator):
    def __init__(self, prefix="```", suffix="```", max_size=50, max_lines=None) -> None:
        self.prefix = prefix
        self.suffix = suffix
        self.max_size = max_size
        self.max_lines = max_lines
        self._current_page = [prefix]
        self._linecount = 0
        self._count = len(prefix) + 1
        self._pages = []

    def add_line(self, line, *, empty=False):
        if len(line) > self.max_size - len(self.prefix) - 2:
            raise RuntimeError(
                "Line exceeds maximum page size {}".format(
                    (self.max_size - len(self.prefix) - 2)
                )
            )
        if self.max_lines is not None:
            if self._linecount >= self.max_lines:
                self._linecount = 0
                self.close_page()

            self._linecount += 1
        if self._count + len(line) + 1 > self.max_size:
            self.close_page()

        self._count += len(line) + 1
        self._current_page.append(line)

        if empty:
            self._current_page.append("")
            self._count += 1

    @classmethod
    async def paginate(
        cls,
        lines: Iterable[str],
        ctx: Context,
        embed: Embed,
        bot,
        prefix: str = "",
        suffix: str = "",
        max_lines: Optional[int] = None,
        max_size: int = 50,
        empty: bool = True,
        restrict_to_user: User = None,
        timeout: int = 30,
        footer_text: str = None,
    ):
        def event_checker(reaction_: Reaction, user_: Member):
            no_restrictions = not restrict_to_user or user_.id == restrict_to_user.id
            return all(
                [
                    reaction_.message.id == message.id,
                    reaction_.emoji in PAGINATION_EMOJI,
                    user_.id != bot.user.id,
                    no_restrictions,
                ]
            )

        paginator = cls(
            prefix=prefix, suffix=suffix, max_size=max_size, max_lines=max_lines
        )

        current_page = 0

        for line in lines:
            try:
                paginator.add_line(line, empty=empty)
            except Exception:
                log.exception(f"Failed to add line to paginator: '{line}'")
                raise
            else:
                log.trace((f"Added line to paginator: '{line}'"))

        log.debug(f"Paginator created with {len(paginator.pages)} pages")

        # Set the page we are at in our embed descritpion
        embed.description = paginator.pages[current_page]

        if len(paginator.pages) <= 1:
            if footer_text:
                embed.set_footer(text=footer_text)
                log.trace(f"Setting embed footer to '{footer_text}'")

            log.debug(
                "There's less than two pages, so we won't paginate - sending single page on its own"
            )

            return await ctx.send(embed=embed)
        else:
            if footer_text:
                embed.set_footer(
                    text=f"{footer_text} (Page {current_page + 1}/{len(paginator.pages)})"
                )
            else:
                embed.set_footer(text=f"Page {current_page + 1}/{len(paginator.pages)}")

            log.trace(f"Setting embed footer to '{embed.footer.text}'")
            log.debug("Sending first page to channel...")
            message = await ctx.send(embed=embed)

        log.debug("Adding emoji reactions to message...")

        for emoji in PAGINATION_EMOJI:
            log.trace(f"Adding reaction: {repr(emoji)}")
            await message.add_reaction(emoji)

        while True:
            try:
                reaction, user = await bot.wait_for(
                    "reaction_add", timeout=timeout, check=event_checker
                )
                log.trace(f"Got reaction: {reaction}")
            except asyncio.TimeoutError:
                log.debug("Timed out waiting for a reaction")
                # No reactions for 30 seconds so we break from the While loop
                break
            if reaction.emoji == DELETE_EMOJI:
                log.debug("User requested we stop")
                break
            if reaction.emoji == FIRST_EMOJI:
                await message.remove_reaction(reaction.emoji, user)
                current_page = 0
                log.debug(
                    f"Got first page reaction - changing to page 1/{len(paginator.pages)}"
                )
                embed.description = ""
                await message.edit(embed=embed)
                embed.description = paginator.pages[current_page]
                if footer_text:
                    embed.set_footer(
                        text=f"{footer_text} (Page {current_page + 1}/{len(paginator.pages)})"
                    )
                else:
                    embed.set_footer(
                        text=f"Page {current_page + 1}/{len(paginator.pages)}"
                    )
                await message.edit(embed=embed)

            if reaction.emoji == LAST_EMOJI:
                await message.remove_reaction(reaction.emoji, user)
                current_page = len(paginator.pages) - 1

                log.debug(
                    f"Got last page reaction - changing to page {current_page + 1}{len(paginator.pages)}"
                )

                embed.description = ""
                await message.edit(embed=embed)
                embed.description = paginator.pages[current_page]
                if footer_text:
                    embed.set_footer(
                        text=f"{footer_text} (Page {current_page + 1} of {len(paginator.pages)})"
                    )
                else:
                    embed.set_footer(
                        text=f"Page {current_page + 1} of {len(paginator.pages)}"
                    )
                await message.edit(embed=embed)

            if reaction.emoji == LEFT_EMOJI:
                await message.remove_reaction(reaction.emoji, user)

                if current_page <= 0:
                    log.debug(
                        "Got previous page reaction, but we're on the first page - ignoring"
                    )
                    continue

                current_page -= 1
                log.debug(
                    f"Got previous page reaction - changing to page {current_page + 1} of {len(paginator.pages)}"
                )

                embed.description = ""
                await message.edit(embed=embed)
                embed.description = paginator.pages[current_page]

                if footer_text:
                    embed.set_footer(
                        text=f"{footer_text} (Page {current_page + 1} of {len(paginator.pages)})"
                    )
                else:
                    embed.set_footer(
                        text=f"Page {current_page + 1}of{len(paginator.pages)}"
                    )

                await message.edit(embed=embed)

            if reaction.emoji == RIGHT_EMOJI:
                await message.remove_reaction(reaction.emoji, user)

                if current_page >= len(paginator.pages) - 1:
                    log.debug(
                        "Got next page reaction, but we're on the last page - ignoring"
                    )
                    continue
                current_page += 1
                log.debug(
                    f"Got next page reaction - changing to page {current_page + 1} of {len(paginator.pages)}"
                )

                embed.description = ""
                await message.edit(embed=embed)
                embed.description = paginator.pages[current_page]

                if footer_text:
                    embed.set_footer(
                        text=f"{footer_text} (Page {current_page + 1} of {len(paginator.pages)})"
                    )
                else:
                    embed.set_footer(
                        text=f"Page {current_page + 1}/{len(paginator.pages)}"
                    )
                await message.edit(embed=embed)
        log.debug("Ending pagination and removing all reactions...")
        await message.clear_reactions()


class ImagePaginator(Paginator):
    def __init__(self, prefix="", suffix="") -> None:
        super().__init__(prefix, suffix)
        self._current_page = [prefix]
        self.images = []
        self._pages = []

    def add_line(self, line: str = "") -> None:
        if line:
            self._count = len(line)
        else:
            self._count = 0
        self._current_page.append(line)
        self.close_page()

    def add_image(self, image_url: str = None) -> None:
        self.images.append(image_url)

    @classmethod
    async def paginate(
        cls,
        pages: List[str],
        ctx: Context,
        embed: Embed,
        bot,
        prefix: str = "",
        suffix: str = "",
        timeout: int = 30,
    ):
        def event_checker(reaction_: Reaction, member: Member) -> bool:
            return all(
                [
                    reaction_.message.id == message.id,
                    reaction_.emoji in PAGINATION_EMOJI,
                    not member.bot,
                ]
            )

        paginator = cls(prefix=prefix, suffix=suffix)
        current_page = 0

        for image in pages:
            #! HACKY METHOD.
            # TODO: Rewrite after more research is done
            paginator.pages.append([None for _ in range(len(pages))])
            paginator.add_image(image)

        image = paginator.images[current_page]

        if image:
            embed.set_image(url=image)

        if len(paginator.pages) <= 1:
            return await ctx.send(embed=embed)

        embed.set_footer(text=f"Page {current_page + 1}/{len(paginator.pages)}")
        message = await ctx.send(embed=embed)

        for emoji in PAGINATION_EMOJI:
            await message.add_reaction(emoji)

        while True:
            try:
                reaction, user = await bot.wait_for(
                    "reaction_add", timeout=timeout, check=event_checker
                )
            except asyncio.TimeoutError:
                await message.clear_reactions()
                log.debug("Timed out to get a reaction")
                break

            await message.remove_reaction(reaction.emoji, user)

            if reaction.emoji == DELETE_EMOJI:
                log.debug(
                    "User wants to get rid of the image gallery, break the circle"
                )
                await message.delete()
                break

            if reaction.emoji == FIRST_EMOJI:
                if current_page == 0:
                    log.debug("Got first page, but we are on 0, ignoring")
                    continue

                current_page = 0
                reaction_type = "first"

            if reaction.emoji == LAST_EMOJI:
                if current_page >= len(paginator.pages) - 1:
                    log.debug(
                        "Got next reaction type but we are on first page, ignoring value"
                    )
                    continue
                current_page = len(paginator.pages) - 1
                reaction_type = "last"

            if reaction.emoji == LEFT_EMOJI:
                if current_page <= 0:
                    log.debug(
                        "Requested to go back but we are on the last page, ignoring"
                    )
                    continue

                current_page -= 1
                reaction_type = "previous"
            if reaction.emoji == RIGHT_EMOJI:
                if current_page >= len(paginator.pages) - 1:
                    log.debug(
                        "Requested to go to the last page, but we are in the last page, ignoring"
                    )
                    continue
                current_page += 1
                reaction_type = "next"

            # Magic happens here, after page and reaction_type is set
            await message.edit(embed=embed)

            image = paginator.images[current_page]
            if image:
                embed.set_image(url=image)

            embed.set_footer(text=f"Page {current_page + 1}/{len(paginator.pages)}")
            log.debug(
                f"Got {reaction_type} page reaction - changing to page {current_page + 1}/{len(paginator.pages)}"
            )

            await message.edit(embed=embed)


class TabPaginator(Paginator):
    """
    Helper class that paginates images for embeds in messages.
    Close resemblance to LinePaginator, except focuses on images over text.
    Refer to ImagePaginator.paginate for documentation on how to use.
    """

    class Tab:
        def __init__(self, embed, emoji, error=False, name=""):
            self.embed = embed
            self.emoji = emoji
            self.error = error
            self.name = name

    def __init__(self, bot, prefix="", suffix="", timeout=0):
        super().__init__(prefix, suffix)
        self._current_page = [prefix]
        self.tabs = []
        self._pages = []
        self.bot = bot
        self.timeout = timeout
        self.message = asyncio.Event()
        self.current_tab = None

    def add_tab(self, tab: Tab = None) -> None:
        """
        Adds an image to a page
        :param image: image url to be appended
        """
        self.tabs.append(tab)

    async def update_tab(self, name, embed=None, error=None, emoji=None):
        for tab in self.tabs:
            if tab.name == name:
                if embed is not None:
                    tab.embed = embed
                if error is not None:
                    tab.error = error
                if emoji is not None:
                    if self.message is not None:
                        await self.message.remove_reaction(tab.emoji)
                        await self.message.add_reaction(emoji)
                    tab.emoji = emoji
                if isinstance(self.message, asyncio.Event):
                    await self.message.wait()
                if tab == self.current_tab:
                    if tab.error:
                        self.current_tab = next(
                            (x for x in self.tabs if not x.error), self.tabs[0]
                        )
                    else:
                        self.current_tab = tab
                    await self.message.edit(embed=self.current_tab.embed)
                elif self.current_tab.error and not tab.error:
                    self.current_tab = next(
                        (x for x in self.tabs if not x.error), self.tabs[0]
                    )
                    await self.message.edit(embed=self.current_tab.embed)

    async def send(self, ctx):
        def check_event(reaction_: Reaction, member: Member) -> bool:
            """
            Checks each reaction added, if it matches our conditions pass the wait_for
            :param reaction_: reaction added
            :param member: reaction added by member
            """

            return all(
                (
                    # Reaction is on the same message sent
                    reaction_.message.id == self.message.id,
                    # The reactor is not a bot
                    not member.bot,
                )
            )

        message = await ctx.send(embed=self.current_tab.embed)
        self.message.set()
        self.message = message
        for tab in self.tabs:
            await message.add_reaction(tab.emoji)
        await message.add_reaction(DELETE_EMOJI)
        while True:
            # Start waiting for reactions
            try:
                reaction, user = await self.bot.wait_for(
                    "reaction_add", timeout=self.timeout, check=check_event
                )
            except asyncio.TimeoutError:
                log.debug("Timed out waiting for a reaction")
                break  # We're done, no reactions for the last 5 minutes

            # Deletes the users reaction
            await self.message.remove_reaction(reaction.emoji, user)

            # Delete reaction press - [:x:]
            if reaction.emoji == DELETE_EMOJI:
                log.debug("Got delete reaction")
                break

            for tab in self.tabs:
                if reaction.emoji == tab.emoji and self.current_tab != tab:
                    await self.message.edit(embed=tab.embed)
                    self.current_tab = tab

        log.debug("Ending pagination and removing all reactions...")
        await self.message.clear_reactions()

    @classmethod
    def create_paginator(
        cls,
        tabs: List[Tab],
        bot,
        prefix: str = "",
        suffix: str = "",
        timeout: int = 300,
        color=None,
    ):
        paginator = cls(bot, prefix=prefix, suffix=suffix, timeout=timeout)

        for tab in tabs:
            paginator.add_tab(tab)
        paginator.current_tab = next(
            (x for x in paginator.tabs if not x.error), paginator.tabs[0]
        )

        return paginator

    @classmethod
    async def paginate(
        cls,
        tabs: List[Tab],
        ctx: Context,
        bot,
        prefix: str = "",
        suffix: str = "",
        timeout: int = 300,
        color=None,
    ):
        await TabPaginator.create_paginator(
            tabs, bot, prefix, suffix, timeout, color
        ).send(ctx)


class UrbanPagintor(Paginator):
    def __init__(self, prefix="", suffix="") -> None:
        super().__init__(prefix, suffix)
        self._current_page = [prefix]
        self.urban_objects = []
        self._pages = []

    def add_line(self, line: str = "") -> None:
        print("here")
        if line:
            self._count = len(line)
        else:
            self._count = 0
        self._current_page.append(line)
        self.close_page()

    @classmethod
    async def paginate(
        cls,
        definitions: List,
        ctx: Context,
        embed: Embed,
        bot,
        prefix: str = "",
        suffix: str = "",
        timeout: int = 30,
    ):
        def event_checker(reaction_: Reaction, member: Member) -> bool:
            return all(
                [
                    reaction_.message.id == message.id,
                    reaction_.emoji in PAGINATION_EMOJI,
                    not member.bot,
                ]
            )

        paginator = cls(prefix=prefix, suffix=suffix)
        current_page = 0

        for _ in definitions:
            paginator.pages.append(None for _ in range(len(definitions)))

        ub_def = definitions[current_page]

        if ub_def:
            embed.title = ub_def.word
            embed.description = "From Urban Dictionary"
            embed.add_field(name="Definition", value=(str(ub_def.definition).replace("[", "")).replace("]",""), inline=True)
            embed.add_field(name="Examples", value=(str(ub_def.example).replace("[", "")).replace("]", ""), inline=True)

        if len(paginator.pages) <= 1:
            return await ctx.send(embed=embed)

        embed.set_footer(text=f"Page {current_page + 1}/{len(paginator.pages)}")
        message = await ctx.send(embed=embed)

        for emoji in PAGINATION_EMOJI:
            await message.add_reaction(emoji)

        while True:
            try:
                reaction, user = await bot.wait_for(
                    "reaction_add", timeout=timeout, check=event_checker
                )
            except asyncio.TimeoutError:
                await message.clear_reactions()
                log.debug("Timed out to get a reaction")
                break

            await message.remove_reaction(reaction.emoji, user)

            if reaction.emoji == DELETE_EMOJI:
                log.debug(
                    "User wants to get rid of the image gallery, break the circle"
                )
                await message.delete()
                break

            if reaction.emoji == FIRST_EMOJI:
                if current_page == 0:
                    log.debug("Got first page, but we are on 0, ignoring")
                    continue

                current_page = 0
                reaction_type = "first"

            if reaction.emoji == LAST_EMOJI:
                if current_page >= len(paginator.pages) - 1:
                    log.debug(
                        "Got next reaction type but we are on first page, ignoring value"
                    )
                    continue
                current_page = len(paginator.pages) - 1
                reaction_type = "last"

            if reaction.emoji == LEFT_EMOJI:
                if current_page <= 0:
                    log.debug(
                        "Requested to go back but we are on the last page, ignoring"
                    )
                    continue

                current_page -= 1
                reaction_type = "previous"
            if reaction.emoji == RIGHT_EMOJI:
                if current_page >= len(paginator.pages) - 1:
                    log.debug(
                        "Requested to go to the last page, but we are in the last page, ignoring"
                    )
                    continue
                current_page += 1
                reaction_type = "next"

            await message.edit(embed=embed)

            ub_def = definitions[current_page]

            if ub_def:
                embed.clear_fields()
                embed.title = ub_def.word
                embed.description = "From Urban Dictionary"
                embed.add_field(name="Definition", value=(str(ub_def.definition).replace("[", "")).replace("]",""), inline=True)
                embed.add_field(name="Examples", value=(str(ub_def.example).replace("[", "")).replace("]", ""), inline=True)

            embed.set_footer(text=f"Page {current_page + 1}/{len(paginator.pages)}")
            log.debug(
                f"Got {reaction_type} page reaction - changing to page {current_page + 1}/{len(paginator.pages)}"
            )

            await message.edit(embed=embed)
