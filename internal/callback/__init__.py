from typing import Optional

from aiogram.filters.callback_data import CallbackData


class ExampleCallbackFactory(CallbackData, prefix="example"):
    action: str
    telegram_id: Optional[int] = None


ACT_EXAMPLE_OK = "ok"
