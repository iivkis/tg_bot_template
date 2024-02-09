from aiogram import Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from internal.config.is_admin import is_admin
from internal.keyboard.command import reply_start
from internal.repository.user import UserRepository


def command_handler(user_repo: UserRepository) -> Router:
    r = Router()

    @r.message(Command("start"))
    async def _(message: Message, state: FSMContext):
        await state.clear()
        await message.answer(
            "*Меню 📖*",
            reply_markup=reply_start(is_admin(message.chat.id)),
        )

    return r
