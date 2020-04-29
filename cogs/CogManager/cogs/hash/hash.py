# Primary imports
import hashlib
import inspect
import asyncio

# AIOHTTP
import aiohttp

# Discord Imports
from redbot.core import commands

__author__ = "Eragon5779"
__version__ = "1.0"


class Hash(commands.Cog):
    """A cog wrapper for hashlib that supports all guarenteed algorithms"""

    def __init__(self, bot):
        self.bot = bot
        self._session = aiohttp.ClientSession(loop=self.bot.loop)

    def __unload(self):
        self.bot.loop.create_task(self._session.close())

    @commands.group(no_pm=True)
    async def hash(self, ctx):
        """Hashes file or text with specified algorithm.\n\nIf hashing file, `hash_data` not needed"""
        if ctx.invoked_subcommand is None:
            pass

    async def get_data(self, algo, hash_data: str = "", hash_file=None):
        if hash_file:
            async with self._session.get(hash_file[0].url) as resp:
                if resp.status == 200:
                    file = await resp.read()
                    return self.text_hash(file, algo)
                else:
                    return "Unable to load file! Please try again."
        elif hash_data:
            return self.text_hash(hash_data, algo)
        else:
            return None

    def text_hash(self, text, algo: str):
        m = getattr(hashlib, algo)()
        if type(text) == str:
            text = text.encode("UTF-8")
        m.update(text)
        if "shake" in algo:
            return m.hexdigest(128)
        return m.hexdigest()

    # SHA algorithms

    @hash.command()
    async def sha1(self, ctx, *, hash_data: str = ""):
        """SHA1 Hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    @hash.command()
    async def sha224(self, ctx, *, hash_data: str = ""):
        """SHA224 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    @hash.command()
    async def sha256(self, ctx, *, hash_data: str = ""):
        """SHA256  hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    @hash.command()
    async def sha384(self, ctx, *, hash_data: str = ""):
        """SHA384 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    @hash.command()
    async def sha512(self, ctx, *, hash_data: str = ""):
        """SHA512 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    # SHA3 algorithms

    @hash.command()
    async def sha3_224(self, ctx, *, hash_data: str = ""):
        """SHA3-224 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    @hash.command()
    async def sha3_256(self, ctx, *, hash_data: str = ""):
        """SHA3-256 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    @hash.command()
    async def sha3_384(self, ctx, *, hash_data: str = ""):
        """SHA3-384 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    @hash.command()
    async def sha3_512(self, ctx, *, hash_data: str = ""):
        """SHA3-512 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    # SHAKE algorithms

    @hash.command()
    async def shake_128(self, ctx, *, hash_data: str = ""):
        """SHAKE-128 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    @hash.command()
    async def shake_256(self, ctx, *, hash_data: str = ""):
        """SHAKE-256 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")

    # Other algorithms

    @hash.command()
    async def md5(self, ctx, *, hash_data: str = ""):
        """MD5 hash algorithm"""
        algo = inspect.stack()[0][3]
        h = await self.get_data(algo, hash_data, ctx.message.attachments)
        if not h:
            await ctx.send_help()
            return
        await ctx.send(f"{h}")
