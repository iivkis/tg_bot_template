import asyncio
import logging

import psycopg2
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from internal.config import (DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER,
                             TOKEN)
from internal.handler.command import command_handler
from internal.handler.mailing import mailing_handler
from internal.middleware.auth import AuthMiddleware
from internal.repository.user import UserRepository

logging.basicConfig(level=logging.INFO)


async def main():
    dp = Dispatcher(
        storage=RedisStorage.from_url("redis://redis:6379/0")
    )

    bot = Bot(
        token=TOKEN,
        parse_mode="markdown"
    )

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )

    user_repo = UserRepository(conn)

    dp.message.middleware.register(AuthMiddleware(bot, dp, user_repo))

    dp.include_routers(
        command_handler(user_repo),
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
