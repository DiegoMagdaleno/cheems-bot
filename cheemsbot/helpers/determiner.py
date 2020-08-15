import discord


async def require_proper_permissions(
    ctx, user: discord.User, bot: discord.ext.commands.Bot
):
    our_member = await ctx.guild.fetch_member(user.id)
    bot_member = await ctx.guild.fetch_member(bot.user.id)

    # The user is admin, so this mean we can't ban them or do any operations
    is_user_admin = our_member.permissions_in(ctx.channel).administrator

    # The user has higher role than the bot
    is_higher_than = our_member.top_role.position >= bot_member.top_role.position

    if is_user_admin or is_higher_than:
        return False

    return True
