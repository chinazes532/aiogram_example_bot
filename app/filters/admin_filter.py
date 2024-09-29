from aiogram.types import Message
from aiogram.filters import Filter

from config import ADMINS

class Admin(Filter):
    def __init__(self):
        self.admins = ADMINS

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins