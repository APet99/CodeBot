from .mycog import Mycog
from redbot.core import Config
def setup(bot):
    bot.add_cog(Mycog())
    self.config = Config.get_conf(self, identifier=1234567890)