from discord.ext import commands

from main import client


class Todolist:  # Skeleton of 'Todolist' class
    def __init__(self, elements: list[str], num_of_elements: int):
        self.elements = elements
        self.num_of_elements = num_of_elements

    @staticmethod
    def save_to_file(self, list_name):
        with open("../lists/" + list_name, "w") as list_file:
            for line in self.elements:
                list_file.writelines(line)

    @staticmethod
    def read_from_file(self, list_name):
        with open("../lists/" + list_name, "r") as list_file:
            line_num: int
            lines: list[str]
            for lines in list_file.readlines():
                line_num += 1
            self.elements = lines
            self.num_of_elements = line_num


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
        filename: str = arg
        try:
            with open(filename, "x"):
                await ctx.send("Created file named " + filename + "!")
        except FileExistsError:
            await ctx.send("File with this name already exists!")
        return

    @commands.command(name="removeList")
    async def remove_list(self, ctx):
        return
