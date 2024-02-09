from internal.config import SETTINGS_ADMINS_ID


def is_admin(chat_id: int) -> bool:
    return chat_id in SETTINGS_ADMINS_ID
