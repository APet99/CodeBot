from redbot.core import commands
from redbot.core import Config
from datetime import date
class School(commands.Cog):
    """My custom cog"""
    '''def __init__(self):
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {
            "name": "Unknown"
        }
        self.config.register_global(**default_global)
    '''

    @commands.command()
    async def get_tutor_link(self, ctx):
        Config.user()
        # link for tutor pre-filled
        # https://docs.google.com/forms/d/e/1FAIpQLScckX09i7Dfv27_k1On8-GlkrB8OOF1l8twY9u_OeGzLc7u6Q/viewform?usp=pp_url&entry.814127073=2020-05-09&entry.1520997077=Chase
        # 2020-05-09
        today = date.today().strftime('%Y-%m-%d')
        await ctx.send("https://docs.google.com/forms/d/e/1FAIpQLScckX09i7Dfv27_k1On8-GlkrB8OOF1l8twY9u_OeGzLc7u6Q/viewform?usp=pp_url&entry.814127073={0}".format(today))
