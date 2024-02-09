from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from internal.config.is_admin import is_admin
from internal.filter import IsAdminFilter
from internal.keyboard.command import (REPLY_START_TEXT_MAILING, reply_cancel,
                                       reply_start)
from internal.repository.user import UserRepository
from internal.state import MailingState

DK_MAILINHG_TEXT = "mailing_text"


def mailing_handler(user_repo: UserRepository) -> Router:
    r = Router()

    @r.message(IsAdminFilter(), F.text == REPLY_START_TEXT_MAILING)
    async def _(message: Message, state: FSMContext):
        await state.set_state(MailingState.set_text)
        await message.answer(
            "*Отправьте текст рассылки*",
            reply_markup=reply_cancel(),
        )

    @r.message(MailingState.set_text)
    async def _(message: Message, state: FSMContext):
        if message.text:
            if message.text.lower() == "отмена":
                await state.clear()
                await message.delete()
                await message.answer(
                    "*Рассылка отменена*",
                    reply_markup=reply_start(is_admin(message.chat.id)),
                )
            else:
                await state.update_data({DK_MAILINHG_TEXT: message.text})
                await state.set_state(MailingState.start_mailing)
                await message.answer(
                    f"*Текст рассылки: *\n"
                    f"{message.text}",
                    reply_markup=reply_cancel(),
                )
                await message.answer(
                    "*Начать рассылку?* \n"
                    "Напишите *\"Да\"*, чтобы начать рассылку, либо *\"Отмена\"*, для отмены действия"
                )

    @r.message(MailingState.start_mailing)
    async def _(message: Message, state: FSMContext):
        if message.text and message.bot:
            if message.text.lower() == "отмена":
                await state.clear()
                await message.delete()
                await message.answer(
                    "*Рассылка отменена*",
                    reply_markup=reply_start(is_admin(message.chat.id)),
                )
            elif message.text.lower() == "да":
                data = await state.get_data()
                await state.clear()

                await message.answer(
                    "*Рассылка началсь* ✅",
                    reply_markup=reply_start(is_admin(message.chat.id)),
                )

                mailing_text = data[DK_MAILINHG_TEXT]
                limit, offset, success, total = 100, 0, 0, 0

                while True:
                    users = user_repo.get_list(limit, offset)

                    if not users:
                        break

                    for user in users:
                        total += 1
                        try:
                            await message.bot.send_message(
                                chat_id=user.telegram_id,
                                text=mailing_text,
                            )
                            success += 1
                        except Exception as e:
                            print(e)

                    offset += limit

                await message.answer(
                    "*Рассылка завершена* ✅\n\n"
                    f"*Всего:* `{total}`\n"
                    f"*Успешно:* `{success}`\n"
                )

    return r
