from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.filters.admin_filter import Admin


admin = Router()


@admin.message(Admin(), Command('admin'))
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот, администратор!')