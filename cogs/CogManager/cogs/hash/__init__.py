from .hash import Hash

async def setup(bot) :
    bot.add_cog(Hash(bot))
