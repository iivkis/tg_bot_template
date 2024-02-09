from aiogram.filters import BaseFilter
from aiogram.types import Message

from internal.config.is_admin import is_admin


class IsAdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return is_admin(message.chat.id)
