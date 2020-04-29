from redbot.core import commands
from redbot.core import Config
import os
import re
class maint(commands.Cog):
    """My custom cog"""
    '''def __init__(self):
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {
            "name": "Unknown"
        }
        self.config.register_global(**default_global)
    '''

    def replace(file, pattern, subst):
        # Read contents from file as a single string
        file_handle = open(file, 'r')
        file_string = file_handle.read()
        file_handle.close()

        # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
        file_string = (re.sub(pattern, subst, file_string))

        # Write contents to file.
        # Using mode 'w' truncates the file.
        file_handle = open(file, 'w')
        file_handle.write(file_string)
        file_handle.close()