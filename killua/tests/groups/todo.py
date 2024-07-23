from ..types import *
from ..types import user
from ...utils.classes import *

from ..testing import Testing, test
from ...cogs.todo import TodoSystem

class TestingToDoSystem(Testing):

    def __init__(self):
        super().__init__(cog=TodoSystem)

class Create(TestingToDoSystem):

    def __init__(self):
        super().__init__()
        

    @test
    async def test_creation_no_arguments(self) -> None:
        try:
            await self.cog.create(self.cog, self.base_context)
        except Exception as e:
            assert(e.__class__ == TypeError)

    @test
    async def test_creation(self) -> None:
        user = await User.new(self.base_author.id)
        await self.cog.create(self.cog, self.base_context, "Test List", "private", "yes")

    @test
    async def test_view_command_valid_list(self) -> None:
        pass