from redbot.core import commands
import os
class Mycog(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @commands.command()
    async def gitpull(self, ctx):
        os.system('git pull')
        await ctx.send("I pulled the code!")