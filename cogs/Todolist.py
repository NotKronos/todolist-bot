import json
from discord.ext import commands

from main import client


class Todolist:  # Skeleton of 'Todolist' class
    def __init__(self, elements: dict):
        self.elements = elements
        self.num_of_elements = len(elements)

    @staticmethod
    def save_to_file(self, list_name):
        """
        Saves a todolist in form of a dict to a file
        :param self:
        :param list_name:
        :return:
        """
        with open("../lists/" + list_name + ".json", "w") as list_file:
            json.dump(self.elements, list_file)

    @staticmethod
    def read_from_file(self, list_name):
        """
        Reads a todolist from a file
        Then it converts it to a dict
        :param self:
        :param list_name:
        :return:
        """
        with open("../lists/" + list_name + ".json", "r") as list_file:
            json_list = json.load(list_file)
            self.elements = json_list.loads()
            self.num_of_elements = len(self.elements)


class TodolistCommands(commands.Cog):   # Skeleton of 'TodolistCommands' class
    def __init__(self):
        self.client = client

    @commands.command(name="printList")
    async def print_list(self, ctx):
        return

    @commands.command(name="markAsDone")
    async def mark_as_done(self, ctx):
        return

    @commands.command(name="markAsNotDone")
    async def mark_as_not_done(self, ctx):
        return

    @commands.command(name="createList")
    async def create_list(self, ctx, arg):
        """
        Creates a file to keep a list in
        Sends a message in case of a failure
        :param ctx:
        :param arg:
        :return:
        """
        filename: str = arg
        try:
            with open("../lists/" + filename + ".json", "x"):
                await ctx.send("Created file named " + filename + "!")
        except FileExistsError:
            await ctx.send("File with this name already exists!")

    @commands.command(name="removeList")
    async def remove_list(self, ctx):
        return
