# discordservices.py
A Simple Python API Wrapper for discordservices.net

# Usage
Installation:

Via pip: `pip install discordservices==0.0.4`

With autopost:
```py
import discord
import discordservices

from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.dsclient = discordservices.DSClient(bot, 'apitoken', autopost=True) # default to False, if sets True it will autoposts every 900 seconds

bot.run('token')
```

Without autopost:
```py
import discord
import discordservices

from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.dsclient = discordservices.DSClient(bot, 'apitoken', autopost=False)

@bot.event
async def on_guild_join(guild):
    await bot.dsclient.post_count()
    print("Guild count posted")

bot.run('token')

```
