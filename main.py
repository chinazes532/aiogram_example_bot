import asyncio
from aiogram import Bot, Dispatcher

from app.handlers.user import user
from app.handlers.admin import admin

from config import TOKEN

from app.database.models import async_main


async def main():
    bot = Bot(token=TOKEN)

    dp = Dispatcher()
    dp.include_routers(user, admin)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    await async_main()
    print('Starting up...')


async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass