import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from database import init_db
from handlers import subscription, menu, admin
from middlewares.admin_forward import AdminForwardMiddleware


async def main():
    logging.basicConfig(level=logging.INFO)
    init_db()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.outer_middleware(AdminForwardMiddleware())

    dp.include_router(subscription.router)
    dp.include_router(admin.router)
    dp.include_router(menu.router)

    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Free Fire bot ishga tushdi ✅")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
