from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

REPLY_START_TEXT_ADD_SITE = "Добавить сайт"
REPLY_START_TEXT_MY_SITES = "Мои сайты"
REPLY_START_TEXT_PROFILE = "Профиль"
REPLY_START_TEXT_WITHDRAWAL_FUNDS = "Вывод средств"
REPLY_START_TEXT_MAILING = "Рассылка"


def reply_start(is_admin: bool) -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text=REPLY_START_TEXT_ADD_SITE),
            KeyboardButton(text=REPLY_START_TEXT_MY_SITES),
        ],
        [
            KeyboardButton(text=REPLY_START_TEXT_PROFILE),
            KeyboardButton(text=REPLY_START_TEXT_WITHDRAWAL_FUNDS),
        ],
    ]

    if is_admin:
        keyboard.append(
            [
                KeyboardButton(
                    text=REPLY_START_TEXT_MAILING,
                )
            ]
        )

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )


REPLY_CANCEL_TEXT_CANCEL = "Отмена"


def reply_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Отмена")],
        ],
        resize_keyboard=True,
    )
