from discord.ext import commands

import main
from main import client

prefix: str = main.config[0]


class Config(commands.Cog):
    def __init__(self):
        self.client = client

    @commands.command(name="prefix")  # I have no idea if this works
    async def prefix(self, ctx, arg):
        """
        Changes 'prefix' value in the config file
        """
        if ctx.message.author.guild_permission.administrator:
            message: str = arg
            try:
                with open("../config/config", "r") as config_file:
                    lines = config_file.readlines()
                    line_num = 0
                    with open("../config/config", "w") as config_file_ow:
                        for line in lines:
                            line_num += 1
                            if line.startswith("prefix:"):
                                config_file_ow.write("prefix:" + message)
                            else:
                                config_file_ow.write(line)
            except IOError:
                print("I/O error!")
        else:
            ctx.message.channel.send("This command requires admin perms")

    @commands.command(name="status")  # I have no idea if this works
    async def status(self, ctx, arg):
        """
        Changes 'prefix' value in the config file
        """
        if ctx.message.author.guild_permission.administrator:
            message: str = arg
            try:
                with open("../config/config", "r") as config_file:
                    lines = config_file.readlines()
                    line_num = 0
                    with open("../config/config", "w") as config_file_ow:
                        for line in lines:
                            line_num += 1
                            if line.startswith("status:"):
                                config_file_ow.write("status:" + message)
                            else:
                                config_file_ow.write(line)
            except IOError:
                print("I/O error!")
        else:
            ctx.message.channel.send("This command requires admin perms")
