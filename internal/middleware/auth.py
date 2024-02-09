from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Bot, Dispatcher
from aiogram.types import Message

from internal.repository.user import UserRepository


class AuthMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot, dp: Dispatcher, user_repo: UserRepository):
        super().__init__()
        self._bot = bot
        self._dp = dp
        self._user_repo = user_repo

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        op = "middleware.AuthMiddleware.__call__"
        try:
            user = self._user_repo.get(event.chat.id)
            if user is None:
                self._user_repo.create(event.chat.id)
            return await handler(event, data)
        except Exception as e:
            print(op, e)
