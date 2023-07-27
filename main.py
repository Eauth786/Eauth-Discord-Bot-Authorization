import interactions
import eauth

bot = interactions.Client(token=eauth.BOT_TOKEN)

@bot.command(
  name="user_id",
  description="Displays the user ID.",
)
async def user_id(ctx: interactions.CommandContext):
  await ctx.send(f"User ID: `{ctx.author.id}`")

@bot.command(
  name="am_i_authorized",
  description="Check if you are one of the authorized users.",
)
async def am_i_authorized(ctx: interactions.CommandContext):
  # Add this to prevent unauthorized access from using your command
  if (eauth.authority_check(ctx.author.id) == False):
    await ctx.send(":x: Access denied!")
    return
    
  await ctx.send(":white_check_mark: Access granted!")

bot.start()
