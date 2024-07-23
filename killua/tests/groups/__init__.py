from .actions import TestingActions
from .cards import TestingCards
from .dev import TestingDev
from .todo import TestingToDoSystem

tests = [TestingActions, TestingCards, TestingDev, TestingToDoSystem]

__all__ = ["tests"]
